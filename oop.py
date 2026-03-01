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
        """
        a: numeric (float) value for A
        operator: one of '+', '-', '*', '/', '%'
        b: numeric (float) value for B
        """
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

        self.value_a = result
        self.value_b = None
        self.current = result

        return result

    def AC(self):
        """Clear all stored values and history."""
        self.value_a = None
        self.value_b = None
        self.operator = None
        self.current = None
        return "Calculator reset."

def parse_and_execute(calc: Calculator, text: str):
    """
    Accept strings of the form:
      <a> <operator> <b>
    where <a> can be '=' to mean 'use previous result' or a number.
    Example: '5 + 3' or '= * 2'
    """
    tokens = text.strip().split()
    if len(tokens) != 3:
        return "Invalid format. Example: 5 + 3 or = + 5"

    a_token, operator, b_token = tokens

    if a_token == "=":
        if calc.current is None:
            return "No previous result to use. Compute something first."
        a = float(calc.current)
    else:
        try:
            a = float(a_token)
        except ValueError:
            return "Invalid value for A. Use a number or '='."

    try:
        b = float(b_token)
    except ValueError:
        return "Invalid value for B. Use a number."

    return calc.compute(a, operator, b)


def main():
    calc = Calculator()

    print("===== Smart Arithmetic Calculator (OOP) =====")
    print("Enter expressions like: 5 + 3   or   = + 5  (use '=' for previous result)")
    print("Available operators: +  -  *  /  %")
    print("Commands: AC (All Clear), quit\n")

    while True:
        user_input = input(">> ").strip()

        if not user_input:
            continue

        cmd_low = user_input.lower()
        if cmd_low == "quit":
            print("Calculator closed.")
            break

        if user_input.upper() == "AC":
            print(calc.AC())
            continue

        output = parse_and_execute(calc, user_input)
        print("Result:", output)

if __name__ == "__main__":
    main()
