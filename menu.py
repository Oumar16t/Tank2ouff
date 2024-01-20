import pygame
from winter import *
from desert import *
pygame.mixer.init()


# Definition de la fonction du menu principale reliant au niveau 'desert' et 'winter'
def menu_de_jeu():


    son_menu = pygame.mixer.Sound("sound\son_menu.mp3")
    son_menu.play()
    son_menu.set_volume(0.1)

    #initialisation de la fenetre de jeu
    icon = pygame.image.load('tank de ouf off.png')
    pygame.display.set_caption("TANK2OUF")
    pygame.display.set_icon(icon)
    screen = pygame.display.set_mode((1490, 690))

    ## creation fond du menu
    acceuil =  pygame.image.load('MENU8TANK2OUF_off.jpg')
    acceuil = pygame.transform.scale(acceuil,(1510,710))

    ## creation des boutons menant au deifferents niveau
    play_button_1 = pygame.image.load('rock_start-removebg-preview.png')
    play_button_1 = pygame.transform.scale(play_button_1,(100,50))
    play_button_1_rect = play_button_1.get_rect()
    play_button_1_rect.x = 420
    play_button_1_rect.y = 400

    play_button_2 = pygame.image.load('rock_start-removebg-preview.png')
    play_button_2 = pygame.transform.scale(play_button_2,(100,50))
    play_button_2_rect = play_button_2.get_rect()
    play_button_2_rect.x = 1070
    play_button_2_rect.y = 400


    running = True

    winter = play_winter()
    desert = play_desert()


    while running:

        if winter.running == True:

            son_menu.fadeout(4000)
            winter.playing()

        elif desert.running == True:
            son_menu.fadeout(4000)
            desert.playing()

        else:
            screen.blit(acceuil, (0, 0))

            screen.blit(play_button_1, play_button_1_rect)
            screen.blit(play_button_2, play_button_2_rect)

        pygame.display.flip()



        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button_1_rect.collidepoint(event.pos):
                    winter.running = True

                elif play_button_2_rect.collidepoint(event.pos):
                    desert.running = True


