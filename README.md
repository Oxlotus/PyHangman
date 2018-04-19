# PyHangman
### Introduction
This is a Python implementation of the word-based game, Hangman.

### How It Works
* __Random Words__: The words are placed in complete lowercase in the assets/words.txt file. From there, a list is built using each word in the file as a member. Once a list is built, the program will generate a random value between 0 and the length of the list. This random value is used to select a member from the list.

* __Guessing__: By technicality, the user should only possess 6 guesses. However, I'm a considerate developer and have provided the end user with 8 total guesses. :) Every entry the user provides is considered a "guess". For example, guessing a letter would increment the value, and all the same, entering a duplicate value (the same guess, but twice) would also increment the value.

* __Testing User Input__: Every randomly pulled word is sliced into characters and placed in a new list; the user's input is tested against this list. The user's final input is placed in a separate list and is provided to the user at the end of the session. (This is for comparison between the random word and their input.)
