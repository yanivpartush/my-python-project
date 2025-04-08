class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
        self._row = {}

    def getName(self):
        return self._name
    
    def setName(self, name):
        self._name = name

    def getAge(self):
        return self._age

    def setAge(self, age):
        self._age = age
    
    def toPrint(self):
        print("     Name: " + self.getName())
        print("     Age: " + str(self.getAge()))

    def buildCsvRow(self,id):
        self._row["id"] = id
        self._row["name"] = self.getName()
        self._row["age"] = self.getAge() 

    def getCsvRow(self):
        return self._row

if __name__ == "__main__":
    test_name = "test_name"
    test_age = 80
    person = Person(test_name, test_age)
    if person.getAge() != test_age:
        print("Error: Age should be " + str(test_age) + " but i got " + str(person.getAge()))
    if person.getName() != test_name:
        print("Error: Name should be " + test_name + " but i got " + str(person.getName()))