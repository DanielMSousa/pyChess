import pygame
from board import board
from square import return_piece

sqsize = 70

def load_img(place):
    img = pygame.image.load(place).convert_alpha()
    img = pygame.transform.scale(img, (sqsize, sqsize))
    return img

pygame.init()

screen = pygame.display.set_mode([8*sqsize, 8*sqsize])
pygame.display.set_caption('pyChess')

selected_tile = [None, None]

running = True

pieces = {
    'white_pawn': load_img('./pieces/white_pawn.png'),
    'white_bishop': load_img('./pieces/white_bishop.png'),
    'white_knight': load_img('./pieces/white_knight.png'),
    'white_tower': load_img('./pieces/white_tower.png'),
    'white_queen': load_img('./pieces/white_queen.png'),
    'white_king': load_img('./pieces/white_king.png'),

    'black_pawn': load_img('./pieces/black_pawn.png'),
    'black_bishop': load_img('./pieces/black_bishop.png'),
    'black_knight': load_img('./pieces/black_knight.png'),
    'black_tower': load_img('./pieces/black_tower.png'),
    'black_queen': load_img('./pieces/black_queen.png'),
    'black_king': load_img('./pieces/black_king.png')
}

clock = pygame.time.Clock()

moves = []

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()

            x = pos[0] // sqsize
            y = pos[1] // sqsize

            for row in board:
                for square in row:
                    square.original_color()

            if([x, y] in moves):
                moves = []
                piece = [board[selected_tile[1]][selected_tile[0]].piece.color, board[selected_tile[1]][selected_tile[0]].piece.name]
                board[y][x].piece = return_piece(piece)
                board[selected_tile[1]][selected_tile[0]].piece = None
                break

            #decidir se só pode selecionar onde tem peça
            if(board[y][x].piece):
                #if(selected_tile[0] != None):
                    #board[selected_tile[1]][selected_tile[0]].original_color()
                
                selected_tile[0] = x
                selected_tile[1] = y

                #Posso colocar o change_color dentro do interact()
                #board[y][x].change_color()
                moves = board[y][x].interact(board)

                for move in moves:
                    board[move[1]][move[0]].set_way()

    for row in board:
        for square in row:
            pygame.draw.rect(screen, square.color, (square.x * sqsize, square.y * sqsize, sqsize, sqsize))
            if(square.piece):
                screen.blit(pieces[square.piece.image_file], (square.x * sqsize, square.y * sqsize))


    pygame.display.flip()
    clock.tick(10)

pygame.quit()