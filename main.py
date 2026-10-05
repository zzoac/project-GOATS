"""Entry point for the group project.

`python main.py` must run your project at every milestone, so keep this file working
from Milestone 1 onward. Replace the placeholder below with your own core loop.
"""
import random

word_list = [
    "apple", "beach", "brain", "bread", "chair",
    "charm", "chase", "chest", "clock", "cloud",
    "crane", "dance", "dream", "drink", "drive",
    "earth", "flame", "flash", "float", "flour",
    "fresh", "fruit", "ghost", "glass", "grape",
    "grass", "green", "happy", "heart", "horse",
    "house", "juice", "lemon", "light", "magic",
    "mango", "money", "mouse", "music", "night",
    "ocean", "paint", "paper", "peach", "piano",
    "plant", "queen", "river", "space", "water"
]

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
    
        if validate_guess(guess):
            return guess
    
        print("Invalid guess. Please enter 5 letters EXACTLY")

def main():
    secret_word = random.choice(word_list)
    attempts = 6
    guesses = []

    print("Welcome to Wordle!")
    print("You have 6 tries to guess the word correctly!")

    while attempts > 0:
        print(f"\nAttempts Remaining: {attempts}")

    
        guess = get_guess()
        guesses.append(guess)
    
        results = compare_input(guess, secret_word)
        print("Guess feedback:", results)
        for i in range(5):
            print(guess[i].upper(), "-", results[i])


        if guess == secret_word:
            print(f"Congratulations! You guessed the word: {secret_word}")
            return
        
        attempts -= 1
        
        if attempts == 0:
            print("\nGame over!")
            print("The word was:", secret_word)


    
    print("CSCI 1030U group project - not built yet.")
    print("Replace main() with your core loop. See MILESTONES.md for what is due when.")




if __name__ == '__main__':
    main()
