# Student Record Management System

students = []

def add_student():
    roll_no = input("Enter Roll No: ")
    name = input("Enter Student Name: ")
    branch = input("Enter Branch: ")
    subjects_input = input("Enter subjects separated by commas: ")

    subjects = []
    for subject in subjects_input.split(","):
        subject = subject.strip()
        if subject != "":
            subjects.append(subject)

    student = (roll_no, name, branch, subjects)
    students.append(student)

    print("Student added successfully!")


def view_students():
    if len(students) == 0:
        print("No student records found.")
        return

    print("\n----- Student Records -----")

    for student in students:
        print("Roll No:", student[0])
        print("Name:", student[1])
        print("Branch:", student[2])
        print("Subjects:", ", ".join(student[3]))
        print("---------------------------")


def search_student():
    roll_no = input("Enter Roll No to search: ")
    found = False

    for student in students:
        if student[0] == roll_no:
            print("\nStudent Found")
            print("Roll No:", student[0])
            print("Name:", student[1])
            print("Branch:", student[2])
            print("Subjects:", ", ".join(student[3]))
            found = True
            break

    if found == False:
        print("Student not found.")


def update_student():
    roll_no = input("Enter Roll No to update: ")

    for i in range(len(students)):
        if students[i][0] == roll_no:
            name = input("Enter New Name: ")
            branch = input("Enter New Branch: ")
            subjects_input = input("Enter new subjects separated by commas: ")

            subjects = []
            for subject in subjects_input.split(","):
                subject = subject.strip()
                if subject != "":
                    subjects.append(subject)

            students[i] = (roll_no, name, branch, subjects)

            print("Student record updated successfully!")
            return

    print("Student not found.")


def delete_student():
    roll_no = input("Enter Roll No to delete: ")

    for i in range(len(students)):
        if students[i][0] == roll_no:
            students.pop(i)
            print("Student record deleted successfully!")
            return

    print("Student not found.")


def show_unique_subjects():
    if len(students) == 0:
        print("No student records found.")
        return

    unique_subjects = set()

    for student in students:
        for subject in student[3]:
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
