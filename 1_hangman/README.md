# Hangman

The program is run using `python hangman.py hangman_word_list.txt`.
You will need to `cd` into this directory to run the commands as written here.

1) Review the `hangman.py` code to understand how it works. Try running it.

2) Look at `test_hangman.py` and understand how it works. You can use
   the internet or a chatbot to understand anything that is new to you
   (such as the `patch` method used to mock a file read).

3) `pytest test_hangman.py` is failing. Implement or fix all the places marked `FIXME`.

4) When you enter a lower case guess, the program tells you to use
   upper case. This is annoying. Fix it so that it converts automatically
   to upper case *and* add a new test case to check for that.
