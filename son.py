import pygame

class SoundManager:

    def __init__(self):
        self.sounds = {
            'son_tire_tank': pygame.mixer.Sound("sound/tire_tank.mp3"),
            'son_dégat_tank': pygame.mixer.Sound("sound/degat_tank.mp3"),
            'son_pic_à_glace': pygame.mixer.Sound("sound/son_pic_à_glace.mp3"),
            'son_metéorite': pygame.mixer.Sound("sound/son_méteorite.mp3"),
            'son_menu': pygame.mixer.Sound("sound/son_menu.mp3"),
            'son_niveau1': pygame.mixer.Sound("sound/son_pokemon.mp3"),
            'son_niveau2': pygame.mixer.Sound("sound/son_lave.mp3"),
            'son_game_Over': pygame.mixer.Sound("sound/Game_Over.mp3"),
        }

    def play(self, name):
        self.sounds[name].play()