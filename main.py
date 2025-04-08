import os
import pandas as pd
import json
from enum import Enum, auto
from Person import Person
from Employee import Employee
from Student import Student

class PersonType(Enum):
    PERSON = auto()
    STUDENT = auto() 
    EMPLOYEE = auto()


def printMenuAndGetUserSelection():
    print("1. Save a new Entry")
    print("2. Search by ID")
    print("3. Print ages avg")
    print("4. Print all names")
    print("5. Print all IDs")
    print("6. Print all entries")
    print("7. Print entry by index")
    print("8. Save all data")
    print("9. Exit")
    userSelection = input("Please enter your choice : ")
    return userSelection


def intPropertyChecker(digit_property_name):
    intValue = input(digit_property_name + ": ")
    while (not intValue.isdigit()):
        print("Error: " + digit_property_name + "  must be a number " + intValue + " is not a number")
        intValue =  input(digit_property_name + ": ")
    return int(intValue)


def enumPersonType(type_from_user):
    if type_from_user == "Employee":
        type = PersonType.EMPLOYEE
    elif type_from_user == "Student":
        type = PersonType.STUDENT
    else:
        type = PersonType.PERSON
    return type


def personTypeDecider(type, name, age):
    if type == PersonType.STUDENT:
        filed_of_study = input("Field Of Study: ")
        year_of_study = intPropertyChecker("Years Of Study")
        score_avg = intPropertyChecker("Score Avg")
        person = Student(name, age, filed_of_study, year_of_study, score_avg)
    elif type == PersonType.EMPLOYEE:
        salary = intPropertyChecker("Salary")
        filed_of_work = input("Field Of Work: ")
        person = Employee(name, age, filed_of_work, salary)
    elif type == PersonType.PERSON:
        person = Person(name, age)
    return person


def saveNewEntry(db, counter):      
    id = intPropertyChecker("ID")
    id_str = str(id)
    if id_str in db:
        print("Error: ID already exists: " + id_str)
        return 0
    name = input("Name: ")
    age = intPropertyChecker("Age")
    type_from_user = input("Which type of person (Employee,Student,Other) ? ")
    type = enumPersonType(type_from_user)
    person = personTypeDecider(type,name,age)
    db[id_str] = person
    persons_map_by_idx[counter] = id_str
    print("ID [ " + id_str + " ] saved successfuly")
    return age


def searchById(db):
    id =  input("Please enter the ID you want to look for: ")
    try:
        person = db[id]
        print("ID: " + id)
        person.toPrint()
    except KeyError:
        print("Error: ID " + id + " is not saved")


def avgAges(total_ages, db):
    try:
        return total_ages / len(db)
    except ZeroDivisionError:
        print("Error: Division by Zero, Reason -> Repository is empty")
        return 0.0


def printAllNames(db):
    for index, value in enumerate(db.values()):
        print(str(index) + "." + " " + value.getName())


def printAllIds(db):
    for index, value in enumerate(db.keys()):
        print(str(index) + "." + " " + value)


def printAllEntries(db):
    for index, idxValue in enumerate(db.keys()):
        print(str(index) + "." + " " + idxValue)   
        person = db[idxValue]
        person.toPrint()


def printEntryByIdx(db):
    inputIdx = intPropertyChecker("Index")
    try :
        print(str(inputIdx) + "." + " " + persons_map_by_idx[inputIdx])
        db[persons_map_by_idx[inputIdx]].toPrint()
    except KeyError:
        print("Error: Index [" + str(inputIdx) + "] out of range. Repository size is [" + str(len(db)) + "]")


def buildDataWithHeader(db):
    result = []
    for it in db.items():
        it[1].buildCsvRow(it[0])
        result.append(it[1].getCsvRow())
    return result


def saveAllData(db):
    output_file_name =  input("What is your output file name ? ")
    curr_directory = os.getcwd()
    rows = buildDataWithHeader(db)
    df = pd.DataFrame(rows)
    df.to_csv(curr_directory + "/" + output_file_name, index=False)


persons = {}
total_ages = 0.0
persons_map_by_idx = {}
personIndex = 0
exitFlag = False

print("Welcome to my first python program!")

while True:
    try:
        userSelection = printMenuAndGetUserSelection()
        if userSelection == "1":
            total_ages += saveNewEntry(persons, personIndex)
            personIndex = personIndex + 1
        elif userSelection == "2":
            searchById(persons)
        elif userSelection == "3":
            print(avgAges(total_ages, persons))  
        elif userSelection == "4":
            printAllNames(persons)
        elif userSelection == "5":
            printAllIds(persons)
        elif userSelection == "6":
            printAllEntries(persons)
        elif userSelection == "7":
            printEntryByIdx(persons)
        elif userSelection == "8":
            saveAllData(persons)
        elif userSelection == "9":
            while True:
                    userSelection = input("Are you sure ? (y/n)")
                    if userSelection == "y":
                        exitFlag = True
                        break
                    elif userSelection == "n":
                        break
            if exitFlag:
                 break
        else:
            print("Option [" + userSelection + "] does not exist. Please try again")
    except KeyboardInterrupt:
        print("\nUser decided to quit")
        break;
    except Exception as e:
        print("Some error occured :" + str(e))
        
print("Goodbye!")
