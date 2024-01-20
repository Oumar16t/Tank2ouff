from classs import game1
import pygame
import time
import random
pygame.mixer.init()

def pause(game):
    i = 0
    while (i == 0):

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                game.pressed[event.key] = True
                if event.key == pygame.K_p:
                    i = 1
                    pygame.mixer.unpause()





class play_winter():

    def __init__(self):
        self.running = False


    def playing(self):
        clock = pygame.time.Clock()
        FPS = 120

        icon = pygame.image.load('tank de ouf off.png')
        pygame.display.set_caption("TANK2OUF")
        pygame.display.set_icon(icon)
        screen = pygame.display.set_mode((1490, 690))
        acceuil =  pygame.image.load('level_1_back.jpg')
        acceuil = pygame.transform.scale(acceuil,(1510,710))
        winter = pygame.image.load('tank_war_background/winter/collage_winter.jpg')
        winter = pygame.transform.scale(winter,(1500,700))


        play_button = pygame.image.load('ice_button-removebg-preview.png')
        play_button_rect = play_button.get_rect()
        play_button_rect.x = 690
        play_button_rect.y = 450

        menu_button = pygame.image.load('menu_but-removebg-preview.png')
        menu_button = pygame.transform.scale(menu_button, (200, 100))
        menu_button_rect = menu_button.get_rect()
        menu_button_rect.x = 50
        menu_button_rect.y = 70


        game = game1()

        time1 = 0
        time2 = 0

        self.running = True



        while self.running:

            screen.blit(acceuil,(0,0))

            if game.is_playing:
                screen.blit(winter, (0,0))
                game.update(screen,time2)

            else:

                screen.blit(play_button,play_button_rect)
                screen.blit(menu_button, menu_button_rect)

            pygame.display.flip()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()


                elif event.type == pygame.KEYDOWN:
                    game.pressed[event.key] = True

                    if event.key == pygame.K_SPACE:
                        time1 = time.time()
                    if event.key == pygame.K_p:
                        pygame.mixer.pause()
                        pause(game)



                elif event.type == pygame.KEYUP:
                    game.pressed[event.key] = False


                    if event.key == pygame.K_SPACE:
                        time2 = time.time()
                        time2 -= time1
                        game.player.lancer()


                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if play_button_rect.collidepoint(event.pos):
                        game.start()
                    elif menu_button_rect.collidepoint(event.pos):
                        self.running = False


            if random.randint(0,700) == 543 and game.ennemie1_dead==0:
                game.ennemie_1.shoot_ennemie()
            if random.randint(0,500)==275 and game.ennemie_2_dead==0:
                game.ennemie_2.shoot_ennemie()


            clock.tick(FPS)



