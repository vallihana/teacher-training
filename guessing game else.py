#!/usr/bin/env python

import random

def main():
    """Start a number guessing game between 1-20."""
    print("Guess the number!")

x = random.randint(1, 20)
guess = None

while x !=guess:

    guess = int(input ("Pick a number between 1 to 20: "))

    if x ==guess:
        print("You Genius!")
    else :
        print("Sorry TRY again.")
main()