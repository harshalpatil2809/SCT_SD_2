import random

def play():
    try:
        computer = random.randint(1, 10)  # Generate a new random number each time
        user_input = 0
        guess = 0  # Initialize guess counter
        
        while user_input != computer:
            user_input = int(input("Guess the number (1-10): "))
            guess += 1  # Increment guess count
            
            if user_input > computer:
                print("Lower number, please!")
            elif user_input < computer:
                print("Higher number, please!")

        print(f"You Win...! The number was {computer}. Total guesses: {guess}")
        play_again()
    
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        play()  # Restart the game if input is invalid

def play_again():
    try:
        play_again_choice = input("Do you want to play again (Y/N)? ").strip().lower()
        if play_again_choice == "y":
            play()
        elif play_again_choice == "n":
            print("Thanks for playing! Goodbye.")
            quit()
        else:
            print("Invalid choice! Please enter Y or N.")
            play_again()  # Ask again if invalid input
    except Exception as e:
        print(f"Error: {e}")

play()
