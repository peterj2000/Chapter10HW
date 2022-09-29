class PayrollDeduction:
    
    # init method to initialize all the arguments
    def __init__(self, description, date, amnt, empID):
        self.__description= description
        self.__date= date
        self.__amnt= amnt
        self.__empID= empID
        
    # accessor method for Description
    def getDescription(self):
        return self.__description
    
    # accessor method for Date
    def getDate(self):
        return self.__date
    
    # accessor method for Amount
    def getAmount(self):
        return self.__amnt
    
    # accessor method for Employee ID number
    def getEmployeeID(self):
        return self.__empID