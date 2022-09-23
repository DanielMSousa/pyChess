class Piece:
    def __init__(self, color, name='pawn'):
        self.color = color
        self.name = name
        self.image_file = f'{self.color}_{self.name}'
    
    def show_movement(self, square, board):
        movements = []
        if(self.color == 'black' and board[square.y+1][square.x].piece == None):
            movements.append([square.x, square.y+1])
            if(square.y == 1):
                movements.append([square.x, square.y+2])

        elif(self.color == 'white' and board[square.y-1][square.x].piece == None):
            movements.append([square.x, square.y-1])
            if(square.y == 6):
                movements.append([square.x, square.y-2])
        return movements

class King(Piece):
    def __init__(self, color):
        super().__init__(color, 'king')
    
    def show_movement(self, square, board):
        movements = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if((square.x + i <= 7 and square.x + i >= 0) and (square.y + j <= 7 and square.y + j >= 0)):
                    if(i != 0 or j != 0):
                        if(board[square.y + j][square.x + i].piece == None):
                            movements.append([square.x + i, square.y + j])
                        elif(board[square.y + j][square.x + i].piece.color != self.color):
                            movements.append([square.x + i, square.y + j])
        
        return movements

class Tower(Piece):
    def __init__(self, color):
        super().__init__(color, 'tower')

    def show_movement(self, square, board):
        movements = []
        for i in range(-7, 8):
            if(i != 0):
                if(square.x + i >= 0 and square.x + i < 8):
                    movements.append([square.x + i, square.y])

        for i in range(-7, 8):
            if(i != 0):
                if(square.y + i >= 0 and square.y + i < 8):
                    movements.append([square.x, square.y + i])
        
        return movements

class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color, 'bishop')

    def show_movement(self, square, board):
        movements = []

        for i in range(-8, 8):
            if(i != 0):
                if((square.x + i >= 0 and square.x + i < 8) and (square.y + i >= 0 and square.y + i < 8)):
                    movements.append([square.x + i, square.y+i])
                if((square.x - i >= 0 and square.x - i < 8) and (square.y + i >= 0 and square.y + i < 8)):
                    movements.append([square.x - i, square.y+i])
        
        return movements

class Queen(Piece):
    def __init__(self, color):
        super().__init__(color, 'queen')

    def show_movement(self, square, board):
        movements = []

        for i in range(-8, 8):
            if(i != 0):
                if((square.x + i >= 0 and square.x + i < 8) and (square.y + i >= 0 and square.y + i < 8)):
                    movements.append([square.x + i, square.y+i])
                if((square.x - i >= 0 and square.x - i < 8) and (square.y + i >= 0 and square.y + i < 8)):
                    movements.append([square.x - i, square.y+i])
                if(square.x + i >= 0 and square.x + i < 8):
                    movements.append([square.x + i, square.y])
                if(square.y + i >= 0 and square.y + i < 8):
                    movements.append([square.x, square.y + i])
        
        return movements

class Knight(Piece):
    def __init__(self, color):
        super().__init__(color, 'knight')

    def show_movement(self, square, board):
        movements = []
        for i in [-1, 1]:
            for j in [-1, 1]:
                if(i != 0 and j != 0):
                    if((square.x + i >= 0 and square.x + i < 8) and (square.y + 2 * j >= 0 and square.y + 2 * j < 8)):
                        movements.append([square.x + i, square.y + 2 * j])
                    if((square.x + 2 * i >= 0 and square.x + 2 * i < 8) and (square.y + j >= 0 and square.y + j < 8)):
                        movements.append([square.x + 2 * i, square.y + j])
        
        return movements