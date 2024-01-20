

import pygame
import math
import time
import random
pygame.mixer.init()
from pic_a_glace import *



class game1:
    def __init__(self):

        self.is_playing = False
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        self.time = game_avanced(self)
        self.all_ennemies = pygame.sprite.Group()
        self.ennemie_1 = ennemies(self)
        self.all_ennemies.add(self.ennemie_1)
        self.all_ennemies_2 = pygame.sprite.Group()
        self.ennemie_2=ennemies_2(self)
        self.all_ennemies_2.add(self.ennemie_2)
        self.score = 0
        self.ennemie1_dead = 0
        self.ennemie_2_dead=0
        self.pressed = {}


    def start(self):
        self.is_playing = True

        son_niveau1 = pygame.mixer.Sound("sound\son_pokemon.mp3")
        son_niveau1.play(0, 0, 6000)
        son_niveau1.set_volume(0.3)


    def game_over(self):
        self.player.health = self.player.max_health
        self.ennemie_1.health = self.ennemie_1.max_health
        self.ennemie_1.health = self.ennemie_2.max_health
        self.player.rect.x = 50
        self.player.rect.y = 515
        self.is_playing = False
        self.score = 0
        pygame.mixer.stop()
        son_game_over = pygame.mixer.Sound("sound/Game_Over.mp3")
        son_game_over.play()
        son_game_over.set_volume(0.3)

    def win(self):
        self.player.health = self.player.max_health
        self.ennemie_1.health = self.ennemie_1.max_health
        self.ennemie_2.health = self.ennemie_2.max_health
        self.ennemie_2_dead=0
        self.ennemie1_dead=0
        self.all_ennemies.add(self.ennemie_1)
        self.all_ennemies_2.add(self.ennemie_2)
        self.player.rect.x = 50
        self.player.rect.y = 515
        self.is_playing = False
        self.score = 0
        pygame.mixer.stop()
        son_win = pygame.mixer.Sound("sound/son_win.mp3")
        son_win.play()
        son_win.set_volume(0.3)







    def update(self, screen,time2):

        screen.blit(self.player.image, self.player.rect)

        if self.ennemie1_dead == 0:
            screen.blit(self.ennemie_1.image, self.ennemie_1.rect)
            self.ennemie_1.update_health_bar(screen)
        if self.ennemie_2_dead==0:
            screen.blit(self.ennemie_2.image,self.ennemie_2.rect)
            self.ennemie_2.update_health_bar(screen)


        self.player.all_projectiles.draw(screen)

        self.player.update_health_bar(screen)

        self.ennemie_1.all_projectiles.draw(screen)

        self.ennemie_2.all_projectiles.draw(screen)

        self.time.update_bar(screen)

        self.time.all_pic.draw(screen)

        if self.ennemie_2_dead!=0 and self.ennemie1_dead!=0:
            self.win()

        for projectile in self.player.all_projectiles:
            projectile.move(time2)

        for projectil_ennemie in self.ennemie_1.all_projectiles:
            projectil_ennemie.tir()

        for projectil_ennemie_2 in self.ennemie_2.all_projectiles:
            projectil_ennemie_2.tir()


        self.ennemie_1.forward()

        for pic in self.time.all_pic:
            pic.fall()


        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x < 1000:
            self.player.move_right()
            self.player.is_moving = True
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 10:
            self.player.move_left()
            self.player.is_moving = True
        elif self.pressed.get(pygame.K_d) and self.player.rect.x < 1000:
            self.player.move_right()
            self.player.is_moving = True
        elif self.pressed.get(pygame.K_q) and self.player.rect.x > 10:
            self.player.move_left()
            self.player.is_moving = True
        else:
            self.player.is_moving = False

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)


class Player(pygame.sprite.Sprite):

    def __init__(self, game1):
        super().__init__()
        self.game1 = game1
        self.health = 100
        self.max_health = 100
        self.attack = 20
        self.velocity = 5
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load('tank_visu/tank_niveau_1.png')
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 515
        self.is_moving = False

    def update_health_bar(self, surface):
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x - 3, self.rect.y - 5, self.max_health, 7])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x - 3, self.rect.y - 5, self.health, 7])

    def damage(self, degats):
        if self.health - degats > degats:
            self.health -= degats
        else:
            self.game1.game_over()

    def lancer(self):
        self.all_projectiles.empty()
        self.all_projectiles.add(Projectile(self))
        son_tir = pygame.mixer.Sound("sound/tire_tank.mp3")
        son_tir.play()

    def move_right(self):
        if not self.game1.check_collision(self, self.game1.all_ennemies):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity


class Projectile(pygame.sprite.Sprite):

    def __init__(self, player):
        super().__init__()
        self.velocity = 7.0
        self.player = player
        self.a = 0.0
        self.image = pygame.image.load('rock-rock-pixel-art-11563244369s0r338s63h-removebg-preview.png')
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 63.0
        self.rect.y = player.rect.y + 0.0

    def remove(self):
        self.player.all_projectiles.empty()

    def move(self, time2):
        if time2 < 2:

            self.a += 0.15
            self.rect.x += self.velocity + (time2 * 4) - 1
            self.rect.y -= self.velocity + (time2 * 5) - 2 * self.a
        else:
            self.rect.x += self.velocity * 2

        for ennemies in self.player.game1.check_collision(self, self.player.game1.all_ennemies):
            self.remove()
            son_dommage = pygame.mixer.Sound("sound/degat_tank.mp3")
            son_dommage.play()
            ennemies.damage(self.player.attack)

        for ennemies_2 in self.player.game1.check_collision(self,self.player.game1.all_ennemies_2):
            self.remove()
            son_dommage = pygame.mixer.Sound("sound/degat_tank.mp3")
            son_dommage.play()
            ennemies_2.damage(self.player.attack)


        if self.rect.y > 580:
            self.remove()


