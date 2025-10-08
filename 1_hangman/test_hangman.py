import sys
from unittest.mock import patch, mock_open
import hangman as hm  # Import the game file to test its functions

from typing import Set, Callable


def test_get_display_word() -> None:
    """
    Tests the function that creates the "P _ T H _ N" display.
    """
    secret_word = "PYTHON"
    
    # Test with no correct guesses
    correct = set()
    assert hm.get_display_word(secret_word, correct) == "_ _ _ _ _ _"
    
    # Test with some correct guesses
    correct = {'P', 'O'}
    assert False  # FIXME
    
    # Test with all correct guesses
    assert False  # FIXME

    # Test a word with repeated letters
    secret_word_repeat = "APPLE"
    correct_repeat = {'P', 'E'}
    assert hm.get_display_word(secret_word_repeat, correct_repeat) == "_ P P _ E"


def test_check_win() -> None:
    """
    Tests the win-condition checking logic.
    """
    secret_word = "TEST" # Unique letters are T, E, S
    
    # Test not won (empty set input)
    correct = set()
    assert not hm.check_win(secret_word, correct), "check_win should be False for empty set"
    
    # Test not won (partially complete)
    correct = {'T', 'E'}
    assert False  # FIXME

    # Test winning condition
    correct = {'T', 'E', 'S'}
    assert False  # FIXME


def test_load_words_from_file_success_and_clean() -> None:
    """
    Tests that the file loader correctly reads, strips, uppercases,
    and filters words from a mock file.
    Uses 'with patch()' as a context manager instead of a decorator.
    """
    mock_content = (
        "  apple\n"
        "Banana\n"
        "\n"
        "TEST\n"
        "12345\n"
        "word-with-hyphen\n"
        "final"
    )
    expected_output = ["APPLE", "BANANA", "TEST", "FINAL"]
    
    # Use patch as a context manager to mock 'open'
    with patch("builtins.open", mock_open(read_data=mock_content)):
        words = hm.load_words_from_file("fake_path.txt")
        assert words == expected_output, f"Expected {expected_output}, but got {words}"


def test_load_words_empty_file() -> None:
    """
    Tests that an empty file correctly returns an empty list.
    """
    with patch("builtins.open", mock_open(read_data="")):
        words = hm.load_words_from_file("empty.txt")
        assert words == [], f"Expected empty list [], but got {words}"


def test_load_words_file_not_found() -> None:
    """
    Tests that the function returns None and prints an error if the file is not found.
    Uses nested 'with' statements to mock both 'open' and 'print'.
    """
    # We patch 'open' to raise an error, and patch 'print' to capture its output.
    with patch("builtins.open", side_effect=FileNotFoundError):
        with patch('builtins.print') as mock_print_call:
            words = hm.load_words_from_file("nonexistent.txt")
            
            # Check that the function returned None as expected
            assert words is None, "Function should return None on FileNotFoundError"
            
            # Check that an error message was printed
            mock_print_call.assert_called_once()
            print_arg = mock_print_call.call_args[0][0]
            assert "Error: The file" in print_arg, "Error message for file not found was incorrect"


def test_load_words_io_error() -> None:
    """
    Tests that the function returns None and prints an error for a general IOError.
    """
    # This simulates a file permission error, for example.
    with patch("builtins.open", side_effect=IOError("Permission denied")):
        with patch('builtins.print') as mock_print_call:
            words = hm.load_words_from_file("protected.txt")
            
            # Check that the function returned None
            assert words is None, "Function should return None on IOError"
            
            # Check that the correct error message was printed
            mock_print_call.assert_called_once()
            print_arg = mock_print_call.call_args[0][0]
            assert "Error: Could not read the file" in print_arg, "Error message for IOError was incorrect"
