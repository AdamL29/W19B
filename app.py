from helpers.addition import add
from helpers.division import divide
from helpers.multiplication import multiply
from helpers.subtraction import minus

print("Select your math operate:")
print("1. Addition")
print("2. Divide")
print("3. Multiply")
print("4. Subtract")

while True:
    pick = input("Enter your choice(1, 2, 3 or 4): ")
    if pick in ('1', '2', '3', '4'):
        try:
            num1 = input("Number 1: ")
            num2 = input("Number 2: ")
            num1 = int(num1)
            num2 = int(num2)
        except ValueError:
            print("Please select a number")
        
        if pick == "1":
            print(add(num1,num2))
        elif pick == "2":
            print(divide(num1,num2))
        elif pick == "3":
            print(multiply(num1,num2))
        elif pick == "4":
            print(minus(num1,num2))
        else:
            print("Invalid entry")