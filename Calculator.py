def add(num1,num2):
    return num1 + num2
def sub(num1,num2):
    return num1 - num2
def mul(num1,num2):
    return num1 * num2
def div(num1,num2):
    return num1 / num2
def modulo(num1,num2):
    return num1 % num2

print("*****Welcome to Calculator!*****\n Select the operation of your choice\n")
print(" Enter 1 for Addition\n Enter 2 for Subtraction\n Enter 3 for Multiplication\n Enter 4 for Division\n Enter 5 for Remainder division\n ")

choice = int(input("Enter your choice: "))
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

if choice == 1:
    print(number1, "+", number2, "=", add(number1,number2))
elif choice == 2:
    print(number1, "-", number2, "=", sub(number1, number2))
elif choice == 3:
    print(number1, "*", number2, "=", mul(number1, number2))
elif choice == 4:
    print(number1, "/", number2, "=", div(number1, number2))
elif choice == 5:
    print(number1, "%", number2, "=", modulo(number1, number2))
else:
    print("Invalid choice")
