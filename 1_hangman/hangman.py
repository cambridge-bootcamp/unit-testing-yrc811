import random
import string
import sys  # Import sys to read command-line arguments

from typing import List, Optional, Set

# --- Constants ---

MAX_WRONG_GUESSES = 6

# ASCII art stages for the hangman.
# Index 0 is the start (0 wrong guesses), index 6 is the end (6 wrong guesses).
HANGMAN_PICS = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========""",
]


# --- Logic Functions ---

def load_words_from_file(filepath: str) -> Optional[List[str]]:
    """Loads a list of words from a text file.  Expects one word per
    line. Words are stripped of whitespace and converted to uppercase.
    Returns a list of valid words, or None if the file can't be read.
    """
    try:
        with open(filepath, 'r') as f:
            lines = f.readlines()
            # Process lines: strip whitespace, convert to upper,
            # and filter out empty strings or non-alphabetic lines.
            words = []
            for line in lines:
                word = line.strip().upper()
                if word and word.isalpha():  # Ensure it's a valid word
                    words.append(word)
            return words
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
        return None
    except IOError as e:
        print(f"Error: Could not read the file '{filepath}'. Reason: {e}")
        return None


def get_random_word(word_list: List[str]) -> str:
    """Selects a single random word from the provided list."""
    return random.choice(word_list)


def draw_hangman(wrong_guesses: int) -> str:
    """Returns the ASCII art string corresponding to the number of wrong guesses."""
    if 0 <= wrong_guesses < len(HANGMAN_PICS):
        return HANGMAN_PICS[wrong_guesses]
    return HANGMAN_PICS[-1]  # Default to the last picture if something goes wrong


def get_display_word(secret_word: str, correct_letters: Set[str]) -> str:
    """
    Returns the word display string with underscores for unguessed letters.
    Example: (secret="PYTHON", correct={'P', 'N'}) -> "P _ _ _ _ N"
    """
    display = ""
    for letter in secret_word:
        if letter in correct_letters:
            display += letter + " "
        else:
            display += "_ "
    # Return the string, removing the trailing space
    return display.strip()


def get_guess(all_guessed_letters: Set[str]) -> str:
    """
    Prompts the user for a single letter guess and validates it.
    Ensures the guess is a single letter, alphabetic, and not already guessed.
    Returns the validated guess in uppercase.
    """
    while True:
        guess = input("Guess a letter: ")

        if len(guess) != 1:
            print("Invalid input. Please enter exactly one letter.")
        elif guess not in string.ascii_uppercase:
            print("Invalid input. Please enter a letter (A-Z).")
        elif guess in all_guessed_letters:
            print(f"You have already guessed '{guess}'. Try again.")
        else:
            return guess


def check_win(secret_word: str, correct_letters: Set[str]) -> bool:
    """
    Checks if the player has won.
    This is true if every unique letter in the secret_word is present
    in the set of correct_letters.
    """
    secret_word_letters = set(secret_word)
    # Returns True if the set of word letters is a subset of correct guesses
    return secret_word_letters <= correct_letters


# --- Main Game Loop ---

def main_game_loop(word_list: List[str]) -> None:
    """Runs the main flow of the Hangman game using the provided word_list."""
    print("==============================")
    print("Welcome to Hangman (CLI Edition)!")
    print("==============================")
    print(f"You have {MAX_WRONG_GUESSES} wrong guesses. Good luck!\n")

    # --- Initialize Game State ---
    secret_word = get_random_word(word_list)  # Use the passed-in list
    correct_letters : Set = set()  # A set of letters the user has guessed correctly
    wrong_letters : Set = set()    # A set of letters the user has guessed incorrectly
    wrong_guesses_made = 0   # Counter for wrong guesses

    # --- The Loop ---
    game_over = False
    while not game_over:
        # 1. Display current state
        print(draw_hangman(wrong_guesses_made))

        # Display wrong letters (if any)
        if wrong_letters:
            # Sort the letters for a clean display
            print(f"Wrong Guesses: {' '.join(sorted(list(wrong_letters)))}\n")

        # Display the word-in-progress (e.g., P _ T H _ N)
        print("The word: " + get_display_word(secret_word, correct_letters))
        print("-" * 30)

        # 2. Get user input
        all_guessed = correct_letters | wrong_letters  # Combine both sets
        guess = get_guess(all_guessed)

        # 3. Process the guess
        if guess in secret_word:
            print(f"\nGood guess! '{guess}' is in the word.\n")
            correct_letters.add(guess)
        else:
            print(f"\nSorry, '{guess}' is not in the word.\n")
            wrong_letters.add(guess)
            wrong_guesses_made += 1

        # 4. Check for Win/Loss conditions
        if check_win(secret_word, correct_letters):
            print("************************************")
            print(f"YOU WIN! Congratulations!")
            print(f"You guessed the word: {secret_word}")
            print("************************************")
            game_over = True
        elif wrong_guesses_made >= MAX_WRONG_GUESSES:
            print(draw_hangman(wrong_guesses_made))  # Show the final hanging
            print("************************************")
            print("GAME OVER. You lost.")
            print(f"The secret word was: {secret_word}")
            print("************************************")
            game_over = True


# --- Entry Point ---
if __name__ == "__main__":
    # Check if a command-line argument (the filepath) was provided
    if len(sys.argv) < 2:
        print("Error: No word list file provided.")
        print("Usage: python hangman_cli.py words.txt")
        sys.exit(1)  # Exit with an error code

    # The first argument (index 1) is the filepath
    word_file_path = sys.argv[1]
    
    # Load words from the specified file
    game_words = load_words_from_file(word_file_path)

    # Check if words were successfully loaded
    if not game_words:  # This catches both None (file error) or an empty list
        print("No valid words found in the file. Cannot start game.")
        sys.exit(1)
    
    # If words are loaded, start the game
    main_game_loop(game_words)
