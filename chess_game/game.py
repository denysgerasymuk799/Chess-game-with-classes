import itertools

from classes_pieces import King, Queen, Rook, Knight, Pawn, Bishop, Pieces


class TwoPlayers:
    """
    A class used to start playing between two players

    ...

    Attributes
    ----------
    name_player1, name_player2 : str
        names of players
    start_positions : dict
        dict for start positions for pieces

    """

    def __init__(self, name_player1, name_player2):
        """
        Description

        """
        self.name_player1, self.name_player2 = name_player1, name_player2
        self.start_positions = {}
        pieces = {"Ki(king)": ['e1', 'm1', 'e12', 'm12'],
                  "Q(queen)": ['d1', 'l1', 'd12', 'l12'],
                  "R(rook)": ['a1', 'h1', 'i1', 'p1', 'a12', 'h12', 'i12', 'p12'],
                  "Kn(knight)": ['b1', 'g1', 'j1', 'o1', 'b12', 'g12', 'j12', 'o12'],
                  "B(bishop)": ['c1', 'f1', 'k1', 'n1', 'c12', 'f12', 'k12', 'n12'],
                  "P(pawn)": [chr(i+97)+'2' for i in range(0, 16)] + [chr(i+97)+'11' for i in range(0, 16)]
                  }
        board = Board("two_players_double_board", pieces)
        board.display()


class ThreePlayers:
    """
    A class used to start playing between two players

    ...

    Attributes
    ----------
    name_player1, name_player2, name_player3 : str
        names of players
    start_positions : dict
        dict for start positions for pieces

    """

    def __init__(self, name_player1, name_player2, name_player3):
        """
        Description

        """
        self.name_player1, self.name_player2, self.name_player3 = name_player1, name_player2, name_player3
        self.start_positions = {}
        pieces = {"Ki(king)": ['d12', 'r13', 'l1'],
                  "Q(queen)": ['e13', 's12', 'k1'],
                  "R(rook)": ['a9', 'h16', 'o16', 'v9', 'o1', 'h1'],
                  "Kn(knight)": ['b10', 'p15', 'u10', 'g15', 'i1', 'n1'],
                  "B(bishop)": ['c11', 'q14', 't11', 'f14', 'j1', 'm1'],
                  "P(pawn)": [chr(i+97)+str(i + 7) for i in range(1, 9)] + [chr(i+97)+str(28 - i) for i in range(13, 21)] +
                  [chr(i+97)+'2' for i in range(7, 15)]
                  }
        board = Board("three_players_board", pieces)
        board.display()


class FourPlayers:
    """
    A class used to start playing between two players

    ...

    Attributes
    ----------
    name_player1, name_player2, name_player3, name_player4 : str
        names of players
    start_positions : dict
        dict for start positions for pieces

    """

    def __init__(self, name_player1, name_player2, name_player3, name_player4):
        """
        Description

        """
        self.name_player1, self.name_player2 = name_player1, name_player2
        self.name_player3, self.name_player4 = name_player3, name_player4
        self.start_positions = {}
        pieces = {"Ki(king)": ['g1', 'h14', 'a7', 'n8'],
                  "Q(queen)": ['h1', 'g14', 'a8', 'n7'],
                  "R(rook)": ['d1', 'k1', 'd14', 'k14', 'a4', 'n4', 'a11', 'n11'],
                  "Kn(knight)": ['e1', 'j1', 'e14', 'j14', 'a5', 'n5', 'a10', 'n10'],
                  "B(bishop)": ['f1', 'i1', 'f14', 'i14', 'a6', 'n6', 'a9', 'n9'],
                  "P(pawn)": [chr(i+97)+'2' for i in range(3, 11)] + [chr(i+97)+'13' for i in range(3, 11)] +
                             ['b'+str(i) for i in range(4, 12)] + ['m'+str(i) for i in range(4, 12)]
                  }
        board = Board("four_players_board", pieces)
        board.display()


