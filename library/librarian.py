def add_book(library, title, author, isbn):
    if isbn in library:
        print("This ISBN already exists.")
    else:
        library[isbn] = {
            "title": title,
            "author": author,
            "isbn": isbn,
            "available": True
        }


def remove_book(library, isbn):
    if isbn in library:
        del library[isbn]
    else:
        print("Book not found.")


def check_out_book(library, isbn):
    if isbn not in library:
        print("Book not found.")
    elif not library[isbn]["available"]:
        print("Book is already checked out.")
    else:
        library[isbn]["available"] = False


def return_book(library, isbn):
    if isbn not in library:
        print("Book not found.")
    else:
        library[isbn]["available"] = True


def display_books(library):
    for isbn, book in library.items():
        status = "Available" if book["available"] else "Checked Out"
        print(
            f'{book["title"]} by {book["author"]} '
            f'(ISBN: {book["isbn"]}) - {status}'
        )