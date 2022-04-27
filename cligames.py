from sources.cliutil import ask_for_choice_in_list
from sources.tictactoe import main as tictactoe
from sources.hangman import main as hangman
from sources.wordguess import main as wordguess


def main():
    games = {
        'tictactoe': tictactoe,
        'hangman': hangman,
        'word guess': wordguess
    }
    options = ["play again", "play a different game", "quit"]

    i = 0
    game = None
    while True:
        if i % 2 == 0:
            game = ask_for_choice_in_list(games, "List of games:", "Which game would you like to play? ")
            games[game]()
            i += 1
        else:
            choice = ask_for_choice_in_list(options, "Options:", "What would you like to do? ")
            if choice == options[0]:
                games[game]()
            elif choice == options[1]:
                i += 1
            else:
                break

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("")