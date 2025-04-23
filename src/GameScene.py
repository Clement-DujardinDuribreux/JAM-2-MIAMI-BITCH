import pygame
from OPTIONS import *
from Scene import Scene
from Button import Button
from Player import Player
from Text import Text
import random
import pygame

class GameScene(Scene):
    """
    Game scene
    """
    def __init__(self, display, skin):
        super().__init__(display)
        self.name_mode = 'normal'
        self.player = Player(self.display, skin)
        self.score = 0
        self.color_score = (0, 0, 0)
        self.item_list = [Button(self.display, (30, 30), (75, 75), (255, 255, 255), (255, 0, 0), "", SET_MAINSCENE, "assets/Arrow_back.png"),
                          Text(self.display, f"{BEST_SCORES.BEST_SCORE_NORMAL}", (30, SCREENINFO.HEIGHT - 60), 40,  "assets/font.ttf", (255, 0, 0))]
        self.set_background("assets/bg_game.jpg")
        self.pillar_texture = pygame.image.load("assets/pillar_img-removebg-preview.png").convert_alpha()
        self.pillars = []
        self.pillar_width = 100
        self.pillar_gap = 200
        self.pillar_speed = 5
        self.spawn_timer = 0
        self.spawn_delay = 70
        self.pillar_texture = pygame.transform.scale(self.pillar_texture, (self.pillar_width, SCREENINFO.HEIGHT))
        self.spawn_pillar()

    def update(self, event = None):
        retour = super().update(event)
        if event != None and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            self.player.jump()
        if event != None and event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            return [SET_MAINSCENE]
        if event == None:
            collision = self.player.update(self.pillars)
            self.get_score()
            if collision or self.player.pos[1] > SCREENINFO.HEIGHT - 100:
                if self.name_mode == 'normal':
                    BEST_SCORES.set_best_score_normal(self.score)
                elif self.name_mode == 'hardcore':
                    BEST_SCORES.set_best_score_hardcore(self.score)
                return [SET_MAINSCENE]
        return retour
    
    def spawn_pillar(self):
        gap_y = random.randint(100, SCREENINFO.HEIGHT - 100 - self.pillar_gap)
        
        pillar = {
            'x': SCREENINFO.WIDTH,
            'top_height': gap_y,
            'bottom_y': gap_y + self.pillar_gap,
            'bottom_height': SCREENINFO.HEIGHT - (gap_y + self.pillar_gap),
            'pillar_width': self.pillar_width,
            'counted':0
        }
        self.pillars.append(pillar)

    def update_pillars(self):
        for pillar in self.pillars:
            pillar['x'] -= self.pillar_speed
        self.pillars = [p for p in self.pillars if p['x'] + self.pillar_width > 0]
        self.spawn_timer += 1
        if self.spawn_timer >= self.spawn_delay:
            self.spawn_timer = 0
            self.spawn_pillar()

    def draw_pillars(self):
        for pillar in self.pillars:
            top_pillar = self.pillar_texture.subsurface((0, SCREENINFO.HEIGHT - pillar['top_height'], 
                                                        self.pillar_width, pillar['top_height']))
            bottom_pillar = self.pillar_texture.subsurface((0, 0, 
                                                           self.pillar_width, pillar['bottom_height']))
            self.display.blit(top_pillar, (pillar['x'], 0))
            self.display.blit(bottom_pillar, (pillar['x'], pillar['bottom_y']))

    def draw(self):
        super().draw()
        self.update_pillars()
        self.draw_pillars()
        self.player.draw()
        Text(self.display, f"Score : {self.score}", (200, 50), 40, "assets/font.ttf", self.color_score).draw()
        if len(self.item_list) > 1:
            for item in self.item_list[1:]:
                item.draw()

    def get_score(self):
        for p in self.pillars:
            if p['x'] < 150 and not p['counted']:
                self.score += 1
                p['counted'] = 1

    def set_best_game_score(cls, score:int):
        if score > cls.BEST_GAME_SCORE:
            cls.BEST_GAME_SCORE = score
    set_best_game_score = classmethod(set_best_game_score)