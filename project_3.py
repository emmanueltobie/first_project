name = input("Enter your name: ")
print(f"Welcome {name} To this Adventure")
answer = input("You are in a dark road and you only have the option to go left or right \n. which way would you go?  ").lower()
if answer =="left":
    answer = input("You have come to a river .\n would you walk around it or swim across? type walk to walk around , type swim to swim across:  ").lower()
    if answer == "walk":
        print("You walked like a lost sheep, exhausted, ran out of water and was eaten by an antelope  and also lost the game")
    elif answer == "swim":
        print("You swam across and was eaten by an alligator, also the remnant of your body was eaten by a crocodile")
elif answer == "right":
    answer = input("You have walked through a dark alley and in a bridge.\nIt looks wobbly, Do you want to cross it or head back? (cross/back):  ")
    if answer == "cross":
        answer = input("You successfully walked through and there is a atranger at around do you want to talk? (yes/no):  ")
        if answer == "yes":
            print("You conversed and you got some gold ,, YOU WON!!")
        else:
            print("You lose!!")
    elif answer == "back":
        answer = input("You have missed the road and now you are lost in the dark alley,\n" "would you like to seek for help (yes/no): ")
        if answer == "yes":
            print("Help not found!!")
        else:
            print("You lose already dont WASTE Your time..")
    else:
            print("You lose already dont WASTE Your time..")
else:
    print("Not a valid option. You lose")

print(f"Thank you {name} beter luck next time!!")
