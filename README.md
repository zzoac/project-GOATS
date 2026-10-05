# <your project name>

## The application

<Two or three sentences: what are you building, and who plays or uses it? It has to fit the
networked, multi-user theme - see the "Suggested projects" section of
[`MILESTONES.md`](MILESTONES.md). Name one of the suggestions, or describe your own idea.>

## The team

| Full name | GitHub username |
|-----------|-----------------|
| Oluwatimilehin Balogun    | @Templeton16     |
| Zachary Cas    | @zzoac     |
| Aaden Nim    | @aadennim-wq     |
| Victor Otuije    | @VictorOtuije     |
| Dashaun Smith-Davis    | @dsmithdavis2378     |

Note:  Be sure to [add all of the group members to as collaborators on this repository](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/repository-access-and-collaboration/inviting-collaborators-to-a-personal-repository).

<!-- Fill this in at Milestone 0. Teams of four: delete the fifth row.
     The GitHub username must be the one that authors your commits, so your work in the
     history can be matched to you - check yours with:  git log --format='%an <%ae>'
     Who owns which slice, and what each member contributed, go in CONTRIBUTIONS.md. -->

## Running it

```
python main.py
```

## Design

<Leave this until Milestone 3. Then add, in about a page: how the pieces fit together
(server, client, engine, storage), and a short **Big-O note** for the algorithm your team
implemented - what it does, its complexity, and why that is fast enough here.>

## Required Files

| File | What it is |
|------|------------|
| [`MILESTONES.md`](MILESTONES.md) | **the project requirements** - all four milestones, what's due when |
| [`CONTRIBUTIONS.md`](CONTRIBUTIONS.md) | who owns which slice, and which commit proves each member did each topic |
| [`AI-USAGE.md`](AI-USAGE.md) | the AI policy, and your team's disclosure |

> **This file is yours.** The sections above are part of your Milestone 0 write-up - fill
> them in together, and fill in the slices table in `CONTRIBUTIONS.md` at the same time.
> From Milestone 1 on, grow "The application" and "Running it" into a real README for your
> project, and keep the team table, the tech plan, and these pointers.


Milestone 1 Commit- Initial Game set-up and Structure- Dashaun Smith-Davis:
For my first commit towards milestone 1, I have organised the initial set up for the game while adding a few important functions, lists, and conditionals. 

I began with a feedback = list which acts as a dictionary which stores word descriptions onto 3 outcomes: correct, incorrect and wrong position. This helps us to identify when words inputed match the hidden word or letters which are included in the word. Then I created a validate_guess function which accepts strings and the checks if they meet the conditional requirements. 

I used the conditionals if len(guess) != 5 and if not guess.alpha(). The len(guess) function checks the length of an input to make sure the user responds with 5 characters and guess.isalpha() makes sure the input only has letters in the alphabet. 

In the main function I defined the secret word as a random word from word_list ensuring that the user gets a random word to guess. Next I created while>0 which acts as the main game loop to start the game and then end once the users attempts have all been used. Next ther is a guesses.append() function that places each user guess string into the guess list to identify the status of the word. The I used results = compare_input and for i in range(5) to determine the result of the input and then print the users feedback for their choice. Lastly I implemented the win/loss conditions to define when a player has guessed correctly, or run out of turns



Milestone 1 Commit- Creation of the input comparing function by Aaden Nim:
For my commitment i started by first creating the function that compares both the input word along with the secret word. This function is then run and starts with first converting both given words into seperate characters through the usage of lists. This helps by seperating each letter in its own index, later on allowing for the comparison of seperate letters. 

a new list is created to record the results of whether the words are correct, incorrect, or in the wrong position. A for loop is then used with the range of the length of the secret word, which is 5. a conditional is then used to see if the guess letter is equal to the secret letter in the same position. if it is correct, the result is added to the result list and both letters are removed to stop any potential issues with position. this runs until it reaches the length of the word.

a second for loop with the same range is then ran to account for incorrect and wrong position answers. Another conditional is used for if a input letter is still in the list but not in the secret word list, which it is then considered incorrect, An else if is also used for if a input letter is still in the list and also in the secret letter word list, which displays in the wrong position. Finally, the list of correct, incorrect, and wrong position is returned.

