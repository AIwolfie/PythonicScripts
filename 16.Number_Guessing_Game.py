import random

print("----------------------------------------------------------------")
print("                      NUMBER GUESSING GAME")
print("----------------------------------------------------------------")
print("-> i am gussing a number between 1 to 100")
print("-> you have to guess the number")
print("-> you have only 5 chance")
print("-> if you guess the number you win the game")
print("----------------------------------------------------------------")

rnum = random.randint(1, 100)
guessing_chance= 5
for chance in range (guessing_chance):
    try:
        print("guess the number between 1 to 100")
        guess_number = int(input(f"chance {chance+1}: Enter you Guess: "))

        if guess_number == rnum:
            print(f"Congratulations! You've guessed the number {guess_number} correctly!")
            break
        elif guess_number < rnum:
            print(f"Your guess {guess_number} is too low.")
        else:
            print(f"Your guess {guess_number} is too high.")
        
        if chance == guessing_chance-1:
            print(f"Sorry! You've run out of chances.")
            print(f"The number was {rnum}")
    except ValueError:
        print("Invalid Input! Please enter a valid number.")