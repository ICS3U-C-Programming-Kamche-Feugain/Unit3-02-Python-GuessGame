#!/usr/bin/env python3\
# Created By:Kamche
# Created on: October 9, 2026
# This program checks if they guessed the right answer
import constants


def main():
    # Create a constant for the correct number
    CORRECT_NUMBER = 5
    # Ask the user to guess a number between 0 and 9
    guess = int(input("Guess a number between 0 and 9:"))

    # Check if the guess is correct
    if guess == CORRECT_NUMBER:
        print(" You have guessed the correct number!!!")

    if guess != CORRECT_NUMBER:
        print(" You have guessed the wrong answer")
        print("Did you get it wrong, well don't worry just try again!!!")


if __name__ == "__main__":
    main()
