# Even odd checker
def is_even(x):
    if x % 2 == 0:
        return "even"
    else:
        return "odd"
while True:
    try:
        num = int(input("What's your number: "))
    except ValueError:
        print("Only numbers are allowed")     
        continue   
    print(f"{num} is {is_even(num)}")
    n = input("Type yes/no to continue or not: ").strip().lower()
    if n != "yes":
        break