import pygame
import sys
import os
from random import choice
from ui.menus import desenhar_botao, TEXTO_S, COR_TEXTO, COR_INATIVA, COR_ATIVA
from ui.lobby import input_boxes, salvar, fonte_input, font_title
from recursos.imagens.missao.missao1.slime import slime_parado, slime_direita
import sqlite3
import pyautogui
from subprocess import Popen
import json
from recursos.imagens.personagem_principal import personagem_parado, personagem_andando_D, personagem_soco_d, personagem_morto, personagem_dano
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from backend.entidades.inimigos import inimigo
from backend.entidades.jogador import jogador
#from backend.app.models.sistema.habilidades_ativa_combatentes import golpe_mortal, intangibilidade, impacto_cruzado, bloqueio_de_espada, ataque_com_escudo, defesa_reforcada, giro_de_lanca, arremesso_de_lanca, disparo_perfurante, camuflagem, ataque_surpresa, fuga_rapida
#from backend.app.models.sistema.habilidades_passivas_combatentes import furtividade, evasao, sangramento, vontade_da_espada, heranca_da_espada, ataque_rapido, bloqueio_de_ataque, repelir, peso_pena, danca_da_lanca, controle_passivo, controle_total, disparo_preciso, passos_silenciosos, flecha_dupla, ataque_silencioso, evasao_rapida, exploracao_furtiva
LARGURA, ALTURA = pyautogui.size()
endereço = os.path.dirname(os.path.abspath(__file__))



font_vida = pygame.font.Font(rf"{endereço}\recursos\fontes\Minha fonte.ttf", 30)

with open(rf"{endereço}\ui\usuario.json", "r") as arquivo:
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
frame_personagem_soco = 0
frame_personagem_parado = 0
frame_personagem_dano = 0
estado_personagem = personagem_parado
diresao = "parado"
cooldown_dano = 5
contador_cooldown = 0
cooldown_jogador = 20
contador_cooldown_jogador = 0
diresao_adiversario = "parado"
frame_inimigo_parado = 0
frame_inimigo_direita = 0
frame_inimigo_esquerda = 0
dados_obtidos = False
andar_inimigo = True
morto = False
frame_morto = 0
time_morrer = 0


if __name__ == "__main__":
    if not os.path.exists(rf"{endereço}\ui\usuario.json"):
        Popen([sys.executable, rf'{endereço}\ui\menus.py'])
        sys.exit()

endereco_banco_de_dados = rf"{endereço}\ui\banco_de_dados.db"

cenario_combate = pygame.image.load(rf"{endereço}\recursos\imagens\cenario\cenario_combate.png")
cenario_combate = pygame.transform.scale(cenario_combate, (LARGURA * 5, ALTURA))

game_over = pygame.image.load(rf"{endereço}\recursos\imagens\finais\game over.png")


# cores
cor_normal = (200, 200, 200)
cor_dano = (190, 80, 80)
cor_normal_adiversario = (200, 200, 200)
cor_dano_adiversario = (190, 80, 80)
cor_usada_adiversario = cor_normal_adiversario
cor_usada = cor_normal



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

