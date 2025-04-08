from Person import Person

class Student(Person):
    def __init__(self, name, age, field_of_study, year_of_study, score_avg):
        super().__init__(name, age)
        self.field_of_study = field_of_study
        self.year_of_study = year_of_study
        self.score_avg = score_avg
    
    def getFieldOfStudy(self):
        return self.field_of_study
    
    def getYearOfStudy(self):
        return self.year_of_study
    
    def getScoreAvg(self):
        return self.score_avg
    
    def toPrint(self):
        print("     [Student]")
        super().toPrint()
        print("     Field Of Study: " + self.getFieldOfStudy())
        print("     Years Of Study: " + str(self.getYearOfStudy()))
        print("     Score Avg: " + str(self.getScoreAvg()))

    def buildCsvRow(self,id):
        super().buildCsvRow(id)
        self._row["field_of_study"] = self.getFieldOfStudy()
        self._row["years_of_study"] = self.getYearOfStudy()
        self._row["score_avg"] = self.getScoreAvg()