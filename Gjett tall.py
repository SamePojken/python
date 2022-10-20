numberOfGuesses = 0
import random

isRunning = True
randomTall = random.randint(1, 10)

print("Gjett på et tall mellom 1 og 10")
#Brukte ikke int input fordi det kom en feilmelding
guess = input("Hva gjetter du? ")



while isRunning:
    
  
    if numberOfGuesses < 3:
        if int(guess) == randomTall:
    
    
         print("Du gjettet riktig")
    
         isRunning = False
    
   
        elif int(guess) < randomTall:
            

         numberOfGuesses

         print("Du gjettet for lavt")
         guess = input("Gjett igjen: ")
            
            
        elif int(guess) > randomTall:
            

         numberOfGuesses

         print("Du gjettet for høyt")
         guess = input("Gjett igjen: ")
                            
            

    else:
    
        print("DU har gjettet feil for mange ganger")
        print("GAME OVER")
        isRunning = False