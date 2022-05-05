from itertools import groupby

from fastapi import FastAPI, Request, Response
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from unscramble import unscramble

app = FastAPI()

templates = Jinja2Templates(directory='templates')


@app.get('/', response_class=HTMLResponse)
def index(request: Request) -> Response:
    return templates.TemplateResponse('index.html.jinja2', {'request': request})


@app.get('/unscramble', response_class=HTMLResponse)
def result(request: Request, chars: str) -> Response:
    unscrambled = sorted(unscramble(chars), key=len, reverse=True)
    num_of_words = len(unscrambled)
    groups = groupby(unscrambled, key=len)
    context = dict(
        request=request,
        chars=chars,
        result=groups,
        num_of_words=num_of_words
    )
    return templates.TemplateResponse('unscramble.html.jinja2', context)
