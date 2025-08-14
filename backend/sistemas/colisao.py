import pygame
import math

def colidiu(p1, p2):
    rect1 = pygame.Rect(p1.posição_x, p1.posição_y, 50, 80)
    rect2 = pygame.Rect(p2.posição_x, p2.posição_y, 50, 80)
    return rect1.colliderect(rect2)

def dentro_do_range(p1, p2, alcance):
    cx1, cy1 = p1.posição_x + 25, p1.posição_y + 40
    cx2, cy2 = p2.posição_x + 25, p2.posição_y + 40
    return math.dist((cx1, cy1), (cx2, cy2)) <= alcance
