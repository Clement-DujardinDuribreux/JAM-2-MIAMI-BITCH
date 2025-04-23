from OPTIONS import *
from Scene import Scene
from Button import Button

class SkinSelect(Scene):

    def __init__(self, display):
        super().__init__(display)
        self.item_list = [Button(self.display, (200, 200), (100, 100), (255, 255, 255), (255, 0, 0), '', INTER_SKINS[0], "assets/player/phoenix/pre.png"),
                          Button(self.display, (500, 200), (100, 100), (255, 255, 255), (255, 0, 0), '', INTER_SKINS[1], "assets/player/easteregg/pre.png"),
                          Button(self.display, (30, 30), (75, 75), (255, 255, 255), (255, 0, 0), "", SET_MAINSCENE, "assets/Arrow_back.png")]
        self.set_background("assets/bg_game.jpg")