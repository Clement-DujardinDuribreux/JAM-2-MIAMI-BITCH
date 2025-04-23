import pygame
import time
from OPTIONS import *
from Sprite import Sprite
from Text import Text

class Button:
    """
    Cette classe permet de creer un boutton via pygame
    display: fenetre pygame
    pos: (x, y) - coin supérieur gauche
    width_height: (width, height) - taille
    col: (r, v, b) - couleur supérieur
    col2: (r, v, b) - couleur inférieur
    text: str - text sur bouton
    renvoi: no type - valeur de renvoi
    sprite_path [OPTION]: str - path vers le sprite
    """
    def __init__(self, display, pos:tuple, width_height:tuple, col:tuple, col2:tuple, text:str, renvoi, sprite_path = '') -> None:
        self.display = display
        self.pos = pos[0], pos[0] + width_height[0], pos[1], pos[1] + width_height[1]
        self.widht_height = width_height
        self.colours = col, col2
        self.text = Text(self.display, text, (0,0), 35 * (SCREENINFO.WIDTH/720), "assets/button_font.ttf")
        self.sound = 'assets/sound_button.mp3'
        self.img = None
        self.renvoi = renvoi
        self.clicked = False
        if sprite_path != '':
            self.img = Sprite(self.display, sprite_path, (self.pos[0] + self.widht_height[0] / 2 - self.widht_height[1] / 2 + 1, self.pos[2] - 6 * (SCREENINFO.HEIGHT/450)), width_height[1], width_height[1])
            if self.text.get_text() is not '': 
                self.img.set_size(width_height[1] - 7, width_height[1] - 7)
                self.img.set_pos((self.pos[0] + 35 * (SCREENINFO.WIDTH/720), self.pos[2] - SCREENINFO.HEIGHT/(450/3)))
        if type(self.img).__name__ is 'Sprite': self.has_img = True
        else: self.has_img = False
               
    def draw(self):
        """
        Draw le bouton sur le display
        """
        decal_click = 0
        if not self.clicked: 
            decal_click = 5*(SCREENINFO.WIDTH/720)
        if self.has_img:
            self.img.set_pos((self.pos[0] + self.widht_height[0] / 2 - self.widht_height[1] / 2 + 1, self.pos[2] - 6 * (SCREENINFO.HEIGHT/450)  + 5*(SCREENINFO.WIDTH/720) - decal_click))
            if self.text.get_text() != '':
                self.img.set_pos((self.pos[0] + 15 * (SCREENINFO.WIDTH/720), self.pos[2] - SCREENINFO.HEIGHT/(450/3) + 5*(SCREENINFO.WIDTH/720) - decal_click))
        pygame.draw.rect(self.display, self.colours[1], pygame.Rect(self.pos[0], self.pos[2], self.widht_height[0], self.widht_height[1]),border_radius=int(15*(SCREENINFO.WIDTH/720)))
        pygame.draw.rect(self.display, self.colours[0], pygame.Rect(self.pos[0], self.pos[2] - decal_click, self.widht_height[0], self.widht_height[1]), border_radius=int(15*(SCREENINFO.WIDTH/720)))                
        self.text.set_pos((self.pos[0] + self.widht_height[0]/2 - self.text.get_size()[0]/2, self.pos[2] + self.widht_height[1]/2 - self.text.get_size()[1]/2 - decal_click))
        self.text.draw()
        if self.has_img:
                self.img.draw()

    def update(self, event):
        """
        Update le bouton
        """
        self.draw()
        self.isClicked(event) 
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and self.clicked:                
            self.clicked = False
            self.draw()
            if pygame.mouse.get_pos()[0] > self.pos[0] and pygame.mouse.get_pos()[0] < self.pos[1] and pygame.mouse.get_pos()[1] > self.pos[2]-7 and pygame.mouse.get_pos()[1] < self.pos[3]-7:
                time.sleep(0.15)
                return self.renvoi

    def isClicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pos()[0] > self.pos[0] and pygame.mouse.get_pos()[0] < self.pos[1] and pygame.mouse.get_pos()[1] > self.pos[2]-7 and pygame.mouse.get_pos()[1] < self.pos[3]-7:
                if pygame.mouse.get_pressed(3)[0]:
                    self.clicked = True
                    sound_button = pygame.mixer.Sound(self.sound)
                    sound_button.set_volume(1)
                    sound_button.play()