usuario = jogador

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
quadrado_4 = pygame.Surface((LARGURA, ALTURA), pygame.SRCALPHA)
quadrado_5 = pygame.Surface((100, 15), pygame.SRCALPHA)
contador = 0
rect_opcoes = pygame.Rect(LARGURA // 2.5, LARGURA // 1.5, ALTURA // 1.6, ALTURA // 2)
click = False
click_e = False





dano_ficticio = 13
vida_ficticia = 120
vida_ficticia_atual = vida_ficticia



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
        botoes = pygame.mouse.get_pressed()

        pygame.draw.ellipse(sombra, (0, 0, 0, tranparencia), sombra.get_rect())

        

        teclas = dados["keys"]
        
        tecla = [teclas["inventario"].lower(), teclas["correr"].lower(), teclas["habilidade"].lower(), teclas["habilidade_1"].lower(), teclas["habilidade_2"].lower(), teclas["mapa"].lower()]
        for nome_tecla in tecla:
            if nome_tecla == "caps":
                tecla[tecla.index(nome_tecla)] = "CAPSLOCK"
            if nome_tecla == "lctrl" or nome_tecla == "lalt" or nome_tecla == "lshift" or nome_tecla == "tab":
                tecla[tecla.index(nome_tecla)] = nome_tecla.upper()


        game_over = pygame.transform.scale(game_over, (LARGURA - 400, ALTURA - 350))

        inventario = getattr(pygame, f"K_{tecla[0]}")
        correr = getattr(pygame, f"K_{tecla[1]}")
        habilidade = getattr(pygame, f"K_{tecla[2]}")
        habilidade_1 = getattr(pygame, f"K_{tecla[3]}")
        habilidade_2 = getattr(pygame, f"K_{tecla[4]}")
        mapa = getattr(pygame, f"K_{tecla[5]}")

        posição_chao = 735

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
            if dados["progresso"]["missao"] == 1 and not dados_obtidos:
                inimigo_local = [("parado", inimigo.posição_x), ("parado", inimigo.posição_x + 1200), ("parado", inimigo.posição_x + 1200 * 2)]
                status_inimigo = [[inimigo.dano_base, inimigo.velocidade_base, inimigo.defesa_base, inimigo.vida_atual],
                                  [inimigo.dano_base, inimigo.velocidade_base, inimigo.defesa_base, inimigo.vida_atual],
                                  [inimigo.dano_base, inimigo.velocidade_base, inimigo.defesa_base, inimigo.vida_atual]]
                status_inimigo_inicial = [[inimigo.dano_final, inimigo.velocidade_final, inimigo.defesa_final, inimigo.vida_final],
                                          [inimigo.dano_final, inimigo.velocidade_final, inimigo.defesa_final, inimigo.vida_final],
                                          [inimigo.dano_final, inimigo.velocidade_final, inimigo.defesa_final, inimigo.vida_final]]
                inimigos_pachs_parado = slime_parado
                inimigos_pachs_direita = slime_direita
                dados_obtidos = True
                inimigo_contato = [False, False, False]
            if contador <= 0:
                vida_inicial = jogador.vida_máxima
                vida_atual = jogador.vida_atual
                contador += 1
            if morto:
                quadrado_4.fill((*(0, 0, 0), 150))
                screen.blit(quadrado_4, (0, 0))
                screen.blit(game_over, (LARGURA // 2 - 800, ALTURA // 2 - 300))
            else:
                if vida_atual > 0:
                    porcentagem_vida = font_vida.render(str(vida_atual * 100 // vida_inicial) + "%", True, cor_usada)
                    screen.blit(porcentagem_vida, (posição_personagem_X + 45, posição_personagem_Y - 20))

                alpha = int(min(255, max(0, contador_cooldown_jogador * 4)))
                quadrado_5.fill((220, 220, 220, alpha))
                screen.blit(quadrado_5, (posição_personagem_X + 45, posição_personagem_Y - 40))

                if vida_atual <= 0:
                    diresao = "morte"
                    if frame_morto >= len(personagem_morto):
                        morto = True

                

                if posição - 1 >= -LARGURA * 2  and posição_personagem_X >= 500 * LARGURA // 1920 and not travar and not morto:
                    if key[pygame.K_d]:
                        posição -= 8 * LARGURA // 1920
                        inimigo_local = [(est, pos - 8 * LARGURA // 1920) for est, pos in inimigo_local]
                        if diresao != "soco" and diresao != "dano":
                            diresao = "direita"
                else:
                    if -posição_personagem_X >= -LARGURA + 150 and not travar and not morto:
                        if key[pygame.K_d]:
                            posição_personagem_X += 8 * LARGURA // 1920
                            if diresao != "soco" and diresao != "dano":
                                diresao = "direita"
                    else:
                        if diresao != "soco" and not morto and diresao != "dano":
                            diresao = "parado"


                    
                if posição <= -20 * LARGURA // 1920 and posição_personagem_X <= 500 * LARGURA // 1920 and not morto:
                    if key[pygame.K_a]:
                        posição += 8 * LARGURA // 1920
                        inimigo_local = [(est, pos + 8 * LARGURA // 1920) for est, pos in inimigo_local]
                        if diresao != "soco" and diresao != "dano":
                            diresao = "esquerda"

                else:
                    if posição_personagem_X >= -21 * LARGURA // 1920 and not morto:
                        if key[pygame.K_a]:
                            posição_personagem_X -= 8 * LARGURA // 1920
                            if diresao != "soco" and diresao != "dano":
                                diresao = "esquerda"
                    else:
                        if diresao != "soco" and not morto and diresao != "dano":
                            diresao = "parado"

                if botoes[0] and contador_cooldown_jogador <= 0 and not morto:
                    contador_cooldown_jogador = cooldown_jogador
                    diresao = "soco"
                    for i, (est, distancia) in enumerate(inimigo_local):
                        if distancia - posição_personagem_X - 20 <= 0 and distancia - posição_personagem_X + 40 >= 0:
                            status_inimigo[i][3] -= usuario.dano_base
                            inimigo_contato[i] = True
                            cor_usada_adiversario = cor_dano_adiversario
                else:
                    if not morto:
                        cor_usada_adiversario = cor_normal_adiversario
                        contador_cooldown_jogador -= 1


                if key[pygame.K_SPACE] and colisao_chao and limite_de_pulo > qnt_de_pulo and not morto and diresao != "dano":
                    qnt_de_pulo += 1
                    pulo_detectado = True
                    vel_y = forca_pulo
                    sombra.set_alpha(tranparencia - (qnt_de_pulo * 25))
                    
                    if qnt_de_pulo == limite_de_pulo:
                        colisao_chao = False


                
                
                vel_y += gravidade
                posição_personagem_Y += vel_y
                if posição_personagem_Y + 200 * LARGURA // 1920 >= posição_chao - 10 * LARGURA // 1920 and not morto:
                    sombra.set_alpha(tranparencia - (qnt_de_pulo * 10))

                if posição_personagem_Y + 200 * LARGURA // 1920 >= posição_chao - 20 * LARGURA // 1920 and not morto:
                    sombra.set_alpha(tranparencia - (qnt_de_pulo * 5))

                if posição_personagem_Y + 200 * LARGURA // 1920 >= posição_chao and not morto:
                    sombra.set_alpha(tranparencia)
                    pulo_detectado = False
                    posição_personagem_Y = posição_chao - 200 * LARGURA // 1920
                    vel_y = 0
                    colisao_chao = True
                    qnt_de_pulo = 0
                
                if not key[pygame.K_a] and not key[pygame.K_d] and not morto:
                    if diresao != "soco" and diresao != "dano":
                        diresao = "parado"

                if vida_atual <= 0:
                    diresao = "morte"
                    if frame_morto >= len(personagem_morto)-1:
                        morto = True

                if diresao == "parado":
                    screen.blit(sombra, (posição_personagem_X + 45 * LARGURA // 1920, posição_chao - 50 * LARGURA // 1920))
                    screen.blit(personagem_parado[int(frame_personagem_parado)], (posição_personagem_X, posição_personagem_Y + 15))
                    frame_personagem_parado += len(personagem_parado) * 0.08
                    if frame_personagem_parado >= len(personagem_parado):
                        frame_personagem_parado = 0

                elif diresao == "soco":
                    screen.blit(sombra, (posição_personagem_X + 40 * LARGURA // 1920, posição_chao - 50 * LARGURA // 1920))
                    screen.blit(personagem_soco_d[int(frame_personagem_soco)], (posição_personagem_X, posição_personagem_Y + 12))
                    frame_personagem_soco += len(personagem_soco_d) * 0.08
                    if frame_personagem_soco >= len(personagem_soco_d):
                        frame_personagem_soco = 0
                        diresao = "parado"

                elif diresao == "dano":
                    screen.blit(sombra, (posição_personagem_X + 40 * LARGURA // 1920, posição_chao - 50 * LARGURA // 1920))
                    screen.blit(personagem_dano[int(frame_personagem_dano)], (posição_personagem_X, posição_personagem_Y))
                    cor_usada = cor_dano
                    frame_personagem_dano += len(personagem_dano) * 0.08
                    if frame_personagem_dano >= len(personagem_dano):
                        frame_personagem_dano = 0
                        diresao = "parado"

                elif diresao == "morte":
                    screen.blit(sombra, (posição_personagem_X + 40 * LARGURA // 1920, posição_chao - 50 * LARGURA // 1920))
                    screen.blit((personagem_morto[int(frame_morto)]), (posição_personagem_X, posição_personagem_Y))
                    if frame_morto <= len(personagem_morto) - len(personagem_morto) * 0.08:
                        frame_morto += len(personagem_morto) * 0.08
                    if time_morrer <= 10:
                        time_morrer += 1
                    else:
                        morte = True
                    


                else:
                    screen.blit(sombra, (posição_personagem_X + 40 * LARGURA // 1920, posição_chao - 50 * LARGURA // 1920))
                    screen.blit(personagem_andando_D[frame_personagem], (posição_personagem_X, posição_personagem_Y))
                    frame_personagem += 1
                    if frame_personagem >= len(personagem_andando_D):
                        frame_personagem = 0






                derrotados = 0
                for i, (diresao_adiversario, posicao_x) in enumerate(inimigo_local):
                    if status_inimigo[i][3] > 0:
                        if posicao_x - 500 >= posição_personagem_X:
                            diresao_adiversario = "parado"

                        if posicao_x - 20 <= posição_personagem_X and posicao_x + 20 >= posição_personagem_X:
                            diresao_adiversario = "soco"

                        elif posicao_x - 500 <= posição_personagem_X and posicao_x >= posição_personagem_X:
                            diresao_adiversario = "esquerda"

                        elif posicao_x - 500 <= posição_personagem_X -300:
                            diresao_adiversario = "direita"

                        if diresao_adiversario == "parado":
                            screen.blit(inimigos_pachs_direita[int(frame_inimigo_direita)], (posicao_x, 735 - 200))
                            if andar_inimigo:
                                frame_inimigo_parado += len(inimigos_pachs_parado) * 0.08
                                andar_inimigo = False
                            if frame_inimigo_parado >= len(inimigos_pachs_parado):
                                frame_inimigo_parado = 0
                        

                        elif diresao_adiversario == "direita":
                            screen.blit(inimigos_pachs_direita[int(frame_inimigo_direita)], (posicao_x, 735 - 180))
                            if andar_inimigo:
                                frame_inimigo_direita += len(inimigos_pachs_direita) * 0.08
                                andar_inimigo = False
                            posicao_x = posicao_x + 6 * LARGURA // 1980
                            if frame_inimigo_direita >= len(inimigos_pachs_direita):
                                frame_inimigo_direita = 0

                        elif diresao_adiversario == "esquerda":
                            screen.blit(inimigos_pachs_direita[int(frame_inimigo_direita)], (posicao_x, 735 - 180))
                            if andar_inimigo:
                                frame_inimigo_direita += len(inimigos_pachs_direita) * 0.08
                                andar_inimigo = False
                            posicao_x = posicao_x - 6 * LARGURA // 1980
                            if frame_inimigo_direita >= len(inimigos_pachs_direita):
                                frame_inimigo_direita = 0

                        elif diresao_adiversario == "soco":
                            screen.blit(inimigos_pachs_direita[int(frame_inimigo_direita)], (posicao_x, 735 - 180))
                            if andar_inimigo:
                                frame_inimigo_direita += len(inimigos_pachs_direita) * 0.08
                                andar_inimigo = False
                            if cooldown_dano <= contador_cooldown:
                                vida_atual -= status_inimigo[i][0]
                                diresao = "dano"
                                contador_cooldown = 0
                            else:
                                contador_cooldown += 0.2
                            if frame_inimigo_direita >= len(inimigos_pachs_direita):
                                frame_inimigo_direita = 0


                        if i == len(inimigo_local) - 1:
                            andar_inimigo = True

                        porcentagem_vida_adiversario = font_vida.render(str(status_inimigo[i][3] * 100 // status_inimigo_inicial[i][3]) + "%", True, cor_usada_adiversario)
                        screen.blit(porcentagem_vida_adiversario, (posicao_x + 60, 735 - 170))

                        inimigo_local[i] = (diresao_adiversario, posicao_x)

                    else:
                        derrotados += 1

                if diresao != "dano":
                    cor_usada = cor_normal
                    
                if derrotados >= len(inimigo_local):
                    print("vitoria")
                
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
                Popen([sys.executable, rf'{endereço}\ui\lobby.py'])
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
                                {"label": "Mapa", "rect": pygame.Rect(LARGURA // 1.8, ALTURA // 4 + ALTURA // 10 + ALTURA // 10 + ALTURA // 10 + ALTURA // 10 + ALTURA // 10, LARGURA // 18, ALTURA // 16), "text": f"{dados["keys"]["mapa"]}", "active": False, "peritido": TEXTO_S}]
                estado = anterior
            
            rect_box = pygame.Rect(LARGURA // 2.7, ALTURA // 4.5, LARGURA // 3.9, ALTURA // 1.6)
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