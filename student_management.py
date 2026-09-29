#student record system

students=[]

def plus():
    rollno= input("enter rollno ; ")
    name =input("enter name ; ")
    branch =input("Enter Branch: ")
    subjects=input("enter subject and seperate them with comma")

    subj=[]
    for i in subjects.split(","):
        i = i.strip()
        if i != "":
            subj.append(i)

    p = (roll_no, name, branch, subjects)
    students.append(p)

    print("Student added ")


def see():
    if len(students)== 0:
        print("empty record")
        return

    for i in students:
        print("Roll No:", i[0])
        print("Name:", i[1])
        print("Branch:",i[2])
        print("Subjects: - ",i[3])


def search():
    rn = input("enter rollno")
    p= False

    for i in students:
        if i[0] == rn:
            print("Student Found")
            print("Rollno ", i[0])
            print("name ", i[1])
            print("Branch:", it[2])
            print("Subjects - "i[3])
            p= True
            break

    if p== False:
        print("missing student")


def update():
    rollno = input("enter rollno ")

    for i in range(len(students)):
        if students[i][0] ==rollno:
            name = input("Enter new name")
            branch = input("Enter branch ")
            subjects= input("Enter subjects seperate by commas")

            subj= []
            for j in subjects.split(","):
                j=j.strip()
                if j != "":
                    subj.append(j)

            students[i] = (rollno, name, branch, subjects)

            print(" record updated ")
            return
    print("not found")


def delete():
    rn= input("Enter rollno ")

    for i in range(len(students)):
        if students[i][0] == rn:
            students.pop(i)
            print("Student record deleted")
            return

    print("Student not found")


def unique():
    if len(students) ==0:
        print("No record")
        return
    a= set()
    for i in students:
        for j in student[3]:
            unique_subjects.add(subject)

    print("\n----- Unique Subjects -----")

    for subject in unique_subjects:
        print(subject)


def main():
    while True:
        print("\n===== STUDENT RECORD MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Show Unique Subjects")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            show_unique_subjects()
        elif choice == "7":
            print("Thank you for using Student Record Management System!")
            break
        else:
            print("Invalid choice. Please try again.")


main()
