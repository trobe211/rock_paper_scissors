user1 = input("What is your name?").upper()
user2 = input("And what is your name player 2?").upper()

def rock_paper_scissors():
    user1_choice = input(user1 + ", choose rock, paper or scissors").lower()
    user2_choice = input(user2 + ", choose rock, paper or scissors").lower()

    if user2_choice == user1_choice:
        print("It is a tie")
    elif user1_choice == "scissors":
        if user2_choice == "rock":
            print(user2 + " is the winner")
        elif user2_choice == "paper":
            print(user1 + " is the winner")
    elif user1_choice == "rock":
        if user2_choice == "scissors":
            print(user1 + " is the winner")
        elif user2_choice == "paper":
            print(user2 + " is the winner")
    elif user1_choice == "paper":
        if user2_choice == "rock":
            print(user1 + " is the winner")
        elif user2_choice == "scissors":
            print(user2 + " is the winner")
    else:
        print("You did not choose rock, paper of scissors")
    play_again = input("Would you like to play again? Y/N").lower()
    if play_again == "y":
        rock_paper_scissors()
    else:
        print("I hope you enjoyed you game!")

rock_paper_scissors()