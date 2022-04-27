from random import randint
from sources.cliutil import delete_output


class tictactoe:
    def __init__(self, players: list[str] = ["X", "O"]):
        self.players = players
        self.map = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.start = randint(0, 1)
        self.winner = None

    def print_grid(self):
        grid = f"\n{self.map[0]} | {self.map[1]} | {self.map[2]}\n--|---|--\n{self.map[3]} | {self.map[4]} | {self.map[5]}\n--|---|--\n{self.map[6]} | {self.map[7]} | {self.map[8]}\n"
        print(grid)
    
    def get_valid_move(self, player, warning=""):
        try:
            input_pos = int(input(f"{warning}Place {player}: "))
            if self.map[input_pos] not in self.players:
                self.map[input_pos] = player
            else:
                delete_output()
                self.get_valid_move(player, warning="(Position Occupied) ")
        except Exception:
            delete_output()
            self.get_valid_move(player, warning="(Invalid Input) ")
        
    def check_win(self):
        win_conditions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
        for player in self.players:
            for condition in win_conditions:
                met = 0
                for check in condition:
                    if self.map[check] == player:
                        met += 1
                if met == 3:
                    return player
        return None

    def print_winner(self):
        self.print_grid()
        if self.winner:
            input(f"Player \"{self.winner}\" wins!")
        else:
            input("Draw!")
        delete_output(8)

    def multiplayer_game(self):
        i = self.start
        while self.winner is None and i <= (8 + self.start):
            current_player = self.players[i % 2]
            self.print_grid()
            self.get_valid_move(current_player)
            delete_output(8)
            if i >= (4 + self.start):
                self.winner = self.check_win()
            i += 1
        self.print_winner()

    def computer_move(self):
        # TODO
        pass

    def solo_game(self):
        i = self.start
        while self.winner is None and i <= (8 + self.start):
            if i % 2 == 0:
                self.print_grid()
                self.get_valid_move(self.players[0])
                delete_output(8)
            else:
                self.computer_move()
            if i >= (4 + self.start):
                self.winner = self.check_win()
            i += 1
        self.print_winner()

def main():
    ttt = tictactoe()
    ttt.multiplayer_game()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("")