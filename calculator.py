from art import logo

def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2
def mul(n1, n2):
    return n1 * n2
def div(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
}

def calculator():
    print(logo)
    calculate = True
    num1 = float(input("Enter first number: "))

    while calculate:
        for i in operations:
            print(i)
        operation_to_perform = input("pick an operation : ")
        num2 = float(input("Enter second number: "))
        result = operations[operation_to_perform](num1, num2)
        print(f"{num1} {operation_to_perform} {num2} = {result}")
        choice = input(f"Type 'y' to continue calculating with {result}, or 'n' to start new calculation: ")
        if choice == "y":
            num1 = result
        elif choice == "n":
            calculate = False
            calculator()

calculator()