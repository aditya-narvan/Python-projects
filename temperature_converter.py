#A temperature convertor
while True:
    try:
        temp = float(input("Enter the temperature: "))        
    except ValueError:
        print("Only numbers are allowed")
        continue
    while True:
        try:
            n = int(input("Choose the conversion:\nPress:\n 1 for Celsius to Fahrenheit\n 2 for Celsius to Kelvin\n 3 for Fahrenheit to Kelvin\n 4 for Fahrenheit to Celsius\n 5 for Kelvin to Celsius\n 6 for Kelvin to Fahrenheit\n "))
            if 1 <= n <= 6:
                break
            else:
                print("Choose between 1 and 6 only")
        except ValueError:
            print("Only numbers are allowed")

#conversions
    if n == 1:
        print("Conversion for Celsius to Fahrenheit is:", round(temp*1.8 + 32, 3))
    elif n == 2:
        print("Conversion for Celsius to Kelvin is:", round(temp + 273.15, 3))
    elif n == 3:
        print("Conversion for Fahrenheit to Kelvin is:", round((temp - 32) * 5/9 + 273.15, 3))
    elif n == 4:
        print("Conversion for Fahrenheit to Celsius is:", round((temp - 32) * 5/9, 3))
    elif n == 5:
        print("Conversion for Kelvin to Celsius is:", round(temp - 273.15, 3))
    elif n == 6:
        print("Conversion for Kelvin to Fahrenheit is:", round((temp - 273.15) * 9/5 +32, 3))
    else:
        print("Invalid input")
    agn = input("\nDo you want to do another conversion?: (yes/no) ").strip().lower()
    if agn != "yes":
        print("Thanks for using our temperature convertor!")
        break
          
        
        