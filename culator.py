print("1 - Add")
print("2 - Subtract")
print("3 - Multiply")
print("4 - Divide")
print()

option = int(input("Choose an operation: "))

if option in [1, 2, 3, 4]:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    
    if option == 1:
        result = num1 + num2
    elif option == 2:
        result = num1 - num2
    elif option == 3:
        result = num1 * num2
    elif option == 4:
        # Added a division by zero check
        if num2 == 0:
            print("Error: Cannot divide by zero.")
        else:
            result = num1 / num2
    
    # This print statement is now inside the main 'if' block.
    # It will only run if a valid operation was chosen.
    # We still need to handle the case where num2 was 0.
    if not (option == 4 and num2 == 0):
        print(f"The result of the operation is {result}")
    
else:
    print("Invalid operation entered.")