from fastapi import FastAPI

app = FastAPI()

jss_1_stud = {
    1: {"name" :  "Ofinni", "surname" : "Emmanuel", "position" : "first" },
    2: {"name" : "Praise", "surname" : "Obaoluwa", "position" : "second"},
    3: {"name" : "Desiree", "surname" : "Mustapha", "position" : "third"}
    4: {"name" : "Emmanuel", "surname" : "Isiaka", "position" : "fourth"}
    5: {"name" : "Deborah", "surname" : "Apata", "position" : "fifth"}
}

@app.get("/jss1")
async def results():
    return jss_1_stud