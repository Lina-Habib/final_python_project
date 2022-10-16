from authentication import AppAuth
from classes.BorrowingOrder import BorrowingOrder
from classes.Person import Person


class Client(Person):

    def __init__(self,id:int,full_name:str, age:int, id_no:str,phone_number:str):
        super(Client,self).__init__(id=id, full_name=full_name, age=age, id_no=id_no)
        self.__phone_number = phone_number

    def add_order(self, order:BorrowingOrder):
        AppAuth.borrowingOrders_list.append(order)
        print("Add Order Successfully")

    def deleteOrder(self, order:BorrowingOrder):
        for item in AppAuth.borrowingOrders_list:
            if order.getClientId() == self.getId() and order.getId() == item.getId():
                AppAuth.borrowingOrders_list.remove(order)
            else:
                print("This order is not exist!")

    def showOrders(self):
        for order in AppAuth.borrowingOrders_list:
            if order.getId() == self.getId():
                order.orderInfo()
            else:
                print("There are no orders exist!")

    def info(self):
        return  super(Client, self)+ ", Phone Number: "+self.__phone_number


    def setPhoneNumber(self,phone_number:str):
        self.__phone_number = phone_number


    def getPhoneNumber(self):
        return self.__phone_number
