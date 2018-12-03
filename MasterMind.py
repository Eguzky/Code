# --- MASTERMIND --- #

import random

print (" --- MASTERMIND --- \n")
print ("Guess the secret color code in as few tries as possible.\n")
print ("Please, enter your color code.\nYou can use red(R), green(G), blue(B), yellow(Y), white(W) and pink(P)")

colors = ["R", "G", "B", "Y", "W", "P"]
attempts = 0
max_attempts = 10
game = True
color_code = ''
color_dictionary = {}
# computer randomly picks four-color code
def color_define():
    global color_code, color_dictionary
    color_code = random.choices(colors, k = 4)	
    print (color_code)
    for i in color_code:
        color_dictionary.setdefault(i, 0)
        color_dictionary[i] += 1

color_define()

# player guesses the number	
while game:
    correct_color = ""
    guessed_color = ""
    player_guess = input().upper()
    
    
    # checking if player's input is correct
    if len(player_guess) != len(color_code):
        print ("\nThe secret code has exactly four colors. Try again!")
        continue
    for i in range(4):
        if player_guess[i] not in colors:
            print ("\nLook up what colors you can use in this game.")
            continue
    attempts += 1
            
    # comparison between player's input and secret code
    guess_dict = {}
    for i in range(4):
        if player_guess[i] == color_code[i]:
            correct_color += "X"
            guess_dict.setdefault(player_guess[i], 0)
            guess_dict[player_guess[i]] += 1

        if  player_guess[i] != color_code[i] and player_guess[i] in color_code:
            guess_dict.setdefault(player_guess[i], 0)
            if color_dictionary[player_guess[i]] > guess_dict[player_guess[i]]:
                guessed_color += "O"
                guess_dict[player_guess[i]] += 1
    print (correct_color +  guessed_color + "\n")		
        
    if correct_color == "XXXX":
        if attempts == 1:
            print ("Wow! You guessed at the first attempt!")
        else:
            print ("Well done... You needed " + str(attempts) + " attempts to guess.")
        game = False
        
    if attempts >= 1 and attempts < max_attempts and correct_color != "XXXX":
        print ("Next attempt: ")
    elif attempts >= max_attempts:
        print ("You didn't guess! The secret color code was: " + str(color_code))	

    # play or not to play
    while game == False:
        finish_game = input("\nDo you want to play again (Y/N)?").upper()	
        attempts = 0
        if finish_game =="N":
            print ("Thanks for the game! Bye, bye!")
            break
        elif finish_game == "Y":
            game = True
            print ("So, let's play again... Guess the secret code: ")
            color_define()

# --- end --- #			