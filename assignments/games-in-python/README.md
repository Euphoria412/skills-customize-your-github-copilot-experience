
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build the classic Hangman word-guessing game using Python strings, loops, conditionals, and user input. This assignment helps you practice program flow, list handling, and game state logic.

## 📝 Tasks

### 🛠️ Game Setup and Word Selection

#### Description
Create the game setup so the program can choose a hidden word and prepare the display for player guesses.

#### Requirements
Completed program should:

- Define a list of possible secret words
- Randomly choose one word from the list
- Display the secret word as blanks (e.g. `_ _ _ _`)
- Track letters the player has guessed correctly and incorrectly

### 🛠️ Main Game Loop and Win/Lose Logic

#### Description
Build the main game loop that processes player guesses, updates the display, and ends the game with a win or loss.

#### Requirements
Completed program should:

- Prompt the player to guess one letter at a time
- Update the displayed progress when letters are correct
- Count and show remaining incorrect attempts
- End the game when the word is fully guessed or attempts run out
- Display a clear win or lose message at the end

### 🛠️ Player Feedback and Replay Option

#### Description
Add user-friendly feedback so the player knows their current progress and can play again if desired.

#### Requirements
Completed program should:

- Show the current state of the word after each guess
- List letters that have already been guessed
- Inform the player when a guess is invalid or already used
- Optionally ask whether the player wants to try again after the game ends
