class HasamiShogiGame:
    """Represents the Hasami Shogi game"""

    def __init__(self):
        """Initializes the players and game board"""
        self._player_1 = "BLACK"
        self._player_2 = "RED"
        self._current_turn = "BLACK"
        # default to RED starting the game
        self._player_1_captured = 0
        # the pieces player 1 has captured from player 2
        self._player_2_captured = 0
        # the pieces player 2 has captured from player 1
        self._game_state = "UNFINISHED"
        # this can only be "UNFINISHED", "RED_WON", or "BLACK_WON"
        self._game_board = []
        self._game_board_list = []
        self.initialize_board()

    def initialize_board(self):
        """Initializes the starting board"""
        self._game_board.append([" ", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
        self._game_board.append(["a", "R", "R", "R", "R", "R", "R", "R", "R", "R"])
        self._game_board.append(["b", "_", "_", "_", "_", "_", "_", "_", "_", "_"])
        self._game_board.append(["c", "_", "_", "_", "_", "_", "_", "_", "_", "_"])
        self._game_board.append(["d", "_", "_", "_", "_", "_", "_", "_", "_", "_"])
        self._game_board.append(["e", "_", "_", "_", "_", "_", "_", "_", "_", "_"])
        self._game_board.append(["f", "_", "_", "_", "_", "_", "_", "_", "_", "_"])
        self._game_board.append(["g", "_", "_", "_", "_", "_", "_", "_", "_", "_"])
        self._game_board.append(["h", "_", "_", "_", "_", "_", "_", "_", "_", "_"])
        self._game_board.append(["i", "B", "B", "B", "B", "B", "B", "B", "B", "B"])

    def print_board(self):
        """Prints out the current board"""
        for rows in self._game_board:
            print(" ".join(rows))

    def get_game_state(self):
        """Returns the current state of the game"""
        return self._game_state

    def get_active_player(self):
        """Returns which players turn it is"""
        return self._current_turn

    def get_num_captured_pieces(self, player_color):
        """Returns how many pieces the other player has captured"""
        player_color = player_color.upper()
        if player_color == "BLACK":
            return self._player_1_captured
        if player_color == "RED":
            return self._player_2_captured

    def change_player_turn(self):
        """Function for make_move to change players after a valid move"""
        if self._current_turn == "BLACK":
            self._current_turn = "RED"
        else:
            self._current_turn = "BLACK"

    def check_game_status(self):
        """Function for make_move to check if either player has won"""
        if self._player_1_captured == 8:
            self._game_state = "BLACK_WON"
            print("BLACK has won.")
            return False
        if self._player_2_captured == 8:
            self._game_state = "RED_WON"
            print("RED has won.")
            return False

    def make_move(self, pos1, pos2):
        """Makes a move using board positions, moves the pieces on the players turn"""
        current_row = pos1[0]
        current_column = pos1[1]  # records the current row and spot
        new_row = pos2[0]
        new_column = pos2[1]  # records the new row and spot

        if self._game_state == "RED_WON":
            print("Game is over, cannot make move.")
            return False
        elif self._game_state == "BLACK_WON":
            print("Game is over, cannot make move.")
            return False

        if current_row == "a":
            current_row = 1
        if current_row == "b":
            current_row = 2
        if current_row == "c":
            current_row = 3
        if current_row == "d":
            current_row = 4
        if current_row == "e":
            current_row = 5
        if current_row == "f":
            current_row = 6
        if current_row == "g":
            current_row = 7
        if current_row == "h":
            current_row = 8
        if current_row == "i":
            current_row = 9

        if new_row == "a":
            new_row = 1
        if new_row == "b":
            new_row = 2
        if new_row == "c":
            new_row = 3
        if new_row == "d":
            new_row = 4
        if new_row == "e":
            new_row = 5
        if new_row == "f":
            new_row = 6
        if new_row == "g":
            new_row = 7
        if new_row == "h":
            new_row = 8
        if new_row == "i":
            new_row = 9

        current_row = int(current_row)
        current_column = int(current_column)
        new_row = int(new_row)
        new_column = int(new_column)

        if current_row != new_row:
            if current_column != new_column:
                print("Invalid move, try again.")  # tried to move out of the same column
                return False

        elif current_row == new_row:
            if current_column == new_column:
                print("Invalid move, try again.")    # tried to move out of the same row
                return False

        if self._game_board[new_row][new_column] != "_":
            print("Move invalid, space is occupied. Try again.")
            return False

        if self._current_turn == "BLACK" and self._game_board[current_row][current_column] != "B":
            print("Move failed, attempted to move other player's piece")
            return False
        if self._current_turn == "RED" and self._game_board[current_row][current_column] != "R":
            print("Move failed, attempted to move other player's piece")
            return False
            # two conditions enforce players moving their own pieces instead of others on their turn

        self._game_board[current_row][current_column] = "_"
        if self._current_turn == "BLACK":
            self._game_board[new_row][new_column] = "B"
        else:
            self._game_board[new_row][new_column] = "R"

        temp_list = ["".join(rows) for rows in self._game_board]    # checking if pieces has been captured
        for lists in temp_list:
            if "BRB" in lists:
                row = lists.index("BRB") + 1
                spot = lists.index("R")
                self._game_board[row][spot] = "_"
                self._player_1_captured += 1
            elif "RBR" in lists:
                row = lists.index("RBR")
                spot = lists.index("B")
                self._game_board[row][spot] = "_"
                self._player_2_captured += 1
        self.check_game_status()
        self.change_player_turn()
        return True

    def get_square_occupant(self, board_spot):
        """Checks for a piece on the board and returns who is occupying that spot"""
        row = board_spot[0]
        column = board_spot[1]

        if row == "a":
            row = 1
        if row == "b":
            row = 2
        if row == "c":
            row = 3
        if row == "d":
            row = 4
        if row == "e":
            row = 5
        if row == "f":
            row = 6
        if row == "g":
            row = 7
        if row == "h":
            row = 8
        if row == "i":
            row = 9

        row = int(row)
        column = int(column)

        if self._game_board[row][column] == "B":
            return "BLACK"
        elif self._game_board[row][column] == "R":
            return "RED"
        else:
            return "UNOCCUPIED"
