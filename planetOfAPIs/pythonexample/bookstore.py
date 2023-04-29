from fastapi import FastAPI
from pydantic import BaseModel
from funny import generate_funny_book_name

app = FastAPI()

# Define the Book model using Pydantic
class Book(BaseModel):
    name: str
    author: str
    description: str

# Create a list of preloaded books
books = [
    Book(name="The Great Gatsby", author="F. Scott Fitzgerald", description="A classic novel about the decadence and excess of the Jazz Age."),
    Book(name="To Kill a Mockingbird", author="Harper Lee", description="A Pulitzer Prize-winning novel about racial injustice in the American South."),
    Book(name="1984", author="George Orwell", description="A dystopian novel about a totalitarian society where individual freedom is suppressed."),
    Book(name="The Catcher in the Rye", author="J.D. Salinger", description="A coming-of-age novel about a teenage boy struggling to find his place in the world."),
    Book(name="Pride and Prejudice", author="Jane Austen", description="A romantic novel about the social and economic status of women in early 19th century England.")
]

# Define a route to get all books
@app.get("/books")
async def get_books():
    return books

# Define a route to get a single book by index
@app.get("/books/{index}")
async def get_book_by_index(index: int):
    if index < 0 or index >= len(books):
        return {"error": "Index out of range"}
    #upate book description with funny name
    else:
        book = books[index]
        book.description = generate_funny_book_name(book.name)
        return book

# Define a route to add a new book
@app.post("/books")
async def add_book(book: Book):
    books.append(book)
    return {"message": "Book added successfully"}

# Define a route to update an existing book by index
@app.put("/books/{index}")
async def update_book(index: int, book: Book):
    if index < 0 or index >= len(books):
        return {"error": "Index out of range"}
    books[index] = book
    return {"message": "Book updated successfully"}

# Define a route to delete a book by index
@app.delete("/books/{index}")
async def delete_book(index: int):
    if index < 0 or index >= len(books):
        return {"error": "Index out of range"}
    del books[index]
    return {"message": "Book deleted successfully"}
