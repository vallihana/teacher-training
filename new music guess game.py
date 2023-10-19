#!/usr/bin/env python

import random

def main():
    """Lets's Start Music Guessing Game."""
    print("most popular genres of music!")

    genres = [
        "pop",
        "rock",
        "hip-pop",
        "rhythm blues",
        "heavy metal",
        "classical",
        "jazz",
        "disco",
        "folk",
        ]

    x = random.choice(genres)
    print (x)
    guess = genres

    while x != guess:

        guess = str(input("What kind genres of music am I thinking of? "))
        
        if x == guess:
            print("You guessed []. Congratulations you got it right!".format(guess))
            break
        else:
            print("You guessed []. Unfortunately you got the wrong answer. Please try again!".format(guess))
main()