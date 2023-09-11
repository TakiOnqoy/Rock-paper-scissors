import argparse
import random

POSSIBLE_PLAYS = ['ROCK', 'PAPER', 'SCISSORS']

def read_user_play():
    parser = argparse.ArgumentParser(
        description="Allows the player to play 'Rock, paper and scissors' on the terminal"
    )
    parser.add_argument(
        "play", nargs='?', type=str, help="enter option 'rock', 'paper' or 'scissors'"
    )
    parser.add_argument(
        "-p",
        "--player",
        type=str,
        default="User",
        help="sets a custom name for the human player"
    )
    return parser.parse_args()

def play_validation(play):
    play = play.upper()
    for option in POSSIBLE_PLAYS:
        if play == option:
            return True
    return False

def user_play(play):
    play = play.upper()
    for i in range(len(POSSIBLE_PLAYS)):
        if play == POSSIBLE_PLAYS[i]:
            return i

def computer_play():
    return random.randint(0,2)

def print_hand(option, player_name):
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


def print_result(user_play, computer_play, user_name):
    computer_taunts = [
        f"{user_name} has lost! All hail the mighty computer!",
        f"Impressive, computer! {user_name} can't keep up with your genius!",
        f"The computer reigns supreme! {user_name}, try harder next time!",
        f"Machine power! {user_name}, you're no match for our AI.",
        f"{user_name}, you've met your match. The computer is unbeatable!",
        f"Resistance is futile, {user_name}. The computer is here to conquer!"
    ]
    human_taunts = [
        f"{user_name} has won! AI will never beat flesh and bones!",
        f"{user_name}, you're on fire! Show that computer who's boss!",
        f"Is that all you've got, computer? {user_name} is unstoppable!",
        f"Computer, you're going down! {user_name} is here to dominate!",
        f"AI, better luck next time! {user_name} is the real champion!",
        f"Don't underestimate {user_name}, computer. They've got the skills to pay the bills!"
    ]
    if user_play == computer_play:
        return f"Bananas, it's a draw!"
    if user_play == 0 and computer_play == 1:
        return f"{computer_taunts[random.randint(0,5)]}"
    if user_play == 0 and computer_play == 2:
        return f"{human_taunts[random.randint(0,5)]}"
    if user_play == 1 and computer_play == 0:
        return f"{human_taunts[random.randint(0,5)]}"
    if user_play == 1 and computer_play == 2:
        return f"{computer_taunts[random.randint(0,5)]}"
    if user_play == 2 and computer_play == 0:
        return f"{computer_taunts[random.randint(0,5)]}"
    if user_play == 2 and computer_play == 1:
        return f"{human_taunts[random.randint(0,5)]}"
    ...
def print_error():
    return "The given input isn't valid.\nPlease be sure to enter 'rock', 'paper' or 'scissors'."


if __name__ == '__main__':
    user_args = read_user_play()
    if play_validation(user_args.play):
        user_choice = user_play(user_args.play)
        computer_choice = computer_play()
        print_hand(user_choice, user_args.player)
        print_hand(computer_choice, "Computer")
        print(print_result(user_choice, computer_choice, user_args.player))
    else:
        print(print_error())

