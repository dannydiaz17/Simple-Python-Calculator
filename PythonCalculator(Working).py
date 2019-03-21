import math

#These functions hold the instructions for any given operation

def add(x, y):
    z = x + y
    print("Your answer is: ")
    print(z)
    
def sub(x, y):
    z = x - y
    print("Your answer is: ")
    print(z)
    
def mul(x, y):
    z = x * y
    print("Your answer is: ")
    print(z)
    
def div(x, y):
    z = x / y
    print("Your answer is: ")
    print(z)

c = int(input("Please select an operation,\n 1. Add\n 2. Subtract\n 3. Multiply\n 4. Divide\n\n"))

while(c <= 0 or c >= 5):
    c = int(input("Please select an operation,\n 1. Add\n 2. Subtract\n 3. Multiply\n 4. Divide\n\n"))
    #This while statement ensures that the user chooses an operation before continuing to the calculation part of the program

x = float(input("Enter first value\n"))
y = float(input("Enter second value\n"))

#Chooses operation based on user input

if(c == 1):
    add(x, y)

elif(c == 2):
    sub(x, y)

elif(c == 3):
    mul(x, y)

elif(c == 4):
    div(x, y)