class Board(Pieces):
    """
    A class used to create a chessboard

    ...

    Attributes
    ----------
    name : str
        name of board
    super().__init__(pieces) : dicts
        dicts from father class


    Methods
    -------
    display()
        Prints different types of boards based on board.name and start_positions
    """

    def __init__(self, name, pieces):
        """
        Description

        """
        self.name = name
        super().__init__(pieces)

    def display(self):
        """ Prints different types of boards based on board.name and start_positions"""
        board_dict = dict()
        if self.name == 'two_players_double_board':
            # fill all cells of board_dict with " " for empty cells
            letters = [chr(i+97) for i in range(0, 16)]
            for number in range(0, 12):
                for letter in letters:
                    position = letter + str(number + 1)
                    board_dict[position] = ' '

            board_dict = self.set_piece_in_cell(board_dict)
            # first line of board
            board_str = "  |"
            for i in range(0, 16):
                board_str += chr(i + 97).ljust(2, ' ') + " | "

            print(board_str)

            # print board
            for number in range(0, 12):
                print("-" * 82)
                print(str(number + 1).rjust(2, ' '), end="|")
                for letter in letters:
                    position = letter + str(number + 1)
                    piece = board_dict[position]
                    print(str(piece).ljust(2, ' ') + ' |', end=" ")
                print()
            print("-" * 82)
            print("\n")
            print("END OF TWO_PLAYERS BOARD")

        elif self.name == "four_players_board":
            # fill all cells of board_dict with " " for empty cells
            letters = [chr(i+97) for i in range(0, 14)]
            for number in range(0, 14):
                for letter in letters:
                    position = letter + str(number + 1)
                    board_dict[position] = ' '

            board_dict = self.set_piece_in_cell(board_dict)
            # first line of board
            board_str = "  |"
            for i in range(0, 14):
                board_str += chr(i + 97).ljust(2, ' ') + " | "

            print(board_str)

            empty_letters, empty_numbers = ['a', 'b', 'c', 'l', 'm', 'n'], ['1', '2', '3', '12', '13', '14']
            empty_cells_tuples = list(itertools.product(empty_letters, empty_numbers))
            empty_cells = []
            for tupl in empty_cells_tuples:
                empty_cells.append(tupl[0] + tupl[1])
            # print board
            for number in range(0, 14):
                print("-" * 76)
                print(str(number + 1).rjust(2, ' '), end="|")
                for letter in letters:
                    position = letter + str(number + 1)
                    piece = board_dict[position]
                    if position not in empty_cells:
                        print(str(piece).ljust(2, ' ') + ' |', end=" ")

                    else:
                        if position.startswith('c'):
                            print('   ', end='| ')

                        else:
                            print('    ', end=' ')

                print()
            print("-" * 76)
            print("\n")
            print("END OF FOUR_PLAYERS BOARD")

        elif self.name == "three_players_board":
            # fill all cells of board_dict with " " for empty cells
            letters = [chr(i + 97) for i in range(0, 22)]
            for number in range(0, 22):
                for letter in letters:
                    position = letter + str(number + 1)
                    board_dict[position] = ' '

            # first line of board
            board_str = "  |"
            for i in range(0, 22):
                board_str += chr(i + 97).ljust(2, ' ') + " | "

            print(board_str)

            empty_cells = []
            for i in range(7):
                for j in range(1, 7 - i + 1):
                    position = letters[i] + str(j)
                    empty_cells.append(position)

                for j in range(1, i + 2):
                    position = letters[i + 15] + str(j)
                    empty_cells.append(position)

                for j in range(10 + i, 17):
                    position = letters[i] + str(j)
                    empty_cells.append(position)

                for j in range(16 - i, 17):
                    position = letters[i + 15] + str(j)
                    empty_cells.append(position)

            board_dict = self.set_piece_in_cell(board_dict)

            # print board
            for number in range(0, 16):
                print("-" * 106)
                print(str(number + 1).rjust(2, ' '), end="|")
                for letter in letters:
                    position = letter + str(number + 1)
                    piece = board_dict[position]
                    if position not in empty_cells:
                        print(str(piece).ljust(2, ' ') + ' |', end=" ")


                    else:
                        if position == 'g1' or position == 'g16':
                            print('   ', end='| ')
                        elif position.startswith('c'):
                            print('   ', end='  ')

                        else:
                            print('    ', end=' ')

                print()
            print("-" * 106)
            print("\n")
            print("END OF THREE_PLAYERS BOARD")

    def set_piece_in_cell(self, board_dict):
        pieces_data = self.collect_all_data_in_lst()
        for piece in pieces_data:
            for position in piece.positions:
                board_dict[position] = piece.mark

        return board_dict


if __name__ == '__main__':
    two_players_double_board = TwoPlayers("Denys", "Olexander")
    print("\n\n\n" + '-' * 120)
    three_players = ThreePlayers("Denys", "Olexander", "Bohdan")
    print("\n\n\n" + '-' * 120)
    four_players = FourPlayers("Denys", "Olexander", "Andriy", "Bohdan")
