from authentication import AppAuth
from classes.Book import Book
from classes.Person import Person


class Librarian(Person):

    def __init__(self,id:int,full_name:str, age:int, id_no:str,emplyment_type:int):
        super(Librarian,self).__init__(id=id,full_name=full_name, age= age, id_no=id_no)
        self.__emplyment_type = emplyment_type

    def addBook(self, book:Book):
        AppAuth.books_list.append(book)

    def showBooksInfo(self):
        if (len(AppAuth.books_list) != 0):
            for book in AppAuth.books_list:
                book.bookInfo()
        else:
            return "There is no book in the library!"

    def showOrdersInfo(self):
        if (len(AppAuth.borrowingOrders_list) != 0):
            for order in AppAuth.borrowingOrders_list:
                order.orderInfo()
        else:
            return "There are no orders!"


    def showClientsInfo(self):
        if (len(AppAuth.clients_list) != 0):
            for client in AppAuth.clients_list:
                client.info()
        else:
            return "There are no clients!"

    def info(self):
        return super(Librarian, self) + ", Emplyment Type: " + str(self.__emplyment_type)

    def setEmplymentType(self,emplyment_type:int):
        self.__emplyment_type = emplyment_type


    def getEmplymentType(self):
        return self.__emplyment_type