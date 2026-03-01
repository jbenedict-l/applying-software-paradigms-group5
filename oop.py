class Calculator:
    def __init__(self):
        self.value_a = None
        self.value_b = None
        self.operator = None
        self.current = None

    def add(self):
        return self.value_a + self.value_b

    def subtract(self):
        return self.value_a - self.value_b

    def multiply(self):
        return self.value_a * self.value_b

    def divide(self):
        if self.value_b == 0:
            return "Error: Cannot divide by zero."
        return self.value_a / self.value_b

    def modulus(self):
        if self.value_b == 0:
            return "Error: Cannot perform modulo by zero."
        return self.value_a % self.value_b

    def compute(self, a, operator, b):
        self.value_a = a
        self.value_b = b
        self.operator = operator

        operations = {
            "+": self.add,
            "-": self.subtract,
            "*": self.multiply,
            "/": self.divide,
            "%": self.modulus
        }

        if operator not in operations:
            return "Invalid operator."

        result = operations[operator]()

        if isinstance(result, str):
            return result

        self.current = result
        self.value_a = result
        self.value_b = None

        return result

def parse_and_execute(calc, text):
    tokens = text.strip().split()

    if len(tokens) != 3:
        return "Invalid format. Example: 5 + 3 or = + 5"

    a_token, operator, b_token = tokens

    if a_token == "=":
        if calc.current is None:
            return "No previous result available."
        a = float(calc.current)
    else:
        try:
            a = float(a_token)
        except ValueError:
            return "Invalid value for A."

    try:
        b = float(b_token)
    except ValueError:
        return "Invalid value for B."

    return calc.compute(a, operator, b)


def main():
    calc = Calculator()

    print("=" * 45)
    print(" Smart Arithmetic Calculator")
    print(" Object-Oriented Paradigm")
    print("=" * 45)

    print("Enter expressions like: 5 + 3")
    print("Use '=' as Value A to reuse the previous result (example: = + 5)")
    print("Available operators: +  -  *  /  %  =")
    print("Type 'quit' to exit.\n")

    while True:
        user_input = input(">> ").strip()

        if user_input.lower() == "quit":
            print("Calculator closed.")
            break

        result = parse_and_execute(calc, user_input)
        print(f"Result: {user_input} = {result}")


if __name__ == "__main__":
    main()
