#A simple calculator
a = input("Press 1 to start with the calculator or quit to close the calculator ")
while(a!="quit"):
    if (a=="1"):
       print("Let's get started ")
       x = float(input("Enter first number "))
       y = float(input("Enter second number "))
       b = int(input("\nPress: \n1 for Addition, \n2 for Subtraction, \n3 for Multiplication, \n4 for Divison "))
       if (b==1):
           print(f"{x} + {y} =", x+y, "\n")
       elif (b==2):
             print(f"{x} - {y} =", x-y, "\n")   
       elif (b==3):
             print(f"{x} * {y} =", x*y, "\n")
       elif (b==4):
            if (y==0):
               print("Division by zero, undefined\n")
            else:    
               print(f"{x} / {y} =", x/y, "\n")
       else:
           print("Invalid input\n")
    else:
        print("Invalid input\n")
    a = input("Press 1 to start with the calculator or quit to close the calculator ")
print("Calculator closed.")