class Calculator:
    def __init__(self):
        self.current = 0

    def add(self, value):
        self.current += value
        return self.current

    def subtract(self, value):
        self.current -= value
        return self.current

    def multiply(self, value):
        self.current *= value
        return self.current

    def divide(self, value):
        if value == 0:
            return "Error: Division by zero is not allowed."
        self.current /= value
        return self.current

    def modulus(self, value):
        if value == 0:
            return "Error: Modulus by zero is not allowed."
        self.current %= value
        return self.current

    def AC(self):
        self.current = 0
        return "Calculator reset to 0."

    def display(self):
        return self.current


def main():
    calc = Calculator()

    print("===== Object-Oriented Paradigm Calculator =====")
    print("Start from 0")
    print("Enter operations like: + 5")
    print("Available operators: +  -  *  /  %")
    print("Commands: AC (All Clear), exit\n")

    while True:
        user_input = input(">> ")

        if user_input.lower() == "exit":
            print("Calculator closed.")
            break

        if user_input.upper() == "AC":
            print(calc.AC())
            continue

        try:
            operator, value = user_input.split()
            value = float(value)
        except:
            print("Invalid format. Example: + 5")
            continue

        if operator == "+":
            print("Result:", calc.add(value))
        elif operator == "-":
            print("Result:", calc.subtract(value))
        elif operator == "*":
            print("Result:", calc.multiply(value))
        elif operator == "/":
            print("Result:", calc.divide(value))
        elif operator == "%":
            print("Result:", calc.modulus(value))
        else:
            print("Invalid operator.")

if __name__ == "__main__":
    main()
