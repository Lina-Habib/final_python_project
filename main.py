from authentication import AppAuth
from classes.Book import Book
from classes.Librarian import Librarian
from classes.Statics import staticVariables
from classes.Client import Client

app_auth = AppAuth()

def actionClient(id:int):
    client = app_auth.search_for_client_by_id(id)
    choice = int(print("What you want to do: \n1_Borrow book.\n2_Show Your orders.\n3-Return a book."))
    match choice:
        case 1:
            print("Choose the book: ")
            app_auth.showBooksAvailable()
            title = input()
            book= app_auth.search_for_book_by_title(title)
            order_id = app_auth.get_last_order_id()+1
            client.add_order(order_id,"Date()",id,book.getId(),staticVariables.ACTIVE)
            book.setStatus(staticVariables.INACTINE)
            print("Borrowed book successfully")

        case 2:
            client.showOrders()

        case 3:
            order_id = input("Enter Order ID: ")
            order = app_auth.search_for_order_by_id(order_id)
            client.deleteOrder(order)

        case default :
            return "Invalid Choice!"

def actionLibrarian(id:int):
    librarian = app_auth.search_for_librarian_by_id(id)
    choice = int(print("What you want to do: \n1_Show books Info.\n2_Add book.\n3-Show Orders.\n4-Show Clients."))
    match choice:
        case 1:
            librarian.showBooksInfo()

        case 2:
            book_id = app_auth.get_last_book_id() + 1
            title = input("Enter the title: ")
            description = input("Enter the description: ")
            author = input("Enter the author: ")
            book = Book(book_id,title,description,author,Book.ACTIVE)
            librarian.addBook(book)
            print("Added Book Successfully")

        case 3:
            librarian.showOrdersInfo()

        case 4:
            librarian.showClientsInfo()

        case default:
            print("Invalid Choice!")

choice = int(input("1- Login \n2- Register as client"))

match choice:
    case 1:
        fullName = input("Your Full Name: ")
        id = int(input("Your ID: "))
        for client in app_auth.clients_list:
            if client.getId() == id and client.getFullName() == fullName:
                actionClient(id)
            else:
                for librarian in app_auth.librarians_list:
                    if librarian.getId() == id and librarian.getFullName() == fullName:
                        actionLibrarian(id)
                    else:
                        print("Invalid Name or ID!")

    case 2:
        fullName = input("Your Full Name: ")
        age = input("Your age: ")
        id_no = input("Your ID no: ")
        phone_num = input("Your Phone Number: ")
        id = app_auth.get_last_client_id()+1
        client = Client(id,fullName,age,id_no,phone_num)
        app_auth.register_new_client(client)
        actionClient()


