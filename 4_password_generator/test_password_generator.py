import string
import pytest
from unittest.mock import patch

# Import the functions we want to test from your .py file
from password_generator import (
    generate_password,
    get_yes_no_input,
    get_int_input
)

## ---------------------------------
## Tests for generate_password()
## ---------------------------------

def test_password_length():
    """Test that the generated password is the correct length."""
    length = 15
    pw = generate_password(length, True, True, True, True)
    assert len(pw) == length

## ---------------------------------
## Tests for helper functions (with mocking)
## ---------------------------------

@patch('builtins.input', return_value='y')
def test_get_yes_no_input_yes(mock_input):
    """Test that 'y' returns True."""
    assert get_yes_no_input("Test prompt?") is True

