# '''
# gissatalet.py: Gissa Talet Spel

# __author__  = "Eric Botander"
# __version__ = "1.0.0"
# __email__   = "eric.botander@elev.ga.dbgy.se"
# '''

import random
import os
os.system('cls')


#Gissa Talet 7 Försök

playing = True

while playing:
    os.system('cls')

    tries = 7
    secret_number = random.randint(1,100)
    print(secret_number)


    while tries > 0:

        try:
            guess = int(input("Gissa Talet:"))

        except:
            print("Skriv endast tal")
            continue
        if guess == secret_number:
            print(f"Du gissade rätt med {tries} försök kvar!")
            break
        
        elif guess > secret_number:
            print("Talet är lägre")
            tries-=1
            print(f"Du har {tries} försök kvar!")
            continue
        else:
            print("Talet är högre")
            tries-=1
            print(f"Du har {tries} försök kvar!")
            continue


