
QUIT_GAME = 0
SET_MAINSCENE = 1
SET_GAMESCENE = 2
SET_EASTEREGG = 3
SET_SKINSELECT = 4

INTER_SKINS = [i + 10 for i in range(2)]

class OPTIONS:
    
    SOUND_ON = True

class SCREENINFO:
    
    WIDTH = 1280
    HEIGHT = 720
    FULLSCREEN = False
    FPS = 60

class BEST_SCORES:

    BEST_SCORE_NORMAL = 0
    BEST_SCORES_HARDCORE = 0

    def set_best_score_normal(cls, score:int):
        if cls.BEST_SCORE_NORMAL < score:
            cls.BEST_SCORE_NORMAL = score
    set_best_score_normal = classmethod(set_best_score_normal)

    def set_best_score_hardcore(cls, score:int):
        if cls.BEST_SCORES_HARDCORE < score:
            cls.BEST_SCORES_HARDCORE = score
    set_best_score_hardcore = classmethod(set_best_score_hardcore)