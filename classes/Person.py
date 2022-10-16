class Person:

    def __init__(self,id:int,full_name:str, age:int, id_no:str):
        self.__id = id
        self.__full_name = full_name
        self.__age = age
        self.__id_no = id_no

    def info(self):
        return "ID: "+str(self.__id)+", Full Name: "+ self.__full_name + ", Age: "+str(self.__age)\
               +", ID Number: "+self.__id_no


    def setId(self,id:int):
        self.__id = id

    def getId(self):
        return self.__id

    def setFullName(self,full_name:str):
        self.__full_name = full_name


    def getFullName(self):
        return self.__full_name


    def setAge(self,age:int):
        self.__age = age

    def getAge(self):
        return self.__age


    def setIdNo(self,id_no:str):
        self.__id_no = id_no

    def getIdNo(self):
        return self.__id_no

