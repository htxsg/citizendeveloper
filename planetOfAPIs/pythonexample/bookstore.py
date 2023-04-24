from fastapi import FastAPI
from callopenai import generate_text

app = FastAPI()

# Preloaded books
books = [
    {"id": 1, "title": "To Kill a Mockingbird", "author": "Harper Lee", "price": 10.99},
    {"id": 2, "title": "1984", "author": "George Orwell", "price": 9.99},
    {"id": 3, "title": "The Catcher in the Rye", "author": "J.D. Salinger", "price": 12.99},
    {"id": 4, "title": "Brave New World", "author": "Aldous Huxley", "price": 8.99},
    {"id": 5, "title": "Animal Farm", "author": "George Orwell", "price": 7.99},
]

# Endpoint to retrieve all books
@app.get("/books")
async def get_books():
    return books

# Endpoint to retrieve a specific book by ID
@app.get("/books/{book_id}")
async def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            funny = generate_text("A funny description for the book " + book["title"] )
            book["title"] = funny
            return book
    return {"error": "Book not found"}

# Endpoint to add a new book
@app.post("/books")
async def add_book(title: str, author: str, price: float):
    book_id = len(books) + 1
    book = {"id": book_id, "title": title, "author": author, "price": price}
    books.append(book)
    return book

# Endpoint to update an existing book
@app.put("/books/{book_id}")
async def update_book(book_id: int, title: str = None, author: str = None, price: float = None):
    for book in books:
        if book["id"] == book_id:
            if title:
                book["title"] = title
            if author:
                book["author"] = author
            if price:
                book["price"] = price
            return book
    return {"error": "Book not found"}

# Endpoint to delete a book by ID
@app.delete("/books/{book_id}")
async def delete_book(book_id: int):
    for i, book in enumerate(books):
        if book["id"] == book_id:
            del books[i]
            return {"message": "Book deleted"}
    return {"error": "Book not found"}