class ennemies(pygame.sprite.Sprite):

    def __init__(self, game1):
        super().__init__()
        self.game1 = game1
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.image = pygame.image.load('Ennemies/tank ennemie 1.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1400
        self.rect.y = 520
        self.velocity = 2
        self.verif = 0
        self.all_projectiles = pygame.sprite.Group()
        self.time = 0

    def update_health_bar(self, surface):

        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x - 9, self.rect.y - 5, self.max_health, 5])
        pygame.draw.rect(surface, (240, 28, 12), [self.rect.x - 9, self.rect.y - 5, self.health, 5])

    def damage(self, degats):

        self.health -= degats

        if self.game1.ennemie_1.health <= 0:
            self.game1.score += 20
            self.game1.all_ennemies.empty()
            self.game1.ennemie1_dead = 1




    def forward(self):

        if self.rect.x > self.game1.player.rect.x + 800:
            self.verif = 1
        elif self.rect.x < self.game1.player.rect.x + 800:
            self.verif = 2
        elif self.rect.x == self.game1.player.rect.x + 800:
            self.verif = 0

        if not self.game1.check_collision(self, self.game1.all_players):

            if self.verif == 1:
                self.rect.x -= self.velocity

                for pro in self.all_projectiles:
                    pro.rect.x -= self.velocity

            elif self.verif == 2 and self.rect.x < 1400:
                self.rect.x += self.velocity

                for pro in self.all_projectiles:
                    pro.rect.x += self.velocity

        else:
            self.game1.player.damage(self.attack)

    def shoot_ennemie(self):
        self.all_projectiles.empty()
        self.all_projectiles.add(projectil_ennemie(self))


class projectil_ennemie(pygame.sprite.Sprite):

    def __init__(self, ennemies):
        super().__init__()
        self.ennemie = ennemies
        self.velocity = 5.5
        self.attack = 20
        self.image = pygame.image.load('pngtree-hot-fireball-sun-free-element-png-image_4528169-removebg-preview (1).png')
        self.rect = self.image.get_rect()
        self.rect.x = ennemies.rect.x - 15.0
        self.rect.y = ennemies.rect.y + 12.0
        self.a = 0.0

    def remove(self):
        self.kill()

    def tir(self):

        self.a += 0.1
        self.rect.x -= self.velocity
        self.rect.y -= self.velocity - self.a

        for player in self.ennemie.game1.check_collision(self, self.ennemie.game1.all_players):
            player.damage(self.attack)

            self.remove()
        if self.rect.x < 10:
            self.remove()
        if self.rect.y > 580:
            self.remove()





class ennemies_2(pygame.sprite.Sprite):

    def __init__(self,game1):
        super().__init__()
        self.game1 = game1
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.image = pygame.image.load('Ennemies/tank ennemie 3.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1000
        self.rect.y = 215
        self.velocity = 2
        self.verif = 0
        self.all_projectiles = pygame.sprite.Group()
        self.time = 0

    def update_health_bar(self,surface):

        pygame.draw.rect(surface, (60,63,60), [self.rect.x - 9 , self.rect.y - 5, self.max_health, 5])
        pygame.draw.rect(surface,(240,28,12),[self.rect.x - 9 ,self.rect.y - 5,self.health,5])


    def damage(self,degats):

        self.health -= degats

        if self.health <= 0:
            self.game1.score += 20
            self.game1.all_ennemies_2.empty()
            self.game1.ennemie_2_dead = 1



    def forward(self):

        if self.rect.x > self.game2.player.rect.x + 800:
            self.verif = 1
        elif self.rect.x < self.game2.player.rect.x + 800:
            self.verif = 2
        elif self.rect.x == self.game2.player.rect.x + 800:
            self.verif = 0

        if not self.game1.check_collision(self,self.game1.all_players):

            if self.verif == 1:
                self.rect.x -= self.velocity

                for pro in self.all_projectiles:
                    pro.rect.x -= self.velocity

            elif self.verif == 2 and self.rect.x < 1400:
                self.rect.x += self.velocity

                for pro in self.all_projectiles:
                    pro.rect.x += self.velocity

        else:
            self.game1.player.damage(self.attack)


    def shoot_ennemie(self):
        self.all_projectiles.empty()
        self.all_projectiles.add(projectil_ennemie_2(self))






class projectil_ennemie_2(pygame.sprite.Sprite):

    def __init__(self,ennemies):
        super().__init__()
        self.ennemie = ennemies
        self.velocity = 3
        self.attack = 20
        self.image = pygame.image.load('pngtree-cartoon-black-bomb-illustration-image_1406692-removebg-preview (1).png')
        self.rect = self.image.get_rect()
        self.rect.x = ennemies.rect.x -15.0
        self.rect.y = ennemies.rect.y +12.0
        self.a=0.0

    def remove(self):
        self.kill()


    def tir(self):

        self.a += 0.1
        self.rect.x -= self.velocity
        self.rect.y -= self.velocity -self.a

        for player in self.ennemie.game1.check_collision(self, self.ennemie.game1.all_players):
            player.damage(self.attack)
            self.remove()

        if self.rect.x < 10:
            self.remove()
        if self.rect.y > 580:
            self.remove()

