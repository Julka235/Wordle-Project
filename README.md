# Wordle Game in Python and Pygame

## Description

This project implements a version of the popular Wordle game using English words. It includes a graphical interface and allows players to input letters either by clicking an on-screen keyboard or typing on their physical keyboard.

## Installation

1. Install Python 3.10.12.
2. Install the pygame 2.5.2 library using:
'''
    pip install pygame
'''

## How to Play

1. Run the main.py file.
2. Enter 5-letter English words using either:
    - Your physical keyboard.
    - The on-screen keyboard by clicking its buttons.
3. Press Enter to submit the word. If the word is invalid, delete it using Backspace and try again.

### Game Rules

- You have 6 attempts to guess the correct word.
- The game provides color-coded hints based on the standard Wordle rules:
    - Green: The letter is correct and in the correct position.
    - Yellow: The letter is correct but in the wrong position.
    - Gray: The letter is not in the word.
- If you guess the word, all letters will turn green, and "YOU WON!" will be displayed.
- If you fail, the correct word will be shown after 6 attempts.

### Game Options

- Try Again: Start a new game.
- Give Up: Reveal the correct word and end the current game.

## Project Overview

The project consists of three main files:

- classes.py: Contains the core logic of the game.
    - Key Classes:
      - Database: Handles loading and validating word lists.
      - Guesswords: Manages the list of possible answers.
      - ValidWords: Checks if a word is valid.
      - Solution: Implements the logic for checking guesses and providing feedback.
- main.py: Implements the graphical interface and gameplay interactions.
- test_classes.py: Contains test cases to validate the functionality of classes.py.

### Technical Details

- Word lists:
  - guesswords.txt: For generating random solutions.
  - valid_words.txt: For validating user input.
- Both lists are pre-processed for compatibility and efficiency.
- Dependencies:
  - Python 3.10.12.
  - Pygame 2.5.2.

### Testing

Key test cases include:

- Validating word searches in ValidWords:
  - Words not in the list.
  - First/last words in the list.
  -  Out-of-bounds cases.
- Testing color feedback in Solution:
  - Duplicate letters in guesses and the solution.
  - Matching letters in different positions.
  - Exact match of the guess with the solution.

## Objective

The goal is to recreate the Wordle experience with an intuitive graphical interface and multiple input methods, making it easy and enjoyable to play.

Enjoy solving puzzles and have fun with Wordle! 😊
