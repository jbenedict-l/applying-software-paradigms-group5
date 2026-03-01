# ------------------------------------------------------------
# FUNCTION 1: get_numeric_input(prompt)
# PURPOSE: Ask the user to enter a number.
#          Keeps asking until a valid number is given.
# ------------------------------------------------------------
def get_numeric_input(prompt):
    while True:  # Loop forever until valid input is received
        try:
            # float() converts the input string into a decimal number
            # This accepts both whole numbers (5) and decimals (3.14)
            value = float(input(prompt))
            return value  # Return the valid number and exit the loop
        except ValueError:
            # If the user types letters or symbols, float() will fail
            # and we catch the error here instead of crashing the program
            print("Invalid input. Please enter a numeric value.")


# ------------------------------------------------------------
# FUNCTION 2: get_operation_choice()
# PURPOSE: Show the menu of operations and get a valid choice.
#          Keeps asking until the user enters 0-5.
# ------------------------------------------------------------
def get_operation_choice():
    # Print the menu options for the user to choose from
    print("\n--- Select Operation ---")
    print("  1. Addition       (+)")
    print("  2. Subtraction    (-)")
    print("  3. Multiplication (*)")
    print("  4. Division       (/)")
    print("  5. Modulus        (%)")
    print("  0. Quit")

    while True:  # Keep looping until a valid choice is entered
        try:
            # int() converts input to a whole number (no decimals for menu)
            choice = int(input("\nEnter choice (0-5): "))

            # Check if the number is within the valid range
            if 0 <= choice <= 5:
                return choice  # Valid choice — return it to the caller
            else:
                print("Please enter a number between 0 and 5.")
        except ValueError:
            # If the user types a word or decimal, catch the error
            print("Invalid input. Please enter a whole number.")


# ------------------------------------------------------------
# FUNCTION 3: perform_operation(a, b, choice)
# PURPOSE: Perform the arithmetic based on the user's choice.
#          Takes two numbers (a, b) and the operation choice.
#          Returns two values: the result AND a message string.
# ------------------------------------------------------------
def perform_operation(a, b, choice):
    if choice == 1:
        # ADDITION: add both numbers together
        result = a + b
        operator = "+"

    elif choice == 2:
        # SUBTRACTION: subtract b from a
        result = a - b
        operator = "-"

    elif choice == 3:
        # MULTIPLICATION: multiply both numbers
        result = a * b
        operator = "*"

    elif choice == 4:
        # DIVISION: divide a by b
        # IMPORTANT: Check for division by zero first to avoid a crash
        if b == 0:
            # Return None (no result) and an error message
            return None, "Error: Cannot divide by zero."
        result = a / b
        operator = "/"

    elif choice == 5:
        # MODULUS: get the remainder when a is divided by b
        # Example: 10 % 3 = 1  (because 10 / 3 = 3 remainder 1)
        # Also check for zero to avoid crash
        if b == 0:
            return None, "Error: Cannot perform modulo by zero."
        result = a % b
        operator = "%"

    else:
        # Fallback for any unexpected choice value
        return None, "Unknown command error. Try executing this program again."

    # Build and return the formatted result message
    # Example: "5.0 + 3.0 = 8.0"
    return result, f"Result: {a} {operator} {b} = {result}"


# ------------------------------------------------------------
# FUNCTION 4: display_result(message)
# PURPOSE: Print the result or error message to the screen.
#          Kept separate so output is easy to modify later.
# ------------------------------------------------------------
def display_result(message):
    print(f"\nResult: {message}")


# ------------------------------------------------------------
# FUNCTION 5: main()
# PURPOSE: The MAIN CONTROL FLOW of the program.
#          This is the "boss" function — it calls all other
#          functions in the correct order, step by step.
# ------------------------------------------------------------
def main():
    # Display the program header/title
    print("=" * 45)
    print(" Smart Arithmetic Calculator")
    print(" Procedural Paradigm")
    print("=" * 45)

    # Main loop — keeps the calculator running until user exits
    while True:

        # STEP 1: Show menu and get the user's operation choice
        choice = get_operation_choice()

        # STEP 2: Check if user wants to exit (choice = 0)
        if choice == "quit":
            print("\nExiting calculator. Goodbye!\n")
            break  # Break out of the loop and end the program

        # STEP 3: Get two numbers from the user
        a = get_numeric_input("Enter first number  (a): ")  
        b = get_numeric_input("Enter second number (b): ")

        # STEP 4: Perform the chosen arithmetic operation
        # perform_operation() returns two values:
        #   result  -> the numeric answer (or None if error)
        #   message -> a formatted string to display
        result, message = perform_operation(a, b, choice)

        # STEP 5: Display the result or error message
        display_result(message)

        # Print a separator line for readability between calculations
        print("-" * 45)

# ------------------------------------------------------------
# ENTRY POINT
# This block ensures main() only runs when this file is
# executed directly — not when imported as a module.
# ------------------------------------------------------------
if __name__ == "__main__":
    main()
