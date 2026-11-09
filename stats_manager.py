
"""Handles Wordle player statistics and leaderboard."""

import json


class StatsManager:
    def __init__(self, filename="profiles.json"):
        self.filename = filename
        self.stats = self.load_stats()

    def load_stats(self):
        """Load player statistics from JSON."""
        try:
            with open(self.filename, "r") as file:
                return json.load(file)

        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_stats(self):
        """Save player statistics to JSON."""
        with open(self.filename, "w") as file:
            json.dump(self.stats, file, indent=4)

    def record_profile(self, username, attempts, won):
        """Record a player's game result."""

        user_profile = None

        for profile in self.stats:
            if profile["username"] == username:
                user_profile = profile
            break

        if user_profile is None:
            user_profile = {
                "username": username,
                "games_played": 0,
                "games_won": 0,
                "attempts_used": 0
            }
            self.stats.append(user_profile)

            user_profile["games_played"] += 1

            if won:
                user_profile["games_won"] += 1
                if user_profile["attempts_used"] == 0 or attempts < user_profile["attempts_used"]:
                    user_profile["attempts_used"] = attempts

                    self.save_stats()

    def recursive_bubble_sort(self, profiles, n=None):
        """Sort profiles by best winning attempts."""

        if n is None:
            n = len(profiles)

            if n <= 1:
                return profiles

            for i in range(n - 1):
                left = self.get_attempts_used(profiles[i])
                right = self.get_attempts_used(profiles[i + 1])

                if left > right:
                    profiles[i], profiles[i + 1] = (
                        profiles[i + 1],
                        profiles[i]
                    )

                    return self.recursive_bubble_sort(profiles, n - 1)

    def get_attempts_used(self, profile):
        """Place players without a win at the bottom of the leaderboard."""

        best = profile.get("attempts_used", 0)

        if best == 0:
            return 99

        return best


    # Alias to support the original class name used by teammates.
        statsManager = StatsManager
