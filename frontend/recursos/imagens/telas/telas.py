import pygame
from os import path

endereço = path.dirname(path.abspath(__file__))

telas = []
provisorio = None

for i in range(1, 30):
    provisorio = pygame.image.load(f"{endereço}/{i}.png")
    if i in (12, 22, 23, 14, 27):
        provisorio = pygame.transform.scale(provisorio, (1920, 1080))
    elif i in (28, 29):
        provisorio = pygame.transform.scale(provisorio, (320, 116))
    else:
        provisorio = pygame.transform.scale(provisorio, (1300, 650))
    telas.append(provisorio)



