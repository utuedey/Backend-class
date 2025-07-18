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

@app.get("/newclub") 
async def club():
    return("Welcome to our club. We're glad to have you here..")

@app.get("/choice")
async def thank_you():
    return("You made the right choice!!")

books_db = {
    1: {"title": "The Hobbit", "author": "J.R.R. Tolkien"},
    2: {"title": "Dune", "author": "Frank Herbert"}
}

@app.get("/books/{book_id}")
async def get_book(book_id: int):
    """Retrieves a single book by its ID."""
    if book_id not in books_db:
        return {"error": "Book not found", "status_code": 404} # We'll cover HTTP exceptions later!
    return books_db[book_id]

# How to test: Open your browser to http://127.0.0.1:8000/books/1
# You'll get: {"title":"The Hobbit","author":"J.R.R. Tolkien"}


next_book_id = 3 # Simple way to generate new IDs

@app.post("/books/")
async def create_book(title: str, author: str):
    """Creates a new book."""
    global next_book_id
    new_book = {"title": title, "author": author}
    books_db[next_book_id] = new_book
    created_id = next_book_id
    next_book_id += 1
    return {"message": "Book created!", "id": created_id, "book": new_book}

# How to test (using Postman/Insomnia):
# Method: POST
# URL: http://127.0.0.1:8000/books/
# Body (raw JSON): {"title": "The Lord of the Rings", "author": "J.R.R. Tolkien"}
# You'll get: {"message":"Book created!","id":3,"book":{"title":"The Lord of the Rings","author":"J.R.R. Tolkien"}}


@app.put("/books/{book_id}")
async def update_book(book_id: int, title: str, author: str):
    """Updates an existing book by replacing its data."""
    if book_id not in books_db:
        return {"error": "Book not found", "status_code": 404}

    books_db[book_id] = {"title": title, "author": author} # Overwrites the old data
    return {"message": f"Book {book_id} updated!", "book": books_db[book_id]}

# How to test (using Postman/Insomnia):
# Method: PUT
# URL: http://127.0.0.1:8000/books/1
# Body (raw JSON): {"title": "The Hobbit: A New Adventure", "author": "J.R.R. Tolkien (Updated)"}
# Now, if you GET http://127.0.0.1:8000/books/1, you'll see the new title and author.


@app.delete("/books/{book_id}")
async def delete_book(book_id: int):
    """Deletes a book by its ID."""
    if book_id not in books_db:
        return {"error": "Book not found", "status_code": 404}

    del books_db[book_id] # Removes the entry from our dictionary
    return {"message": f"Book {book_id} deleted successfully!"}

# How to test (using Postman/Insomnia):
# Method: DELETE
# URL: http://127.0.0.1:8000/books/2
# (No body usually required)
# You'll get: {"message":"Book 2 deleted successfully!"}
# Now, if you try to GET http://127.0.0.1:8000/books/2, you'll get the "Book not found" error.

# ASSIGNMENT_1
jss_1_stud = {
    1: {"name" :  "Ofinni", "surname" : "Emmanuel", "position" : "first" },
    2: {"name" : "Praise", "surname" : "Obaoluwa", "position" : "second"},
    3: {"name" : "Desiree", "surname" : "Mustapha", "position" : "third"},
    4: {"name" : "Emmanuel", "surname" : "Isiaka", "position" : "fourth"},
    5: {"name" : "Deborah", "surname" : "Apata", "position" : "fifth"},
}

position_index = 6

@app.get("/jss1")
async def results():
    return jss_1_stud     #returns the whole class results

@app.get("/jss1/{position}")
async def get_position(position: int):
    """Returns specific positions and their holders"""
    if position not in jss_1_stud:     #Ensures the position is within available range
        return {"error": "position not found", "status_code": 404}
    return jss_1_stud[position]  #Returns specific positions

@app.post("/jss1/newresult")
async def extra_result(name: str, surname: str, position: str):
    """Adds a new result to the list """
    global position_index
    new_result = {"name": name, "surname": surname, "position": f"{position_index}th"}
    jss_1_stud[position_index] = new_result
    new_position = position_index
    position_index += 1
    return {"message": "New result uploaded", "position index" : new_position, "info" : new_result}

@app.put("/jss1/{position_index}")
async def updated_result(position_index: int, name: str, surname: str):
    """Updates an existing result"""

    if position_index not in jss_1_stud:
        return {"message":  "position out of range", "error" : "404"}
    if position_index == 1:
        suf = "st"
    elif position_index == 2:
        suf = "nd"
    elif position_index == 3:
        suf = "rd"
    else:
        suf = "th"
    jss_1_stud[position_index] = {"name": name, "surname": surname, "position": f"{position_index}{suf}"}

    return {"message": f"{position_index}{suf} position updated", "details": jss_1_stud[position_index] }
   
   
@app.delete("/jss1/{position_index}")
async def delete_result(position_index: int):
    """Deletes a specific result by its position index"""
    if position_index not in jss_1_stud:
        return {"message": "position is out of range", "error": "404"}
    
    del jss_1_stud[position_index]
    return {"message" : "Successfully deleted the result"}