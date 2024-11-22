import add_books
import view_all_books

all_books = []

while True:
    print("Welcome to Library Management System")
    print("0. Exit")
    print("1. Add Books")
    print("2. View All Books")

    menu = input("Select a option from the list: ")

    if menu == "0":
        print("Thanks for using the Library Management System ")
        break
    elif menu == "1":
        all_books = add_books.add_books(all_books)
    elif menu == "2":
        view_all_books.view_all_books(all_books)
    else:
        print("Please, Choose a valid Option!!!")