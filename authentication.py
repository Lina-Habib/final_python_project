from classes.Client import Client
from classes.Statics import staticVariables
from classes.Book import Book
from classes.Librarian import Librarian
from classes.BorrowingOrder import BorrowingOrder

class AppAuth:

    clients_list: list[Client] = [
        Client(1, "Ahmad", 22, "3123", "123"),
        Client(2, "Sami", 23, "3123", "456"),
        Client(3, "Zain", 21, "3123", "789"),
    ]

    librarians_list: list[Librarian] = [
        Librarian(1, "Mohammed", 30, "3123", staticVariables.FULL),
        Librarian(2, "Basem", 25, "3123", staticVariables.PART),
    ]

    books_list = list[Book] = [
        Book(1, "Database", "database description", "", staticVariables.ACTIVE),
        Book(2, "Operating System", "operating system description", "", staticVariables.ACTIVE),
        Book(3, "Security", "security description", "", staticVariables.INACTINE)
    ]
    borrowingOrders_list = list[BorrowingOrder] = [
        BorrowingOrder(1, "22/3/2022", 1, 1, staticVariables.ACTIVE),
        BorrowingOrder(2, "1/5/2022", 2, 2, staticVariables.ACTIVE),
        BorrowingOrder(3, "30/9/2022", 3, 3, staticVariables.ACTIVE)
    ]

    def get_last_client_id(self):
        return self.clients_list[len(self.clients_list) - 1].get_id()

    def get_last_book_id(self):
        return self.books_list[len(self.books_list) - 1].get_id()

    def get_last_order_id(self):
        return self.borrowingOrders_list[len(self.borrowingOrders_list) - 1].get_id()

    def register_new_client(self, client: Client):
        if not self.check_if_client_exsist(client.getFullName()):
            self.clients_list.append(client)
        else:
            print("Client already Used!")

    def check_if_client_exsist(self, fullName: str):
        for item in self.clients_list:
            if item.getFullName() == fullName:
                return True
        return False

    def get_clients_list(self):
        return self.clients_list

    def search_for_client_by_id(self, id: int):
        if self.clients_list == None or len(self.clients_list) == 0:
            return None
        else:
            for item in self.clients_list:
                if item.get_id() == id:
                    return item
    def search_for_librarian_by_id(self, id: int):
        if self.librarians_list == None or len(self.librarians_list) == 0:
            return None
        else:
            for item in self.librarians_list:
                if item.get_id() == id:
                    return item

    def search_for_order_by_id(self, id: int):
        if self.borrowingOrders_list == None or len(self.borrowingOrders_list) == 0:
            return None
        else:
            for item in self.borrowingOrders_list:
                if item.get_id() == id:
                    return item

    def search_for_book_by_title(self, title: str):
        if self.books_list == None or len(self.books_list) == 0:
            return None
        else:
            for item in self.books_list:
                if item.getTitle() == title:
                    return item

    def showBooksAvailable(self):
        for book in self.books_list:
            if book.getStatus() == staticVariables.ACTIVE:
                print(book.getTitle())
