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
from stats_manager import StatsManager

def main():
    parser = argparse.ArgumentParser(description="Wordle terminal game")

    parser.add_argument(
        "--attempts",
        type=int,
        choices=[4, 6, 8],
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

    parser.add_argument(
        "--profile",
        default="profiles.json",
        help="Choose player statistics file"
    )

    parser.add_argument(
        "--leaderboard",
        action="store_true",
        help="Display player leaderboard"
    )

    args = parser.parse_args()

    tracker = StatsManager(args.profile)

    if args.leaderboard:
        print("\nWordle Leaderboard")
        print("------------------------")

        for i, profile in enumerate(tracker.stats, start=1):
            print(
                f"{i}. User: {profile.get('username', 'Unknown')} | "
                f"Games played: {profile.get('games_played', 0)} | "
                f"Games won: {profile.get('games_won', 0)} | "
                f"Best attempts: {profile.get('attempts_used', 0)}"
            )
        return

    menu = WordleMenu(settings_file=args.settings, tracker=tracker)

    # Direct attempts override difficulty if both are provided.
    if args.attempts is not None:
        menu.attempts = args.attempts
        menu.difficulty = {
            4: "Hard",
            6: "Normal",
            8: "Easy"
        }.get(args.attempts, menu.difficulty)

    elif args.difficulty is not None:
        menu.difficulty = args.difficulty.capitalize()
        difficulty_attempts = {
            "Easy": 8,
            "Normal": 6,
            "Hard": 4
        }
        menu.attempts = difficulty_attempts[menu.difficulty]

    menu.run()


if __name__ == "__main__":
    main()
