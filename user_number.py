import random
import time

def play():
    number = int(input("Of course! Choose a number between 1 and 10: "))
    guess = random.randint(1, 10)

    print("Ok, let me try...")
    time.sleep(5)
    print("I am reading your mind...")
    time.sleep(3)
    print("Almost there...")
    time.sleep(2)
    print("I KNOW!! The number that you tought was")
    time.sleep(2)
    print(guess)
    if (number == guess):
        print("HAHA!! I WON!! Good Game!")
    else:
        print("Oh, it wasn't! You tought on {}, you won!! Congratulations!".format(number))