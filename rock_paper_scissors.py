import argparse
import random

POSSIBLE_PLAYS = ['ROCK', 'PAPER', 'SCISSORS']

def read_user_play():
    parser = argparse.ArgumentParser(
        description="Allows the player to play 'Rock, paper and scissors' on the terminal"
    )
    parser.add_argument(
        "play", nargs=1, type=str, help="enter option 'rock', 'paper' or 'scissors'"
    )
    """
    parser.add_argument(
        "-p",
        "--player",
        type=str,
        help="sets a name for the human player"
    )
    """
    return parser.parse_args()

def play_validation(play):
    play[0] = play[0].upper()
    for option in POSSIBLE_PLAYS:
        if play[0] == option:
            return True
    return False

def user_play(play):
    play[0] = play[0].upper()
    for i in range(len(POSSIBLE_PLAYS)):
        if play[0] == POSSIBLE_PLAYS[i]:
            return i

def computer_play():
    return random.randint(0,2)

def print_hand(option, player_name="User"):
    # Rock
    rock = """
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """

    # Paper
    paper = """
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    """

    # Scissors
    scissors = """
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """

    if option == 0:
        print(f"{player_name} has chosen: {POSSIBLE_PLAYS[option]}\n{rock}")
    elif option == 1:
        print(f"{player_name} has chosen: {POSSIBLE_PLAYS[option]}\n{paper}")
    else:
        print(f"{player_name} has chosen: {POSSIBLE_PLAYS[option]}\n{scissors}")


def print_result(a, b):
    ...
def print_error():
    return "The given input isn't valid.\nPlease be sure to enter 'rock', 'paper' or 'scissors'."


if __name__ == '__main__':
    user_args = read_user_play()
    if play_validation(user_args.play):
        user_choice = user_play(user_args.play)
        computer_choice = computer_play()
        print_hand(user_choice)  # , user_args.player)
        print_hand(computer_choice, "Computer")
    else:
        print(print_error())

