from fastapi import FastAPI 

app = FastAPI()

# home
@app.get('/')
async def home():
    return {'status code':'200'}


if __name__ == "__main__":
    uvicorn.run(app)
