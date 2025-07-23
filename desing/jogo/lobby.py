import pygame
import sys
import os
from random import choice
from tela_criacao_personagem import desenhar_botao
import sqlite3
import pyautogui
from subprocess import Popen
import json


endereço = os.path.dirname(os.path.abspath(__file__))

endereco_banco_de_dados = rf"{endereço}\banco_de_dados.db"

imagem_fundo_secundario = pygame.image.load(rf"{endereço}\Imagens\classes\fundo_secundario.png")
imagem_fundo_secundario = pygame.transform.scale(imagem_fundo_secundario, (1920, 1080))

pygame.init()
clock = pygame.time.Clock()

# Telas
MENU = "menu"
estado = MENU
LARGURA, ALTURA = pyautogui.size()


# Tela
pygame.display.set_caption("Meu RPG")

if __name__ == "__main__":
    if not os.path.exists(rf"{endereço}\usuario.json"):
        Popen([sys.executable, rf'{endereço}\tela_criacao_personagem.py'])
        sys.exit()
    screen = pygame.display.set_mode((LARGURA, ALTURA), pygame.FULLSCREEN)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        if estado == MENU:
            screen.blit(imagem_fundo_secundario, (0, 0))

            if desenhar_botao("Sair",
                            LARGURA // 2 - LARGURA // 4,
                            ALTURA // 2 + ALTURA // 4,
                            LARGURA // 2,
                            ALTURA // 9,
                            50,
                            (150, 150, 230),
                            (130, 130, 210),
                            20,
                            fonte = 50):
                pygame.quit()
                if os.path.exists(rf"{endereço}\usuario.json"):
                    os.remove(rf"{endereço}\usuario.json")
                Popen([sys.executable, rf'{endereço}\tela_criacao_personagem.py'])
                sys.exit()


        pygame.display.flip()
        clock.tick(60)

sys.exit()