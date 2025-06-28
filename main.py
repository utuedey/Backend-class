from fastapi import FastAPI


# The entry point of your FastAPI application
app = FastAPI()

# path operation
@app.get("/homepage")
def home():
    return {"message": "Welcome to the homepage!"}
    