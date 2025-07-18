def division_calculator():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        result = num1 / num2
        print(f"Result: {result}")

    except ValueError:
        print(" Invalid input. Please enter a numeric value.")

    except ZeroDivisionError:
        print(" Cannot divide by zero.")

    finally:
        print(" Division operation completed.\n")


def file_reader():
    try:
        filename = input("Enter the filename to read (e.g., sample.txt): ")

        with open(filename, 'r') as file:
            content = file.read()
            print("\n File Content:\n")
            print(content)

    except FileNotFoundError:
        print(" Error: File not found. Please check the filename.")

    except PermissionError:
        print(" Error: You don't have permission to read this file.")

    except Exception as e:
        print(f" An unexpected error occurred: {e}")

    finally:
        print("File reading operation completed.\n")


def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    elif age > 120:
        raise ValueError("Age is too high to be realistic.")
    else:
        print(f" Age {age} is valid!")


def age_validator():
    try:
        user_input = input("Enter your age: ")
        age = int(user_input)
        validate_age(age)

    except ValueError as ve:
        print(f" Error: {ve}")

    finally:
        print("Age validation completed.\n")


# Main Menu
def main():
    while True:
        print("Choose a Task:")
        print("1. Division Calculator")
        print("2. File Reader")
        print("3. Age Validator")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            division_calculator()
        elif choice == '2':
            file_reader()
        elif choice == '3':
            age_validator()
        elif choice == '4':
            print(" Exiting program. Goodbye!")
            break
        else:
            print(" Invalid choice. Please enter a number from 1 to 4.\n")


if __name__ == "__main__":
    main()
