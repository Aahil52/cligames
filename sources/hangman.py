import json
from random import choice
from sources.cliutil import ask_for_int_between, delete_output


class hangman:
    with open('./resources/wordbank.json') as f:
        word_bank = json.load(f)
    def __init__(self, word_length):
        self.word_length = word_length
        self.word = choice(self.word_bank[str(self.word_length)]).upper()
        self.correct = set()
        self.incorrect = set()

    def print_gallows(self):
        backslash_char = "\\"
        gallows = f"\n┌-----┐\n|     {'@' if len(self.incorrect) > 0 else ' '}\n|    {'/' if len(self.incorrect) > 2 else ' '}{'|' if len(self.incorrect) > 1 else ' '}{backslash_char if len(self.incorrect) > 3 else ' '}\n|     {'|' if len(self.incorrect) > 1 else ' '}\n|    {'/' if len(self.incorrect) > 4 else ' '} {backslash_char if len(self.incorrect) > 5 else ' '}\n|\n"
        print(gallows.format())

    def print_guessed(self):
        guessed = set()
        guessed.update(self.correct)
        guessed.update(self.incorrect)
        print("Guessed:", ", ".join(sorted(guessed)), end="\n\n")

    def print_letters(self):
        string = [letter if letter in self.correct else '_' for letter in self.word]
        print(" ".join(string), end="\n\n")

    def print_display(self):
        self.print_gallows()
        self.print_guessed()
        self.print_letters()

    def get_valid_guess(self, warning=""):
        guess = input(f"{warning}Guess: ").upper()
        if guess.lower() == "give up":
            return None
        elif guess.isalpha():
            return guess
        else:
            delete_output()
            return self.get_valid_guess(warning="(Invalid Input) ")

    def check(self, guess):
        if len(guess) == 1:
            if guess in self.word:
                self.correct.update(guess)
                return True
            else:
                self.incorrect.update(guess)
                return True
        elif guess == self.word:
            self.correct.update(guess)
            return True

    def iscomplete(self):
        for letter in self.word:
            if letter not in self.correct:
                return False
        return True
    
    def game(self):
        while not self.iscomplete() and len(self.incorrect) < 6:
            self.print_display()
            guess = self.get_valid_guess()
            delete_output(13)
            if guess is None:
                break
            self.check(guess)
        if self.iscomplete():
            self.print_display()
            input("You win!")
        else:
            self.print_gallows()
            self.print_guessed()
            self.correct.update(self.word)
            self.print_letters()
            input("You lose!")
        delete_output(13)

def main():
    hm = hangman(ask_for_int_between("Specify word length (5 to 10): ", 5, 10, random_option=True))
    hm.game()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("")