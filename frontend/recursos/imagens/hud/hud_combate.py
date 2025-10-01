import pygame
import pyautogui
import os

LARGURA, ALTURA = pyautogui.size()
endereço = os.path.dirname(os.path.abspath(__file__))

vida_hud = []
vida_inimigo_hud = []
xp_hud = []
estamina_hud = []
vitoria_tela = []
derrota_tela = []
armas_hud = None
usaveis_hud = None

provisorio = None

for i in range(0, 11):
    provisorio = pygame.image.load(f"{endereço}/estamina/estamina{i}.png")
    provisorio = pygame.transform.scale(provisorio, (321, 120))
    estamina_hud.append(provisorio)

for i in range(0, 11):
    provisorio = pygame.image.load(f"{endereço}/vida/vida{i}.png")
    provisorio = pygame.transform.scale(provisorio, (321, 120))
    vida_hud.append(provisorio)

for i in range(0, 11):
    provisorio = pygame.image.load(f"{endereço}/XP/XP{i}.png")
    provisorio = pygame.transform.scale(provisorio, (321, 120))
    xp_hud.append(provisorio)

for i in range(0, 11):
    provisorio = pygame.image.load(f"{endereço}/vida_inimigo/vida_inimigo{i}.png")
    provisorio = pygame.transform.scale(provisorio, (110, 18))
    vida_inimigo_hud.append(provisorio)

for i in range(0, 18):
    provisorio = pygame.image.load(f"{endereço}/vitoria/vitoria{i}.png")
    provisorio = pygame.transform.scale(provisorio, (1080, 1080))
    vitoria_tela.append(provisorio)

for i in range(0, 27):
    provisorio = pygame.image.load(f"{endereço}/gameover/gameover{i}.png")
    provisorio = pygame.transform.scale(provisorio, (1080, 1080))
    derrota_tela.append(provisorio)



armas_hud = pygame.image.load(f"{endereço}/demonstrativos/armas.png")
armas_hud = pygame.transform.scale(armas_hud, (87, 356))

usaveis_hud = pygame.image.load(f"{endereço}/demonstrativos/usaveis.png")
usaveis_hud = pygame.transform.scale(usaveis_hud, (820, 77))