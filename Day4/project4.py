import random

options = ["Rock", "Paper", "Scissors"]

user = computer = 0

while user == computer:
    user = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors "))
    computer = random.randint(0,2)

    print("You chose: ", options[user])
    print("Computer chose: ", options[computer])

    if user > 2 or user < 0:
        print("You typed aan invalid number")

    elif user == 0 and computer == 2:
        print("You win!")

    elif user == 2 and computer == 0:
        print("You lose!")

    elif user > computer:
        print("You win!")

    elif user < computer:
        print("You lose!")

    elif user == computer:
        print("It is a Draw!")
