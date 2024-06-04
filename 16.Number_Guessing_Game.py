import random

print("---------------------------------------------------------------------------")
print("                      Welcome to Rock-Paper-Scissors!")
print("---------------------------------------------------------------------------")

def user_choice():
    print("1. Rock     2. Paper     3. Scissors")
    user_choice = input('Enter your choice (1, 2, 3 or rock, paper, scissor): ').lower()
    while user_choice not in ['1', '2', '3', 'rock', 'paper', 'scissor']:
        user_choice = input('Invalid choice. Enter again (1, 2, 3 or rock, paper, scissor): ').lower()

    if user_choice == '1':
        return 'rock'
    elif user_choice == '2':
        return 'paper'
    elif user_choice == '3':
        return 'scissor'
    else:
        return user_choice

def computer_choice():
    return random.choice(["rock", "paper", "scissor"])

def choose_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissor") or \
         (user_choice == "scissor" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

def start_game():
    while True:
        users_choice = user_choice()
        computers_choice = computer_choice()
        print(f"\nYou chose: {users_choice}")
        print(f"Computer chose: {computers_choice}")
        result = choose_winner(users_choice, computers_choice)
        print(f"\n{result}")

        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        while play_again not in ["yes", "no"]:
            play_again = input("Invalid choice. Do you want to play again? (yes/no): ").lower()
        if play_again == "no":
            print("Thanks for playing!")
            break

start_game()
