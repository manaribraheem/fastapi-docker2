from fastapi import FastAPI

# CREATE A FASTAPI OBJECT
app = FastAPI()

#CREATE AN ENPOINT (ROUTE)
@app.get("/")
async def root():
    return {"message": "Hello World, Hahaha!"}

#another endpoint with parameter
@app.get("/{name}")
async def hello(name: str):
    return {"message": f"Hello, {name}!"}
    #the f-string above is equivalent to:
    #"hello", " + name + "!"
    #"hello, {}!".format(name)
    #("hello, ", name, "!")
