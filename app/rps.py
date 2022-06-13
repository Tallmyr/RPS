import random


def game():
    """
    Rock, Paper, Scissors game.
    """

    RPS = ["Rock", "Paper", "Scissors"]

    p_score = 0
    c_score = 0

    print("Welcome! Lets play Rock, Paper, Scissors! Best of 5 wins!")

    while p_score < 3 and c_score < 3:

        # Set up choices

        p_choice = player_choice(RPS)
        c_choice = random.choice(RPS)

        print(f"You chose {p_choice}. The computer picked {c_choice}.")

        # Get winners and add points
        winner, p_add, c_add = pick_winner(p_choice, c_choice)
        p_score += p_add
        c_score += c_add

        # Print results
        print(winner)
        print(f"Currents score: Player {p_score}, Computer {c_score}")

    if p_score == 3:
        print("Player wins the game!")
    else:
        print("Sorry, you lost to the computer!")


def player_choice(rps: list):
    """
    Retrieves and validates player input. Input valid options as List.
    """
    while True:
        try:
            choice = input(
                "Choose Rock, Paper or Scissors by typing it in.\n"
            ).capitalize()
            assert choice in rps  # Check for valid input
            return choice
        except AssertionError:
            print(f"{choice} is not a valid choice in this game! Try again!")


def pick_winner(player=str, computer=str):
    """
    Checks which player wins. Returns output and scores.
    """

    winconditions = {"Rock": "Paper", "Paper": "Scissors", "Scissors": "Rock"}

    player_point = 0
    computer_point = 0

    if player == computer:
        message = "It's a tie, try again!"
    elif computer == winconditions[player]:
        message = "Computer wins this round!"
        computer_point = 1
    else:
        message = "You win this round!"
        player_point = 1

    return message, player_point, computer_point


if __name__ == "__main__":
    game()
