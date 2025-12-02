books = {}

def add_book():
    print("\n--- Add a Book ---")
    isbn = input("Enter ISBN (13 digits): ").strip()

    while not isbn.isdigit() or len(isbn) != 13:
        print("Invalid ISBN. It must be exactly 13 digits and no letters.")
        isbn = input("Enter ISBN (13 digits): ").strip()

    if isbn in books:
        print("A book with this ISBN already exist.")

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


add_book() 
