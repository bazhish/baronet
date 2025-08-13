import pygame
import sys
import os
from random import choice
from tela_criacao_personagem import desenhar_botao, TEXTO_S, COR_TEXTO, COR_INATIVA, COR_ATIVA
from lobby import input_boxes, salvar, fonte_input, font_title
import sqlite3
import pyautogui
from subprocess import Popen
import json
from Imagens.personagem_principal import personagem_parado, personagem_andando_D
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
#from backend.app.models.sistema.habilidades_ativa_combatentes import golpe_mortal, intangibilidade, impacto_cruzado, bloqueio_de_espada, ataque_com_escudo, defesa_reforcada, giro_de_lanca, arremesso_de_lanca, disparo_perfurante, camuflagem, ataque_surpresa, fuga_rapida
#from backend.app.models.sistema.habilidades_passivas_combatentes import furtividade, evasao, sangramento, vontade_da_espada, heranca_da_espada, ataque_rapido, bloqueio_de_ataque, repelir, peso_pena, danca_da_lanca, controle_passivo, controle_total, disparo_preciso, passos_silenciosos, flecha_dupla, ataque_silencioso, evasao_rapida, exploracao_furtiva
LARGURA, ALTURA = pyautogui.size()
endereço = os.path.dirname(os.path.abspath(__file__))



with open(rf"{endereço}\usuario.json", "r") as arquivo:
    dados = json.load(arquivo)

teclas = dados["keys"]

posição = 0
colisao_chao = True
continuar_esquerda = False
continuar_direita = False
vel_y = 0
travar = False
gravidade = 1.5 * LARGURA // 1920
forca_pulo = -10 * LARGURA // 1920
pulo_detectado = False
parede = False
limite_de_pulo = 2
qnt_de_pulo = 0
posição_personagem_X = 500 * LARGURA // 1920
posição_personagem_Y = 520 * LARGURA // 1920
frame_personagem = 0
estado_personagem = personagem_parado
diresao = "parado"

if __name__ == "__main__":
    if not os.path.exists(rf"{endereço}\usuario.json"):
        Popen([sys.executable, rf'{endereço}\tela_criacao_personagem.py'])
        sys.exit()

endereco_banco_de_dados = rf"{endereço}\banco_de_dados.db"

cenario_combate = pygame.image.load(rf"{endereço}\imagens\cenario\cenario_combate.png")
cenario_combate = pygame.transform.scale(cenario_combate, (LARGURA * 5, ALTURA))



# if dados["dados_pessoais"]["Classe"] == "arqueiro":
#     habilidade_1_usavel = disparo_perfurante
#     habilidade_2_usavel = camuflagem
#     habilidade_passiva_1 = disparo_preciso
#     habilidade_passiva_2 = passos_silenciosos
#     habilidade_passiva_3 = flecha_dupla
# elif dados["dados_pessoais"]["Classe"] == "espadachin":
#     habilidade_1_usavel = impacto_cruzado
#     habilidade_2_usavel = bloqueio_de_espada
#     habilidade_passiva_1 = vontade_da_espada
#     habilidade_passiva_2 = heranca_da_espada
#     habilidade_passiva_3 = ataque_rapido
# elif dados["dados_pessoais"]["Classe"] == "assassino":
#     habilidade_1_usavel = golpe_mortal
#     habilidade_2_usavel = intangibilidade
#     habilidade_passiva_1 = furtividade
#     habilidade_passiva_2 = evasao
#     habilidade_passiva_3 = sangramento
# elif dados["dados_pessoais"]["Classe"] == "escudeiro":
#     habilidade_1_usavel = ataque_com_escudo
#     habilidade_2_usavel = defesa_reforcada
#     habilidade_passiva_1 = bloqueio_de_ataque
#     habilidade_passiva_2 = repelir
#     habilidade_passiva_3 = peso_pena
# elif dados["dados_pessoais"]["Classe"] == "lanceiro":
#     habilidade_1_usavel = giro_de_lanca
#     habilidade_2_usavel = arremesso_de_lanca
#     habilidade_passiva_1 = danca_da_lanca
#     habilidade_passiva_2 = controle_passivo
#     habilidade_passiva_3 = controle_total
# elif dados["dados_pessoais"]["Classe"] == "batedor":
#     habilidade_1_usavel = ataque_surpresa
#     habilidade_2_usavel = fuga_rapida
#     habilidade_passiva_1 = ataque_silencioso
#     habilidade_passiva_2 = evasao_rapida
#     habilidade_passiva_3 = exploracao_furtiva



pygame.init()
clock = pygame.time.Clock()

usuario = {"nivel": dados["status"]["nivel"],
           "estamina": dados["status"]["dano"] * 10,
           "defesa": dados["status"]["defesa"],
           "vida": dados["status"]["vida"] * 10,
           "velocidade": dados["status"]["velocidade"],
           "dano": dados["status"]["dano"],
           "experiencia": dados["status"]["experiencia"]}

# Estados
JOGO = "jogo"
OPCOES = "opcoes"
MENU = "menu"
INVENTARIO = "inventario"
COMBATE = "combate"
estado = COMBATE

