from fastapi import FastAPI # pyright: ignore[reportMissingImports]

app = FastAPI()

# Imagine this is our database of books
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

@app.put("/books/{book_id}")
async def update_book(book_id: int, title: str, author: str):
    """Updates an existing book by replacing its data."""
    if book_id not in books_db:
        return {"error": "Book not found", "status_code": 404}

    books_db[book_id] = {"title": title, "author": author} # Overwrites the old data
    return {"message": f"Book {book_id} updated!", "book": books_db[book_id]}

@app.delete("/books/{book_id}")
async def delete_book(book_id: int):
    """Deletes a book by its ID."""
    if book_id not in books_db:
        return {"error": "Book not found", "status_code": 404}

    del books_db[book_id] # Removes the entry from our dictionary
    return {"message": f"Book {book_id} deleted successfully!"}