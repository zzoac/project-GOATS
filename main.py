"""Entry point for the group project.

`python main.py` must run your project at every milestone, so keep this file working
from Milestone 1 onward. Replace the placeholder below with your own core loop.
"""
import random
import webbrowser
import tkinter as tk
import json 
import argparse
from menu import WordleMenu

class PlayerProfile: #f2ff1b3
    def __init__(self, username):
        self.username = username
        self.games_played = 0
        self.games_won = 0

    def display_profile(self):
        print("Username:", self.username)
        print("Games played:", self.games_played)
        print("Games won:", self.games_won)

    def save_profile(self): #cdbc78a
        with open("player_profile.json", "w") as file:
            json.dump({
                "username": self.username,
                "games_played": self.games_played,
                "games_won": self.games_won
            }, file, indent=4)

    def load_profile(self):
        try:
            with open("player_profile.json", "r") as file:
                data = json.load(file)

            self.username = data["username"]
            self.games_played = data["games_played"]
            self.games_won = data["games_won"]

        except FileNotFoundError:
            print("No saved profile found.")

    def count_games(self, history, index=0): #4676f1d
        if index == len(history):
                return 0
        return 1 + self.count_games(history, index + 1)

class statsManager:
    def __init__(self, filename="profiles.json"):
        self.filename=filename
        self.stats=self.loadStats()
    
    def loadStats(self):
        with open(self.filename, "r") as file:
            return json.load(file) 

    def saveStats(self):
        with open(self.filename,"w") as file:
            json.dump(self.stats,file,indent=4)

    def recordstats(self, username, attempts, won):#records each statistic for each player by username
        userStatHolder=None
        for p in self.stats:
            if p["username"]== username:
                userStatHolder = p
                break

        if userStatHolder in self.stats:#checks if user is already in the dictionary
            userStatHolder["games_played"]+=1
            if won:
                userStatHolder["games_won"]+=1
                if userStatHolder["attempts_used"]>attempts or userStatHolder["attempts_used"]==0:
                    userStatHolder["attempts_used"]=attempts
        else:
            new_profile={
                "username":username,
                "games_played":1,
                "games_won":1 if won else 0,
                "attempts_used": attempts if won else 0
            }
            self.stats.append(new_profile)

        self.stats= self.recursiveBubbleSort(self.stats,len(self.stats))
        self.saveStats()

    def recursiveBubbleSort(self,profiles,n=None):
        if n<=1:
            return profiles

        for i in range(n-1):
            left=self.getAttemptsUsed(profiles[i])
            right=self.getAttemptsUsed(profiles[i+1])

            if left> right:
                temp=profiles[i]
                profiles[i]=profiles[i+1]
                profiles[i+1]=temp

        return self.recursiveBubbleSort(profiles, n-1 ) #sorts the list of users by attempts recursively

    def getAttemptsUsed(self,profile):
        best=profile.get("attempts_used",99)
        if best == 0:
            return 99   
        else:
            return best
        

if __name__ =="__main__":
    parser= argparse.ArgumentParser(description="stat tracker")
    parser.add_argument("--profile",type=str,default="Player",help="Choose a player profile") #4122370
    parser.add_argument("--file", default="profiles.json", help="path to profile json")
    parser.add_argument("--leaderboard", action="store_true",help="print leaderboard")
    args = parser.parse_args()
    manager= statsManager(filename=args.file)
    if args.leaderboard:
        print("Wordle leaderboard")
        print("------------------------")
        
        count = 1
        for p in manager.stats:
            
            best= p.get('attempts_used','')
            print(f"{count}. user:{p['username']}\t games played: {p['games_played']}\t least attempts used:{p['attempts_used']}")
            count+=1
            print("--------------------------------------------------------------------")# splits between each rank
    else:
        print("loading wordle")
            

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
    "wrong_position":"🟨",
    "incorrect": "⬜"
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
def show_wordle_video(): #Timi
    video_url = "https://www.youtube.com/watch?v=lv4Zg-209MY"
    print("Here is a video that explains how to play Wordle:")
    print(video_url)
    if not webbrowser.open(video_url):
        print("Your browser could not be opened automatically. Copy and paste the link above.")#Timi
def main():

    parser = argparse.ArgumentParser(
        description="Wordle terminal game"
    )

    parser.add_argument(
        "--attempts",
        type=int,
        choices=[4, 6, 8, 10],
        help="Choose the number of attempts"
    )

    parser.add_argument(
        "--difficulty",
        choices=["easy", "normal", "hard"],
        help="Choose game difficulty"
    )

    parser.add_argument(
        "--settings",
        default="settings.json",
        help="Choose the settings file"
    )

    args = parser.parse_args()

    menu = WordleMenu(settings_file=args.settings)

    # Command-line options override saved settings.
    if args.attempts is not None:
        menu.attempts = args.attempts

    if args.difficulty is not None:

        menu.difficulty = args.difficulty.capitalize()

        if menu.difficulty == "Easy":
            menu.attempts = 8
        elif menu.difficulty == "Normal":
            menu.attempts = 6
        elif menu.difficulty == "Hard":
            menu.attempts = 4

    menu.run()

    
    tracker = statsManager()
    while True: #Timi
        knows_how_to_play = input(
            "Do you know how to play Wordle? (yes/no): "
        ).strip().lower()

        if knows_how_to_play in ("yes", "y"):
            print("Great! You can continue to the game.")
            break
        if knows_how_to_play in ("no", "n"):
            show_wordle_video()
            break

        print("Please answer yes or no.") #TImi
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
            name= input("please enter a name:")
            tracker.recordstats(name,6-attempts, won=True)
            return
        
        attempts -= 1
        
        if attempts == 0:
            print("\nGame over!")
            print("The word was:", secret_word)
            name= input("please enter a name:")
            tracker.recordstats(name,6-attempts,won=False)
            break
            
    play_again = input("Do you want to play again? (yes/no): ").strip().lower() #Timi
    if play_again not in ("yes", "y"):
           print("Thanks for playing!")#Timi
           print("CSCI 1030U group project - not built yet.")
           print("Replace main() with your core loop. See MILESTONES.md for what is due when.")
           return  
         
            
if __name__ == '__main__':
    main()
