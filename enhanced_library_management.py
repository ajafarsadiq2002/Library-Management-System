# Simple Library Management System

# Library class to handle book operations

class Library:
    def __init__(self, book_list=None, name=''):
        self.books = {}
        self.name = name  # Name of the library
        if book_list:
            for book in book_list:
                self.books[book["id"]] = {
                    "title": book["title"],
                    "author": book["author"],
                    "Borrowed": False
                }

        print(f"Library '{self.name}' initialized.")

    def add_book(self, book_id, book_name, book_author):
        # Validate book ID
        if not self.is_valid_book_id(book_id):
            print("Invalid book ID. It must be a positive number.")
            return
        # Validate book name and author
        if not book_name.strip() or not book_author.strip():
            print("Book name and author cannot be empty.")
            return
        # Check for duplicate book ID
        if book_id in self.books:
            print(f"Book ID {book_id} already exists.")
            return
        # Add the book
        self.books[book_id] = {
            "title": book_name,
            "author": book_author,
            "Borrowed": False
        }
        print(f"Book '{book_name}' added successfully.")
    
    def borrow_books(self, book_id):
        # Validate book ID
        if not self.is_valid_book_id(book_id):
            print("Invalid book ID. It must be a positive number.")
            return
        # Check if the book exists
        if book_id not in self.books:
            print(f"Book ID {book_id} not found.")
            return
        # Check if the book is already borrowed
        if self.books[book_id]["Borrowed"]:
            print(f"The book '{self.books[book_id]['title']}' is already borrowed.")
        else:
            self.books[book_id]["Borrowed"] = True
            print(f"You have successfully borrowed '{self.books[book_id]['title']}'.")
    
    def return_books(self, book_id):
        # Validate book ID
        if not self.is_valid_book_id(book_id):
            print("Invalid book ID. It must be a positive number.")
            return
        # Check if the book exists
        if book_id not in self.books:
            print(f"Book ID {book_id} not found.")
            return
        # Check if the book is actually borrowed
        if not self.books[book_id]["Borrowed"]:
            print(f"The book '{self.books[book_id]['title']}' is not borrowed.")
        else:
            self.books[book_id]["Borrowed"] = False
            print(f"You have successfully returned '{self.books[book_id]['title']}'.")
    
    def display_books(self):
        if not self.books:
            print("No books available in the library.")
            return
        print("Books available in the library:")
        for book_id, details in self.books.items():
            status = "Borrowed" if details["Borrowed"] else "Available"
            print(f"Book ID: {book_id}, Title: {details['title']}, Author: {details['author']}, Status: {status}")

    def is_valid_book_id(self, book_id):
        # Validate that the book_id is a positive number
        return book_id.isdigit() and int(book_id) > 0

# Main function

def main():
    # Initialize the library with a sample list of books and a name
    sample_books = [
        {"id": "1", "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
        {"id": "2", "title": "1984", "author": "George Orwell"},
        {"id": "3", "title": "To Kill a Mockingbird", "author": "Harper Lee"}
    ]
    library_name = "My Library"
    library = Library(sample_books, library_name)
    
    while True:
        print("\nLibrary Management System -", library.name)
        print("1. Add a book")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Display all books")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            book_id = input("Enter the book ID: ")
            book_name = input("Enter the book name: ")
            book_author = input("Enter the book author: ")
            library.add_book(book_id, book_name, book_author)

        elif choice == "2":
            book_id = input("Enter the book ID to borrow: ")
            library.borrow_books(book_id)

        elif choice == "3":
            book_id = input("Enter the book ID to return: ")
            library.return_books(book_id)

        elif choice == "4":
            library.display_books()

        elif choice == "5":
            print("Exiting the Library Management System.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()