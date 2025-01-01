Dice Game

This is a simple multiplayer dice-rolling game implemented in Python. The game allows 2-4 players to take turns rolling a dice, accumulating scores, and competing to reach a target score of 50 points.

How It Works

Number of Players:

The game starts by prompting the user to enter the number of players (2-4).

Input validation ensures that the number of players is within the allowed range.

Rolling the Dice:

On a player's turn, they can choose to roll a dice or end their turn.

If the dice roll results in a 1, the player's turn ends, and their score for that turn is forfeited.

If the roll is greater than 1, the result is added to the player's current score for that turn.

Score Tracking:

Each player's cumulative score is tracked and updated after their turn.

The first player to reach or exceed the target score of 50 wins the game.

Winning:

Once a player reaches 50 or more points, the game announces the winner and their score.

Code Breakdown

roll() Function

A helper function that simulates rolling a 6-sided dice.

Returns a random integer between 1 and 6.

Input Validation

Ensures that the number of players entered is valid (between 2 and 4).

If invalid input is provided, the user is prompted to try again.

Main Game Loop

Alternates turns between players.

Displays the current player's total score at the start of their turn.

Allows the player to roll the dice repeatedly or end their turn.

Ends when any player's total score reaches or exceeds 50.

Scoring Rules

Rolling a 1 forfeits the current turn's score.

Scores accumulate across turns for each player.

Determining the Winner

The game checks the scores and identifies the first player to reach the maximum score.

The winner is announced along with their score.

How to Run

Save the script to a file, e.g., dice_game.py.

Run the script using Python:

python dice_game.py

Follow the on-screen prompts to play the game.

Example Gameplay

Enter the number of players (2 - 4): 2

Player number 1 turn has just started!
Your total score is: 0
Would you like to roll (y)? y
You rolled a: 4
Your score for this turn is: 4
Would you like to roll (y)? y
You rolled a: 6
Your score for this turn is: 10
Would you like to roll (y)? n
Your total score is now: 10

Player number 2 turn has just started!
Your total score is: 0
Would you like to roll (y)? y
You rolled a: 1
You rolled a 1! Turn done!
Your total score is now: 0

...

Player 1 is the winner with a score of: 50

Notes

The game uses Python's built-in random module to simulate dice rolls.

Players should strategize when to stop rolling to avoid losing their turn's score by rolling a 1.

Customization

You can change the target score (max_score) by modifying the variable in the script.

You can also adjust the range of dice rolls by altering the min_value and max_value in the roll() function.

Enjoy the game