import random

def roll():
    max_value = 6
    min_value = 1

    roll = random.randint(min_value, max_value)

    return roll

value = roll()
print(value)

while True:
    player =  input("Enter the numbers of players (2-4): ")
    if player.isdigit():
        player = int(player)
        if 2 <= player <= 4:
            break
        else:
            print("must be between 2-4 players")
    else:
        print("invalid try again")   



max_score = 50
player_score = [0 for _ in range(player)]

while max(player_score) < max_score:
    for player_idx in range(player):
        print( "\nplayer number",player_idx + 1 ,"has just started!\n",)
        Current_score = 0

        while True:
            should_roll = input("would you like to roll? (yes/no) ").lower()
            if should_roll != "yes":
                break

            new = roll()
            if new == 1:
                print("you rolled a 1! all your scores is cleared! ")
                Current_score = 0
            else:
                Current_score += new
                print ("you rolled a: ", new )

            print("your score is: ",Current_score)

        player_score[player_idx] += Current_score
        print("your total score is: " ,player_score[player_idx] )

max_score = max(player_score)

