import json
from random import choice
from sources.cliutil import delete_output, get_valid_choice ,ask_for_int_between, bcolors


class wordguess:
    with open('./resources/wordbank.json') as f:
        word_bank = json.load(f)
    guesses_allowed = 6
    def __init__(self, word_length=5, hard_mode=False):
        self.hard_mode = hard_mode
        self.word_length = word_length
        self.word = choice(self.word_bank[str(self.word_length)]).upper()
        self.guesses = [[] for _ in range(self.guesses_allowed)]
        self.guess_count = 0
        self.correct_letters = []
        self.misplaced_letters = []
        self.incorrect_letters = set()
        self.complete = False
    
    def print_board(self):
        board = [[f"{letter}" for letter in guess] if guess != [] else "_" * self.word_length for guess in self.guesses]
        print("")
        for guess in board:
            print(" ".join(guess))
        print("")

    def print_incorrect_letters(self):
        print("Incorrect Letters:", ", ".join(sorted(self.incorrect_letters)), end="\n\n")

    def uses_hints(self, guess):
        for letter in self.correct_letters + self.misplaced_letters:
            if letter not in guess:
                return False
        return True

    def get_valid_word(self, warning=""):
        guess = input(f"{warning}Guess: ")
        if guess.lower() == "give up":
            return None
        elif guess.lower() in self.word_bank[str(self.word_length)]:
            if not self.hard_mode or self.uses_hints(guess.upper()):
                return guess.upper()
            else:
                delete_output()
                return self.get_valid_word(warning=f"(Hints Not Used) ")
        elif len(guess) == self.word_length:
            delete_output()
            return self.get_valid_word(warning="(Not in List) ")
        else:
            delete_output()
            return self.get_valid_word(warning=f"(Not of Length {self.word_length}) ")

    def check(self, guess):
        remaining_letters = list(self.word)
        for guess_letter, word_letter in zip(guess, self.word):
            if guess_letter == word_letter:
                self.guesses[self.guess_count].append(f"{bcolors.OKGREEN}{guess_letter}{bcolors.ENDC}")
                remaining_letters.remove(guess_letter)
                self.correct_letters.append(guess_letter)
            elif guess_letter in remaining_letters:
                self.guesses[self.guess_count].append(f"{bcolors.WARNING}{guess_letter}{bcolors.ENDC}")
                remaining_letters.remove(guess_letter)
                self.misplaced_letters.append(guess_letter)
            else:
                self.guesses[self.guess_count].append(guess_letter)
                if guess_letter not in self.correct_letters + self.misplaced_letters:
                    self.incorrect_letters.add(guess_letter)
        return True if len(self.correct_letters) == self.word_length else False

    def game(self):
        while not self.complete and self.guess_count < self.guesses_allowed:
            self.print_board()
            self.print_incorrect_letters()
            guess = self.get_valid_word()
            delete_output(11)
            if guess is None:
                break
            self.complete = self.check(guess)
            self.correct_letters = []
            self.misplaced_letters = []
            self.guess_count += 1
        self.print_board()
        if self.complete:
            input("You win!")
        else:
            input(f"You lose! The word is {self.word}")
        delete_output(9)

def main():
    print("")
    hard_mode = (get_valid_choice(["y", "n"], "Enable hard mode (y/n)? ") == "y")
    delete_output(2)
    wg = wordguess(ask_for_int_between("Specify word length (2 to 20): ", 2, 20, 5, random_option=True), hard_mode=hard_mode)
    wg.game()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("")
