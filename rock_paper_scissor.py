import random  # Library to generate random numbers

# Variable for restarting the game
restart = True

# Function to print ASCII frames around messages
def print_frame(message):
    length = len(message) + 4
    print("+" + "-" * length + "+")
    print("|  " + message + "  |")
    print("+" + "-" * length + "+")

# Function to start the game
def start_game():
    print("ROCK, PAPER, SCISSORS!")
    print("Choose an option: ")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    
    while True:  # Loop to ensure valid input
        try:
            # Player's choice
            player_choice = int(input("Enter the number corresponding to your choice (1-3): "))
            if player_choice not in [1, 2, 3]:  # Check if the choice is valid
                raise ValueError("Invalid choice. You must enter 1, 2, or 3.")
            break  # Exit the loop if the input is valid
        except ValueError:
            print("Invalid input. Please ensure you enter an integer between 1 and 3.")  # Custom message for invalid input

    # Computer's choice generated randomly
    computer_choice = random.randint(1, 3)

    # Conditions for win, draw, and loss
    if player_choice == computer_choice:
        print_frame("DRAW!")
    elif player_choice == 1 and computer_choice == 2:
        print_frame("YOU LOST! Paper beats Rock.")
    elif player_choice == 1 and computer_choice == 3:
        print_frame("YOU WON! Rock beats Scissors.")
    elif player_choice == 2 and computer_choice == 1:
        print_frame("YOU WON! Paper beats Rock.")
    elif player_choice == 2 and computer_choice == 3:
        print_frame("YOU LOST! Scissors beat Paper.")
    elif player_choice == 3 and computer_choice == 1:
        print_frame("YOU LOST! Rock beats Scissors.")
    elif player_choice == 3 and computer_choice == 2:
        print_frame("YOU WON! Scissors beat Paper.")

    # Loop for restarting the game 
    global restart  # Declare the global variable
    while True:  # Loop to ensure valid input for restart
        restart = input("Do you want to play again? (y/n): ").lower()
        if restart in ['y', 'n']:
            break  # Exit the loop if the input is valid
        else:
            print("Invalid input. You must enter 'y' for yes or 'n' for no.")  # Custom message for invalid input

    # Check the response to decide whether to restart the game
    if restart == "n":
        print_frame("THANK YOU FOR PLAYING!")
        exit()  # Terminate the program
    else:
        start_game()  # Restart the game

# Start the game
start_game()
