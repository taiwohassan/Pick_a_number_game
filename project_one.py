import random


def roll():
    min_value = 1
    max_value = 6
    return random.randint(min_value, max_value)


# Input validation for the number of players
while True:
    players = input("Enter the number of players (2 - 4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4 players.")
    else:
        print("Invalid, try again.")

# Initialize variables
max_score = 50
player_scores = [0 for _ in range(players)]

# Main game loop
while max(player_scores) < max_score:
    for player_idx in range(players):
        print("\nPlayer number", player_idx + 1, "turn has just started!")
        print("Your total score is:", player_scores[player_idx], "\n")

        current_score = 0  # Reset current score at the start of the player's turn

        while True:
            should_roll = input("Would you like to roll (y)? ")
            if should_roll.lower() != "y":
                break

            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done!")
                # current_score = 0  # Reset current score for this turn
                break
            else:
                print("You rolled a:", value)
                current_score += value  # Increment current score correctly

            print("Your score for this turn is:", current_score)

        # Add current score to total score
        player_scores[player_idx] += current_score
        print("Your total score is now:", player_scores[player_idx])


# Determine the winner

winning_idx=player_scores.index(max_score)
print("Player", winning_idx + 1, "is the winner with score of:", max_score)
