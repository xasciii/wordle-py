# Python Wordle

A simple Wordle inspired game made in Python

I made this as a small Python project to practice stuff like lists, loops, conditions, input and importing data from another Python file

## breakdown

The game randomly chooses a 5 letter word from `words.py`

You get **10 attempts** to guess the word

The results work like this:

* **UPPERCASE** = correct letter in the correct position
* **lowercase** = correct letter but in the wrong position
* **_** = letter isn't in the word

eg:

```text
Welcome to Python Wordle!
Guess the 5-letter word. You have 10 attempts.

Guess 1/6: house
H__SE
```
<img width="432" height="160" alt="image" src="https://github.com/user-attachments/assets/7dbaf557-50ad-405f-9ae1-399a56a6be5b" />


## extras

This is a basic version for now. Some things I could add later:

* Proper Wordle colours
* A bigger word list
* Better handling of duplicate letters
* Checking that guesses are actual words
* A graphical interface
* Win/loss statistics
* Replay option
* Keyboard display

## why I made it

This is a small project I made while learning Python and getting more comfortable with programming, it's nothing huge, but it's a good way to practice the basics

