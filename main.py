
import random
import re

# If the two players choose the same “character” it’s a tie, and the game repeats
# Rock beats Scissors
# Paper beats Rock
# Scissors beats Paper

def playGame():
    options = ["R", "P", "S"]
    userInput = input("Pick a valid choice, R-Rock P-Paper S-Scissors: ")
    while userInput.upper() not in options:
        print("ERROR! invalid input, Try Again!!!")
        userInput  = input("Pick a valid choice, R-Rock P-Paper S-Scissors: ")

    cpuInput = random.choice(options)
    print(f"\n You choose {userInput}, computer choose {cpuInput}")

    if(userInput.upper() == cpuInput):
        print("The game is a tie, try again!")
        playGame()
    elif userInput.upper() == "R":
        if cpuInput == "S":
            print("Rock smash scissors! You wins")
        else: 
            print("Paper wraps Rock! COMPUTER wins")
    elif userInput.upper() == "S":
        if cpuInput == "R": 
            print("Rock smash Scissors! COMPUTER wins")
        else: 
            print("Scissors cuts paper! You win")
    elif userInput.upper() == "P":
        if cpuInput == "R":
            print("Paper wraps Rock! You win")
        else:
            print("Scissors cuts Paper! COMPUTER wins")

# This part can be commented out as it is not part of the technical requirement for the task
    retry = input("Do you want to play again? y/n: ")
    if retry.lower() != "n":
        playGame()
    else: 
        return "Nice playing with you"


print(playGame())
 