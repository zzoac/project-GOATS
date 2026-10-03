"""Entry point for the group project.

`python main.py` must run your project at every milestone, so keep this file working
from Milestone 1 onward. Replace the placeholder below with your own core loop.
"""
feedback = {
    "correct": "Correct",
    "wrong_position":"Wrong Position",
    "incorrect": "Not in word"
}

def compare_input(guess, secret_word):    
    guess_list=list(guess)
    secret_list=list(secret_word)
    result_list=[""]*5
    for i in range(len(guess_list)):
        
        if guess_list[i] == secret_list[i]:
            result_list[i] = feedback["correct"]
            guess_list[i] = "_"
            secret_list[i] = "_"
    for i in range(len(guess_list)):
        
        if guess_list[i] != "_" and guess_list[i] in secret_list:
            result_list[i] = feedback["wrong_position"]
            index=secret_list.index(guess_list[i])
            secret_list[index] = "_"
        
        elif guess_list[i] != "_" and guess_list[i] not in secret_list:
            result_list[i] = feedback["incorrect"]
    
    return result_list
def validate_guess(guess):
    if len(guess) != 5:
        return False
    if not guess.isalpha():
        return False

    return True

def get_guess():
    while True:
        guess = input("Enter your 5-letter guess: ").lower()

        if len(guess) == 5 and guess.isalpha():
            return guess

        print("Invalid guess. Please enter 5 words EXACTLY")

def main():
    secret_word = "space"
    attempts = 6

    print("Welcome to Wordle!")
    print("You have 6 tries to guess the word correctly!")

    guesses = []

    
    guess = get_guess()
    guesses.append(guess)

    print("Recorded guesses:", guesses)

    
    print("CSCI 1030U group project - not built yet.")
    print("Replace main() with your core loop. See MILESTONES.md for what is due when.")




if __name__ == '__main__':
    main()
