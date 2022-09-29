
class Employee:
    
    
    def __init__(self, name, ID, depart, jobt, sal):

        self.__name= name
        self.__ID= ID
        self.__depart= depart
        self.__jobt= jobt
        self.__sal= sal
    


    def getName(self):
        return self.__name
    

    def getID(self):
        return self.__ID
    

    def getDepartment(self):
        return self.__depart
    
    def getJobTitle(self):
        return self.__jobt
    


    def getSalary(self):
        return self.__sal