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
gravidade = 1.5
forca_pulo = -10
pulo_detectado = False
limite_de_pulo = 2
qnt_de_pulo = 0
posição_personagem_X = 500
posição_personagem_Y = 520
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
sombra = pygame.Surface((100, 20), pygame.SRCALPHA)



quadrado = pygame.Surface((LARGURA, ALTURA), pygame.SRCALPHA)
quadrado_2 = pygame.Surface((LARGURA, ALTURA), pygame.SRCALPHA)
quadrado_3 = pygame.Surface((LARGURA, ALTURA), pygame.SRCALPHA)
contador = 0
rect_opcoes = pygame.Rect(LARGURA // 2.5, LARGURA // 1.5, ALTURA // 1.6, ALTURA // 2)
click = False
click_e = False




def colisao_chao_batalha():
    global posição_chao, posição_personagem_X, posição
    if posição_personagem_X <= 200:
        posição_chao = 684
    elif posição_personagem_X <= 220:
        posição_chao = 680
    elif posição_personagem_X <= 240:
        posição_chao = 676
    elif posição_personagem_X <= 260:
        posição_chao = 672
    elif posição_personagem_X <= 280:
        posição_chao = 668
    elif posição_personagem_X <= 300:
        posição_chao = 666
    elif posição_personagem_X <= 320:
        posição_chao = 664
    elif posição_personagem_X <= 340:
        posição_chao = 662
    elif posição_personagem_X <= 360:
        posição_chao = 660
    elif posição_personagem_X <= 380:
        posição_chao = 658
    elif posição_personagem_X <= 400:
        posição_chao = 656
    elif posição_personagem_X < 500:
        posição_chao = 653
    elif posição >= -10:
        posição_chao = 659
    elif posição >= -20:
        posição_chao = 663
    elif posição >= -30:
        posição_chao = 667
    elif posição >= -40:
        posição_chao = 669
    elif posição >= -50:
        posição_chao = 672
    elif posição >= -60:
        posição_chao = 677
    elif posição >= -70:
        posição_chao = 681
    elif posição >= -80:
        posição_chao = 685
    elif posição >= -90:
        posição_chao = 693
    elif posição >= -100:
        posição_chao = 705
    elif posição >= -110:
        posição_chao = 715
    elif posição >= -180:
        posição_chao = 723
    elif posição >= -200:
        posição_chao = 730
    elif posição >= -220:
        posição_chao = 734
    elif posição >= -240:
        posição_chao = 738
    elif posição >= -250:
        posição_chao = 742
    elif posição >= -260:
        posição_chao = 748
    elif posição >= -270:
        posição_chao = 752
    elif posição >= -290:
        posição_chao = 748
    elif posição >= -400:
        posição_chao = 752
    elif posição >= -540:
        posição_chao = 690
    elif posição >= -600:
        posição_chao = 685
    elif posição >= -630:
        posição_chao = 690
    elif posição >= -650:
        posição_chao = 685
    elif posição >= -680:
        posição_chao = 680
    elif posição >= -700:
        posição_chao = 675
    elif posição >= -720:
        posição_chao = 672
    elif posição >= -830:
        posição_chao = 670
    elif posição >= -840:
        posição_chao = 673
    elif posição >= -850:
        posição_chao = 676
    elif posição >= -860:
        posição_chao = 680
    elif posição >= -870:
        posição_chao = 683
    elif posição >= -880:
        posição_chao = 686
    elif posição >= -890:
        posição_chao = 689
    elif posição >= -900:
        posição_chao = 694
    elif posição >= -910:
        posição_chao = 700
    elif posição >= -920:
        posição_chao = 705
    elif posição >= -930:
        posição_chao = 710
    elif posição >= -940:
        posição_chao = 720
    elif posição >= -950:
        posição_chao = 730
    elif posição >= -960:
        posição_chao = 735
    elif posição >= -970:
        posição_chao = 738
    elif posição >= -980:
        posição_chao = 735
    elif posição >= -1120:
        posição_chao = 730
    elif posição >= -1130:
        posição_chao = 725
    elif posição >= -1140:
        posição_chao = 720
    elif posição >= -1150:
        posição_chao = 715
    elif posição >= -1160:
        posição_chao = 710
    elif posição >= -1310:
        posição_chao = 705
    elif posição >= -1320:
        posição_chao = 700
    elif posição >= -1330:
        posição_chao = 695
    elif posição >= -1340:
        posição_chao = 690
    elif posição >= -1350:
        posição_chao = 684
    elif posição >= -1600:
        posição_chao = 680
    elif posição >= -1620:
        posição_chao = 676
    elif posição >= -1640:
        posição_chao = 672
    elif posição >= -1660:
        posição_chao = 668
    elif posição >= -1680:
        posição_chao = 666
    elif posição >= -1700:
        posição_chao = 664
    elif posição >= -1720:
        posição_chao = 662
    elif posição >= -1740:
        posição_chao = 660
    elif posição >= -1760:
        posição_chao = 658
    elif posição >= -1780:
        posição_chao = 656
    elif posição >= -1800:
        posição_chao = 653

    elif posição >= -1810:
        posição_chao = 659
    elif posição >= -1820:
        posição_chao = 663
    elif posição >= -1830:
        posição_chao = 667
    elif posição >= -1840:
        posição_chao = 669
    elif posição >= -1850:
        posição_chao = 672
    elif posição >= -1860:
        posição_chao = 677
    



    return posição_chao

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


        if posição_chao == 752 and posição <= -400 and colisao_chao:
            travar = True
        elif not colisao_chao or posição > -400 or key[pygame.K_SPACE]:
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

            if posição - 1 >= -LARGURA * 2  and posição_personagem_X >= 500 and not travar:
                if key[pygame.K_d]:
                    posição -= 10
                    diresao = "direita"
            else:
                if -posição_personagem_X >= -LARGURA + 150 and not travar:
                    if key[pygame.K_d]:
                        posição_personagem_X += 10
                        diresao = "direita"
                else:
                    diresao = "parado"


                
            if posição <= -20 and posição_personagem_X <= 500:
                if key[pygame.K_a]:
                    posição += 10
                    diresao = "esquerda"

            else:
                if posição_personagem_X >= -21:
                    if key[pygame.K_a]:
                        posição_personagem_X -= 10
                        diresao = "esquerda"
                else:
                    diresao = "parado"

            if key[pygame.K_SPACE] and colisao_chao:
                qnt_de_pulo += 0.5
                pulo_detectado = True
                vel_y = forca_pulo
                sombra.set_alpha(tranparencia - (qnt_de_pulo * 25))
                travar = False
                
                if qnt_de_pulo == limite_de_pulo:
                    colisao_chao = False



               
            vel_y += gravidade
            posição_personagem_Y += vel_y
            if posição_personagem_Y + 200 >= posição_chao - 10:
                sombra.set_alpha(tranparencia - (qnt_de_pulo * 10))

            if posição_personagem_Y + 200 >= posição_chao - 20:
                sombra.set_alpha(tranparencia - (qnt_de_pulo * 5))

            if posição_personagem_Y + 200 >= posição_chao:
                sombra.set_alpha(tranparencia)
                pulo_detectado = False
                posição_personagem_Y = posição_chao - 200
                vel_y = 0
                colisao_chao = True
                qnt_de_pulo = 0


            
            if not key[pygame.K_a] and not key[pygame.K_d]:
                diresao = "parado"

            if diresao == "parado":
                screen.blit(sombra, (posição_personagem_X + 40, posição_chao - 50))
                screen.blit(personagem_parado, (posição_personagem_X, posição_personagem_Y))
            else:
                screen.blit(sombra, (posição_personagem_X + 40, posição_chao - 50))
                screen.blit(personagem_andando_D[frame_personagem], (posição_personagem_X, posição_personagem_Y))
                frame_personagem += 1
                if frame_personagem >= len(personagem_andando_D):
                    frame_personagem = 0
            
            
            if dados["progresso"]["capitulo"] == 1 and "missao" == 0 and not dados_do_alvo_recebidos:
                alvo = {"dano": 0,
                        "nome": 0,
                        "vida": 0,
                        "defesa": 0,
                        "velocidade": 0}
                dados_do_alvo_recebidos = True
            elif dados["progresso"]["capitulo"] == 1 and "missao" == 1 and not dados_do_alvo_recebidos:
                alvo = {"dano": 0,
                        "nome": 0,
                        "vida": 0,
                        "defesa": 0,
                        "velocidade": 0}
                dados_do_alvo_recebidos = True
            elif dados["progresso"]["capitulo"] == 1 and "missao" == 2 and not dados_do_alvo_recebidos:
                alvo = {"dano": 0,
                        "nome": 0,
                        "vida": 0,
                        "defesa": 0,
                        "velocidade": 0}
                dados_do_alvo_recebidos = True
            elif dados["progresso"]["capitulo"] == 1 and "missao" == 3 and not dados_do_alvo_recebidos:
                alvo = {"dano": 0,
                        "nome": 0,
                        "vida": 0,
                        "defesa": 0,
                        "velocidade": 0}
                dados_do_alvo_recebidos = True
            elif dados["progresso"]["capitulo"] == 1 and "missao" == 4 and not dados_do_alvo_recebidos:
                alvo = {"dano": 0,
                        "nome": 0,
                        "vida": 0,
                        "defesa": 0,
                        "velocidade": 0}
                dados_do_alvo_recebidos = True
            elif dados["progresso"]["capitulo"] == 1 and "missao" == 5 and not dados_do_alvo_recebidos:
                alvo = {"dano": 0,
                        "nome": 0,
                        "vida": 0,
                        "defesa": 0,
                        "velocidade": 0}
                dados_do_alvo_recebidos = True
            elif dados["progresso"]["capitulo"] == 1 and "missao" == 6 and not dados_do_alvo_recebidos:
                alvo = {"dano": 0,
                        "nome": 0,
                        "vida": 0,
                        "defesa": 0,
                        "velocidade": 0}
                dados_do_alvo_recebidos = True
            elif dados["progresso"]["capitulo"] == 1 and "missao" == 7 and not dados_do_alvo_recebidos:
                alvo = {"dano": 0,
                        "nome": 0,
                        "vida": 0,
                        "defesa": 0,
                        "velocidade": 0}
                dados_do_alvo_recebidos = True
            elif dados["progresso"]["capitulo"] == 1 and "missao" == 8 and not dados_do_alvo_recebidos:
                alvo = {"dano": 0,
                        "nome": 0,
                        "vida": 0,
                        "defesa": 0,
                        "velocidade": 0}
                dados_do_alvo_recebidos = True
            elif dados["progresso"]["capitulo"] == 1 and "missao" == 0 and not dados_do_alvo_recebidos:
                alvo = {"dano": 0,
                        "nome": 0,
                        "vida": 0,
                        "defesa": 0,
                        "velocidade": 0}
                dados_do_alvo_recebidos = True
            elif dados["progresso"]["capitulo"] == 1 and "missao" == 0 and not dados_do_alvo_recebidos:
                alvo = {"dano": 0,
                        "nome": 0,
                        "vida": 0,
                        "defesa": 0,
                        "velocidade": 0}
                dados_do_alvo_recebidos = True
            elif dados["progresso"]["capitulo"] == 1 and "missao" == 0 and not dados_do_alvo_recebidos:
                alvo = {"dano": 0,
                        "nome": 0,
                        "vida": 0,
                        "defesa": 0,
                        "velocidade": 0}
                dados_do_alvo_recebidos = True
            elif dados["progresso"]["capitulo"] == 1 and "missao" == 0 and not dados_do_alvo_recebidos:
                alvo = {"dano": 0,
                        "nome": 0,
                        "vida": 0,
                        "defesa": 0,
                        "velocidade": 0}
                dados_do_alvo_recebidos = True
            elif dados["progresso"]["capitulo"] == 1 and "missao" == 0 and not dados_do_alvo_recebidos:
                alvo = {"dano": 0,
                        "nome": 0,
                        "vida": 0,
                        "defesa": 0,
                        "velocidade": 0}
                dados_do_alvo_recebidos = True
            elif dados["progresso"]["capitulo"] == 1 and "missao" == 0 and not dados_do_alvo_recebidos:
                alvo = {"dano": 0,
                        "nome": 0,
                        "vida": 0,
                        "defesa": 0,
                        "velocidade": 0}
                dados_do_alvo_recebidos = True
            elif dados["progresso"]["capitulo"] == 1 and "missao" == 0 and not dados_do_alvo_recebidos:
                alvo = {"dano": 0,
                        "nome": 0,
                        "vida": 0,
                        "defesa": 0,
                        "velocidade": 0}
                dados_do_alvo_recebidos = True
            elif dados["progresso"]["capitulo"] == 1 and "missao" == 0 and not dados_do_alvo_recebidos:
                alvo = {"dano": 0,
                        "nome": 0,
                        "vida": 0,
                        "defesa": 0,
                        "velocidade": 0}
                dados_do_alvo_recebidos = True
            elif dados["progresso"]["capitulo"] == 1 and "missao" == 0 and not dados_do_alvo_recebidos:
                alvo = {"dano": 0,
                        "nome": 0,
                        "vida": 0,
                        "defesa": 0,
                        "velocidade": 0}
                dados_do_alvo_recebidos = True
            elif dados["progresso"]["capitulo"] == 1 and "missao" == 0 and not dados_do_alvo_recebidos:
                alvo = {"dano": 0,
                        "nome": 0,
                        "vida": 0,
                        "defesa": 0,
                        "velocidade": 0}
                dados_do_alvo_recebidos = True
            

            
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
        clock.tick(16)

    pygame.quit()