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

slime_ataque4 =pygame.image.load(fr"{endereço}\ataque 4.png")
slime_ataque4 = pygame.transform.scale(slime_ataque4, (200 * LARGURA // 1920, 200 * LARGURA // 1920))

slime_ataque5 =pygame.image.load(fr"{endereço}\ataque 5.png")
slime_ataque5 = pygame.transform.scale(slime_ataque5, (200 * LARGURA // 1920, 200 * LARGURA // 1920))

slime_ataque6 =pygame.image.load(fr"{endereço}\ataque 6.png")
slime_ataque6 = pygame.transform.scale(slime_ataque6, (200 * LARGURA // 1920, 200 * LARGURA // 1920))

slime_ataque7 =pygame.image.load(fr"{endereço}\ataque 7.png")
slime_ataque7 = pygame.transform.scale(slime_ataque7, (200 * LARGURA // 1920, 200 * LARGURA // 1920))

slime_ataque8 =pygame.image.load(fr"{endereço}\ataque 8.png")
slime_ataque8 = pygame.transform.scale(slime_ataque8, (200 * LARGURA // 1920, 200 * LARGURA // 1920))

slime_ataque9 =pygame.image.load(fr"{endereço}\ataque 9.png")
slime_ataque9 = pygame.transform.scale(slime_ataque9, (200 * LARGURA // 1920, 200 * LARGURA // 1920))

slime_ataque10 =pygame.image.load(fr"{endereço}\ataque 10.png")
slime_ataque10 = pygame.transform.scale(slime_ataque10, (200 * LARGURA // 1920, 200 * LARGURA // 1920))

slime_ataque11 =pygame.image.load(fr"{endereço}\ataque 11.png")
slime_ataque11 = pygame.transform.scale(slime_ataque11, (200 * LARGURA // 1920, 200 * LARGURA // 1920))

slime_ataque12 =pygame.image.load(fr"{endereço}\ataque 12.png")
slime_ataque12 = pygame.transform.scale(slime_ataque12, (200 * LARGURA // 1920, 200 * LARGURA // 1920))

slime_ataque13 =pygame.image.load(fr"{endereço}\ataque 13.png")
slime_ataque13 = pygame.transform.scale(slime_ataque13, (200 * LARGURA // 1920, 200 * LARGURA // 1920))

slime_ataque14 =pygame.image.load(fr"{endereço}\ataque 14.png")
slime_ataque14 = pygame.transform.scale(slime_ataque14, (200 * LARGURA // 1920, 200 * LARGURA // 1920))

slime_ataque15 =pygame.image.load(fr"{endereço}\ataque 15.png")
slime_ataque15 = pygame.transform.scale(slime_ataque15, (200 * LARGURA // 1920, 200 * LARGURA // 1920))

slime_direita = [slime_ataque1,
                 slime_ataque2,
                 slime_ataque3,
                 slime_ataque4,
                 slime_ataque5,
                 slime_ataque6,
                 slime_ataque7,
                 slime_ataque8,
                 slime_ataque9,
                 slime_ataque10,
                 slime_ataque11,
                 slime_ataque12,
                 slime_ataque13,
                 slime_ataque14,
                 slime_ataque15,]
