import random

def play_game():
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100. Can you guess it?")
    
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    # Initialize the number of guesses to 0
    num_guesses = 0
    
    # Allow the player to guess up to 5 times
    while num_guesses < 5:
        # Prompt the player to enter their guess
        guess = int(input("Enter your guess: "))
        
        # Increment the number of guesses
        num_guesses += 1
        
        # Check if the guess is correct
        if guess == secret_number:
            print("Congratulations, you guessed the number!")
            break
        elif guess < secret_number:
            print("Your guess is too low. Try again.")
        else:
            print("Your guess is too high. Try again.")
            
    # If the player has used all their guesses, reveal the secret number
    if num_guesses == 5:
        print("Sorry, you have used all your guesses.")
        print("The secret number was", secret_number)

# Call the play_game() function to start the game
play_game()