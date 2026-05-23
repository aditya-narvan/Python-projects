import random
#computer choosing a random number between 1 to 10
while True:
    tries = 0
    n = random.randint(1, 10)

#asking the user to guess the number
    g = int(input("Guess a number (1-10): "))
    while 1 <= g <= 10:
            if g > n:
                print("Wrong guess, Too high\n")
                tries += 1
            elif g < n:
                 print("Wrong guess, Too low\n")
                 tries += 1
            else:
                print("your guess was right!\n")
                tries += 1
                print(f"You got it right in {tries} tries")
                break                
            g = int(input("Take another guess: "))
    else:
        print("Invalid guess - must be between 1 and 10\n")
    again = input("You want to play again?: yes/no ").strip().lower()
    if again != "yes":
        print("Thanks for playing!")
        break