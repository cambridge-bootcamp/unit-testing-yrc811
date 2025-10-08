import random
import secrets
import string
from typing import List


# --- Core Logic Function ---

def generate_password(length: int, use_lower: bool, use_upper: bool, use_digits: bool, use_symbols: bool) -> str:
    """
    Generates a secure, random password based on user-specified criteria.
    
    Args:
        length: The total desired length of the password.
        use_lower: Whether to include lowercase letters.
        use_upper: Whether to include uppercase letters.
        use_digits: Whether to include digits (0-9).
        use_symbols: Whether to include punctuation symbols.
        
    Returns:
        A randomly generated password string.
        
    Raises:
        ValueError: If no character types are selected or if the length
                    is too short to include one of each selected type.
    """
    
    character_pool: List[str] = []
    guaranteed_chars: List[str] = []

    # 1. Build the character pool and select one guaranteed char from each chosen set
    if use_lower:
        character_pool.extend(string.ascii_lowercase)
        guaranteed_chars.append(secrets.choice(string.ascii_lowercase))
        
    if use_upper:
        character_pool.extend(string.ascii_uppercase)
        guaranteed_chars.append(secrets.choice(string.ascii_uppercase))
        
    if use_digits:
        character_pool.extend(string.digits)
        guaranteed_chars.append(secrets.choice(string.digits))
        
    if use_symbols:
        character_pool.extend(string.punctuation)
        guaranteed_chars.append(secrets.choice(string.punctuation))

    # 2. Validation Checks
    if not character_pool:
        # This error is *also* checked in main(), but it's good practice
        # to have the core function be robust on its own.
        raise ValueError("Cannot generate password. At least one character type must be selected.")

    if length < len(guaranteed_chars):
        raise ValueError(
            f"Password length ({length}) is too short. "
            f"It must be at least {len(guaranteed_chars)} to include one of each selected character type."
        )

    # 3. Fill the rest of the password
    remaining_length = length - len(guaranteed_chars)
    
    # Add random characters from the *full* pool to fill the remaining length
    # This list comprehension is a more "Pythonic" way to write a for-loop
    other_chars = [secrets.choice(character_pool) for _ in range(remaining_length)]

    # 4. Combine guaranteed chars with other chars and shuffle
    password_list = guaranteed_chars + other_chars
    random.shuffle(password_list)

    # 5. Convert the list of characters back into a final string
    return "".join(password_list)

# --- User Input Helper Functions ---

def get_yes_no_input(prompt: str) -> bool:
    """
    Gets a simple yes/no (y/n) boolean input from the user.
    It will loop until a valid 'y' or 'n' is given.
    """
    while True:
        answer = input(prompt + " (y/n): ").lower().strip()
        if answer == 'y':
            return True
        if answer == 'n':
            return False
        print("Invalid input. Please enter 'y' or 'n'.")

def get_int_input(prompt: str, min_val: int = 1) -> int:
    """
    Gets a valid integer input from the user.
    It will loop until a valid integer >= min_val is given.
    """
    while True:
        try:
            value_str = input(prompt + f" (minimum {min_val}): ")
            value_int = int(value_str)
            
            if value_int < min_val:
                print(f"Value must be at least {min_val}.")
            else:
                return value_int
        except ValueError:
            print("Invalid input. Please enter a whole number.")

# --- Main CLI Execution ---

def main() -> None:
    """Main function to run the password generator CLI."""
    print("--- 🔐 Secure Password Generator ---")
    
    # 1. Get user preferences
    # We ask for length *after* criteria so we can calculate the *true* minimum length
    use_lower = get_yes_no_input("Include lowercase letters (a-z)?")
    use_upper = get_yes_no_input("Include uppercase letters (A-Z)?")
    use_digits = get_yes_no_input("Include numbers (0-9)?")
    use_symbols = get_yes_no_input("Include symbols (!@#$%)?")

    # 2. Validate that at least one character type was selected
    if not any([use_lower, use_upper, use_digits, use_symbols]):
        print("\n❌ Error: You must select at least one character type to generate a password.")
        return  # Exit the program

    # 3. Calculate minimum possible length and get length from user
    # The sum() of bools works because True==1 and False==0
    min_length = sum([use_lower, use_upper, use_digits, use_symbols])
    print(f"Note: Your password must be at least {min_length} character(s) long to include one of each selected type.")
    
    length = get_int_input("Enter desired password length", min_val=min_length)

    # 4. Generate and display the password
    try:
        password = generate_password(length, use_lower, use_upper, use_digits, use_symbols)
        print("\n✅ Your new secure password is:")
        print("-------------------------------")
        print(f"   {password}")
        print("-------------------------------")
    except ValueError as e:
        # This will catch the errors raised from generate_password
        print(f"\n❌ Error: {e}")

if __name__ == "__main__":
    main()