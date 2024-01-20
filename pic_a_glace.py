import pygame
import random
pygame.mixer.init()
class game_avanced:

    def __init__(self,game):
        self.percent = 0
        self.percent_speed = 0.1
        self.all_pic = pygame.sprite.Group()
        self.verif = 0
        self.game = game

    def add_percent(self):
        self.percent += self.percent_speed

    def pic_fall(self):
        x = random.randint(760,1240)
        y = 35

        self.all_pic.add(Stalactic(self, x, y))

    def pic_fall_2(self):
        x = random.randint(400 ,590)
        y = 90

        self.all_pic.add(Stalactic(self,x,y))



    def full_loaded(self):
        return self.percent >= 100


    def update_bar(self,surface):


        if not self.full_loaded():
            self.add_percent()

        self.verif = random.randint(0,800)

        if self.verif  == 1 or self.verif == 200:
            self.pic_fall()

        if self.verif == 200 or self.verif == 400:
            self.pic_fall_2()




class Stalactic(pygame.sprite.Sprite):

    def __init__(self,game_avanced,x,y):
        super().__init__()

        self.image = pygame.image.load('icicles (2) (1).png')
        self.image = pygame.transform.scale(self.image,(30,30))
        self.rect = self.image.get_rect()
        self.game_avanced = game_avanced
        self.rect.x = x
        self.rect.y = y




    def fall(self):

        self.rect.y += random.randint(10,15)
        son_pic_à_glace = pygame.mixer.Sound("sound/son_pic_à_glace.mp3")
        son_pic_à_glace.play()
        son_pic_à_glace.set_volume(0.1)


        if self.rect.y > 575:
            self.game_avanced.all_pic.remove(self)

        if self.game_avanced.game.check_collision(self,self.game_avanced.game.all_players):
            self.game_avanced.all_pic.remove(self)
            self.game_avanced.game.player.damage(30)

        if self.game_avanced.game.check_collision(self,self.game_avanced.game.all_ennemies):
            self.game_avanced.all_pic.remove(self)

