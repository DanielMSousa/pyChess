from pieces import Piece

class CheckerSquare:
    def __init__(self, x, y, color, piece=None):
        self.x = x
        self.y = y

        self.original_color()

        if(piece):
            self.piece = Piece(piece[0], piece[1])
        else:
            self.piece = None

    def change_color(self):
        self.color = 'red'

    def original_color(self):
        if(self.x + self.y) % 2:
            self.color = '#eeeed2'
        else:
            self.color = '#769656'