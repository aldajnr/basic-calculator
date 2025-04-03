def basic_calculator():
    """A simple calculator program that takes two numbers and an operator as input.
    It performs the specified operation and prints the result."""
    
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            operator = input("Enter the operator (+, -, *, /) or 'exit' to quit: ").strip()

            if operator == 'exit':
                print("Exiting the calculator. Goodbye!")
                break

            if operator == '+':
                result = num1 + num2
                print(f"{num1} + {num2} = {result}")
            elif operator == '-':
                result = num1 - num2
                print(f"{num1} - {num2} = {result}")
            elif operator == '*':
                result = num1 * num2
                print(f"{num1} * {num2} = {result}")
            elif operator == '/':
                if num2 == 0:
                    print("Error: Division by zero is not allowed.")
                else:
                    result = num1 / num2
                    print(f"{num1} / {num2} = {result}")
            else:
                print("Invalid operator. Please enter +, -, *, or /.")
                
        except ValueError:
            print("Invalid input. Please enter valid numbers.")

basic_calculator()

