import sys
from roman_numerals import to_roman

def test_single_digits():
    """Tests the conversion of single-digit numbers."""
    print("Running test_single_digits...")
    assert to_roman(1) == 'I', "Test for 1 failed"
    assert to_roman(2) == 'II', "Test for 2 failed"
    assert to_roman(3) == 'III', "Test for 3 failed"
    print("test_single_digits passed.")

def test_basic_numerals():
    """Tests the conversion of basic Roman numerals (V, X, L, C, D, M)."""
    print("Running test_basic_numerals...")
    assert to_roman(5) == 'V', "Test for 5 failed"
    assert to_roman(10) == 'X', "Test for 10 failed"
    assert to_roman(50) == 'L', "Test for 50 failed"
    assert to_roman(100) == 'C', "Test for 100 failed"
    assert to_roman(500) == 'D', "Test for 500 failed"
    assert to_roman(1000) == 'M', "Test for 1000 failed"
    print("test_basic_numerals passed.")

def test_subtractive_numerals():
    """Tests the conversion of numbers using the subtractive principle (IV, IX, etc.)."""
    print("Running test_subtractive_numerals...")
    assert to_roman(4) == 'IV', "Test for 4 failed"
    assert to_roman(9) == 'IX', "Test for 9 failed"
    assert to_roman(40) == 'XL', "Test for 40 failed"
    assert to_roman(90) == 'XC', "Test for 90 failed"
    assert to_roman(400) == 'CD', "Test for 400 failed"
    assert to_roman(900) == 'CM', "Test for 900 failed"
    print("test_subtractive_numerals passed.")

def test_combined_numerals():
    """Tests the conversion of more complex numbers."""
    print("Running test_combined_numerals...")
    assert to_roman(38) == 'XXXVIII', "Test for 38 failed"
    assert to_roman(194) == 'CXCIV', "Test for 194 failed"
    assert to_roman(444) == 'CDXLIV', "Test for 444 failed"
    assert to_roman(1994) == 'MCMXCIV', "Test for 1994 failed"
    assert to_roman(2023) == 'MMXXIII', "Test for 2023 failed"
    assert to_roman(3999) == 'MMMCMXCIX', "Test for 3999 failed"
    print("test_combined_numerals passed.")

def test_error_handling():
    """Tests that the function raises a ValueError for invalid input."""
    print("Running test_error_handling...")
    try:
        to_roman(0)
        assert False, "Test for 0 failed: expected ValueError"
    except ValueError:
        pass  # Test passed

    try:
        to_roman(4000)
        assert False, "Test for 4000 failed: expected ValueError"
    except ValueError:
        pass  # Test passed

    try:
        to_roman("abc")
        assert False, "Test for string input failed: expected ValueError"
    except ValueError:
        pass  # Test passed
    
    print("test_error_handling passed.")

if __name__ == "__main__":
    try:
        test_single_digits()
        test_basic_numerals()
        test_subtractive_numerals()
        test_combined_numerals()
        test_error_handling()
        print("\nAll tests passed successfully!")
    except AssertionError as e:
        print(f"\nOne or more tests failed: {e}")
        sys.exit(1)
