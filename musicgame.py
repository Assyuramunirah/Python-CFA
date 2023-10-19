#!/usr/bin/env python

import random

def main():


    """Start a music guessing game."""
    print("*****Guess the instrument!******")

    alat_muzik = [
        "kompang"
        ]

    x = random.choice(alat_muzik)
    print(x)
    guess = None

    while x != guess:

        guess = str(input("Apakah alat muzik yang digunakan semasa acara menyambut tetamu? "))
        
        if x == guess:
            print("You guessed {}. Tahniah, anda berjaya!".format(guess))
            break
        else:
            print("You guessed {}. Maaf, anda tidak berjaya. Cuba lagi!".format(guess))

main()