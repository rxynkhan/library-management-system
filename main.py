import random


class Book:
    def __init__(self, title, author, book_id):
        self.title = title
        self.author = author
        self.book_id = book_id
        self.available = True


class Library:
    def __init__(self):
        self.books = []

    def generate_unique_id(self):
        while True:
            new_id = random.randint(1000, 9999)

            id_exists = False

            for book in self.books:
                if book.book_id == new_id:
                    id_exists = True

            if id_exists == False:
                return new_id

    def add_book(self, title, author):
        book_id = self.generate_unique_id()

        new_book = Book(title, author, book_id)

        self.books.append(new_book)

        print("Book added successfully.")
        print("Book ID:", book_id)

    def view_books(self):
        if len(self.books) == 0:
            print("Library is empty.")

        else:
            print("\nAll Books")

            for book in self.books:

                if book.available == True:
                    status = "Available"
                else:
                    status = "Borrowed"

                print(
                    "ID:", book.book_id,
                    "| Title:", book.title,
                    "| Author:", book.author,
                    "| Status:", status
                )

    def search_book(self):
        if len(self.books) == 0:
            print("Library is empty.")
            return

        print("\nSearch by:")
        print("1. Title")
        print("2. Author")
        print("3. ID")

        choice = input("Choose: ")

        found = False

        if choice == "1":

            search_title = input("Enter title: ").lower()

            for book in self.books:

                if search_title in book.title.lower():
                    print(
                        "ID:", book.book_id,
                        "| Title:", book.title,
                        "| Author:", book.author
                    )

                    found = True

        elif choice == "2":

            search_author = input("Enter author: ").lower()

            for book in self.books:

                if search_author in book.author.lower():
                    print(
                        "ID:", book.book_id,
                        "| Title:", book.title,
                        "| Author:", book.author
                    )

                    found = True

        elif choice == "3":

            search_id = int(input("Enter book ID: "))

            for book in self.books:

                if book.book_id == search_id:
                    print(
                        "ID:", book.book_id,
                        "| Title:", book.title,
                        "| Author:", book.author
                    )

                    found = True

        else:
            print("Invalid choice.")
            return

        if found == False:
            print("Book not found.")

    def borrow_book(self, book_id):

        found = False

        for book in self.books:

            if book.book_id == book_id:

                found = True

                if book.available == True:
                    book.available = False
                    print("You borrowed:", book.title)

                else:
                    print("This book is already borrowed.")

        if found == False:
            print("Book ID not found.")

    def return_book(self, book_id):

        found = False

        for book in self.books:

            if book.book_id == book_id:

                found = True

                if book.available == False:
                    book.available = True
                    print("Book returned:", book.title)

                else:
                    print("This book was not borrowed.")

        if found == False:
            print("Book ID not found.")

    def remove_book(self, book_id):

        found = False
        book_to_remove = None

        for book in self.books:

            if book.book_id == book_id:
                found = True
                book_to_remove = book

        if found == True:

            self.books.remove(book_to_remove)

            print("Book removed:", book_to_remove.title)

        else:
            print("Book ID not found.")

    def show_statistics(self):

        total_books = len(self.books)

        available_books = 0
        borrowed_books = 0

        for book in self.books:

            if book.available == True:
                available_books = available_books + 1

            else:
                borrowed_books = borrowed_books + 1

        print("\nLibrary Statistics")

        print("Total books:", total_books)
        print("Available books:", available_books)
        print("Borrowed books:", borrowed_books)


library = Library()


book1 = Book("1984", "George Orwell", 101)
book2 = Book("Animal Farm", "George Orwell", 102)
book3 = Book("The Alchemist", "Paulo Coelho", 103)
book4 = Book("To Kill a Mockingbird", "Harper Lee", 104)
book5 = Book("The Great Gatsby", "F. Scott Fitzgerald", 105)
book6 = Book("Atomic Habits", "James Clear", 106)
book7 = Book("Deep Work", "Cal Newport", 107)
book8 = Book("The Psychology of Money", "Morgan Housel", 108)
book9 = Book("Rich Dad Poor Dad", "Robert Kiyosaki", 109)
book10 = Book("The Hobbit", "J.R.R. Tolkien", 110)


library.books.append(book1)
library.books.append(book2)
library.books.append(book3)
library.books.append(book4)
library.books.append(book5)
library.books.append(book6)
library.books.append(book7)
library.books.append(book8)
library.books.append(book9)
library.books.append(book10)


while True:

    print("\n==============================")
    print("LIBRARY MANAGEMENT SYSTEM")
    print("==============================")

    print("1. Add a book")
    print("2. View all books")
    print("3. Search for a book")
    print("4. Borrow a book")
    print("5. Return a book")
    print("6. Remove a book")
    print("7. Show statistics")
    print("8. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        title = input("Enter book title: ")
        author = input("Enter author name: ")

        library.add_book(title, author)

    elif choice == "2":

        library.view_books()

    elif choice == "3":

        library.search_book()

    elif choice == "4":

        book_id = int(input("Enter book ID: "))

        library.borrow_book(book_id)

    elif choice == "5":

        book_id = int(input("Enter book ID: "))

        library.return_book(book_id)

    elif choice == "6":

        book_id = int(input("Enter book ID: "))

        library.remove_book(book_id)

    elif choice == "7":

        library.show_statistics()

    elif choice == "8":

        print("Goodbye.")
        break

    else:

        print("Invalid choice.")
