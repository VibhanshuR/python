import random
randNumber=random.randint(1,10)
#print(randNumber)
userGuess=None
guesses=0

while(userGuess!=randNumber):
    userGuess=int(input("Enter you guess: "))
    guesses+=1
    if(userGuess==randNumber):
         print("you guessed it right!")
    else:
        if(userGuess>randNumber):
            print("you guesses it wrong!enter smaller number")
        else:
            print("you guesses it wrong!enter larger number")

print(f"you guessed the number in {guesses} guesses")
