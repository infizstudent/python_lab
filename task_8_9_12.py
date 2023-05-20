import random


def determine_winner(user_choice, computer_choice):
    choices = ["rock", "paper", "scissors"]

    print(f"You chose: {choices[user_choice]}")
    print(f"The computer chose: {choices[computer_choice]}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice - computer_choice) % 3 == 1:
        print("You win!")
    else:
        print("You lose!")


if __name__ == "__main__":
    print("Welcome to Rock, Paper, Scissors!")
    print("Choose:\n1. Rock\n2. Paper\n3. Scissors")

    user_choice = int(input("Your choice (enter a number from 1 to 3): ")) - 1

    if user_choice not in range(3):
        print("Invalid choice!")
    else:
        computer_choice = random.randint(0, 2)
        determine_winner(user_choice, computer_choice)
