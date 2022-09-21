import numpy as np
import matplotlib.pyplot as plt

from square import CheckerSquare

pieces_position = [
 [('black', 'tower'), ('black', 'knight'), ('black', 'bishop'), ('black', 'king'), ('black', 'queen'), ('black', 'bishop'), ('black', 'knight'), ('black', 'tower')],
 [('black', 'pawn'), ('black', 'pawn'), ('black', 'pawn'), ('black', 'pawn'), ('black', 'pawn'), ('black', 'pawn'), ('black', 'pawn'), ('black', 'pawn')],
 [None, None, None, None, None, None, None, None],
 [None, None, None, None, None, None, None, None],
 [None, None, None, None, None, None, None, None],
 [None, None, None, None, None, None, None, None],
 [('white', 'pawn'), ('white', 'pawn'), ('white', 'pawn'), ('white', 'pawn'), ('white', 'pawn'), ('white', 'pawn'), ('white', 'pawn'), ('white', 'pawn')],
 [('white', 'tower'), ('white', 'knight'), ('white', 'bishop'), ('white', 'king'), ('white', 'queen'), ('white', 'bishop'), ('white', 'knight'), ('white', 'tower')]
]

#massa que eu não vou poder fazer assim, vou ter que gerar uma nova instância da classe
#que herda a classe peça
def generateBoard():
    #Como posso tornar essa operação menos custosa computacionalmente?
    matrix = []
    for y in range(8):
        row = []
        for x in range(8):
            piece = pieces_position[y][x]
            if(piece != None):
                piece = (piece[0], piece[1])
            p = CheckerSquare(x, y, (x + y) % 2, piece)
            row.append(p)
        matrix.append(row)
    return matrix

board = generateBoard()