def main(): #johnray
    while True:
        print("\n=== Library Management System ===")
        print("1. Add a Book")
        print("2. Edit Existing Book")
        print("3. Delete a Book")
        print("4. List All Books")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_book()
        elif choice == "2":
            edit_existing_book()
        elif choice == "3":
            delete_book()
        elif choice == "4":
            list_all_books()
        elif choice == "5":
            print("Exiting program... Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

books = {} #empty dict

def add_book():

    print("\n--- Add a Book ---")
    isbn = input("Enter ISBN (13 digits): ").strip()

    while not isbn.isdigit() or len(isbn) != 13:
        print("Invalid ISBN. It must be exactly 13 digits and no letters.")
        isbn = input("Enter ISBN (13 digits): ").strip()

    if isbn in books:
        print("A book with this ISBN already exist.")
        return

    title = input("Enter Title: ").strip().title()
    author = input("Enter Author: ").strip().title()

    if title == "" or author == "":
        print("Error: Title and Author cannot be empty.")
        return

    books[isbn] = {
        "title": title,
        "author": author,
        "status": "Available"
    }

    print(f"Book '{title}' added successfully.")

def edit_existing_book(): #liezel
    pass

def delete_book(): #vincent
    print("\n--- Delete a Book ---")
    isbn = input("Enter ISBN of the book to delete: ").strip()

    if isbn not in books:
        print("Book not found.")
        return

    confirm = input(f"Are you sure you want to delete '{books[isbn]['title']}'? (y/n): ").lower()

    if confirm == "y":
        del books[isbn]
        print("Book deleted successfully.")
    else:
        print("Delete cancelled.")

def list_all_books(): #chelzy
    print("\n--- List All Books ---")
    if not books:
        print("No books in the system.")
        return
    for isbn, book in books.items():
        print(f"ISBN: {isbn}, Title: {book['title']}, Author: {book['author']}, Status: {book['status']}")


main()
