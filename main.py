# peanuts
import random
import uvicorn
from fastapi import FastAPI
from typing import Optional


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

# dict of course and prayers #
prayers = {
    'physics':["May the Lord who made the cosmos grant you divine understanding", "Atoms are small, but guess who isn't? God! He will guide you as you write your exams"],
    'math':["Jesus made math not make sense, receive divine wisdom in Jesus' name", "The patience to make accurate calculations, receive now in Jesus name"],
    'biology':["May the creator of life give life to all you have read in Jesus name", "May the creator of life give you divine understanding as you study in Jesus name"]
}


# peanuts api

# get the html
@app.get('/shell', response_class=HTMLResponse)
async def shell(request: Request):
    return templates.TemplateResponse("index.html", {'request':request})


@app.post('/shell', response_class=HTMLResponse)
async def shell(request:Request, course: str|None =Form(None)):

    if course is None or not course.strip():
        error_message = "Please input a valid  course"
        return templates.TemplateResponse("index.html", {'request':request, 'error_message':error_message})


    course = course.lower()
    if course == 'physics':
        prayer = random.choice(prayers[course])
    elif course == 'math':
        prayer = random.choice(prayers[course])
    else:
        prayer = random.choice(prayers['biology'])

    return templates.TemplateResponse("index.html", {'request':request, 'prayer':prayer})



# run
if __name__ == '__main__':
    uvicorn.run(app)
    