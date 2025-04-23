from OPTIONS import *
from GameScene import GameScene
from Text import Text

class EasterEggScene(GameScene):

    BEST_GAME_SCORE = 0

    def __init__(self, display):
        super().__init__(display, "easteregg")
        self.name_mode = 'hardcore'
        self.set_music("assets/easter_egg.mp3")
        self.set_background("assets/bg_easteregg.png")
        self.color_score = (255, 255, 255)
        self.play_music()
        self.item_list[2] = Text(self.display, f"{BEST_SCORES.BEST_SCORES_HARDCORE}", (30, SCREENINFO.HEIGHT - 60), 40,  "assets/font.ttf", (255, 0, 255))
        self.pillar_gap = 300
        self.pillar_speed *= 4
        self.spawn_delay = 20
        self.player.velocity_dicreese *= 1.5