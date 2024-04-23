from random import randrange # Random number function used to generate computer choices

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
            print("Unexpected error occured:\n{err}")
        else:
            valid_choice = True
    
    return player_input

#--------------------------------------------------------------------------------------#

def computer_move():

    return randrange(1, 6) # Computer picks a random amount, TODO - implement smart play for computer

#--------------------------------------------------------------------------------------#

def check_pennies(pennies):

    return True if pennies > 0 else False

#--------------------------------------------------------------------------------------#

def play_again(): # Function to ask the user if they wish to play again
                  # Would be good to add error handling here
    print("Would you like to play again?")
    choice = input("Enter yes or no: ").lower()
    if choice == "yes":
        
        return True

    elif choice == "no":

        return False
    
#--------------------------------------------------------------------------------------#

def main(): # Main game
            # Would be good to add error handling here

    play = True

    while play == True:

        player_turn = True
        total = 20

        print(f"\nGame starting\nNumber of pennies: {total}")

        while True: # Infinite loop - check_pennies will break out
            if player_turn == True:
                total -= player_move()
                print(f"Pennies left: {total}")
                player_turn = False

                if check_pennies(total) == False: # Check if player has lost 
                    print("Player loses")
                    break
            else:
                computer = computer_move()
                print(f"Computer takes {computer}")
                total -= computer
                print(f"Pennies left: {total}")
                player_turn = True

                if check_pennies(total) == False: # Check if computer has lost
                    print("Player Wins!")
                    break
        
        # Check if player wishes to play again
        play = play_again() # Will be true or false - true restarts loop, false exits loop

#--------------------------------------------------------------------------------------#

if __name__ == "__main__":
    main()