from pieces import Piece, King, Queen, Knight, Tower, Bishop

def return_piece(piece):
    if(piece):
        if(piece[1] == 'king'):
            piece = King(piece[0])

        elif(piece[1] == 'queen'):
            piece = Queen(piece[0])

        elif(piece[1] == 'bishop'):
            piece = Bishop(piece[0])
        
        elif(piece[1] == 'tower'):
            piece = Tower(piece[0])
        
        elif(piece[1] == 'knight'):
            piece = Knight(piece[0])
        
        else:    
            piece = Piece(piece[0], piece[1])
    else:
        piece = None

    return piece

class CheckerSquare:
    def __init__(self, x, y, color, piece=None):
        self.x = x
        self.y = y
        self.original_color()
        self.origin_color = self.color
        self.piece = return_piece(piece)

    def change_color(self):
        self.color = 'red'

    def set_way(self):
        if(self.origin_color == '#eeeed2'):
            self.color = '#A9A9F1'
        else:
            self.color = '#86A6D1'

    def original_color(self):
        if(self.x + self.y) % 2:
            self.color = '#eeeed2'
        else:
            self.color = '#769656'
    
    def interact(self, board, color):
        return self.piece.show_movement(self, board, color)
