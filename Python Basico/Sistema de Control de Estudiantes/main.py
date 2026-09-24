from actions import add_students, show_students,show_top_students,show_average, export_students,import_students
from menu import show_menu

def main():
    students = []

    while True:
        option = show_menu()
        if option==1:
            add_students(students)
        if option==2:
            show_students(students)
        if option==3:
            show_top_students(students)
        if option==4:
            show_average(students)
        if option==5:
            export_students(students)
        if option==6:
            import_students(students)
        if option==7:
            break

if __name__ == "__main__":
    main()