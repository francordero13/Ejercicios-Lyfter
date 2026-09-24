
#EJERCICIO 1
class Circle:
    def __init__(self):##atributo 
        self.radius = 10

    def get_area(self):#metodo  - es la accion que le estoy pidiendo que haga
        return 3.14 * (self.radius * self.radius)

circle=Circle()
circle.get_area()



#EJERCICIO 2
class Bus:
    def __init__(self):
        self.max_passenger=50
        self.passengers=[]

    def add_passenger(self,person):
        if len(self.passengers)<self.max_passenger:
            self.passengers.append(person)
            print(f"{person.name} has boarded the bus")
        else:
            print("Bus is full")

    def remove(self,person):
        if person in self.passengers:
            self.passengers.remove(person)

        else:
            print("Esa persona no esta en el bus")



#EJERCICIO 4
class Human:
    def __init__(self, torso):
        self.torso=torso

class Torso:
    def __init__(self, head, arm, leg):
        self.head = head
        self.arm = arm
        self.leg = leg

class Head:
    def __init__(self):
            pass

class Hand:
    def __init__(self):
        pass

class Arm:
    def __init__(self,hand):
        self.hand=hand

class Leg:
    def __init__(self,feet):
        self.feet=feet

class Feet:
    def __init__(self):
            pass

hand=Hand()
arm=Arm(hand)
feet=Feet()
leg=Leg(feet)
head=Head()
torso=Torso(head,arm,leg)
human=Human(torso)



#EJERCICIO 3
import csv
class Student:
    def __init__(self, name, section, spanish, english, history, science):
        self.name = name
        self.section = section
        self.spanish = spanish
        self.english = english
        self.history = history
        self.science = science


def add_students(students):

    quantity = int(input("How many students do you want to add? "))
    for i in range(quantity):
        print(f"\nStudent {i + 1}")
        name = input("Full name: ")
        section = input("Section: ")
        spanish = int(input("Spanish grade: "))
        english = int(input("English grade: "))
        history = int(input("History grade: "))
        science = int(input("Science grade: "))
        student = Student(
            name,
            section,
            spanish,
            english,
            history,
            science
        )
        students.append(student)


def show_students(students):
    for student in students:
        print(
            f"Name: {student.name}, "
            f"Section: {student.section}, "
            f"Spanish: {student.spanish}, "
            f"English: {student.english}, "
            f"History: {student.history}, "
            f"Science: {student.science}"
        )


def show_top_students(students):
    students_sorted = sorted(
        students,
        key=lambda student: (
            student.spanish
            + student.english
            + student.history
            + student.science
        ) / 4,
        reverse=True
    )

    for student in students_sorted[:3]:
        print(
            f"Name: {student.name}, "
            f"Average: {(student.spanish + student.english + student.history + student.science) / 4:.2f}"
        )


def show_average(students):
    if not students:
        print("There are no students")
        return
    total = 0
    for student in students:
        average = (
            student.spanish
            + student.english
            + student.history
            + student.science
        ) / 4

        total = total + average
    general_average = total / len(students)
    print(f"General average: {general_average:.2f}")


def export_students(students):
    with open("students.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([
            "name",
            "section",
            "spanish",
            "english",
            "history",
            "science"
        ])
        for student in students:
            writer.writerow([
                student.name,
                student.section,
                student.spanish,
                student.english,
                student.history,
                student.science
            ])

    print("Students are exported successfully")


def import_students(students):
    try:
        with open("students.csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for data in reader:
                student = Student(
                    data["name"],
                    data["section"],
                    int(data["spanish"]),
                    int(data["english"]),
                    int(data["history"]),
                    int(data["science"])
                )
                students.append(student)
        return students
    except FileNotFoundError:
        print("There is no exported file")
        return []
