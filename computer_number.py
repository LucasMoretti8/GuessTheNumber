import random
import time

def play():
    print("Ok! I will think in a number between 1 and 10")
    number = random.randint(1, 10)
    time.sleep(5)
    print("Almost there...")
    time.sleep(2)
    print("Ok, i got a number! Which number did i tought?")
    guess = int(input("Your guess: "))
    time.sleep(2)
    if (number == guess):
        print("WHAT?! That's impossible!  It was {}! You got it!".format(number) + "\n" + "Congratulations. good game!")
    else:
        print("HAHA!! YOU LOSE!! It was {}!".format(number) + "\n" + "Better luck next time")