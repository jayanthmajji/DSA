def main():
    total = 0
    while True:
        user_input = input("Enter a number (or 'x' to stop): ")
        if user_input.lower() == 'x':
            break
        try:
            number = float(user_input)
            total += number
        except ValueError:
            print("Invalid input. Please enter a valid number or 'x' to stop.")

    print(f"The sum of all entered numbers is: {total}")


if __name__ == "__main__":
    main()
