import argparse
import random

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
        action="store_true",
        help=""
    )
    """
    return parser.parse_args()

def user_play(play):
    play_is_valid = False
    possible_plays = ['ROCK', 'PAPER', 'SCISSORS']
    play[0] = play[0].upper()
    for i in range(len(possible_plays)):
        if play[0] == possible_plays[i]:
            play_is_valid = True
            break
    if play_is_valid:
        return print_hand(i)
    else:
        return print("The input entered isn't valid.\nPlease be sure to enter 'rock', 'paper' or 'scissors'.")

def computer_play():
    return print_hand(random.randint(0,2))

def print_hand(play):
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

    if play == 0:
        print(f"Player has chosen: ROCK\n{rock}")
    elif play == 1:
        print(f"Player has chosen: PAPER\n{paper}")
    else:
        print(f"Player has chosen: SCISSORS\n{scissors}")


if __name__ == '__main__':
    user_args = read_user_play()
    user_play(user_args.play)
    computer_play()

