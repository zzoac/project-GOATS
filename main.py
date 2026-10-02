"""Entry point for the group project.

`python main.py` must run your project at every milestone, so keep this file working
from Milestone 1 onward. Replace the placeholder below with your own core loop.
"""
feedback = {
    "correct": "Correct",
    "wrong_position":"Wrong Position",
    "incorrect": "Not in word"
}

def validate_guess(guess):
    if len(guess) != 5:
        return False
    if not guess.isalpha():
        return False

    return True

def main():
    secret_word = "space"
    attempts = 6

    print("Welcome to Wordle!")
    print("You have 6 tries to guess the word correctly!")

    
    print("CSCI 1030U group project - not built yet.")
    print("Replace main() with your core loop. See MILESTONES.md for what is due when.")




if __name__ == '__main__':
    main()
