""" Wordle TUI Menu for Milestone 2
Including:
- Terminal menu with classes
- JSON settings implementation
- Recursive Menu navigation
- Difficulty and attempts option
"""

import json
import os
from game import play_game
from stats_manager import StatsManager



class WordleMenu:
    """Controls terminal menu and settings"""

    def __init__(self, settings_file="settings.json", tracker=None):
        self.settings_file = settings_file
        self.tracker = tracker
        self.running = True
        self.attempts = 6
        self.difficulty = "Normal"

        
        self.load_settings()

        #Menu structure for recursive navigation
        self.menu_options = {
            "Settings": {
                "Difficulty": ["Easy", "Normal", "Hard"],
                "Attempts": ["4", "6", "8"]
            },
        }

        #Main Menu

    def display_menu(self):
            """Displays main menu"""

            print("\n=====================================")
            print("          Welcome to WORDLE")
            print("=======================================")
            print("  1. Start New Game")
            print("  2. Resume Saved Game")
            print("  3. Instructions")
            print("  4. Settings")
            print("  5. Exit")

    def run(self):
            """Runs main menu until the user quits"""

            while self.running:

                self.display_menu()

                choice = input("\nEnter your choice: ").strip()

                if choice == "1":
                    self.start_game()

                elif choice == "2":
                    self.resume_game()

                elif choice == "3":
                    self.show_instructions()

                elif choice == "4":
                    self.open_settings()

                elif choice == "5":
                    self.save_settings()
                    print("Thanks for playing Wordle!")
                    self.running = False

                else:
                    print("Invalid choice. Please select 1-5.")


        # Wordle game implemented inside function
    def start_game(self):
            """Start a new game."""

            print("\nStarting a new Wordle game...")
            print("Difficulty:", self.difficulty)
            print("Attempts:", self.attempts)
            
            play_game(self.attempts, self.tracker)
        # Game file connected


    def resume_game(self):
            """Resume a previously saved game."""

            print("\nResume Saved Game")

            if os.path.exists("save_game.json"):
                print("A saved game was found.")
                print("Connect your group's load-game function here.")
            else:
                print("No saved game was found.")


        # Instructions

    def show_instructions(self):
            """Display instructions for Wordle."""

            print("\n========== INSTRUCTIONS ==========")
            print("1. Guess the hidden five-letter word.")
            print("2. You have a limited number of attempts.")
            print("3. Green means the letter is correct.")
            print("4. Yellow means the letter is in the word")
            print("   but in the wrong position.")
            print("5. White means the letter is not in the word.")
            print("======================================")

            input("\nPress Enter to return to the menu.")


        #Settings
    def open_settings(self):
            """Open the settings menu."""

            settings_menu = {
        "1": ("Game Settings", {
            "1": ("Difficulty", self.change_difficulty),
            "2": ("Number of Attempts", self.change_attempts),
            "3": ("Save Settings", self.save_settings),
            "4": ("Return", None)
        }),
        "2": ("Return to Main Menu", None)
    }
            self.recursive_menu(settings_menu)

    
    def recursive_menu(self, options, depth=0):
        """Display and navigate a menu recursively."""

        while True:

            print("\n" + "  " * depth + "Settings Menu")

            for key, option in options.items():
                print("  " * depth + key + ". " + option[0])

            choice = input("\nEnter your choice: ").strip()

            if choice not in options:
                print("Invalid choice.")
                continue

            selected_option = options[choice]
            action = selected_option[1]

            # Return to the previous menu
            if action is None:
                return

            # If the option contains another menu, call recursively
            elif isinstance(action, dict):
                self.recursive_menu(action, depth + 1)

                # Otherwise, execute the selected function
            else:
                action()

           

    def change_difficulty(self):
            """Change the game's difficulty."""

            difficulty_options = {
            "1": "Easy",
            "2": "Normal",
            "3": "Hard"
        }

            print("\nSelect Difficulty:")
            print("1. Easy")
            print("2. Normal")
            print("3. Hard")

            choice = input("Choice: ").strip()

            if choice in difficulty_options:
                self.difficulty = difficulty_options[choice]

            # Difficulty controls the number of attempts.
                if self.difficulty == "Easy":
                    self.attempts = 8
                elif self.difficulty == "Normal":
                    self.attempts = 6
                elif self.difficulty == "Hard":
                    self.attempts = 4

                print("Difficulty updated:", self.difficulty)
                print("Attempts:", self.attempts)

            else:
                print("Invalid difficulty.")
    def change_attempts(self):
        """Allow the player to customize attempts."""

        print("\nAvailable attempts: 4, 6, 8")
        print("\nAttempts are determined by difficulty.")
        print("Easy: 8 attempts")
        print("Normal: 6 attempts")
        print("Hard: 4 attempts")

        print(f"\nYour current difficulty is {self.difficulty}.")
        print(f"You currently have {self.attempts} attempts.")


    # JSON file I/O
    def save_settings(self):
        """Save settings to a JSON file."""

        settings = {
            "attempts": self.attempts,
            "difficulty": self.difficulty
        }

        try:
            with open(self.settings_file, "w") as file:
                json.dump(settings, file, indent=4)

            print("Settings saved successfully.")

        except OSError:
            print("Unable to save settings.")

    def load_settings(self):
        """Load settings from a JSON file."""

        if not os.path.exists(self.settings_file):
            return

        try:
            with open(self.settings_file, "r") as file:
                settings = json.load(file)

            self.attempts = settings.get("attempts", self.attempts)
            self.difficulty = settings.get(
                "difficulty", self.difficulty
            )

            print("Settings loaded successfully.")

        except (OSError, json.JSONDecodeError):
            print("Could not load settings. Using defaults.")


