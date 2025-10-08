import math

# --- Constants ---
TOLERANCE = 1e-7  # How close to the root we need to be.
MAX_ITERATIONS = 100 # Safety limit to prevent infinite loops.

# --- Core Functions ---

def func(x: float) -> float:
    """
    The function we want to find the root of. 
    This calculates f(x) for the equation: f(x) = x^3 - x - 1
    """
    return x**3 - x - 1

def deriv(x: float) -> float:
    """
    The derivative of our function, f'(x).
    For f(x) = x^3 - x - 1, the derivative is: f'(x) = 3x^2 - 1
    """
    return 3 * x**2 - 1

from typing import Callable, Tuple, Optional

def newton_raphson_find_root(
    f: Callable[[float], float],
    df: Callable[[float], float],
    initial_guess: float,
    tolerance: float,
    max_iter: int
) -> Tuple[Optional[float], int]:
    """
    Finds a root of a function using the Newton-Raphson iterative method.

    This is a "pure" function: it takes functions as arguments and returns a value.
    - f: The function to solve (e.g., func)
    - df: The derivative of the function (e.g., deriv)
    - initial_guess (float): Where to start the search.
    - tolerance (float): The stopping criterion.
    - max_iter (int): The maximum number of iterations to attempt.
    
    Returns: The (float) root if found within max_iter, otherwise None.
    """
    x_n = initial_guess  # Our starting point, x_0

    for i in range(max_iter):
        fx = f(x_n)
        dfx = df(x_n)

        # Check for convergence: if f(x_n) is very close to 0, we found the root.
        if abs(fx) < tolerance:
            # Return the root and the number of iterations it took
            return x_n, i

        # Check for division by zero (horizontal tangent), which fails the method.
        # We check against a very small number, not just literal 0.
        if abs(dfx) < 1e-12:
            print(f"\nError: Derivative was zero at x = {x_n}. Failed to converge.")
            return None, i

        # The Newton-Raphson formula: x_n+1 = x_n - f(x_n) / f'(x_n)
        x_n_plus_1 = x_n - (fx / dfx)
        
        # Update our current guess for the next loop iteration
        x_n = x_n_plus_1

    # If the loop completes, we failed to converge within max_iterations
    print(f"\nError: Failed to converge after {max_iter} iterations.")
    return None, max_iter

def get_user_float(prompt_message: str) -> float:
    """
    Prompts the user for a float and validates it.
    Loops until a valid float is entered.
    """
    while True:
        num_str = input(prompt_message)
        try:
            # Attempt to convert the input string to a float
            num_float = float(num_str)
            return num_float
        except ValueError:
            # This triggers if float(num_str) fails
            print(f"'{num_str}' is not a valid floating-point number. Please try again.")

# --- Main Program Flow ---

def main() -> None:
    """Main execution function for the CLI."""
    print("===================================")
    print(" Newton-Raphson Root Finder ")
    print("===================================")
    print("This program finds a real root for the equation: f(x) = x^3 - x - 1")
    print(f"It will stop when the result is within {TOLERANCE} of the true root.\n")

    # Get the starting point from the user
    initial_guess = get_user_float("Enter your initial guess (e.g., 1.0 or 2.0): ")

    print(f"\nCalculating root starting from x_0 = {initial_guess}...")
    
    # Run the core logic function
    root, iterations = newton_raphson_find_root(
        func, 
        deriv, 
        initial_guess, 
        TOLERANCE, 
        MAX_ITERATIONS
    )

    print("-----------------------------------")
    if root is not None:
        print(f"SUCCESS: Root found!")
        print(f"  x = {root}")
        print(f"  f(x) = {func(root)}")
        print(f"  Found in {iterations} iterations.")
    else:
        print("FAILURE: Could not find a root from that starting point.")
    print("-----------------------------------")


# --- Entry Point ---
if __name__ == "__main__":
    main()
