import pygame
from backend.configuracoes import AZUL, VERMELHO

def desenhar_personagem(tela, personagem, cor):
    pygame.draw.rect(tela, cor, (personagem.posição_x, personagem.posição_y, 50, 80))

def desenhar_range_ataque(tela, personagem, alcance, cor):
    cx, cy = personagem.posição_x + 25, personagem.posição_y + 40
    pygame.draw.circle(tela, cor, (cx, cy), alcance, 1)
