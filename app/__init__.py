from itertools import groupby

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from unscramble import unscramble

app = FastAPI()

app.mount('/static', StaticFiles(directory='static'), name='static')

templates = Jinja2Templates(directory='templates')


@app.get('/', response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse('index.html.jinja2', {'request': request})


@app.get('/unscramble', response_class=HTMLResponse)
def result(request: Request, chars: str):
    unscrambled = unscramble(chars)
    result = groupby(unscrambled, key=len)
    return templates.TemplateResponse('unscramble.html.jinja2', {'request': request, 'chars': chars, 'result': result})
