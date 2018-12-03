"""
The Guessing Game will do the following:
1. Randomly generate a number between a user defined low and a user defined high number
2. Have The Game run for 10 rounds
3. Store the incorrect guesses and only accept new guesses
4. End game if max round or correct number is reached.
5. Report if guess is too high or too low
"""

import random

guessesTaken = 0

minGuess = 0
maxGuess = 0

def user_random():
    global minGuess
    global maxGuess
    minGuess = int(input("Input Minimum Number: "))
    maxGuess = int(input("Input Maximum Number: "))

user_random()

badGuess = []

correctGuess = random.randint(minGuess, maxGuess)

guessedRight = False

def guess(uGuess):
    global guessedRight
    if uGuess in badGuess:
        print("You Have Already Guessed This!")
        return
    else:
        if uGuess == correctGuess:
            print("You Guessed Correctly!")
            guessedRight = True
            return
        else:
            if uGuess > correctGuess:
                print("You're Guess Is Too High!")
            else:
                print("You're Guess Is Too Low!")
            badGuess.append(uGuess)

def user_guess():
    print(badGuess)
    uGuess = input("Guess A Number: ")
    guess(int(uGuess))


while len(badGuess) < 10 and guessedRight == False:
    user_guess()

if guessedRight == False:
    print("Better Luck Next Time!")
