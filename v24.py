class Person :

    def __init__ (self,name,adress) :
        self.name = name
        self.adress = adress

    def getAddress(self) -> str:
        return self.adress
    
    def getName(self) -> str:
        return self.name

    def setAddress(self,address = str) -> None:
        self.adress = address
        print(self.adress)
    
    def toString(self) -> str:
        return f"{self.getName()}({self.getAddress()})"

class Student(Person) :

    def __init__(self, name, adress,numCourses: int = 0):
        super().__init__(name, adress)
        self.numCourses = numCourses
        self.courses = []
        self.grades = []
    
    def addCourseGrade(self,course: str,grade: int) :
        self.courses.append(course)
        self.grades.append(grade)

    def printGrades(self) :
        for i in self.grades :
            print(i, end = " ")

    def getAvarageGrade(self) :
        x = sum(self.grades) / len(self.grades)
        return x

    def toString(self) :
        return f"Student: {self.name}({self.adress})"

class Teacher(Person) :

    def __init__(self, name, adress,numCourses: int = 0):
        super().__init__(name, adress)
        self.numCourses = numCourses
        self.courses = []
    
    def addCourse(self,course: str) :
        if course in self.courses :
            return False
        else :
            self.courses.append(course)

    def removeCourse(self,course: str) :
        count = 0
        for i in self.courses :
            if i == course :
                count = 1
                self.courses.remove(i)
        if count == 0 :
            return False

    def toString(self) :
        return f"Teacher: {self.name}({self.adress})"


# user = Person('Firdavs','Qibray')
# user = Student('Zufar','Bobojonov')
# user = Teacher("Samiya","Tashkent")

# print(user.getAddress())
# user.addCourseGrade("Math",5)
# user.addCourseGrade("Biology",4)
# print(user.addCourse("Samiya"))
# print(user.toString())
# print(user.removeCourse("Sami"))
# print(user.toString())
# user.addCourseGrade("Geography",3)
# user.addCourseGrade("English",5)
# user.printGrades()
# print(user.setAddress("Fargona"))
# print(user.getAddress())
# print(user.getName())
# print(user.toString())