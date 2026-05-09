import random

options = ["rock", "paper", "scissors"]
wins = 0
computer_wins = 0
print("first to 5 wins")

while True:
    computer_choice = random.choice(options)
    player_choice = input("enter rock, paper, or scissors to play: ")
    if computer_choice == player_choice:
        print("tie")
    elif computer_choice == "paper" and player_choice == "rock":
        print("you lose")
        computer_wins += 1
    elif computer_choice == "paper" and player_choice == "scissors":
        print("you win!")
        wins += 1
    elif computer_choice == "rock" and player_choice == "paper":
        print("you win!")
        wins += 1
    elif computer_choice == "rock" and player_choice == "scissors":
        print("you lose")
        computer_wins += 1
    elif computer_choice == "scissors" and player_choice == "paper":
        print("you lose")
        computer_wins += 1
    elif computer_choice == "scissors" and player_choice == "rock":
        print("you win!")
        wins += 1
    elif player_choice == "gun":
        print("you won twice!")
        wins += 2
    else:
        print("You lose, you did not input a correct choice ")
        wins -= 1

    print("your score: ", wins)
    print("computer score: ", computer_wins)
    if wins >= 5:
        print("you win win win!")
        print("final score: ")
        print("you", wins)
        print("computer_wins", computer_wins)
        restart = input("input y to continue or n to exit")
        if restart == "y":
            continue
        elif restart == "n":
            break
        else:
            break
    elif computer_wins >= 5:
        print("you lost to a computer!")
        print("final score: ")
        print("you", wins)
        print("computer_wins", computer_wins)
        restart = input("input y to continue or n to exit ")
        if restart == "y":
            continue
        elif restart == "n":
            break
        else:
            break






