import csv

def add_students(students):
    quantity = int(input("How many students do you want to add?"))

    for i in range(quantity):
        print(f"\nstudents {i+1}")
        name=input("full name: ")
        section=input("section: ")
        spanish=int(input("Spanish grade: "))
        english=int(input("English grade: "))
        history=int(input("History grade: "))
        sciencie=int(input("Science grade: "))

        student= {
            "name":name,
            "section":section,
            "spanish":spanish,
            "english":english,
            "history":history,
            "science":sciencie,
    }
        students.append(student)

def show_students(students):
    for student in students:
        print(student)

def show_top_students(students):
    students_sorted=sorted(
        students,
        key=lambda student: (
            student["spanish"]
            + student["english"]
            + student["history"]
            + student["science"]
        ) /4,
        reverse=True
    )
    for student in students_sorted[:3]:
        print(student)

def show_average(students):
    if not students: #Verifica si hay estudiantes
        print("There is not students")
        return #nos saca de la funcion
    total=0 #esto es para ir acumulando el promedio de cada estudiantes
    for student in students: #por cada estudiante que exista en students has:
        average=(
                student["spanish"]
                + student["english"]
                + student["history"]
                + student["science"]
                ) /4
        total=total+average
    general_average = total/len(students) #Len nos da la cantidad de elementos de una lista, o sea, cantidad de estudiantes en este caso
    print(f"General average: {general_average: .2f}")

def export_students(students):
    with open ("students.csv","w",newline="",encoding="utf-8") as file: #Aca lo que hacemos es que creamos el archivo students.json - Usamos with para que cuando se termine el bucle el mismo python sea quien cierre el archivo y no tener que porner una linea de codigo file.close(students)
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
                student["name"],
                student["section"],
                student["spanish"],
                student["english"],
                student["history"],
                student["science"]
                ])
    print ("students are exported successfully")

def import_students(students):
    try:
        with open("students.csv","r",newline="",encoding="utf-8") as file:
            reader = csv.DictReader(file)
            students=list(reader)

        for student in students:
            student["spanish"]=int(student["spanish"])
            student["english"]=int(student["english"])
            student["science"]=int(student["science"])
            student["history"]=int(student["history"])
        return students
    
    except FileNotFoundError:
        print("There is not exported file")
        return[]