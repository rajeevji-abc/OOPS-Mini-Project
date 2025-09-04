# ----------------------------
# Student Report Card Generator
# ----------------------------

class Student:
    def __init__(self, name, roll_no, marks):
        # Encapsulation: private attributes
        self.__name = name
        self.__roll_no = roll_no
        self.__marks = marks  # list of marks

    # Getter methods
    def get_name(self):
        return self.__name

    def get_roll_no(self):
        return self.__roll_no

    def get_marks(self):
        return self.__marks

    # Business logic
    def calculate_total(self):
        return sum(self.__marks)

    def calculate_average(self):
        return self.calculate_total() / len(self.__marks)

    def calculate_grade(self):
        avg = self.calculate_average()
        if avg >= 90:
            return "A+"
        elif avg >= 75:
            return "A"
        elif avg >= 60:
            return "B"
        elif avg >= 40:
            return "C"
        else:
            return "F"

# File Handling - Save Report
def save_report(student, filename="report.txt"):
    with open(filename, "a") as f:
        f.write("----- Student Report -----\n")
        f.write(f"Name: {student.get_name()}\n")
        f.write(f"Roll No: {student.get_roll_no()}\n")
        f.write(f"Marks: {student.get_marks()}\n")
        f.write(f"Total: {student.calculate_total()}\n")
        f.write(f"Average: {student.calculate_average():.2f}\n")
        f.write(f"Grade: {student.calculate_grade()}\n")
        f.write("--------------------------\n\n")

# ----------------------------
# CLI Menu (runs directly)
# ----------------------------

while True:
    print("\n---- Student Report Card Generator ----")
    print("1. Add Student")
    print("2. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter Student Name: ")
        roll = input("Enter Roll No: ")

        marks = []
        num_subjects = int(input("Enter number of subjects: "))
        for i in range(num_subjects):
            mark = int(input(f"Enter marks for subject {i+1}: "))
            marks.append(mark)

        student = Student(name, roll, marks)
        save_report(student)
        print(f"\nReport generated for {name} ✅")

    elif choice == "2":
        print("Exiting program... Goodbye!")
        break

    else:
        print("Invalid choice! Please try again.")

