from PenniesGame import Pennies, Computer, Player
from time import sleep
import os

def clear_screen():
    """Clears the terminal screen of information"""
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def Main():
    
    clear_screen()

    # Create game objects
    pennies = Pennies()
    player = Player()
    computer = Computer()

    play = True

    while play == True:

        player_move = player.play_first() # Decide if player or computer moves first

        while True:
            
            if player_move == True:
                clear_screen()
                pennies.total -= player.player_move(pennies.total)
                print(f"There are {pennies.total} pennies left.")
                player_move = False


                # Check if player has lost
                if pennies.total <= 0: 
                    print("There are zero pennies left. Computer wins.")
                    break
            else:

                pennies.total -= computer.move(pennies.total)
                print(f"There are {pennies.total} pennies left.")
                player_move = True

                # Check if computer has lost
                if pennies.total <= 0:
                    print("There are zero pennies left. Player wins.")
                    break
            sleep(2)
        
        # Ask player if they want to play again
        play = player.play_again()

if __name__ == "__main__":
    Main()