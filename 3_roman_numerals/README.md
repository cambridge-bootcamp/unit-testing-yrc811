# Roman Numerals

In this task you have a set of tests for an application that takes
as input decimal numbers up to 3,999 and prints their roman numeral
representation. Here is an intended example exchange:

```
$ python3 roman_numerals.py 
Welcome to the Roman Numeral Converter!
Enter a number to convert, or type 'quit' to exit.
Enter a number: 1
The Roman numeral for 1 is I
Enter a number: 12
The Roman numeral for 12 is XII
Enter a number: 5000
Error: Input must be an integer between 1 and 3999. Please enter a valid number or 'quit'.
Enter a number: 2025
The Roman numeral for 2025 is MMXXV
...
```

1) Write the missing code in `roman_numerals.py`. 
   Try not to change `test_roman_numerals.py`; run `pylint` and use the existing tests
   to experiment with test-driven development. Fix the errors `pylint` finds, and re-run
   `pylint` iteratively.
