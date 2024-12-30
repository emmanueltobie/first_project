print("Welcome")
game = input("Would you like to play a game: ").lower()
if game == "yes":
    print("Okay lets play :)")
else:
    print("sorry Could not process your request!")
    quit()
question = input("What is CPU: ").lower()
score = 0
if question == "central processing unit":
    print("Correct!!")
    score += 1
    print(f" congratulations!! you got {score} out of 5 questions!!")

else:
    print("sorry your answer was incorrect")
    print(f" congratulations!! you got {score} out of 5 questions!!")

question = input("What is AI: ").lower()    
if question == "artificial inteligence":
    print("Correct!!")
    score += 1
    print(f" congratulations!! you got {score} out of 5 questions!!")
else:
    print("Sorry your answer was incorrect")
    print(f" congratulations!! you got {score} out of 5 questions!!")

question = input("What is RAM: ").lower()    
if question == "random access memory":
    print("Correct!!")
    score += 1
    print(f" congratulations!! you got {score} out of 5 questions!!")
else:
    print("Sorry your answer was incorrect")
    print(f" congratulations!! you got {score} out of 5 questions!!")
question = int(input("Guess a number between number 1 to 10: "))
if question == int(4):
    print("correct!!")
    print(f" congratulations!! you got {score} out of 5 questions!!")

else:
    print("Sorry your answer was incorrect")
    print(f" congratulations!! you got {score} out of 5 questions!!")

question = int(input("Guess another number between number 1 to 10: "))
if question == int(6):
    print("correct!!")
    print(f" congratulations!! you got {score} out of 5 questions!!")
    print("you Got all the question correctly!!")
    print('CONGRAGTULATIONS!!')

else:
    print("Sorry your answer was incorrect")
    print(f" congratulations!! you got {score} out of 5 questions!!")

solve = (score / 5) * 100
print(f"You got {solve}%")
trials = 0
print ("You have two trials")
while True:
    if trials == 2:
        break
import random
trange = int(input("Enter a number: "))
if trange.isdigit():
    if trange <= 0 :
       print("Type in number greater than 0 next time")
       
    else:
        print("Good choice!!")
        r = random.randint(0,trange)
        q = input("Pick a number that ranges from 0 to the number you picked: ")
        if q == r:
            print("Correct, You picked a right number")
        else:
            print("Incorrect, you picked the wrong number.")
    trials += 1        
else:
    print("Type in a number next time")
    quit()

print("Better luck next time ")
