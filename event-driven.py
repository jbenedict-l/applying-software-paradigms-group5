# ── State ────────────────────────────────
state = {
    "current":   "IDLE",   # current state
    "operation": None,     # chosen operation
    "a":         None,     # first number
    "b":         None,     # second number
}

# ── Helpers ───────────────────────────────
def is_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def show_menu():
    print("=" * 45)
    print("--- Calculator ---")
    print("--- Event-driven Paradigm ---")
    print("Commands: add, subtract, multiply, divide, quit")
    print("=" * 45)

def show_prompt():
    prompts = {
        "IDLE":             "Enter command: ",
        "WAITING_FOR_A":    "Enter first number: ",
        "WAITING_FOR_B":    "Enter second number: ",
    }
    print(prompts.get(state["current"], ">>> "), end="")

# ── Handlers ──────────────────────────────
def handle_idle(event):
    if event in ("add", "subtract", "multiply", "divide"):
        state["operation"] = event
        state["current"]   = "WAITING_FOR_A"

    elif event == "quit":
        print("Goodbye!")
        return "QUIT"

    else:
        print(f"Unknown command '{event}'. Try: add, subtract, multiply, divide, quit")


def handle_waiting_for_a(event):
    if is_number(event):
        state["a"]       = float(event)
        state["current"] = "WAITING_FOR_B"
    
    elif event == "quit":
        print("Goodbye!")
        return "QUIT"
    
    else:
        print(f"'{event}' is not a valid number. Please enter a number.")


def handle_waiting_for_b(event):
    if is_number(event):
        state["b"]       = float(event)
        state["current"] = "COMPUTING"
        handle_computing()

    elif event == "quit":
        print("Goodbye!")
        return "QUIT"
    
    else:
        print(f"'{event}' is not a valid number. Please enter a number.")


def handle_computing():
    a, b, op = state["a"], state["b"], state["operation"] #Tuple assignment
    operations = {
        "add":      a + b,
        "subtract": a - b,
        "multiply": a * b,
    }

    if op == "divide":
        if b == 0:
            print("Error: Cannot divide by zero.")
        else:
            result = a / b
            # Clean up result display
            result = int(result) if result == int(result) else round(result, 10) #Ternary Operator
            print(f"\nResult: {a} ÷ {b} = {result}")
    else:
        result = operations[op]
        result = int(result) if result == int(result) else round(result, 10)
        symbols = {"add": "+", "subtract": "-", "multiply": "x"}
        print(f"\nResult: {a} {symbols[op]} {b} = {result}")

    # Reset state back to IDLE after computing
    state["current"]   = "IDLE"
    state["operation"] = None
    state["a"]         = None
    state["b"]         = None


# ── Dispatcher ────────────────────────────
# Maps each state to its handler
dispatcher = {
    "IDLE":          handle_idle,
    "WAITING_FOR_A": handle_waiting_for_a,
    "WAITING_FOR_B": handle_waiting_for_b,
}

# ── Event Loop ────────────────────────────
def main():
    show_menu()

    while True:
        show_prompt()

        event = input().strip().lower()  # Event is captured here

        handler = dispatcher.get(state["current"])  # Look up handler for current state
        result  = handler(event)                    # Fire the handler

        if result == "QUIT":
            break

if __name__ == "__main__":
    main()