import pygame
from OPTIONS import *
from Sprite import Sprite

class Player:

    def __init__(self, display, skin):
        self.pos = 150, SCREENINFO.HEIGHT / 2
        self.sprite = Sprite(display, "assets/Arrow_back.png", self.pos, 150, 150)
        self.sprite.set_rotation(180)
        self.skin = skin
        self.list_sprite = ['01.png', '02.png', '03.png', '04.png', '05.png', '06.png', '07.png', '08.png', '09.png']
        self.count_sprite = 0
        self.clock = pygame.time.Clock()
        self.clock.tick(60)
        self.time = 0
        self.velocity = 0
        self.velocity_dicreese = 0.07
        self.display = display
        self.collision = False

    def  update(self, pillars=None):
        self.velocity -= self.velocity_dicreese
        self.sprite = Sprite(self.sprite.display, f"assets/player/{self.skin}/{self.list_sprite[self.count_sprite]}", self.pos, 150, 150)
        if self.velocity > -3:
            self.sprite.set_rotation(self.velocity * 10)
        else:
            self.sprite.set_rotation(-30)
        self.pos = (self.pos[0], self.pos[1] - self.velocity * 3)
        self.time += self.clock.get_time()
        if self.time > 100:
            self.count_sprite += 1
            self.count_sprite = self.count_sprite % 9
            self.time = 0
        if pillars is not None:
            self.check_collision(pillars) 
        return self.collision

    def jump(self):
        self.pos = (self.pos[0], self.pos[1] - 30)
        if self.pos[1] < 0:
            self.pos = (self.pos[0], -10)
        self.velocity = 2

    def check_collision(self, pillars):
        player_rect = pygame.Rect(self.pos[0] + 75, self.pos[1] + 70, 60, 40)
        #pygame.draw.rect(self.sprite.display, (0, 255, 0), player_rect)
        #self.sprite.draw()
        for pillar in pillars:
            top_pillar_rect = pygame.Rect(pillar['x'], 0, 
                                        pillar['pillar_width'], pillar['top_height'])
            bottom_pillar_rect = pygame.Rect(pillar['x'], pillar['bottom_y'],
                                           pillar['pillar_width'], pillar['bottom_height'])
            if player_rect.colliderect(top_pillar_rect) or player_rect.colliderect(bottom_pillar_rect):
                self.collision = True
                return True
        return False

    def draw(self):
        self.sprite.set_pos(self.pos)
        self.sprite.draw()
