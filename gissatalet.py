# '''
# FILNAMN.PY: Beskrivning av fil/program

# __author__  = "Eric Botander"
# __version__ = "1.0.0"
# __email__   = "eric.botander@elev.ga.dbgy.se"
# '''

import random
import os
os.system('cls')


#Gissa Talet 7 Försök

playing = True

while playing: #loop att man är i spelet
    os.system('cls') 

    tries = 7 # hur många försök man har
    


    while tries > -1: #att spelet är igång om man har mer försök än 0 så att det slutar när man har för lite försök

        secret_number = random.randint(1,100) # generera ett tal man ska gissa

        if tries == 0:
            print(f"Du gissade tyvärr inte rätt. Talet var {secret_number}")
            yesno = input("Vill du spela igen j/n?: ")
                
            if yesno.upper() == "J": # så att spelaren får välja om den vill spela igen eller inte
                tries = 7
                continue 
            elif yesno.upper() == "N": # så spelaren kan avsluta spelet
                playing = False
                break
            else:
                os.system('cls')
                print("Du skrev inte in J eller N. Spela igen eller Skriv 0 för att avsluta.") #motverkar error och ger instruktioner 
                continue

        try:
            guess = int(input("(Skriv 0 för att avsluta) Gissa Talet mellan 1-100:")) #kollar så att de man skriver in är en integer

        except:
            print("Skriv endast tal") # ifall man skriver in nåt annat så säger den till
            continue
        
        if guess == secret_number:
            print(f"Du gissade rätt med {tries} försök kvar!") #Om man gissar rätt säger den det och säger hur många försök man hade kvar och om man vill spela igen
            yesno = input("Vill du spela igen j/n?: ")
                
            if yesno.upper() == "J": # så att spelaren får välja om den vill spela igen eller inte
                continue 
            elif yesno.upper() == "N": #Så spelaren kan avsluta
                playing = False
                break
            else:
                os.system('cls')
                print("Du skrev inte in J eller N. Spela igen eller Skriv 0 för att avsluta.") #motverkar error och ger instruktioner 
                continue

        elif guess == 0: # om man skriver 0 så avslutas spelet
            playing = False
            break
                     
        elif guess > secret_number: # säger om gissningen är för låg
            print("Talet är lägre")
            tries-=1
            print(f"Du har {tries} försök kvar!") # Hur många försök man har kvar
            continue
        else:
            print("Talet är högre") # säger om gissningen är för hög
            tries-=1
            print(f"Du har {tries} försök kvar!") # Hur många försök man har kvar
            continue
    break       