tranparencia = 150
sombra = pygame.Surface((100 * LARGURA // 1920, 20 * LARGURA // 1920), pygame.SRCALPHA)



quadrado = pygame.Surface((LARGURA, ALTURA), pygame.SRCALPHA)
quadrado_2 = pygame.Surface((LARGURA, ALTURA), pygame.SRCALPHA)
quadrado_3 = pygame.Surface((LARGURA, ALTURA), pygame.SRCALPHA)
contador = 0
rect_opcoes = pygame.Rect(LARGURA // 2.5, LARGURA // 1.5, ALTURA // 1.6, ALTURA // 2)
click = False
click_e = False




def colisao_chao_batalha():
    global posição_chao, posição_personagem_X, posição, parede
    if posição_personagem_X <= 200 * LARGURA // 1920:
        posição_chao = 684 + 5 * LARGURA // 1920
    elif posição_personagem_X <= 220 * LARGURA // 1920:
        posição_chao = 680 + 5 * LARGURA // 1920
    elif posição_personagem_X <= 240 * LARGURA // 1920:
        posição_chao = 676 + 5 * LARGURA // 1920
    elif posição_personagem_X <= 260:
        posição_chao = 672 + 5 * LARGURA // 1920
    elif posição_personagem_X <= 280 * LARGURA // 1920:
        posição_chao = 668 + 5 * LARGURA // 1920
    elif posição_personagem_X <= 300 * LARGURA // 1920:
        posição_chao = 666 + 5 * LARGURA // 1920
    elif posição_personagem_X <= 320 * LARGURA // 1920:
        posição_chao = 664 + 5 * LARGURA // 1920
    elif posição_personagem_X <= 340 * LARGURA // 1920:
        posição_chao = 662 + 5 * LARGURA // 1920
    elif posição_personagem_X <= 360 * LARGURA // 1920:
        posição_chao = 660 + 5 * LARGURA // 1920
    elif posição_personagem_X <= 380 * LARGURA // 1920:
        posição_chao = 658 + 5 * LARGURA // 1920
    elif posição_personagem_X <= 400 * LARGURA // 1920:
        posição_chao = 656 + 5 * LARGURA // 1920
    elif posição_personagem_X < 500 * LARGURA // 1920:
        posição_chao = 653 + 5 * LARGURA // 1920
    elif posição >= -10 * LARGURA // 1920:
        posição_chao = 659 + 5 * LARGURA // 1920
    elif posição >= -20 * LARGURA // 1920:
        posição_chao = 663 + 5 * LARGURA // 1920
    elif posição >= -30 * LARGURA // 1920:
        posição_chao = 667 + 5 * LARGURA // 1920
    elif posição >= -40 * LARGURA // 1920:
        posição_chao = 669 + 5 * LARGURA // 1920
    elif posição >= -50 * LARGURA // 1920:
        posição_chao = 672 + 5 * LARGURA // 1920
    elif posição >= -60 * LARGURA // 1920:
        posição_chao = 677 + 5 * LARGURA // 1920
    elif posição >= -70 * LARGURA // 1920:
        posição_chao = 681 + 5 * LARGURA // 1920
    elif posição >= -80 * LARGURA // 1920:
        posição_chao = 685 + 5 * LARGURA // 1920
    elif posição >= -90 * LARGURA // 1920:
        posição_chao = 693 + 5 * LARGURA // 1920
    elif posição >= -100 * LARGURA // 1920:
        posição_chao = 705 + 5 * LARGURA // 1920
    elif posição >= -110 * LARGURA // 1920:
        posição_chao = 715 + 5 * LARGURA // 1920
    elif posição >= -180 * LARGURA // 1920:
        posição_chao = 723 + 5 * LARGURA // 1920
    elif posição >= -200 * LARGURA // 1920:
        posição_chao = 730 + 5 * LARGURA // 1920
    elif posição >= -220 * LARGURA // 1920:
        posição_chao = 734 + 5 * LARGURA // 1920
    elif posição >= -240 * LARGURA // 1920:
        posição_chao = 738 + 5 * LARGURA // 1920
    elif posição >= -250 * LARGURA // 1920:
        posição_chao = 742 + 5 * LARGURA // 1920
    elif posição >= -260 * LARGURA // 1920:
        posição_chao = 748 + 5 * LARGURA // 1920
    elif posição >= -270 * LARGURA // 1920:
        posição_chao = 752 + 5 * LARGURA // 1920
    elif posição >= -290 * LARGURA // 1920:
        posição_chao = 748 + 5 * LARGURA // 1920
    elif posição >= -400 * LARGURA // 1920:
        posição_chao = 752 + 5 * LARGURA // 1920
        if posição <= -400 * LARGURA // 1920:
            parede = True
        else:
            parede = False
    elif posição >= -540 * LARGURA // 1920:
        posição_chao = 690 + 5 * LARGURA // 1920
    elif posição >= -600 * LARGURA // 1920:
        posição_chao = 685 + 5 * LARGURA // 1920
    elif posição >= -630 * LARGURA // 1920:
        posição_chao = 690 + 5 * LARGURA // 1920
    elif posição >= -650 * LARGURA // 1920:
        posição_chao = 685 + 5 * LARGURA // 1920
    elif posição >= -680 * LARGURA // 1920:
        posição_chao = 680 + 5 * LARGURA // 1920
    elif posição >= -700 * LARGURA // 1920:
        posição_chao = 675 + 5 * LARGURA // 1920
    elif posição >= -720 * LARGURA // 1920:
        posição_chao = 672 + 5 * LARGURA // 1920
    elif posição >= -830 * LARGURA // 1920:
        posição_chao = 670 + 5 * LARGURA // 1920
    elif posição >= -840 * LARGURA // 1920:
        posição_chao = 673 + 5 * LARGURA // 1920
    elif posição >= -850 * LARGURA // 1920:
        posição_chao = 676 + 5 * LARGURA // 1920
    elif posição >= -860 * LARGURA // 1920:
        posição_chao = 680 + 5 * LARGURA // 1920
    elif posição >= -870 * LARGURA // 1920:
        posição_chao = 683 + 5 * LARGURA // 1920
    elif posição >= -880 * LARGURA // 1920:
        posição_chao = 686 + 5 * LARGURA // 1920
    elif posição >= -890 * LARGURA // 1920:
        posição_chao = 689 + 5 * LARGURA // 1920
    elif posição >= -900 * LARGURA // 1920:
        posição_chao = 694 + 5 * LARGURA // 1920
    elif posição >= -910 * LARGURA // 1920:
        posição_chao = 700 + 5 * LARGURA // 1920
    elif posição >= -920 * LARGURA // 1920:
        posição_chao = 705 + 5 * LARGURA // 1920
    elif posição >= -930 * LARGURA // 1920:
        posição_chao = 710 + 5 * LARGURA // 1920
    elif posição >= -940 * LARGURA // 1920:
        posição_chao = 720 + 5 * LARGURA // 1920
    elif posição >= -950 * LARGURA // 1920:
        posição_chao = 730 + 5 * LARGURA // 1920
    elif posição >= -960 * LARGURA // 1920:
        posição_chao = 735 + 5 * LARGURA // 1920
    elif posição >= -970 * LARGURA // 1920:
        posição_chao = 738 + 5 * LARGURA // 1920
    elif posição >= -980 * LARGURA // 1920:
        posição_chao = 735 + 5 * LARGURA // 1920
    elif posição >= -1120 * LARGURA // 1920:
        posição_chao = 730 + 5 * LARGURA // 1920
    elif posição >= -1130 * LARGURA // 1920:
        posição_chao = 725 + 5 * LARGURA // 1920
    elif posição >= -1140 * LARGURA // 1920:
        posição_chao = 720 + 5 * LARGURA // 1920
    elif posição >= -1150 * LARGURA // 1920:
        posição_chao = 715 + 5 * LARGURA // 1920
    elif posição >= -1160 * LARGURA // 1920:
        posição_chao = 710 + 5 * LARGURA // 1920
    elif posição >= -1310 * LARGURA // 1920:
        posição_chao = 705 + 5 * LARGURA // 1920
    elif posição >= -1320 * LARGURA // 1920:
        posição_chao = 700 + 5 * LARGURA // 1920
    elif posição >= -1330 * LARGURA // 1920:
        posição_chao = 695 + 5 * LARGURA // 1920
    elif posição >= -1340 * LARGURA // 1920:
        posição_chao = 690 + 5 * LARGURA // 1920
    elif posição >= -1350 * LARGURA // 1920:
        posição_chao = 684 + 5 * LARGURA // 1920
    elif posição >= -1600 * LARGURA // 1920:
        posição_chao = 680 + 5 * LARGURA // 1920
    elif posição >= -1620 * LARGURA // 1920:
        posição_chao = 676 + 5 * LARGURA // 1920
    elif posição >= -1640 * LARGURA // 1920:
        posição_chao = 672 + 5 * LARGURA // 1920
    elif posição >= -1660 * LARGURA // 1920:
        posição_chao = 668 + 5 * LARGURA // 1920
    elif posição >= -1680 * LARGURA // 1920:
        posição_chao = 666 + 5 * LARGURA // 1920
    elif posição >= -1700 * LARGURA // 1920:
        posição_chao = 664 + 5 * LARGURA // 1920
    elif posição >= -1720 * LARGURA // 1920:
        posição_chao = 662 + 5 * LARGURA // 1920
    elif posição >= -1740 * LARGURA // 1920:
        posição_chao = 660 + 5 * LARGURA // 1920
    elif posição >= -1760 * LARGURA // 1920:
        posição_chao = 658 + 5 * LARGURA // 1920
    elif posição >= -1780 * LARGURA // 1920:
        posição_chao = 656 + 5 * LARGURA // 1920
    elif posição >= -1920 * LARGURA // 1920:
        posição_chao = 653 + 5 * LARGURA // 1920
    elif posição >= -1930 * LARGURA // 1920:
        posição_chao = 659 + 5 * LARGURA // 1920
    elif posição >= -1940 * LARGURA // 1920:
        posição_chao = 663 + 5 * LARGURA // 1920
    elif posição >= -1950 * LARGURA // 1920:
        posição_chao = 667 + 5 * LARGURA // 1920
    elif posição >= -1960 * LARGURA // 1920:
        posição_chao = 669 + 5 * LARGURA // 1920
    elif posição >= -1970 * LARGURA // 1920:
        posição_chao = 672 + 5 * LARGURA // 1920
    elif posição >= -1980 * LARGURA // 1920:
        posição_chao = 677 + 5 * LARGURA // 1920
    elif posição >= -1990 * LARGURA // 1920:
        posição_chao = 681 + 5 * LARGURA // 1920
    elif posição >= -2000 * LARGURA // 1920:
        posição_chao = 685 + 5 * LARGURA // 1920
    elif posição >= -2010 * LARGURA // 1920:
        posição_chao = 693 + 5 * LARGURA // 1920
    elif posição >= -2020 * LARGURA // 1920:
        posição_chao = 705 + 5 * LARGURA // 1920
    elif posição >= -2030 * LARGURA // 1920:
        posição_chao = 715 + 5 * LARGURA // 1920
    elif posição >= -2100 * LARGURA // 1920:
        posição_chao = 723 + 5 * LARGURA // 1920
    elif posição >= -2120 * LARGURA // 1920:
        posição_chao = 730 + 5 * LARGURA // 1920
    elif posição >= -2140 * LARGURA // 1920:
        posição_chao = 734 + 5 * LARGURA // 1920
    elif posição >= -2160 * LARGURA // 1920:
        posição_chao = 738 + 5 * LARGURA // 1920
    elif posição >= -2170 * LARGURA // 1920:
        posição_chao = 742 + 5 * LARGURA // 1920
    elif posição >= -2180 * LARGURA // 1920:
        posição_chao = 748 + 5 * LARGURA // 1920
    elif posição >= -2190 * LARGURA // 1920:
        posição_chao = 752 + 5 * LARGURA // 1920
    elif posição >= -2210 * LARGURA // 1920:
        posição_chao = 748 + 5 * LARGURA // 1920
    elif posição >= -2320 * LARGURA // 1920:
        posição_chao = 752 + 5 * LARGURA // 1920
        if posição <= -2320 * LARGURA // 1920:
            parede = True
        else:
            parede = False
    elif posição >= -2460 * LARGURA // 1920:
        posição_chao = 690 + 5 * LARGURA // 1920
    elif posição >= -2520 * LARGURA // 1920:
        posição_chao = 685 + 5 * LARGURA // 1920
    elif posição >= -2550 * LARGURA // 1920:
        posição_chao = 690 + 5 * LARGURA // 1920
    elif posição >= -2570 * LARGURA // 1920:
        posição_chao = 685 + 5 * LARGURA // 1920
    elif posição >= -2600 * LARGURA // 1920:
        posição_chao = 680 + 5 * LARGURA // 1920
    elif posição >= -2620 * LARGURA // 1920:
        posição_chao = 675 + 5 * LARGURA // 1920
    elif posição >= -2640 * LARGURA // 1920:
        posição_chao = 672 + 5 * LARGURA // 1920
    elif posição >= -2750 * LARGURA // 1920:
        posição_chao = 670 + 5 * LARGURA // 1920
    elif posição >= -2760 * LARGURA // 1920:
        posição_chao = 673 + 5 * LARGURA // 1920
    elif posição >= -2770 * LARGURA // 1920:
        posição_chao = 676 + 5 * LARGURA // 1920
    elif posição >= -2780 * LARGURA // 1920:
        posição_chao = 680 + 5 * LARGURA // 1920
    elif posição >= -2790 * LARGURA // 1920:
        posição_chao = 683 + 5 * LARGURA // 1920
    elif posição >= -2800 * LARGURA // 1920:
        posição_chao = 686 + 5 * LARGURA // 1920
    elif posição >= -2810 * LARGURA // 1920:
        posição_chao = 689 + 5 * LARGURA // 1920
    elif posição >= -2820 * LARGURA // 1920:
        posição_chao = 694 + 5 * LARGURA // 1920
    elif posição >= -2830 * LARGURA // 1920:
        posição_chao = 700 + 5 * LARGURA // 1920
    elif posição >= -2840 * LARGURA // 1920:
        posição_chao = 705 + 5 * LARGURA // 1920
    elif posição >= -2850 * LARGURA // 1920:
        posição_chao = 710 + 5 * LARGURA // 1920
    elif posição >= -2860 * LARGURA // 1920:
        posição_chao = 720 + 5 * LARGURA // 1920
    elif posição >= -2870 * LARGURA // 1920:
        posição_chao = 730 + 5 * LARGURA // 1920
    elif posição >= -2880 * LARGURA // 1920:
        posição_chao = 735 + 5 * LARGURA // 1920
    elif posição >= -2890 * LARGURA // 1920:
        posição_chao = 738 + 5 * LARGURA // 1920
    elif posição >= -2900 * LARGURA // 1920:
        posição_chao = 735 + 5 * LARGURA // 1920
    elif posição >= -3040 * LARGURA // 1920:
        posição_chao = 730 + 5 * LARGURA // 1920
    elif posição >= -3050 * LARGURA // 1920:
        posição_chao = 725 + 5 * LARGURA // 1920
    elif posição >= -3060 * LARGURA // 1920:
        posição_chao = 720 + 5 * LARGURA // 1920
    elif posição >= -3070 * LARGURA // 1920:
        posição_chao = 715 + 5 * LARGURA // 1920
    elif posição >= -3080 * LARGURA // 1920:
        posição_chao = 710 + 5 * LARGURA // 1920
    elif posição >= -3230 * LARGURA // 1920:
        posição_chao = 705 + 5 * LARGURA // 1920
    elif posição >= -3240 * LARGURA // 1920:
        posição_chao = 700 + 5 * LARGURA // 1920
    elif posição >= -3250 * LARGURA // 1920:
        posição_chao = 695 + 5 * LARGURA // 1920
    elif posição >= -3260 * LARGURA // 1920:
        posição_chao = 690 + 5 * LARGURA // 1920
    elif posição >= -3270 * LARGURA // 1920:
        posição_chao = 684 + 5 * LARGURA // 1920
    elif posição >= -3520 * LARGURA // 1920:
        posição_chao = 680 + 5 * LARGURA // 1920
    elif posição >= -5460 * LARGURA // 1920:
        posição_chao = 676 + 5 * LARGURA // 1920
    elif posição >= -5480 * LARGURA // 1920:
        posição_chao = 672 + 5 * LARGURA // 1920
    elif posição >= -5500 * LARGURA // 1920:
        posição_chao = 668 + 5 * LARGURA // 1920
    elif posição >= -5520 * LARGURA // 1920:
        posição_chao = 666 + 5 * LARGURA // 1920
    elif posição >= -5540 * LARGURA // 1920:
        posição_chao = 664 + 5 * LARGURA // 1920
    elif posição >= -5560 * LARGURA // 1920:
        posição_chao = 662 + 5 * LARGURA // 1920
    elif posição >= -5580 * LARGURA // 1920:
        posição_chao = 660 + 5 * LARGURA // 1920
    elif posição >= -5600 * LARGURA // 1920:
        posição_chao = 658 + 5 * LARGURA // 1920
    elif posição >= -5620 * LARGURA // 1920:
        posição_chao = 656 + 5 * LARGURA // 1920
    elif posição >= -5760 * LARGURA // 1920:
        posição_chao = 653 + 5 * LARGURA // 1920
    elif posição >= -5770 * LARGURA // 1920:
        posição_chao = 659 + 5 * LARGURA // 1920
    elif posição >= -5780 * LARGURA // 1920:
        posição_chao = 663 + 5 * LARGURA // 1920
    elif posição >= -5790 * LARGURA // 1920:
        posição_chao = 667 + 5 * LARGURA // 1920
    elif posição >= -5800 * LARGURA // 1920:
        posição_chao = 669 + 5 * LARGURA // 1920
    elif posição >= -5810 * LARGURA // 1920:
        posição_chao = 672 + 5 * LARGURA // 1920
    elif posição >= -5820 * LARGURA // 1920:
        posição_chao = 677 + 5 * LARGURA // 1920
    elif posição >= -5830 * LARGURA // 1920:
        posição_chao = 681 + 5 * LARGURA // 1920
    elif posição >= -5840 * LARGURA // 1920:
        posição_chao = 685 + 5 * LARGURA // 1920
    elif posição >= -5850 * LARGURA // 1920:
        posição_chao = 693 + 5 * LARGURA // 1920
    elif posição >= -5860 * LARGURA // 1920:
        posição_chao = 705 + 5 * LARGURA // 1920
    elif posição >= -5870 * LARGURA // 1920:
        posição_chao = 715 + 5 * LARGURA // 1920
    elif posição >= -5940 * LARGURA // 1920:
        posição_chao = 723 + 5 * LARGURA // 1920
    elif posição >= -5960 * LARGURA // 1920:
        posição_chao = 730 + 5 * LARGURA // 1920
    elif posição >= -5980 * LARGURA // 1920:
        posição_chao = 734 + 5 * LARGURA // 1920
    elif posição >= -6000 * LARGURA // 1920:
        posição_chao = 738 + 5 * LARGURA // 1920
    elif posição >= -6010 * LARGURA // 1920:
        posição_chao = 742 + 5 * LARGURA // 1920
    elif posição >= -6020 * LARGURA // 1920:
        posição_chao = 748 + 5 * LARGURA // 1920
    elif posição >= -6030 * LARGURA // 1920:
        posição_chao = 752 + 5 * LARGURA // 1920
    elif posição >= -6050 * LARGURA // 1920:
        posição_chao = 748 + 5 * LARGURA // 1920
    elif posição >= -6160 * LARGURA // 1920:
        posição_chao = 752 + 5 * LARGURA // 1920
        if posição <= -6160 * LARGURA // 1920:
            parede = True
        else:
            parede = False
    elif posição >= -6300 * LARGURA // 1920:
        posição_chao = 690 + 5 * LARGURA // 1920
    elif posição >= -6360 * LARGURA // 1920:
        posição_chao = 685 + 5 * LARGURA // 1920
    elif posição >= -6390 * LARGURA // 1920:
        posição_chao = 690 + 5 * LARGURA // 1920
    elif posição >= -6410 * LARGURA // 1920:
        posição_chao = 685 + 5 * LARGURA // 1920
    elif posição >= -6440 * LARGURA // 1920:
        posição_chao = 680 + 5 * LARGURA // 1920
    elif posição >= -6460 * LARGURA // 1920:
        posição_chao = 675 + 5 * LARGURA // 1920
    elif posição >= -6480 * LARGURA // 1920:
        posição_chao = 672 + 5 * LARGURA // 1920
    elif posição >= -6590 * LARGURA // 1920:
        posição_chao = 670 + 5 * LARGURA // 1920
    elif posição >= -6600 * LARGURA // 1920:
        posição_chao = 673 + 5 * LARGURA // 1920
    elif posição >= -6610 * LARGURA // 1920:
        posição_chao = 676 + 5 * LARGURA // 1920
    elif posição >= -6620 * LARGURA // 1920:
        posição_chao = 680 + 5 * LARGURA // 1920
    elif posição >= -6630 * LARGURA // 1920:
        posição_chao = 683 + 5 * LARGURA // 1920
    elif posição >= -6640 * LARGURA // 1920:
        posição_chao = 686 + 5 * LARGURA // 1920
    elif posição >= -6650 * LARGURA // 1920:
        posição_chao = 689 + 5 * LARGURA // 1920
    elif posição >= -6660 * LARGURA // 1920:
        posição_chao = 694 + 5 * LARGURA // 1920
    elif posição >= -6670 * LARGURA // 1920:
        posição_chao = 700 + 5 * LARGURA // 1920
    elif posição >= -6680 * LARGURA // 1920:
        posição_chao = 705 + 5 * LARGURA // 1920
    elif posição >= -6690 * LARGURA // 1920:
        posição_chao = 710 + 5 * LARGURA // 1920
    elif posição >= -6700 * LARGURA // 1920:
        posição_chao = 720 + 5 * LARGURA // 1920
    elif posição >= -6710 * LARGURA // 1920:
        posição_chao = 730 + 5 * LARGURA // 1920
    elif posição >= -6720 * LARGURA // 1920:
        posição_chao = 735 + 5 * LARGURA // 1920
    elif posição >= -6730 * LARGURA // 1920:
        posição_chao = 738 + 5 * LARGURA // 1920
    elif posição >= -6740 * LARGURA // 1920:
        posição_chao = 735 + 5 * LARGURA // 1920
    elif posição >= -6880 * LARGURA // 1920:
        posição_chao = 730 + 5 * LARGURA // 1920
    elif posição >= -6890 * LARGURA // 1920:
        posição_chao = 725 + 5 * LARGURA // 1920
    elif posição >= -6900 * LARGURA // 1920:
        posição_chao = 720 + 5 * LARGURA // 1920
    elif posição >= -6910 * LARGURA // 1920:
        posição_chao = 715 + 5 * LARGURA // 1920
    elif posição >= -6920 * LARGURA // 1920:
        posição_chao = 710 + 5 * LARGURA // 1920
    elif posição >= -7070 * LARGURA // 1920:
        posição_chao = 705 + 5 * LARGURA // 1920
    elif posição >= -7080 * LARGURA // 1920:
        posição_chao = 700 + 5 * LARGURA // 1920
    elif posição >= -7090 * LARGURA // 1920:
        posição_chao = 695 + 5 * LARGURA // 1920
    elif posição >= -7100 * LARGURA // 1920:
        posição_chao = 690 + 5 * LARGURA // 1920
    elif posição >= -7110 * LARGURA // 1920:
        posição_chao = 684 + 5 * LARGURA // 1920
    elif posição >= -7360 * LARGURA // 1920:
        posição_chao = 680 + 5 * LARGURA // 1920
    elif posição >= -7380 * LARGURA // 1920:
        posição_chao = 676 + 5 * LARGURA // 1920
    elif posição >= -7400 * LARGURA // 1920:
        posição_chao = 672 + 5 * LARGURA // 1920
    elif posição >= -7420 * LARGURA // 1920:
        posição_chao = 668 + 5 * LARGURA // 1920
    elif posição >= -7440 * LARGURA // 1920:
        posição_chao = 666 + 5 * LARGURA // 1920
    elif posição >= -7460 * LARGURA // 1920:
        posição_chao = 664 + 5 * LARGURA // 1920
    elif posição >= -7480 * LARGURA // 1920:
        posição_chao = 662 + 5 * LARGURA // 1920
    elif posição >= -7500 * LARGURA // 1920:
        posição_chao = 660 + 5 * LARGURA // 1920
    elif posição >= -7520 * LARGURA // 1920:
        posição_chao = 658 + 5 * LARGURA // 1920
    elif posição >= -7540 * LARGURA // 1920:
        posição_chao = 656 + 5 * LARGURA // 1920
    elif posição >= -7680 * LARGURA // 1920:
        posição_chao = 653 + 5 * LARGURA // 1920
    elif posição >= -7690 * LARGURA // 1920:
        posição_chao = 659 + 5 * LARGURA // 1920
    elif posição >= -7700 * LARGURA // 1920:
        posição_chao = 663 + 5 * LARGURA // 1920
    elif posição >= -7710 * LARGURA // 1920:
        posição_chao = 667 + 5 * LARGURA // 1920
    elif posição >= -7720 * LARGURA // 1920:
        posição_chao = 669 + 5 * LARGURA // 1920
    elif posição >= -7730 * LARGURA // 1920:
        posição_chao = 672 + 5 * LARGURA // 1920
    elif posição >= -7740 * LARGURA // 1920:
        posição_chao = 677 + 5 * LARGURA // 1920
    elif posição >= -7750 * LARGURA // 1920:
        posição_chao = 681 + 5 * LARGURA // 1920
    elif posição >= -7760 * LARGURA // 1920:
        posição_chao = 685 + 5 * LARGURA // 1920
    elif posição >= -7770 * LARGURA // 1920:
        posição_chao = 693 + 5 * LARGURA // 1920
    elif posição >= -7780 * LARGURA // 1920:
        posição_chao = 705 + 5 * LARGURA // 1920
    elif posição >= -7790 * LARGURA // 1920:
        posição_chao = 715 + 5 * LARGURA // 1920
    elif posição >= -7860 * LARGURA // 1920:
        posição_chao = 723 + 5 * LARGURA // 1920
    elif posição >= -7880 * LARGURA // 1920:
        posição_chao = 730 + 5 * LARGURA // 1920
    elif posição >= -7900 * LARGURA // 1920:
        posição_chao = 734 + 5 * LARGURA // 1920
    elif posição >= -7920 * LARGURA // 1920:
        posição_chao = 738 + 5 * LARGURA // 1920
    elif posição >= -7930 * LARGURA // 1920:
        posição_chao = 742 + 5 * LARGURA // 1920
    elif posição >= -7940 * LARGURA // 1920:
        posição_chao = 748 + 5 * LARGURA // 1920
    elif posição >= -7950 * LARGURA // 1920:
        posição_chao = 752 + 5 * LARGURA // 1920
    elif posição >= -7970 * LARGURA // 1920:
        posição_chao = 748 + 5 * LARGURA // 1920
    elif posição >= -8080 * LARGURA // 1920:
        posição_chao = 752 + 5 * LARGURA // 1920
        if posição <= -8080 * LARGURA // 1920:
            parede = True
        else:
            parede = False
    elif posição >= -8220 * LARGURA // 1920:
        posição_chao = 690 + 5 * LARGURA // 1920
    elif posição >= -8280 * LARGURA // 1920:
        posição_chao = 685 + 5 * LARGURA // 1920
    elif posição >= -8310 * LARGURA // 1920:
        posição_chao = 690 + 5 * LARGURA // 1920
    elif posição >= -8330 * LARGURA // 1920:
        posição_chao = 685 + 5 * LARGURA // 1920
    elif posição >= -8360 * LARGURA // 1920:
        posição_chao = 680 + 5 * LARGURA // 1920
    elif posição >= -8380 * LARGURA // 1920:
        posição_chao = 675 + 5 * LARGURA // 1920
    elif posição >= -8400 * LARGURA // 1920:
        posição_chao = 672 + 5 * LARGURA // 1920
    elif posição >= -8510 * LARGURA // 1920:
        posição_chao = 670 + 5 * LARGURA // 1920
    elif posição >= -8520 * LARGURA // 1920:
        posição_chao = 673 + 5 * LARGURA // 1920
    elif posição >= -8530 * LARGURA // 1920:
        posição_chao = 676 + 5 * LARGURA // 1920
    elif posição >= -8540 * LARGURA // 1920:
        posição_chao = 680 + 5 * LARGURA // 1920
    elif posição >= -8550 * LARGURA // 1920:
        posição_chao = 683 + 5 * LARGURA // 1920
    elif posição >= -8560 * LARGURA // 1920:
        posição_chao = 686 + 5 * LARGURA // 1920
    elif posição >= -8570 * LARGURA // 1920:
        posição_chao = 689 + 5 * LARGURA // 1920
    elif posição >= -8580 * LARGURA // 1920:
        posição_chao = 694 + 5 * LARGURA // 1920
    elif posição >= -8590 * LARGURA // 1920:
        posição_chao = 700 + 5 * LARGURA // 1920
    elif posição >= -8600 * LARGURA // 1920:
        posição_chao = 705 + 5 * LARGURA // 1920
    elif posição >= -8610 * LARGURA // 1920:
        posição_chao = 710 + 5 * LARGURA // 1920
    elif posição >= -8620 * LARGURA // 1920:
        posição_chao = 720 + 5 * LARGURA // 1920
    elif posição >= -8630 * LARGURA // 1920:
        posição_chao = 730 + 5 * LARGURA // 1920
    elif posição >= -8640 * LARGURA // 1920:
        posição_chao = 735 + 5 * LARGURA // 1920
    elif posição >= -8650 * LARGURA // 1920:
        posição_chao = 738 + 5 * LARGURA // 1920
    elif posição >= -8660 * LARGURA // 1920:
        posição_chao = 735 + 5 * LARGURA // 1920
    elif posição >= -8800 * LARGURA // 1920:
        posição_chao = 730 + 5 * LARGURA // 1920
    elif posição >= -8810 * LARGURA // 1920:
        posição_chao = 725 + 5 * LARGURA // 1920
    elif posição >= -8820 * LARGURA // 1920:
        posição_chao = 720 + 5 * LARGURA // 1920
    elif posição >= -8830 * LARGURA // 1920:
        posição_chao = 715 + 5 * LARGURA // 1920
    elif posição >= -8840 * LARGURA // 1920:
        posição_chao = 710 + 5 * LARGURA // 1920
    elif posição >= -8990 * LARGURA // 1920:
        posição_chao = 705 + 5 * LARGURA // 1920
    elif posição >= -9000 * LARGURA // 1920:
        posição_chao = 700 + 5 * LARGURA // 1920
    elif posição >= -9010 * LARGURA // 1920:
        posição_chao = 695 + 5 * LARGURA // 1920
    elif posição >= -9020 * LARGURA // 1920:
        posição_chao = 690 + 5 * LARGURA // 1920
    elif posição >= -9030 * LARGURA // 1920:
        posição_chao = 684 + 5 * LARGURA // 1920
    elif posição >= -9280 * LARGURA // 1920:
        posição_chao = 680 + 5 * LARGURA // 1920
    elif posição >= -9300 * LARGURA // 1920:
        posição_chao = 676 + 5 * LARGURA // 1920
    elif posição >= -9320 * LARGURA // 1920:
        posição_chao = 672 + 5 * LARGURA // 1920
    elif posição >= -9340 * LARGURA // 1920:
        posição_chao = 668 + 5 * LARGURA // 1920
    elif posição >= -9360 * LARGURA // 1920:
        posição_chao = 666 + 5 * LARGURA // 1920
    elif posição >= -9380 * LARGURA // 1920:
        posição_chao = 664 + 5 * LARGURA // 1920
    elif posição >= -9400 * LARGURA // 1920:
        posição_chao = 662 + 5 * LARGURA // 1920
    elif posição >= -9420 * LARGURA // 1920:
        posição_chao = 660 + 5 * LARGURA // 1920
    elif posição >= -9440 * LARGURA // 1920:
        posição_chao = 658 + 5 * LARGURA // 1920
    elif posição >= -9460 * LARGURA // 1920:
        posição_chao = 656 + 5 * LARGURA // 1920
    elif posição >= -9500 * LARGURA // 1920:
        posição_chao = 653 + 5 * LARGURA // 1920
    elif posição >= -9510 * LARGURA // 1920:
        posição_chao = 659 + 5 * LARGURA // 1920
    elif posição >= -9520 * LARGURA // 1920:
        posição_chao = 663 + 5 * LARGURA // 1920
    elif posição >= -9530 * LARGURA // 1920:
        posição_chao = 667 + 5 * LARGURA // 1920
    elif posição >= -9540 * LARGURA // 1920:
        posição_chao = 669 + 5 * LARGURA // 1920
    elif posição >= -9550 * LARGURA // 1920:
        posição_chao = 672 + 5 * LARGURA // 1920
    elif posição >= -9560 * LARGURA // 1920:
        posição_chao = 677 + 5 * LARGURA // 1920
    elif posição >= -9570 * LARGURA // 1920:
        posição_chao = 681 + 5 * LARGURA // 1920
    elif posição >= -9580 * LARGURA // 1920:
        posição_chao = 685 + 5 * LARGURA // 1920
    elif posição >= -9590 * LARGURA // 1920:
        posição_chao = 693 + 5 * LARGURA // 1920
    elif posição >= -9600 * LARGURA // 1920:
        posição_chao = 705 + 5 * LARGURA // 1920

    elif posição_personagem_X <= 510 * LARGURA // 1920:
        posição_chao = 684 + 5 * LARGURA // 1920
    elif posição_personagem_X <= 520 * LARGURA // 1920:
        posição_chao = 680 + 5 * LARGURA // 1920
    elif posição_personagem_X <= 530 * LARGURA // 1920:
        posição_chao = 676 + 5 * LARGURA // 1920
    elif posição_personagem_X <= 540:
        posição_chao = 672 + 5 * LARGURA // 1920
    elif posição_personagem_X <= 550 * LARGURA // 1920:
        posição_chao = 668 + 5 * LARGURA // 1920
    elif posição_personagem_X <= 560 * LARGURA // 1920:
        posição_chao = 666 + 5 * LARGURA // 1920
    elif posição_personagem_X <= 570 * LARGURA // 1920:
        posição_chao = 664 + 5 * LARGURA // 1920
    elif posição_personagem_X <= 580 * LARGURA // 1920:
        posição_chao = 662 + 5 * LARGURA // 1920
    elif posição_personagem_X <= 590 * LARGURA // 1920:
        posição_chao = 660 + 5 * LARGURA // 1920
    elif posição_personagem_X <= 600 * LARGURA // 1920:
        posição_chao = 658 + 5 * LARGURA // 1920
    elif posição_personagem_X <= 610 * LARGURA // 1920:
        posição_chao = 656 + 5 * LARGURA // 1920
    elif posição_personagem_X < 680 * LARGURA // 1920:
        posição_chao = 653 + 5 * LARGURA // 1920


    return posição_chao

posições_chao = list(range(0, -LARGURA * 5, -10 * LARGURA // 1920))
print(len(posições_chao) // 5)


if __name__ == "__main__":
    screen = pygame.display.set_mode((LARGURA, ALTURA), pygame.FULLSCREEN)
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            # Caixas de texto
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                for box in input_boxes:
                    box["active"] = box["rect"].collidepoint(evento.pos)

            elif evento.type == pygame.KEYDOWN:
                mods = evento.mod
                for box in input_boxes:
                    if box["active"]:
                        
                        if evento.key == pygame.K_BACKSPACE:
                            box["text"] = box["text"][:-1]
                        elif evento.key == pygame.K_RETURN:
                            box["active"] = False
                        else:
                            box["text"] = ""
                            if evento.unicode in box["peritido"]:
                                box["text"] += evento.unicode
                            if mods & pygame.KMOD_ALT:
                                box["text"] = "Lalt"
                            if mods & pygame.KMOD_CAPS:
                                box["text"] = "Caps"
                            if mods & pygame.KMOD_CTRL:
                                box["text"] = "Lctrl"
                            if mods & pygame.KMOD_SHIFT:
                                box["text"] = "Lshift"
                            if evento.key == pygame.K_TAB:
                                box["text"] = "Tab"

        key = pygame.key.get_pressed()

        pygame.draw.ellipse(sombra, (0, 0, 0, tranparencia), sombra.get_rect())

        
        tecla = [teclas["inventario"].lower(), teclas["correr"].lower(), teclas["habilidade"].lower(), teclas["habilidade_1"].lower(), teclas["habilidade_2"].lower(), teclas["mapa"].lower()]
        for nome_tecla in tecla:
            if nome_tecla == "caps":
                tecla[tecla.index(nome_tecla)] = "CAPSLOCK"
            if nome_tecla == "lctrl" or nome_tecla == "lalt" or nome_tecla == "lshift" or nome_tecla == "tab":
                tecla[tecla.index(nome_tecla)] = nome_tecla.upper()
                
                    

        inventario = getattr(pygame, f"K_{tecla[0]}")
        correr = getattr(pygame, f"K_{tecla[1]}")
        habilidade = getattr(pygame, f"K_{tecla[2]}")
        habilidade_1 = getattr(pygame, f"K_{tecla[3]}")
        habilidade_2 = getattr(pygame, f"K_{tecla[4]}")
        mapa = getattr(pygame, f"K_{tecla[5]}")

        posição_chao = colisao_chao_batalha()


        if  parede and colisao_chao:
            travar = True
        elif not colisao_chao or posição > -400 * LARGURA // 1920 or key[pygame.K_SPACE]:
            parede = False


        
        if not parede:
            travar = False



        if estado == JOGO:
            anterior = JOGO
            dados_do_alvo_recebidos = False
            screen.fill((210, 210, 210))
            if key[pygame.K_ESCAPE] and not click:
                click = True
                contador = 0
                estado = OPCOES
            if not key[pygame.K_ESCAPE]:
                click = False
            if key[inventario] and not click_e:
                click_e = True
                contador = 0
                estado = INVENTARIO
            if not key[inventario]:
                click_e = False

        if estado == COMBATE:
            anterior = COMBATE
            screen.blit(cenario_combate, (posição, 0))

            if posição - 1 >= -LARGURA * 2  and posição_personagem_X >= 500 * LARGURA // 1920 and not travar:
                if key[pygame.K_d]:
                    posição -= 8 * LARGURA // 1920
                    diresao = "direita"
            else:
                if -posição_personagem_X >= -LARGURA + 150 and not travar:
                    if key[pygame.K_d]:
                        posição_personagem_X += 8 * LARGURA // 1920
                        diresao = "direita"
                else:
                    diresao = "parado"


                
            if posição <= -20 * LARGURA // 1920 and posição_personagem_X <= 500 * LARGURA // 1920:
                if key[pygame.K_a]:
                    posição += 8 * LARGURA // 1920
                    diresao = "esquerda"

            else:
                if posição_personagem_X >= -21 * LARGURA // 1920:
                    if key[pygame.K_a]:
                        posição_personagem_X -= 8 * LARGURA // 1920
                        diresao = "esquerda"
                else:
                    diresao = "parado"

            if key[pygame.K_SPACE] and colisao_chao and limite_de_pulo > qnt_de_pulo:
                qnt_de_pulo += 1
                pulo_detectado = True
                vel_y = forca_pulo
                sombra.set_alpha(tranparencia - (qnt_de_pulo * 25))
                
                if qnt_de_pulo == limite_de_pulo:
                    colisao_chao = False



               
            vel_y += gravidade
            posição_personagem_Y += vel_y
            if posição_personagem_Y + 200 * LARGURA // 1920 >= posição_chao - 10 * LARGURA // 1920:
                sombra.set_alpha(tranparencia - (qnt_de_pulo * 10))

            if posição_personagem_Y + 200 * LARGURA // 1920 >= posição_chao - 20 * LARGURA // 1920:
                sombra.set_alpha(tranparencia - (qnt_de_pulo * 5))

            if posição_personagem_Y + 200 * LARGURA // 1920 >= posição_chao:
                sombra.set_alpha(tranparencia)
                pulo_detectado = False
                posição_personagem_Y = posição_chao - 200 * LARGURA // 1920
                vel_y = 0
                colisao_chao = True
                qnt_de_pulo = 0


            
            if not key[pygame.K_a] and not key[pygame.K_d]:
                diresao = "parado"

            if diresao == "parado":
                screen.blit(sombra, (posição_personagem_X + 40 * LARGURA // 1920, posição_chao - 50 * LARGURA // 1920))
                screen.blit(personagem_parado, (posição_personagem_X, posição_personagem_Y))
            else:
                screen.blit(sombra, (posição_personagem_X + 40 * LARGURA // 1920, posição_chao - 50 * LARGURA // 1920))
                screen.blit(personagem_andando_D[frame_personagem], (posição_personagem_X, posição_personagem_Y))
                frame_personagem += 1
                if frame_personagem >= len(personagem_andando_D):
                    frame_personagem = 0
            
            
            
            

            
            if key[pygame.K_ESCAPE] and not click:
                click = True
                contador = 0
                estado = OPCOES
            if not key[pygame.K_ESCAPE]:
                click = False
            if key[habilidade_1]:
                None
                #habilidade_1_usavel(usuario, alvo)
            if key[habilidade_2]:
                None
                #habilidade_2_usavel(usuario, alvo)

            


            



        if estado == OPCOES:
            if key[pygame.K_ESCAPE] and not click:
                click = True
                contador = 0
                estado = anterior
            if not key[pygame.K_ESCAPE]:
                click = False
            if contador == 0:
                quadrado.fill((*(0, 0, 0), 150))
                screen.blit(quadrado, (0, 0))
            contador += 1
            rect_box = pygame.Rect(LARGURA // 3, ALTURA // 6, LARGURA // 3, ALTURA // 1.4)
            pygame.draw.rect(screen, (180, 180, 180), rect_box, border_radius=15)

            if desenhar_botao("Continuar", LARGURA // 2.86, ALTURA // 4.7, LARGURA // 3.3, ALTURA // 8, ALTURA // 18, (150, 150, 150), (120, 120, 120), ALTURA // 30, fonte= ALTURA // 18):
                estado = anterior

            if desenhar_botao("Opçoes", LARGURA // 2.86, ALTURA // 2.2, LARGURA // 3.3, ALTURA // 8, ALTURA // 18, (150, 150, 150), (120, 120, 120), ALTURA // 30, fonte= ALTURA // 18):
                contador = 0
                estado = MENU

            if desenhar_botao("Sair", LARGURA // 2.86, ALTURA // 1.4, LARGURA // 3.3, ALTURA // 8, ALTURA // 18, (150, 150, 150), (120, 120, 120), ALTURA // 30, fonte= ALTURA // 18):
                Popen([sys.executable, rf'{endereço}\lobby.py'])
                sys.exit()

        if estado == MENU:
            if contador == 0:
                quadrado_2.fill((*(0, 0, 0), 150))
                screen.blit(quadrado_2, (0, 0))
            contador += 1
            texto_surface = font_title.render("RPG", True, (190, 190, 230))
            texto_rect = texto_surface.get_rect(center=(LARGURA // 2, ALTURA // 7))
            screen.blit(texto_surface, texto_rect)
            

            if desenhar_botao("<", LARGURA // 18, ALTURA // 13, LARGURA // 14, ALTURA // 8, ALTURA // 19, (140, 140, 140), (110, 110, 110), 75, fonte= ALTURA // 13):
                input_boxes = [
                                {"label": "Inventario", "rect": pygame.Rect(LARGURA // 1.8, ALTURA // 4, LARGURA // 18, ALTURA // 16), "text": f"{dados["keys"]["inventario"]}", "active": False, "peritido": TEXTO_S},
                                {"label": "Correr", "rect": pygame.Rect(LARGURA // 1.8, ALTURA // 4 + ALTURA // 10, LARGURA // 18, ALTURA // 16), "text": f"{dados["keys"]["correr"]}", "active": False, "peritido": TEXTO_S},
                                {"label": "Habilidades", "rect": pygame.Rect(LARGURA // 1.8, ALTURA // 4 + ALTURA // 10 + ALTURA // 10, LARGURA // 18, ALTURA // 16), "text": f"{dados["keys"]["habilidade"]}", "active": False, "peritido": TEXTO_S},
                                {"label": "Habilidade 1", "rect": pygame.Rect(LARGURA // 1.8, ALTURA // 4 + ALTURA // 10 + ALTURA // 10 + ALTURA // 10, LARGURA // 18, ALTURA // 16), "text": f"{dados["keys"]["habilidade_1"]}", "active": False, "peritido": TEXTO_S},
                                {"label": "Habilidade 2", "rect": pygame.Rect(LARGURA // 1.8, ALTURA // 4 + ALTURA // 10 + ALTURA // 10 + ALTURA // 10 + ALTURA // 10, LARGURA // 18, ALTURA // 16), "text": f"{dados["keys"]["habilidade_2"]}", "active": False, "peritido": TEXTO_S},
                                {"label": "Mapa", "rect": pygame.Rect(LARGURA // 1.8, ALTURA // 4 + ALTURA // 10 + ALTURA // 10 + ALTURA // 10 + ALTURA // 10 + ALTURA // 10 + ALTURA // 10, LARGURA // 18, ALTURA // 16), "text": f"{dados["keys"]["mapa"]}", "active": False, "peritido": TEXTO_S},
                            ]
                estado = MENU
            
            rect_box = pygame.Rect(LARGURA // 2.7, ALTURA // 4.5, LARGURA // 3.9, ALTURA // 1.4)
            pygame.draw.rect(screen, (210, 210, 210), rect_box, border_radius=15)
            
            # Verifica se todos os campos estão preenchidos
            todos_preenchidos = all(box["text"] != "" for box in input_boxes)

            # Verifica se houve alguma alteração nas teclas
            alguma_tecla_alterada = (
                input_boxes[0]["text"] != teclas["inventario"] or
                input_boxes[1]["text"] != teclas["correr"] or
                input_boxes[2]["text"] != teclas["habilidade"] or
                input_boxes[3]["text"] != teclas["habilidade_1"] or
                input_boxes[4]["text"] != teclas["habilidade_2"] or
                input_boxes[5]["text"] != teclas["mapa"]
            )

            # Aplica as cores dependendo das condições
            if todos_preenchidos and alguma_tecla_alterada:
                cor_atualizar = (200, 200, 220)
                cor_atualizar_ativo = (180, 180, 200)
            else:
                cor_atualizar = (100, 100, 120)
                cor_atualizar_ativo = (80, 80, 100)


            if desenhar_botao("Salvar", LARGURA // 1.4, ALTURA // 1.35, LARGURA // 4.7, ALTURA // 10, ALTURA // 20, cor_atualizar, cor_atualizar_ativo, ALTURA // 19, fonte= ALTURA // 18):
                if cor_atualizar == (200, 200, 220):
                    teclas["inventario"] = input_boxes[0]["text"]
                    teclas["correr"] = input_boxes[1]["text"]
                    teclas["habilidade"] = input_boxes[2]["text"]
                    teclas["habilidade_1"] = input_boxes[3]["text"]
                    teclas["habilidade_2"] = input_boxes[4]["text"]
                    teclas["mapa"] = input_boxes[5]["text"]
                    salvar(teclas)
                    estado = anterior

            
            for box in input_boxes:
                box["text"] = box["text"].title()
                cor_borda = COR_ATIVA if box["active"] else COR_INATIVA
                pygame.draw.rect(screen, cor_borda, box["rect"], 2, border_radius=15)
                
                # Label
                label_surface = fonte_input.render(box["label"] + ":", True, COR_TEXTO)
                screen.blit(label_surface, (box["rect"].x - LARGURA // 6, box["rect"].y + 5))

                # Texto
                texto_surface = fonte_input.render(box["text"], True, COR_TEXTO)
                screen.blit(texto_surface, (box["rect"].x + 5, box["rect"].y + 5))

        if estado == INVENTARIO:
            if contador == 0:
                quadrado_3.fill((*(0, 0, 0), 150))
                screen.blit(quadrado_3, (0, 0))
            contador += 1
            
            if key[inventario] and not click_e:
                click_e = True
                estado = JOGO
            if not key[inventario]:
                click_e = False

            if key[pygame.K_ESCAPE] and not click:
                click = True
                contador = 0
                estado = JOGO
            if not key[pygame.K_ESCAPE]:
                click = False

            
        pygame.display.flip()
        clock.tick(32)

    pygame.quit()