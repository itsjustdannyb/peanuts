from fastapi import FastAPI 

app = FastAPI()

# home
@app.get('/')
async def home():
    return "try '/go' "


if __name__ == "__main__":
    uvicorn.run(app)
