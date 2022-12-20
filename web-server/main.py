import store

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def get_list():
    return [1,2,3]

@app.get('/contact', response_class=HTMLResponse)
def get_contact():
    return """
        <h1>Hi I am apage</h1>
        <p>I am text.</p>
    """


def run():
    store.get_categories()


if __name__ == '__main__':
    run()