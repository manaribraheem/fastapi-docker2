from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}




# Another endpoint with parameter   .. here we change and personalise
@app.get("/{name}")
async def hello(name: str):
    return {"message": f"Hello, {name}!"}
