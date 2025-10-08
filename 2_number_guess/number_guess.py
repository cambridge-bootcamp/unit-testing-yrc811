

# --- Constants ---
MIN_NUMBER = 0
MAX_NUMBER = 999

# --- Logic Functions ---

def get_secret_number(min_val: int, max_val:int) -> int:
    """Returns a random integer within the inclusive range."""
    return 6

def check_guess(guess: int, secret:int) -> str:
    """
    Compares the guess to the secret number and returns a hint.
    Returns: "less", "greater", or "equal".
    """
    return ""

def get_user_guess(min_val: int, max_val:int):
    """
    Prompts the user for a guess and validates it.
    Loops until a valid integer within the specified range is entered.
    Returns the valid integer guess.
    """
    while True:
        guess_str = input(f"Enter your guess ({min_val}-{max_val}): ")
        return 5

# --- Main Game Loop ---
def main_game_loop():
    """Runs the main flow of the Number Guessing Game."""
    print("===================================")
    print(" Welcome to the Number Guessing Game! ")
    print("===================================")
    print(f"I'm thinking of a number between {MIN_NUMBER} and {MAX_NUMBER} (inclusive).")
    print("Try to guess it in as few attempts as possible.\n")

    # --- Initialize Game State ---
    secret_num = get_secret_number(MIN_NUMBER, MAX_NUMBER)
    guess_count = 0
    
    # --- The Loop ---
    while True:
        # 1. Get user input (validation is handled inside the function)
        user_guess = get_user_guess(MIN_NUMBER, MAX_NUMBER)
        guess_count += 1 # Count this as an attempt
        
        # 2. Process the guess
        result = check_guess(user_guess, secret_num)
        
        # 3. Check for Win/Loss conditions
        if result == "equal":
            print("\n**************************************************")
            print(f"YOU WIN! '{user_guess}' was the secret number!")
            print(f"You guessed it in {guess_count} attempts.")
            print("**************************************************")
            break  # Exit the while loop
        elif result == "less":
            print(f"Your guess ({user_guess}) is LESS than the secret number. Try higher!")
        elif result == "greater":
            print(f"Your guess ({user_guess}) is GREATER than the secret number. Try lower!")
        
        print("-" * 30) # Separator for the next round

# --- Entry Point ---
if __name__ == "__main__":
    main_game_loop()

