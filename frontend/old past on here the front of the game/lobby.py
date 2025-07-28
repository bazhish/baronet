import pygame
import sys
import os
from random import choice
from tela_criacao_personagem import desenhar_botao, font_title
import sqlite3
import pyautogui
from subprocess import Popen
import json



LARGURA, ALTURA = pyautogui.size()
endereço = os.path.dirname(os.path.abspath(__file__))

if __name__ == "__main__":
    if not os.path.exists(rf"{endereço}\usuario.json"):
        Popen([sys.executable, rf'{endereço}\tela_criacao_personagem.py'])
        sys.exit()

endereco_banco_de_dados = rf"{endereço}\banco_de_dados.db"

imagem_personagem = pygame.image.load(rf"{endereço}\Imagens\classes\personagem_representacao.png")
imagem_personagem = pygame.transform.scale(imagem_personagem, (LARGURA // 4, ALTURA // 3))

imagem_fundo_secundario = pygame.image.load(rf"{endereço}\Imagens\classes\fundo_secundario.png")
imagem_fundo_secundario = pygame.transform.scale(imagem_fundo_secundario, (LARGURA, ALTURA))
font_title = pygame.font.Font(rf"{endereço}\fonte\Minha fonte.ttf", 100)
font_nome = pygame.font.Font(rf"{endereço}\fonte\Minha fonte.ttf", 30)

with open(rf"{endereço}\usuario.json", "r") as arquivo:
    dados = json.load(arquivo)

nome_separado = dados["dados_pessoais"]["Nome"].split()
primeiro_nome = nome_separado[0].title()
classe = dados["dados_pessoais"]["Classe"].title()

teclas = dados["keys"]

pygame.init()
clock = pygame.time.Clock()

# Telas
MENU = "menu"
OPCOES = "opcoes"
estado = MENU

nome = font_nome.render(f"{primeiro_nome}", True, (190, 190, 230))

# Centraliza o nome em determinada posição
nome_rect = nome.get_rect(center=(LARGURA - LARGURA // 8, ALTURA // 2.1))

# Cria um retângulo atrás do nome com padding (espaçamento interno)
padding_x = 10
padding_y = 5

# Corrige a criação do retângulo (a coordenada Y estava errada)
rect = pygame.Rect(
                nome_rect.x - padding_x,
                nome_rect.y - padding_y,
                nome_rect.width + 2 * padding_x,
                nome_rect.height + 2 * padding_y
                )

# Tela
pygame.display.set_caption("Meu RPG")

if __name__ == "__main__":
    screen = pygame.display.set_mode((LARGURA, ALTURA), pygame.FULLSCREEN)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        if estado == MENU:
            screen.blit(imagem_fundo_secundario, (0, 0))

            texto_surface = font_title.render("RPG", True, (190, 190, 230))
            texto_rect = texto_surface.get_rect(center=(LARGURA // 2, ALTURA // 5))
            screen.blit(texto_surface, texto_rect)

            screen.blit(imagem_personagem, (LARGURA - LARGURA // 4, ALTURA // 2))

            # Desenha o retângulo cinza atrás do nome
            pygame.draw.rect(screen, (100, 100, 100), rect, border_radius=5)

            # Desenha o texto do nome por cima do retângulo
            screen.blit(nome, nome_rect)


            nome_classe = font_nome.render(f"{classe}", True, (190, 190, 230))
            nome_classe_rect = nome_classe.get_rect(center=(LARGURA - LARGURA // 8, ALTURA // 1.17))
            

            pygame.draw.rect(screen, (100, 100, 100), (nome_classe_rect.x - padding_x, nome_classe_rect.y - padding_y, nome_classe_rect.width + 2 * padding_x, nome_classe_rect.height + 2 * padding_y), border_radius=5)
            screen.blit(nome_classe, nome_classe_rect)

            if desenhar_botao("Sair",
                            LARGURA // 2 - LARGURA // 4,
                            ALTURA // 2 + ALTURA // 4,
                            LARGURA // 2,
                            ALTURA // 9,
                            ALTURA // 20,
                            (150, 150, 230),
                            (130, 130, 210),
                            20,
                            fonte = ALTURA // 18):
                pygame.quit()
                if os.path.exists(rf"{endereço}\usuario.json"):
                    os.remove(rf"{endereço}\usuario.json")
                Popen([sys.executable, rf'{endereço}\tela_criacao_personagem.py'])
                sys.exit()
            
            if desenhar_botao("Opções",
                            LARGURA // 2 - LARGURA // 4,
                            ALTURA // 2 + ALTURA // 10,
                            LARGURA // 2,
                            ALTURA // 9,
                            ALTURA // 20,
                            (150, 150, 230),
                            (130, 130, 210),
                            20,
                            fonte = ALTURA // 18):
                estado = OPCOES
                screen.blit(imagem_fundo_secundario, (0, 0))

                texto_surface = font_title.render("RPG", True, (190, 190, 230))
                texto_rect = texto_surface.get_rect(center=(LARGURA // 2, ALTURA // 5))
                screen.blit(texto_surface, texto_rect)

            if desenhar_botao("Jogar",
                            LARGURA // 2 - LARGURA // 4,
                            ALTURA // 2 - ALTURA // 20,
                            LARGURA // 2,
                            ALTURA // 9,
                            ALTURA // 20,
                            (150, 150, 230),
                            (130, 130, 210),
                            20,
                            fonte = ALTURA // 18):
                pygame.quit()
                if os.path.exists(rf"{endereço}\usuario.json"):
                    os.remove(rf"{endereço}\usuario.json")
                Popen([sys.executable, rf'{endereço}\tela_criacao_personagem.py'])
                sys.exit()
            
        if estado == OPCOES:
            screen.blit(imagem_fundo_secundario, (0, 0))

            texto_surface = font_title.render("RPG", True, (190, 190, 230))
            texto_rect = texto_surface.get_rect(center=(LARGURA // 2, ALTURA // 7))
            screen.blit(texto_surface, texto_rect)

            if desenhar_botao("<", LARGURA // 18, ALTURA // 13, LARGURA // 14, ALTURA // 8, ALTURA // 19, (140, 140, 140), (110, 110, 110), 40, fonte= ALTURA // 13):
                estado = MENU
            


        pygame.display.flip()
        clock.tick(16)

sys.exit()