class Pieces:
    """class to create Pieces"""

    def __init__(self, pieces_Pieces):
        """
        Description

        """
        self.p = Pawn(pieces_Pieces['P(pawn)'])
        self.r = Rook(pieces_Pieces['R(rook)'])
        self.q = Queen(pieces_Pieces['Q(queen)'])
        self.kn = Knight(pieces_Pieces['Kn(knight)'])
        self.ki = King(pieces_Pieces['Ki(king)'])
        self.b = Bishop(pieces_Pieces['B(bishop)'])

    def collect_all_data_in_lst(self):
        return [self.p, self.r, self.q, self.kn, self.ki, self.b]


class Bishop:
    """class to create bishop"""

    def __init__(self, positions_bishop):
        """
        Description

        """
        self.positions = positions_bishop
        self.mark = "B"


class Pawn:
    """class to create Pawn"""

    def __init__(self, positions_pawn):
        """
        Description

        """
        self.positions = positions_pawn
        self.mark = "P"

    def __str__(self):
        """
        Return: a string

        """
        return "P"


class Knight:
    """class to create Knight"""

    def __init__(self, positions_knight):
        """
        Description

        """
        self.positions = positions_knight
        self.mark = "Kn"


class King:
    """class to create King"""

    def __init__(self, positions_king):
        """
        Description

        """
        self.positions = positions_king
        self.mark = "Ki"


class Queen:
    """class to create Queen"""

    def __init__(self, positions_queen):
        """
        Description

        """
        self.positions = positions_queen
        self.mark = "Q"


class Rook:
    """class to create Rook"""

    def __init__(self, positions_rook):
        """
        Description

        """
        self.positions = positions_rook
        self.mark = "R"
