def show_menu():
    print("===== STUDENT CONTROL SYSTEM =====")
    print("1. Add students")
    print("2. Show students")
    print("3. Show top 3 students")
    print("4. Show average")
    print("5. Export students")
    print("6. Import students")
    print("7. Exit")

    while True: #Esto quiere decirle al sistema, repite esto hasta que se cumpla
        try:
            option = int(input("Choose an option: "))
            if 1 <= option <= 7:
                return option #Aqui le decimos al WhileTrue que si todo es correcto entonces nos saque del bucle
            print("Invalid option, please use one from 1 to 7")

        except ValueError:
            print("Please enter a number.")