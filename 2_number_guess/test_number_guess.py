from unittest.mock import patch
import number_guess as ng  # Import the new game file


# --- Test Functions for Number Guesser ---

def test_check_guess_logic():
    """
    Tests the core logic function 'check_guess'.
    This is a pure function and doesn't require mocking.
    """
    secret = 500
    
    # Test "less"
    assert ng.check_guess(100, secret) == "less", "100 should be 'less' than 500"
    
    # Test "greater"
    assert ng.check_guess(800, secret) == "greater", "800 should be 'greater' than 500"
    
    # Test "equal"
    assert ng.check_guess(500, secret) == "equal", "500 should be 'equal' to 500"
    
    # Test boundaries (assuming 0-999 range, check logic relative to secret)
    secret_low = 1
    assert ng.check_guess(0, secret_low) == "less", "Boundary 0 check failed"
    
    secret_high = 998
    assert ng.check_guess(999, secret_high) == "greater", "Boundary 999 check failed"


def test_get_user_guess_valid():
    """
    Tests the 'get_user_guess' function with a single valid input.
    We mock 'builtins.input' to provide the value directly.
    """
    # Use patch() as a context manager to mock 'input'
    # We also patch 'print' to silence the function's output during the test.
    with patch('builtins.input', return_value='123'):
        with patch('builtins.print'):
            guess = ng.get_user_guess(0, 999)
            assert guess == 123, "Should return the integer 123"

def test_get_user_guess_nan_then_valid():
    """
    Tests that 'get_user_guess' rejects non-numeric input and re-prompts.
    We use 'side_effect' to provide a list of inputs over multiple calls.
    """
    # 'side_effect' provides these values sequentially to calls to 'input()'
    mock_inputs = ['hello', 'fifty', '250']
    
    with patch('builtins.input', side_effect=mock_inputs):
        with patch('builtins.print'): # Suppress print calls (like "not a valid number")
            guess = ng.get_user_guess(0, 999)
            # The function should loop until it gets '250'
            assert guess == 250, "Should reject 'hello' and 'fifty', and return 250"


def test_get_user_guess_range_then_valid():
    """
    Tests that the function rejects numbers out of range and re-prompts.
    """
    # Simulate user typing -5 (too low), 1000 (too high), then 500 (valid)
    mock_inputs = ['-5', '1000', '500']
    
    with patch('builtins.input', side_effect=mock_inputs):
        with patch('builtins.print'): # Suppress print calls (like "out of range")
            guess = ng.get_user_guess(0, 999)
            # The function should loop until it gets '500'
            assert guess == 500, "Should reject -5 and 1000, and return 500"
