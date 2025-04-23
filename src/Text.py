import pygame

class Text:
    """
    Cette classe permet de creer un texte (affichable) via pygame
    display: Display pygame
    text: str - text qui sera ecrit
    pos: (x, y) - coin supérieur gauche
    width: int - taille du text
    col: (r, v, b) - coleur du text (base noir)
    """
    def __init__(self, display, text:str, pos:tuple, width:float, fontpath:str, col = (0,0,0)) -> None:
        self.display = display
        self.text = text
        self.pos = pos
        self.col = col
        self.font = pygame.font.Font(fontpath, int(width))
        self.render = self.font.render(self.text, True, self.col)

    def get_text(self):
        return self.text
    
    def set_text(self, text:str):
        self.text = text
        self.render = self.font.render(self.text, True, self.col)
    
    def get_pos(self):
        return self.pos
    
    def set_pos(self, pos:tuple):
        self.pos = pos

    def get_size(self):
        return pygame.font.Font.size(self.font, self.text)

    def draw(self):
        """
        Draw le text sur le display
        """
        self.display.blit(self.render, self.pos)