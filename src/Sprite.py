import pygame

class Sprite:
    """
    Cette classe permet de creer une image via pygame
    path: str - path vers l'image
    pos: (x, y) - coin supérieur gauche
    width: int
    height: int
    """
    def __init__(self, display, path:str, pos:tuple, width:int, height:int) -> None:
        self.display = display
        self.file = path
        self.rotation = 0
        if path != '':
            self.set_img(path)
        self.set_size(width, height)
        self.pos_init = pos
        self.pos = pos

    def get_pos(self):
        return self.pos

    def set_pos(self, pos:tuple):
        self.pos = pos
        self.pos_init = pos
    
    def set_size(self, width:int, height:int):
        self.img = pygame.transform.scale(self.img, (width, height))

    def set_img(self, path):
        self.img = pygame.image.load(path)

    def set_rotation(self, rotation:float):
        #self.img = pygame.transform.rotate(self.img, -self.rotation)
        #self.rotation = rotation
        self.img = pygame.transform.rotate(self.img, rotation)
    
    def __str__(self) -> str:
        return self.file
    
    def draw(self):
        """
        Draw l'img sur le display
        """
        self.display.blit(self.img, self.pos)