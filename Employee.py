from Person import Person

class Employee(Person):
    def __init__(self, name, age, filed_of_work, salary):
        super().__init__(name, age)
        self.salary = salary
        self.field_of_work = filed_of_work

    def getFieldOfWork(self):
        return self.field_of_work
    
    def getSalary(self):
        return self.salary
    
    def toPrint(self):
        print("     [Employee]")
        super().toPrint()
        print("     Field Of Work: " + str(self.getSalary()))
        print("     Salary: " + self.getFieldOfWork())

    def buildCsvRow(self,id):
        super().buildCsvRow(id)
        self._row["filed_of_work"] = self.getFieldOfWork()
        self._row["salary"] = self.getSalary()