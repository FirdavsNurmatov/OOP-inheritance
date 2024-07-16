class Developer :

    def __init__(self,surname,position,salary) :
        self.surname = surname
        self.position = position
        self.salary = salary

class SoftwareEngineer(Developer) :

    def __init__(self, surname, position, salary,bonus,department) :
        super().__init__(surname, position, salary)
        self.bonus = bonus
        self.department = department
        self.dct = {}

lst = [
    SoftwareEngineer("Anvar", "Junior", 500, 100, "1-bo'lim"),
    SoftwareEngineer("Asror", "Middle", 1500, 500, "2-bo'lim"),
    SoftwareEngineer("Kamola", "Senior", 2500, -100, "3-bo'lim"),
    SoftwareEngineer("Vali", "Junior", 500, -100, "1-bo'lim"),
    SoftwareEngineer("Davron", "Middle", 1500, 100, "2-bo'lim"),
    SoftwareEngineer("Bahodir", "Senior",2500, -100, "3-bo'lim"),
    SoftwareEngineer("Farrux", "Junior", 500, 100, "1-bo'lim"),
    SoftwareEngineer("Jamila", "Middle", 1500, 200, "2-bo'lim"),
    SoftwareEngineer("Jasur", "Senior", 2500, 500, "3-bo'lim"),
    SoftwareEngineer("Komila", "Junior", 500, -100, "1-bo'lim")
]

departments = {}
for dev in lst:
    if dev.department not in departments:
        departments[dev.department] = 0
    departments[dev.department] += dev.salary + dev.bonus


for department, total in departments.items():
    print(f"{department}: {total}")