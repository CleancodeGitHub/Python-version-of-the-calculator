# Function to get a valid number input from the user
def get_number(number):
    while True:
        try:
            # Attempt to convert the input to a float
            return float(input(f"Number {number}: "))
        except ValueError:
            # If conversion fails, print an error message and ask again
            print("Invalid number, try again.")

# Main calculator function
def calculator():
    try:
        # Get two numbers from the user
        operand1 = get_number(1)
        operand2 = get_number(2)
        
        # Get the operation sign from the user
        sign = input("Sign (+, -, *, /): ")

        # Dictionary of operations
        # Each operation is represented by a lambda function
        operations = {
            '+': lambda x, y: x + y,  # Addition
            '-': lambda x, y: x - y,  # Subtraction
            '*': lambda x, y: x * y,  # Multiplication
            '/': lambda x, y: x / y if y != 0 else "Division by zero."  # Division with zero check
        }

        # Check if the entered sign is a valid operation
        if sign in operations:
            # Perform the calculation
            result = operations[sign](operand1, operand2)
            
            # Check if the result is a string (in case of division by zero)
            if isinstance(result, str):
                print(result)
            else:
                # Print the result rounded to 2 decimal places
                print(f"Result: {result:.2f}")
        else:
            # If the sign is not in our operations dictionary, it's invalid
            print("Invalid sign.")

    except Exception as e:
        # Catch any unexpected errors and print them
        print(f"An error occurred: {e}")

# Run the calculator function
calculator()