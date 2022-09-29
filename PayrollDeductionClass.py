

class PD:
    
    def __init__(self, descrip, date, amount, eID):

        self.__descrip= descrip
        self.__date= date
        self.__amount= amount
        self.__eID= eID



    def getDescription(self):
        return self.__descrip
    

    def getDate(self):
        return self.__date
    
    
    def getAmount(self):
        return self.__amount
    

    def getEmployeeID(self):
        return self.__eID