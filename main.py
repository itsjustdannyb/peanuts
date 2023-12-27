# peanuts
import random
import uvicorn
from fastapi import FastAPI, Request

# HTML
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")


app = FastAPI()


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
async def shell(request:Request, entry: str = Form(.        cd cdcls

    entry = entry.lower()
    if entry == 'physics':
        prayer = random.choice(prayers[entry])
    elif entry == 'math':
        prayer = random.choice(prayers[entry])
    else:
        prayer = random.choice(prayers['biology'])

    return templates.TemplateResponse("index.html", {'request':request, 'prayer':prayer})



# run
if __name__ == '__main__':
    uvicorn.run(app)
    