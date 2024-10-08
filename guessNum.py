from random import randint

num = randint(1,9)
userGuess = 0

guess = 0

while userGuess != num:
    userGuess = int(input("Enter a guess from 1 to 9: "))
    guess += 1
    
    if userGuess < num:
        print("Guess is low")
    elif userGuess > num:
        print("Guess is high")
    else:
        print(f"You guessed it! You won in {guess} guesses!")
