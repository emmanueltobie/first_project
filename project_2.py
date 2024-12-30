import random

user_wins = 0
computer_wins = 0
options = ["rock","paper","sicssors"]
while True:
    f1 = input("Type in Either Rock/Paper/Scissors or q to quit: ").lower()
    if f1 =="q":
        break
    if f1 not in options:
        continue

    r = random.randint(0,2)
    comp = options[r]
    print(f"Computer picked {comp}.")
    if f1 == "rock" and comp == "sicssors":
        print("You won😊 !!")
        user_wins += 1
        print(f"Your score: {user_wins}    ,   Computer score: {computer_wins}")

    elif f1 == "sicssors" and comp == "rock":
        print("computer won😊 !!")
        print("You lost😥")
        computer_wins += 1
        print(f"Your score: {user_wins}    ,   Computer score: {computer_wins}")

    elif f1 == "paper" and comp == "rock":
        print("computer won😊 !!")
        print("You lost😥")
        computer_wins += 1
        print(f"Your score: {user_wins}    ,   Computer score: {computer_wins}")
    
    elif f1 == "rock" and comp == "paper":
        print("You won😊 !!")
        user_wins += 1
        print(f"Your score: {user_wins}    ,   Computer score: {computer_wins}")

    elif f1 == "scissors" and comp == "paper":
        print("You won😊 !!")
        user_wins += 1
        print(f"Your score: {user_wins}    ,   Computer score: {computer_wins}")

    elif f1 == "paper" and comp == "sicssors":
        print("computer won😊 !!")
        print("You lost😥")
        computer_wins += 1 
        print(f"Your score: {user_wins}    ,   Computer score: {computer_wins}")

    elif comp == f1:
        print("It was a tie") 
        print(f"Your score: {user_wins}    ,   Computer score: {computer_wins}")
    else:
        print("You lose😥")
 
print("Goodbye !")
    
