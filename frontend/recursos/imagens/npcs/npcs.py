import pygame
import os
import sys

pygame.init()
pygame.display.set_mode((1, 1))
LArgura, Altura = pygame.display.Info().current_w, pygame.display.Info().current_h
endereço = os.path.dirname(os.path.abspath(__file__))

fazendeiro_npc_images = []
slime_npc_images = []
for i in range(2):
    npc_image = pygame.image.load(fr"{endereço}\fazendeiro_{i}.png").convert_alpha()
    scaled_image = pygame.transform.scale(npc_image, (70, 70))
    fazendeiro_npc_images.append(scaled_image)

for i in range(2):
    npc_image = pygame.image.load(fr"{endereço}\slime {i}.png").convert_alpha()
    scaled_image = pygame.transform.scale(npc_image, (480, 480))
    slime_npc_images.append(scaled_image)

class npc:
    def __init__(self, tipo, x, y, imagem):
        self.tipo = tipo
        self.x = x
        self.y = y
        self.imagem = imagem
        self.frame = 0
        self.rect = pygame.Rect(self.x - 1, self.y - 1, imagem[0].get_width() + 42, imagem[0].get_height() + 42)

fazendeiro_npc = npc("fazendeiro", 761, 630, fazendeiro_npc_images)
slime_npc = npc("slime", 1029, 270, slime_npc_images)

def atualizar_npc(obj, pos_chao_x, pos_chao_y):
    screen_x = ((obj.x - 1 - 500) * 19200) // (1380 - 500) + pos_chao_x
    screen_y = ((obj.y - 1 - 100) * 19200) // (980 - 100) + pos_chao_y
    obj.rect.topleft = (screen_x, screen_y)
npcs = [fazendeiro_npc, slime_npc]