class Piece:
    def __init__(self, color, name='pawn'):
        self.color = color
        self.name = name
        self.image_file = f'{self.color}_{self.name}'