# main.py

# First, we import FastAPI from the fastapi library
from fastapi import FastAPI

# Then, we create an "app" instance. This is the heart of our FastAPI application.
# Think of 'app' as the main entry point for all our web routes.
app = FastAPI()

# @app.get("/") is a "decorator". It tells FastAPI that the function below
# should run when someone sends a GET request to the "/" (root) URL.
# The 'async def' means this function can do other things while waiting (more on async later!).
@app.get("/")
async def read_root():
    # This function simply returns a Python dictionary.
    # FastAPI automatically converts Python dictionaries to JSON when sending them back as a response.
    return {"message": "Hello, FastAPI World!"}