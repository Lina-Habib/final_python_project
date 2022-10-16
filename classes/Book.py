class Book:

    def __init__(self,id:int, title:str, description:str, author:str, status:int):
        self.__id = id
        self.__title = title
        self.__description = description
        self.__author = author
        self.__status = status


    def bookInfo(self):
        return "ID: "+str(self.__id)+", Title: "+self.__title + ", Description: " +self.__description\
               +", Author: " + self.__author + ", Status: "+str(self.__status)

    def setId(self,id):
        self.__id = id

    def getId(self):
        return self.__id

    def setTitle(self,title):
        self.__title = title

    def getTitle(self):
        return self.__title

    def setDescription(self,description):
        self.__description = description

    def getDescription(self):
        return self.__description

    def setAuthor(self,author):
        self.__author = author

    def getAuthor(self):
        return self.__author

    def setStatus(self,status):
        self.__status = status

    def getStatus(self):
        return self.__status


