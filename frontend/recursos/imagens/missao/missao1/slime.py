import pygame
import pyautogui
import os

LARGURA, ALTURA = pyautogui.size()
endereço = os.path.dirname(os.path.abspath(__file__))

screen = pygame.display.set_mode((1, 1))
pygame.display.iconify()

pygame.init()

slime_ataque0 =pygame.image.load(fr"{endereço}\ataque 0.png").convert_alpha()
slime_ataque0 = pygame.transform.scale(slime_ataque0, (200 * LARGURA // 1920, 200 * LARGURA // 1920))

slime_ataque1 =pygame.image.load(fr"{endereço}\ataque 1.png").convert_alpha()
slime_ataque1 = pygame.transform.scale(slime_ataque1, (200 * LARGURA // 1920, 200 * LARGURA // 1920))

slime_ataque2 =pygame.image.load(fr"{endereço}\ataque 2.png").convert_alpha()
slime_ataque2 = pygame.transform.scale(slime_ataque2, (200 * LARGURA // 1920, 200 * LARGURA // 1920))

slime_ataque3 =pygame.image.load(fr"{endereço}\ataque 3.png").convert_alpha()
slime_ataque3 = pygame.transform.scale(slime_ataque3, (200 * LARGURA // 1920, 200 * LARGURA // 1920))

slime_morto0 = pygame.image.load(fr"{endereço}\morte 0.png").convert_alpha()
slime_morto0 = pygame.transform.scale(slime_morto0, (200 * LARGURA // 1920, 200 * LARGURA // 1920))

slime_morto1 = pygame.image.load(fr"{endereço}\morte 1.png").convert_alpha()
slime_morto1 = pygame.transform.scale(slime_morto1, (200 * LARGURA // 1920, 200 * LARGURA // 1920))

slime_morto2 = pygame.image.load(fr"{endereço}\morte 2.png").convert_alpha()
slime_morto2 = pygame.transform.scale(slime_morto2, (200 * LARGURA // 1920, 200 * LARGURA // 1920))

slime_morto3 = pygame.image.load(fr"{endereço}\morte 3.png").convert_alpha()
slime_morto3 = pygame.transform.scale(slime_morto3, (200 * LARGURA // 1920, 200 * LARGURA // 1920))

slime_morto4 = pygame.image.load(fr"{endereço}\morte 4.png").convert_alpha()
slime_morto4 = pygame.transform.scale(slime_morto4, (200 * LARGURA // 1920, 200 * LARGURA // 1920))

slime_morto5 = pygame.image.load(fr"{endereço}\morte 5.png").convert_alpha()
slime_morto5 = pygame.transform.scale(slime_morto5, (200 * LARGURA // 1920, 200 * LARGURA // 1920))

slime_morto6 = pygame.image.load(fr"{endereço}\morte 6.png").convert_alpha()
slime_morto6 = pygame.transform.scale(slime_morto6, (200 * LARGURA // 1920, 200 * LARGURA // 1920))

slime_morto7 = pygame.image.load(fr"{endereço}\morte 7.png").convert_alpha()
slime_morto7 = pygame.transform.scale(slime_morto7, (200 * LARGURA // 1920, 200 * LARGURA // 1920))

slime_morto8 = pygame.image.load(fr"{endereço}\morte 8.png").convert_alpha()
slime_morto8 = pygame.transform.scale(slime_morto8, (200 * LARGURA // 1920, 200 * LARGURA // 1920))

slime_morto9 = pygame.image.load(fr"{endereço}\morte 9.png").convert_alpha()
slime_morto9 = pygame.transform.scale(slime_morto9, (200 * LARGURA // 1920, 200 * LARGURA // 1920))

slime_direita = [slime_ataque0,
                 slime_ataque1,
                 slime_ataque2,
                 slime_ataque3]

slime_parado = [slime_ataque0,
                slime_ataque1,
                slime_ataque2,
                slime_ataque3]

slime_morto =  [slime_morto0,
                slime_morto1,
                slime_morto2,
                slime_morto3,
                slime_morto4,
                slime_morto5,
                slime_morto6,
                slime_morto7,
                slime_morto8,
                slime_morto9]


