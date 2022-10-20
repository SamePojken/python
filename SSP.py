import os
import random


#  random action
# 1 = rock, 
# 2 = paper,
# 3 = scissors

isRunning = True
playerWins = 0
computerWins = 0

# Best Of Three Wins

while(isRunning):
    if (computerWins == 3):
        print("Game Over, Computer is the Champ!")
        isRunning = False 
        break
    if (playerWins == 3):
        print("GLORIOUS VICTORY! PLayer wins!")
        isRunning = False
        break

    computerMove = random.randint(1, 3)


    print("--------------------------------------------")
    print(" ROCK, PAPER, SCISSORS \n\n")
    print("--------------------------------------------")
    print(f"Score: Player {playerWins}\tComputer: {computerWins}\n")
    print("--------------------------------------------")

    print("Make your choice: ")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    playerMove = int( input() )
    os.system('cls')

    if (computerMove == playerMove):
        
            print("Draw, you made the same move. Try again.")
        
    elif (computerMove == 1 and playerMove == 2):
        
            print("Player wins, paper beats rock!")
            playerWins = playerWins + 1
        
    elif (computerMove == 1 and playerMove == 3):
        
            print("Computer wins, rock beats scissors!")
            computerWins = computerWins + 1
        
    elif (computerMove == 2 and playerMove == 1):
        
            print("Computer wins, paper beats rock!")
            computerWins = computerWins + 1
        
    elif (computerMove == 2 and playerMove == 3):
        
            print("Player wins, scissors beats paper")
            playerWins = playerWins + 1

    elif (computerMove == 3 and playerMove == 1):
        
            print("Player wins, rock beats scissors")
            playerWins = playerWins + 1
        
    elif (computerMove == 3 and playerMove == 2):
        
            print("Computer wins, scissors beats paper")
            computerWins = computerWins + 1
        



