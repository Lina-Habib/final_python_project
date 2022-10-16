class BorrowingOrder:

    def __init__(self,id:int,date:str, client_id:int, book_id:int, status:int):
        self.__id = id
        self.__date = date
        self.__client_id = client_id
        self.__book_id = book_id
        self.__status = status

    def orderInfo(self):
        return "ID: "+str(self.__id)+", Date: " + self.__date + ", Client ID: "+ str(self.__client_id) \
               + ", Book ID: " + str(self.__book_id) + ", Status: " + str(self.__status)

    def setId(self,id:int):
        self.__id = id

    def getId(self):
        return self.__id

    def setDate(self,date:str):
        self.__date = date

    def getDate(self):
        return self.__date

    def setClientId(self,client_id:int):
        self.__client_id = client_id

    def getClientId(self):
        return self.__client_id

    def setBookId(self,book_id:int):
        self.__book_id = book_id

    def getBookId(self):
        return self.__book_id

    def setStatus(self,status:int):
        self.__status = status

    def getStatus(self):
        return self.__status

