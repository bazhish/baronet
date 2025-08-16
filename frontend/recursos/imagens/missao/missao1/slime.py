import pygame
import pyautogui
import os

LARGURA, ALTURA = pyautogui.size()
endereço = os.path.dirname(os.path.abspath(__file__))

pygame.init()

slime_parado1 =pygame.image.load(f"{endereço}\parado 1.png")
slime_parado1 = pygame.transform.scale(slime_parado1, (200 * LARGURA // 1920, 200 * LARGURA // 1920))

slime_parado2 =pygame.image.load(f"{endereço}\parado 2.png")
slime_parado2 = pygame.transform.scale(slime_parado2, (200 * LARGURA // 1920, 200 * LARGURA // 1920))

slime_parado3 =pygame.image.load(f"{endereço}\parado 3.png")
slime_parado3 = pygame.transform.scale(slime_parado3, (200 * LARGURA // 1920, 200 * LARGURA // 1920))

slime_parado4 =pygame.image.load(f"{endereço}\parado 4.png")
slime_parado4 = pygame.transform.scale(slime_parado4, (200 * LARGURA // 1920, 200 * LARGURA // 1920))

slime_parado = [slime_parado1,
                slime_parado2,
                slime_parado3,
                slime_parado4,
                slime_parado3,
                slime_parado2,
                slime_parado1]


slime_ataque1 =pygame.image.load(fr"{endereço}\ataque 1.png")
slime_ataque1 = pygame.transform.scale(slime_ataque1, (200 * LARGURA // 1920, 200 * LARGURA // 1920))

slime_ataque2 =pygame.image.load(fr"{endereço}\ataque 2.png")
slime_ataque2 = pygame.transform.scale(slime_ataque2, (200 * LARGURA // 1920, 200 * LARGURA // 1920))

slime_ataque3 =pygame.image.load(fr"{endereço}\ataque 3.png")
slime_ataque3 = pygame.transform.scale(slime_ataque3, (200 * LARGURA // 1920, 200 * LARGURA // 1920))

slime_direita = [slime_ataque1,
                 slime_ataque2,
                 slime_ataque3]
