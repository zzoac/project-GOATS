import webbrowser


def show_wordle_video():
    video_url = "https://www.youtube.com/watch?v=lv4Zg-209MY"
    print("Here is a video that explains how to play Wordle:")
    print(video_url)
    if not webbrowser.open(video_url):
        print("Your browser could not be opened automatically. Copy and paste the link above.")


def main():
    while True:
        knows_how_to_play = input("Do you know how to play Wordle? (yes/no): ").strip().lower()

        if knows_how_to_play in ("yes", "y"):
            print("Great! You can continue to the game.")
            return
        if knows_how_to_play in ("no", "n"):
            show_wordle_video()
            return

        print("Please answer yes or no.")


if __name__ == "__main__":
    main()
