from random import randrange
from time import sleep
class Pennies:
    def __init__(self) -> None:
        self.total = 20

class Player:
    def __init__(self) -> None:
        pass

    def player_move(self, pennies):
        
        valid_choice = False

        while valid_choice != True:
            try:
                player_input = int(input(f"How many coins do you want to take, there are {pennies} left: "))
                if player_input not in range(1, 6):
                    raise ValueError
            except ValueError:
                print("Please ensure you enter an integer between 1 and 5")
                valid_choice = False
            except Exception as err:
                print(f"Unexpected error occured:\n{err}")
            else:
                valid_choice = True

        return player_input
    
    def play_again(self):
        print("Would you like to play again?")
        choice = self.yes_or_no()
        return choice
    
    def play_first(self):
        print("Would you like to go first?")
        choice = self.yes_or_no()
        return choice
        
    def yes_or_no(self):

        valid_input = False
        while valid_input != True:
            try:
                choice = input("Enter yes or no: ").lower()
                if choice == "yes":
                    return True
                elif choice == "no":
                    return False
                else:
                    raise ValueError
            except ValueError:
                print("Please ensure you enter either 'yes' or 'no'")
                valid_input = False

class Computer:
    def __init__(self) -> None:
        self.mode = self.level()
    
    def level(self):
        valid_input = False
        valid_choices = ["easy", "hard"]
        try:
            while valid_input != True:
                print("Choose what level difficulty you wish to play.")
                user_choice = input("Type either 'easy' or 'hard': ").lower()

                if user_choice not in valid_choices:
                    print("TEMP")
                    raise ValueError
                
                valid_input = True
                
        except ValueError:
            print("Please ensure you enter either 'easy' or 'hard'")
            valid_input = False
        except Exception as err:
            print(f"Unexpected error occured:\n\n{err}")
            print("\nPlease try again")
            valid_input = False

        return user_choice

    def move(self, pennies):
        try:
            if self.mode == "easy":
                choice = randrange(1, 6)
                print(f"The computer has taken: {choice} pennies.")
                return choice

            elif self.mode == "hard":
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
            else:
                raise ValueError
        except ValueError:
            print("Unexpected error occured. Computer difficulty has not been set")
            print("Aborting")
            sleep(2)
            exit()