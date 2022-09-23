class Piece:
    def __init__(self, color, name='pawn'):
        self.color = color
        self.name = name
        self.image_file = f'{self.color}_{self.name}'
    
    def show_movement(self, square, board, piece_color):
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
    
    @staticmethod
    def show_movement(square, board, piece_color):
        movements = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                x = square.x + i
                y = square.y + j
                if((x <= 7 and x >= 0) and (y <= 7 and y >= 0)):
                    if(i != 0 or j != 0):
                        if(board[y][x].piece == None):
                            movements.append([x, y])
                        elif(board[y][x].piece.color != piece_color):
                            movements.append([x, y])
        
        return movements

class Tower(Piece):
    def __init__(self, color):
        super().__init__(color, 'tower')

    @staticmethod
    def show_movement(square, board, piece_color):
        movements = []
        
        y = square.y
        i = 1
        while(square.x - i >= 0):
            x = square.x - i
            if(board[y][x].piece):
                if(board[y][x].piece.color != piece_color):
                    movements.append([x, y])
                    break
                break
            
            movements.append([x, y])
            i += 1
        
        i = 1
        while(square.x + i <= 7):
            x = square.x + i
            if(board[y][x].piece):
                if(board[y][x].piece.color != piece_color):
                    movements.append([x, y])
                    break
                break

            movements.append([x, y])
            i += 1

        x = square.x
        j = 1
        while(square.y - j >= 0):
            y = square.y - j
            if(board[y][x].piece):
                if(board[y][x].piece.color != piece_color):
                    movements.append([x, y])
                    break
                break
            
            movements.append([square.x, square.y - j])
            j += 1

        j = 1
        while(square.y + j <= 7):
            y = square.y + j
            if(board[y][x].piece):
                if(board[y][x].piece.color != piece_color):
                    movements.append([x, y])
                    break
                break
            
            movements.append([x, y])
            j += 1
        
        return movements

class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color, 'bishop')

    def show_movement(self, square, board, piece_color):
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

    def show_movement(self, square, board, piece_color):
        movements = Tower.show_movement(square, board, piece_color)

        # for i in range(-8, 8):
        #     if(i != 0):
        #         if((square.x + i >= 0 and square.x + i < 8) and (square.y + i >= 0 and square.y + i < 8)):
        #             movements.append([square.x + i, square.y+i])
        #         if((square.x - i >= 0 and square.x - i < 8) and (square.y + i >= 0 and square.y + i < 8)):
        #             movements.append([square.x - i, square.y+i])
        #         if(square.x + i >= 0 and square.x + i < 8):
        #             movements.append([square.x + i, square.y])
        #         if(square.y + i >= 0 and square.y + i < 8):
        #             movements.append([square.x, square.y + i])
        
        return movements

class Knight(Piece):
    def __init__(self, color):
        super().__init__(color, 'knight')

    def show_movement(self, square, board, piece_color):
        movements = []
        for i in [-1, 1]:
            for j in [-1, 1]:
                if(i != 0 and j != 0):
                    if((square.x + i >= 0 and square.x + i < 8) and (square.y + 2 * j >= 0 and square.y + 2 * j < 8)):
                        movements.append([square.x + i, square.y + 2 * j])
                    if((square.x + 2 * i >= 0 and square.x + 2 * i < 8) and (square.y + j >= 0 and square.y + j < 8)):
                        movements.append([square.x + 2 * i, square.y + j])
        
        return movements