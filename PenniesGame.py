from random import randrange # Random number function used to generate computer choices
import os

def clear_screen():
    """Clears the terminal screen of information"""
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

#--------------------------------------------------------------------------------------#

def first_move():

    clear_screen()

    valid_choice = False

    while valid_choice != True:
        try:
            player_choice = input("Would you like to go first (yes/no): ").lower()
            if player_choice == "yes": player_choice = True
            elif player_choice == "no": player_choice = False
            else: raise ValueError
        except ValueError:
            print("Please enter either \"yes\" or \"no\"")
        except Exception as err:
            print(f"Unexpected error occured:\n{err}")
        else:
            valid_choice = True
        clear_screen()
    return player_choice


#--------------------------------------------------------------------------------------#

def player_move():

    valid_choice = False

    while valid_choice != True:
        try:
            player_input = int(input("How many coins do you want to take: "))
            if player_input not in range(1, 6):
                raise ValueError
        except ValueError:
            print("Please ensure you enter an integer between 1 and 5")
            valid_choice = False
        except Exception as err:
            print(f"Unexpected error occured:\n{err}")
        else:
            valid_choice = True
    clear_screen()
    return player_input

#--------------------------------------------------------------------------------------#

def computer_move(pennies):

    """Function makes computer nearly unbeatable - but is possible"""

    if pennies == 1:
        return 1
    elif pennies < 7: # Force total to 1
        return pennies - 1
    elif pennies == 7: # Computer cannot win here
        return randrange(1, 6)
    elif pennies < 13: # Force total to 7
        return pennies - 7
    elif pennies == 13: # Computer in danger of loss here
        return 1
    elif pennies < 19: # Force total to 13
        return pennies - 13
    else:
        return 1

#--------------------------------------------------------------------------------------#

def check_pennies(pennies):

    return True if pennies > 0 else False

#--------------------------------------------------------------------------------------#

def play_again():

    print("Would you like to play again?")
    choice = input("Enter yes or no: ").lower()
    if choice == "yes":
        
        return True

    elif choice == "no":

        return False
    
#--------------------------------------------------------------------------------------#

def main():

    play = True

    while play == True:

        player_turn = first_move() # Player decides whether to go first or second
        total = 20

        print(f"Game starting\nNumber of pennies: {total}")

        while True: # Infinite loop - check_pennies will break out
            if player_turn == True:
                total -= player_move()
                print(f"Pennies left: {total}")
                player_turn = False

                if check_pennies(total) == False: # Check if player has lost 
                    print("Player loses")
                    break
            else:
                computer = computer_move(total)
                print(f"Computer takes {computer}")
                total -= computer
                print(f"Pennies left: {total}")
                player_turn = True

                if check_pennies(total) == False: # Check if computer has lost
                    print("Player Wins!")
                    break
              
        play = play_again()# Check if player wishes to play again
        
    clear_screen()

#--------------------------------------------------------------------------------------#

if __name__ == "__main__":
    main()