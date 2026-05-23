# A simle password validator
while True:
    pas = input("Enter the password: ")
    num = any(char.isdecimal() for char in pas)
    if len(pas) >= 8 and num:
        print("Valid Password!")
        break
    elif len(pas) < 8:
        print("It must contain at least eight characters\n")
    elif num == False:
        print("It must contain at least one number\n")