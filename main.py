import json
from library import librarian



# To-Do List


while True:
    answer = input("Do you want to add a new To-Do item? (y/n or exit): ")

    if answer == "exit":
        print("Thank you for using the To-Do program, come back again soon")
        break

    if answer == "y":
        todo = input("Type your new To-Do item: ")

        with open("to_do.txt", "a") as file:
            file.write(todo + "\n")

    elif answer == "n":
        answer = input("Do you want to list your To-Do items? (y/n): ")

        if answer == "y":
            with open("to_do.txt", "r") as file:
                for item in file:
                    print(item.strip())



# Library


library = {}

try:
    with open("library.json", "r") as file:
        library = json.load(file)
except FileNotFoundError:
    library = {}


def save_library():
    with open("library.json", "w") as file:
        json.dump(library, file, indent=4)


while True:
    print("\nLibrary Menu")
    print("1. Add a book")
    print("2. Display all books")
    print("3. Search for a book")
    print("4. Delete a book")
    print("5. Borrow a book")
    print("6. Return a book")
    print("7. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        title = input("Enter book title: ")
        author = input("Enter author: ")
        isbn = input("Enter ISBN: ")

        librarian.add_book(library, title, author, isbn)
        save_library()

    elif choice == "2":
        librarian.display_books(library)

    elif choice == "3":
        isbn = input("Enter ISBN to search: ")

        if isbn in library:
            book = library[isbn]
            status = "Available" if book["available"] else "Checked Out"

            print(
                f'{book["title"]} by {book["author"]} '
                f'(ISBN: {book["isbn"]}) - {status}'
            )
        else:
            print("Book not found.")

    elif choice == "4":
        isbn = input("Enter ISBN to delete: ")

        librarian.remove_book(library, isbn)
        save_library()

    elif choice == "5":
        isbn = input("Enter ISBN to borrow: ")

        librarian.check_out_book(library, isbn)
        save_library()

    elif choice == "6":
        isbn = input("Enter ISBN to return: ")

        librarian.return_book(library, isbn)
        save_library()

    elif choice == "7":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
