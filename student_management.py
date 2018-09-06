def adding_students(students):
    """inputs students, name, age and favourite colour into a list.

    Args:
        students (list): The list of students.

    Returns:
        updated list of students.
    """
    adding = True
    #Checks students name is using letters.
    while adding:
        student = input("\nName:").strip().title()
        if student.isalpha():
            adding = False
            run = True
            #Checks age is viable.
            while run:
                try:
                    age = int(input("Age:"))
                    if age < 0 or age > 150:
                        print("\nInvalid age, please enter correctly\n")
                    else:
                        run = False
                        cool = True
                        #Checks the students colour is using letters.
                        while cool:
                            colour = input("Favourite colour:").strip().title()
                            if colour.isalpha():
                                students.append([student, age, colour])
                                print()
                                cool = False
                            else:
                                print("\nPlease enter A-Z")
                except ValueError:
                    print("Please enter a number")
        elif student in students:
            print("This student is already in the system," 
                  "please differentiate students with the same name")
        else:
            print("\nPlease enter A-Z")
    return students


def print_students(students):
    """prints list of students names, ages and colours.

    Args:
        students (list): the list of students.
    """
    # Checks that there are students in the list before printing.
    if len(students) > 0:
        print("\n_--_--Students--_--_")
        for student in students:
            name = student[0]
            number = student[1]
            light = student[2]
            print("- {}, {}, {}\n".format(name, number, light))
    else:
        print("\nYour list has no students\n")


def remove_students(students):
    """removes a students name, age and colour.

    Args:
        students (list): the list of students.

    Returns: the updated list of students.
    """
    #Checks there are students to remove.
    if len(students) > 0:
        remove = True
        while remove:
            name = input("\nStudent's name to remove:").strip().title()
            if name.isalpha():
                remove = False
                play = True
                #Checks for value errors
                while play:
                    try:
                        number = int(input("Student's age:"))
                        play = False
                    except ValueError:
                        print("Please enter a number")
                    if number < 0 or number > 150:
                        print("Invalid age, please enter correctly")
                        play = True
                    else:
                        minus = True
                        #Checks the student colour is using letters and whether it is int the list
                        while minus:
                            light = input("Student's favourite colour:").strip().title()
                            if light.isalpha():
                                if [name, number, light] in students:
                                    students.remove([name, number, light])
                                    minus = False
                                    print()
                                else:
                                    print("\nThere no student with this profile: {}, {}, {}\n".format(name, number, light))
                                    print_students(students)
                                    remove = True
                                    minus = False
                            else:
                                print("\nPlease enter A-Z")
            else:
                print("\nPlease enter A-Z")
    else:
        print("\nThere are no students to remove\n")
    return students


def main():
    """gives the main menu for option.

    Returns: returns of functions to main code.
    """
    students = []
    while True:
        ask = True
        #Brings up menus
        while ask:
            try:
                option = int(input("1) Add a new student\n"
                                   "2) Print all students names\n"
                                   "3) Remove a student\n"
                                   "4) Exit\n"
                                   "Your choice: "))
                ask = False
            except ValueError:
                print("\nPlease enter a number\n")
        #Links functions to the option choosen
        if option == 1:
            students = adding_students(students)
        elif option == 2:
            print_students(students)
        elif option == 3:
            students = remove_students(students)
        elif option == 4:
            print("Thank you!")
            exit()
        else:
            print("\nPlease enter a number between 1 and 4\n")


main()
