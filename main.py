# peanuts
import uvicorn
from fastapi import FastAPI
from typing import Optional
import requests


# HTML
from fastapi import Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

# css
from fastapi.staticfiles import StaticFiles


app = FastAPI()

# mount css to api
app.mount("/static", StaticFiles(directory="static"), name="static")


# home
@app.get('/')
async def home():
    return " Welcome to peanuts API, Jesus loves you. try '/shell'"

# peanuts api

# get the html
@app.get('/shell', response_class=HTMLResponse)
async def shell(request: Request):
    return templates.TemplateResponse("index.html", {'request':request})


@app.post('/shell', response_class=HTMLResponse)
async def shell(request:Request, course: str=Form(None)):

    if course is None or not course.strip():
        error_message = "Please input a valid  course"
        return templates.TemplateResponse("index.html", {'request':request, 'error_message':error_message})

    api_url = "peanuts-api-production.up.railway.app"
    data = {'prompt':prompt}

    response = requests.post(api_url, data=data)

    if response.status_code == 200:
        prayer = response.json()["prayer"]
        return templates.TemplateResponse("index.html", {'request': request, 'prayer': prayer})

    else:
        error_message = f"Error: {response.status_code} - {response.text}"
        return templates.TemplateResponse("index.html", {'request': request, 'error_message': error_message})


# run
if __name__ == '__main__':
    uvicorn.run(app)
    