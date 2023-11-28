import random
import user_number, computer_number

class GuessTheNumber():
    
#Welcomes the player
    print("Greetings player!" + "\n" + "Welcome to the guess the number game")

#Looping
    play = "y"
    while play != "n":

#Give the option
        print("Do you wanna think or guess?")
        option = int(input("1 - Think  2 - Guess: "))

#User choice
        if (option == 1):
            user_number.play()
        elif (option == 2):
            computer_number.play()
        else:
            print("Wrong option!")

#Endgame
        print("Do you wanna play again?" + "\n" + "y for yes n for no:")
        play = input("Choose: ")
        if (play == "y"):
            print("Ok, lets go again!")

#Program exit
    print("Ok, See you soon! Bye!")