#****************ATM simulator ("project")************************

correct_pin = "1234"
balance = 10000
attempts = 0
history = []

# Stage 1: PIN check
while attempts < 3:
    pin = input("Enter your PIN: ")

    if pin == correct_pin:
        print("PIN accepted!")
        break
    else:
        attempts += 1

        if attempts < 3:
            print("Wrong PIN. Attempts left:", 3 - attempts)
        else:
            print("Card blocked.")

if attempts < 3:

    # Stage 2, 3 and 4: ATM menu
    while True:
        print("\n--- ATM MENU ---")
        print("1. Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Current balance:", balance)

        elif choice == "2":
            amount = float(input("Enter deposit amount: "))

            if amount > 0:
                balance += amount
                history.append(f"Deposit {amount:g}")
                print("New balance:", f"{balance:g}")
            else:
                print("Amount must be above 0.")

        elif choice == "3":
            amount = float(input("Enter withdrawal amount: "))

            if amount <= 0:
                print("Amount must be above 0.")
            elif amount > balance:
                print("Insufficient balance")
            else:
                balance -= amount
                history.append(f"Withdraw {amount:g}")
                print("New balance:", f"{balance:g}")

        elif choice == "4":
            print("\nTransaction History:")

            for transaction in history:
                print(transaction)

            print("Thank you!")
            break

        else:
            print("Invalid choice. Try again.")


#***************Student Marks Manager (Python Second project)***********************

students = {
    "Aman": [85, 90, 78],
    "Riya": [92, 88, 95],
    "Zoya": [70, 65, 80]
}


# Function to calculate average
def calculate_average(marks):
    return round(sum(marks) / len(marks), 2)


# Function to calculate grade
def calculate_grade(average):
    if average >= 85:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 50:
        return "C"
    else:
        return "F"


# Function to find topper
def find_topper():
    topper = None
    highest_average = -1

    for name, marks in students.items():
        average = calculate_average(marks)

        if average > highest_average:
            highest_average = average
            topper = name

    if topper is not None:
        print("Topper:", topper)


# Stage 1 and 2: View all students and grades
def view_all():
    for name, marks in students.items():
        average = calculate_average(marks)
        grade = calculate_grade(average)

        print(name, f"{average:.2f}", grade)


# Stage 5: Add student with validation
def add_student():
    name = input("Enter student name: ").strip()

    if name in students:
        print("Student already exists.")
        return

    marks = []

    for i in range(3):
        while True:
            try:
                mark = float(input(f"Enter mark {i + 1} (0-100): "))

                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Invalid mark, try again.")

            except ValueError:
                print("Invalid mark, try again.")

    students[name] = marks
    print("Student added successfully!")


# Stage 4: Repeating menu
while True:
    print("\n--- STUDENT MARKS MANAGER ---")
    print("1. Add student")
    print("2. View all")
    print("3. Show topper")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_all()

    elif choice == "3":
        find_topper()

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
