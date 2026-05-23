def grade(x):                 
        if 90 <= x <= 100:
            return(f"Got an A")
        elif 80 <= x <= 89:             
            return(f"Got a B")
        elif 70 <= x <= 79:
            return(f"Got a C")
        elif 60 <= x <= 69:
            return(f"Got a D")
        elif 0 <= x <= 59:
            return(f"Got a F")
        else:
            try:
                raise ValueError
            except ValueError:
                print("the marks must be between 0 to 100")
                
while True:
    marks =[]   
    name = input("Enter the name of the student: ").strip().title()
    for i in range(1, 6):
        while True:
            try:
                m = float(input(f"Enter the marks of sub {i} for student {name}: "))
                if 0 <= m <= 100:
                   marks.append(m)
                   break
                else:
                    print("Marks mut be between 0 and 100")
            except ValueError:
                print("Numbers only please")
    for i in range(5):
        print(f"{name} {grade(marks[i])} in sub {i+1}")
    total = sum(marks)
    percentage = (total/500) * 100
    print(f"total: {total} | Percentage: {percentage: .2f}%")
    agn = input("Do you want to do for another student: (yes/no) ")
    if agn !="yes":
        break
