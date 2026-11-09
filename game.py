

import random
import webbrowser


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
    "correct": "🟩",
    "wrong_position": "🟨",
    "incorrect": "⬜"
}


def compare_input(guess, secret_word):
    """Compare the guess with the secret word."""

    guess_list = list(guess)
    secret_list = list(secret_word)
    result_list = [""] * 5

    # First pass: correct letters in the correct position.
    for i in range(len(guess_list)):
        if guess_list[i] == secret_list[i]:
            result_list[i] = feedback["correct"]
            guess_list[i] = "_"
            secret_list[i] = "_"

    # Second pass: correct letters in the wrong position.
    for i in range(len(guess_list)):
        if guess_list[i] != "_" and guess_list[i] in secret_list:
            result_list[i] = feedback["wrong_position"]

            index = secret_list.index(guess_list[i])
            secret_list[index] = "_"

        elif guess_list[i] != "_" and guess_list[i] not in secret_list:
            result_list[i] = feedback["incorrect"]

    return result_list


def validate_guess(guess):
    """Check that the guess contains exactly five letters."""

    if len(guess) != 5:
        return False

    if not guess.isalpha():
        return False

    return True


def get_guess():
    """Ask the player for a valid guess."""

    while True:
        guess = input("Enter your 5-letter guess: ").lower()

        if validate_guess(guess):
            return guess

        print("Invalid guess. Please enter 5 letters EXACTLY.")

# Timi
def offer_hint(secret_word, guesses, revealed, hints_left):
    """Ask if the player wants a hint and reveal one unfound letter."""
    if hints_left == 0:
        return hints_left

    answer = input(
        f"Use a hint? ({hints_left} left) (yes/no): "
    ).strip().lower()
    if answer not in ("yes", "y"):
        return hints_left

    found = set(revealed)
    for guess in guesses:
        for i in range(len(secret_word)):
            if guess[i] == secret_word[i]:
                found.add(i)

    options = [i for i in range(len(secret_word)) if i not in found]
    if not options:
        print("You've already found every letter!")
        return hints_left

    pos = random.choice(options)
    revealed.add(pos)
    print(f"Hint: letter {pos + 1} is '{secret_word[pos].upper()}'")
    return hints_left - 1



def show_wordle_video():
    """Open the Wordle tutorial."""

    video_url = "https://www.youtube.com/watch?v=lv4Zg-209MY"

    print("Here is a video that explains how to play Wordle:")
    print(video_url)

    if not webbrowser.open(video_url):
        print("Your browser could not be opened automatically.")
        print("Copy and paste the link above.")

#Timi : pass difficulty so the hint count matches the selected setting.
def play_game(attempts, tracker, difficulty):
    """Run a Wordle game using the selected attempt limit."""

    while True:

        # Ask whether the player knows how to play.
        while True:
            knows_how_to_play = input(
                "Do you know how to play Wordle? (yes/no): "
            ).strip().lower()

            if knows_how_to_play in ("yes", "y"):
                print("Great! You can continue to the game.")
                break

            elif knows_how_to_play in ("no", "n"):
                show_wordle_video()
                break

            else:
                print("Please answer yes or no.")

        secret_word = random.choice(word_list)

        #Timi
        guesses = []
        revealed = set()
        hints_left = {"Easy": 3, "Normal": 2, "Hard": 1}[difficulty]

        starting_attempts = attempts
        remaining_attempts = attempts

        print("\nWelcome to Wordle!")
        print(f"You have {attempts} tries to guess the word!")

        won = False

        while remaining_attempts > 0:

            print(f"\nAttempts Remaining: {remaining_attempts}")

            # Timi
            hints_left = offer_hint(
                secret_word, guesses, revealed, hints_left
            )

            guess = get_guess()

            #Timi
            guesses.append(guess)

            results = compare_input(guess, secret_word)

            print("Guess feedback:", results)

            for i in range(5):
                print(guess[i].upper(), "-", results[i])

            if guess == secret_word:
                print(
                    f"Congratulations! You guessed the word: "
                    f"{secret_word}"
                )

                won = True
                break

            remaining_attempts -= 1

        if not won:
            print("\nGame over!")
            print("The word was:", secret_word)

        username = input("Please enter your name: ").strip()

        while not username:
            username = input("Name cannot be empty. Enter your name: ").strip()

        attempts_used = starting_attempts - remaining_attempts

        tracker.record_profile(username, attempts_used, won)

        play_again = input(
            "Do you want to play again? (yes/no): "
        ).strip().lower()

        if play_again not in ("yes", "y"):
            print("Thanks for playing!")
            break
