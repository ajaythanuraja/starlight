"""Simple Math Calculator for Kids 🎉

Practice addition, subtraction, multiplication, and division.
Great for kids learning basic math!
"""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return None  # can't divide by zero!
    return a / b


def get_number(prompt):
    """Ask for a number until the kid types a valid one."""
    while True:
        text = input(prompt)
        try:
            return float(text)
        except ValueError:
            print("Oops! Please type a number like 5 or 3.2 😊")


def show_menu():
    print("\n===== 🧮 MATH CALCULATOR FOR KIDS 🧮 =====")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (x)")
    print("4. Divide (/)")
    print("5. Quit")


def main():
    print("Hi! Let's practice math together! 🌟")

    while True:
        show_menu()
        choice = input("Pick 1, 2, 3, 4 or 5: ").strip()

        if choice == "5":
            print("Great job today! Bye bye! 👋")
            break

        if choice not in ("1", "2", "3", "4"):
            print("Please pick 1, 2, 3, 4, or 5.")
            continue

        a = get_number("Type the first number: ")
        b = get_number("Type the second number: ")

        if choice == "1":
            print(f"{a} + {b} = {add(a, b)} ✅")
        elif choice == "2":
            print(f"{a} - {b} = {subtract(a, b)} ✅")
        elif choice == "3":
            print(f"{a} x {b} = {multiply(a, b)} ✅")
        elif choice == "4":
            result = divide(a, b)
            if result is None:
                print("We can't divide by zero! Try another number. 🚫")
            else:
                print(f"{a} / {b} = {result} ✅")


if __name__ == "__main__":
    main()
