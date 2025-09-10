import pygame
import sys
import os
from random import choice
from ui.menus import desenhar_botao, TEXTO_S, COR_TEXTO, COR_INATIVA, COR_ATIVA
from ui.lobby import input_boxes, salvar, fonte_input, font_title, nome_rect, primeiro_nome
from recursos.imagens.missao.missao1.slime import slime_parado, slime_direita, slime_morto
from recursos.imagens.cenario.cenario_explorar import inventario_pach, inventario_icon, mapa_img, chao
import sqlite3
import pyautogui
from subprocess import Popen
import json
from recursos.imagens.personagem_principal import personagem_parado, personagem_andando_D, personagem_soco_d, personagem_morto, personagem_dano
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from backend.entidades.inimigos import slime
from backend.entidades.jogador import jogador
from backend.sistemas.itens import itens, itens_icons
#from backend.app.models.sistema.habilidades_ativa_combatentes import golpe_mortal, intangibilidade, impacto_cruzado, bloqueio_de_espada, ataque_com_escudo, defesa_reforcada, giro_de_lanca, arremesso_de_lanca, disparo_perfurante, camuflagem, ataque_surpresa, fuga_rapida
#from backend.app.models.sistema.habilidades_passivas_combatentes import furtividade, evasao, sangramento, vontade_da_espada, heranca_da_espada, ataque_rapido, bloqueio_de_ataque, repelir, peso_pena, danca_da_lanca, controle_passivo, controle_total, disparo_preciso, passos_silenciosos, flecha_dupla, ataque_silencioso, evasao_rapida, exploracao_furtiva
LARGURA, ALTURA = pyautogui.size()
endereço = os.path.dirname(os.path.abspath(__file__))



font_vida = pygame.font.Font(rf"{endereço}\recursos\fontes\Minha fonte.ttf", 30)

with open(rf"{endereço}\ui\usuario.json", "r") as arquivo:
    dados = json.load(arquivo)
dados["inventario"]["item"] = json.loads(dados["inventario"]["item"])
dados["inventario"]["equipado"] = json.loads(dados["inventario"]["equipado"])


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
dados_obtidos = False
andar_inimigo = True
morto = False
frame_morto = 0
time_morrer = 0
mesma_linha = 0

estrucao = 0
vel_letra = 0.5
tamanho_estrucao = 36
font_estrucao = pygame.font.Font(rf"{endereço}\recursos\fontes\Minha fonte.ttf", tamanho_estrucao)

font_nome = pygame.font.Font(rf"{endereço}\recursos\fontes\Minha fonte.ttf", ALTURA // 50)
nome = font_nome.render(f"{primeiro_nome}", True, (190, 190, 230))

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

buff_vida = 0
buff_estamina = 0
buff_dano = 0
buff_defesa = 0
buff_recebido = False

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

tamanho_font = 30

pygame.init()
clock = pygame.time.Clock()
botao_segurado = False



usuario = jogador

# Estados
JOGO = "jogo"
OPCOES = "opcoes"
MENU = "menu"
INVENTARIO = "inventario"
MAPA = "mapa"
COMBATE = "combate"
estado = JOGO

tranparencia = 150
sombra = pygame.Surface((100 * LARGURA // 1920, 20 * LARGURA // 1920), pygame.SRCALPHA)

marcado = False
desmarcar = True

pos_chao_x, pos_chao_y = (-5000, -3500)

quadrado = pygame.Surface((LARGURA, ALTURA), pygame.SRCALPHA)
quadrado_2 = pygame.Surface((LARGURA, ALTURA), pygame.SRCALPHA)
quadrado_3 = pygame.Surface((LARGURA, ALTURA), pygame.SRCALPHA)
quadrado_4 = pygame.Surface((LARGURA, ALTURA), pygame.SRCALPHA)
quadrado_5 = pygame.Surface((100, 15), pygame.SRCALPHA)
contador = 0
rect_opcoes = pygame.Rect(LARGURA // 2.5, LARGURA // 1.5, ALTURA // 1.6, ALTURA // 2)
click = False
click_e = False
quadrado_3.fill((*(0, 0, 0), 150))

quadrado_7 = pygame.Surface((50, 50))
personagem_x = LARGURA // 2
personagem_y = ALTURA // 2
personagem = pygame.Rect(personagem_x, personagem_y, 50, 50)

tempo_salvar = 0
travar_mapa = False

dano_ficticio = 13
vida_ficticia = 120
vida_ficticia_atual = vida_ficticia

rect = pygame.Rect(
                personagem_x - (len(list(primeiro_nome)) * 7),
                personagem_y - 45,
                nome_rect.width,
                nome_rect.height
                )


dados["inventario"]["item"].append([[itens[0].nome, "comum"], 1])
dados["inventario"]["item"].append([[itens[-1].nome, itens[-1].raridade], 1])

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

        tempo_salvar += 1
        mouse_pos = pygame.mouse.get_pos()

        if (tempo_salvar % 32) >= 10 * 60:
            tempo_salvar = 0
            salvar(teclas, dados)

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

        for i, item in enumerate(dados["inventario"]["item"]):
            for i2, item2 in enumerate(dados["inventario"]["item"]):
                if i != i2:
                    if item[0] == item2[0]:
                        item[1] += item2[1]
                        dados["inventario"]["item"].pop(i2)          

        font_estrucao = pygame.font.Font(rf"{endereço}\recursos\fontes\Minha fonte.ttf", int(tamanho_estrucao))

        if estado == JOGO:
            from backend.sistemas.colisao import pach_objects, pach_objects_colision, pach_objects_hit_boxes_colision, pach_objects_rects_colision, gerenciador_colisao, pach_objects_intamgible
            anterior = JOGO
            dados_do_alvo_recebidos = False
            screen.blit(chao, (pos_chao_x, pos_chao_y))
            rect = pygame.Rect(
                personagem_x - (len(list(primeiro_nome)) * 7),
                personagem_y - 45,
                nome_rect.width,
                nome_rect.height
                )
            rect.x = personagem_x - font_nome.size(primeiro_nome)[0] // 3
            nome_rect.x = personagem_x - font_nome.size(primeiro_nome)[0] // 9
            nome_rect.y = personagem_y - 40


            quadrado_7.fill((0, 200, 0))
            personagem = pygame.Rect(personagem_x, personagem_y, 50, 50)
            for obj in pach_objects_intamgible:
                screen.blit(obj.imagem_pach, (obj.x, obj.y))
            screen.blit(quadrado_7, (personagem_x, personagem_y))
            for obj in pach_objects:
                screen.blit(obj.imagem_pach, (obj.x, obj.y))

                    
            # Desenha o retângulo cinza atrás do nome
            pygame.draw.rect(screen, (100, 100, 100), rect, border_radius=5)

            # Desenha o texto do nome por cima do retângulo
            screen.blit(nome, nome_rect)

            # atualiza todos os objetos do gerenciador de colisão
            gerenciador_colisao.atualizar()

            if marcado:
                loc_mapa = [
                            ((loc_marcado[0] - 500) * 19200) // (1380 - 500) + pos_chao_x,
                            ((loc_marcado[1] - 100) * 10800) // (980 - 100) + pos_chao_y
                        ]
                
                if loc_mapa[0] <= 0:
                    loc_mapa[0] = 0
                if loc_mapa[0] >= 1920:
                    loc_mapa[0] = 1920
                if loc_mapa[1] <= 0:
                    loc_mapa[1] = 0
                if loc_mapa[1] >= 1080:
                    loc_mapa[1] = 1080

                loc_mapa = (loc_mapa[0],
                            loc_mapa[1])

                pygame.draw.circle(screen, (190, 60, 60), loc_mapa, 30)

            item_x = 1800
            item_y = 250
            # icon do inventario
            screen.blit(inventario_icon, (1800, 250))
            screen.blit(inventario_icon, (1800, 370))
            screen.blit(inventario_icon, (1800, 490))
            screen.blit(inventario_icon, (1800, 610))
            screen.blit(inventario_icon, (1800, 730))

            for equipamento in dados["inventario"]["equipado"]:
                for i, item in enumerate(itens):
                    if item.nome == equipamento[0] and item.raridade == equipamento[1] and item.type != "comum" and item.type != "defesa":
                        screen.blit(itens_icons[i], (1800, item_y))
                        item_y += 120

            print(personagem_x, personagem_y)

            # velocidade
            vel = dados["status"]["velocidade"] * 2

            # limites do mapa (10x a largura/altura da tela)
            MAPA_LARGURA = LARGURA * 10
            MAPA_ALTURA = ALTURA * 10

            # ---------------------------
            # Movimento diagonal (A + W)
            if key[pygame.K_a] and key[pygame.K_w] and not gerenciador_colisao.colide(personagem.move(-vel, -vel)):
                novo_personagem = personagem.move(-vel, -vel)
                if not gerenciador_colisao.colide(novo_personagem):

                    move_x = False
                    move_y = False

                    # Controle eixo X (esquerda)
                    if pos_chao_x < 0 and personagem_x <= LARGURA // 2:
                        for obj in gerenciador_colisao.todos_objetos:
                            obj.x += vel // 2
                        pos_chao_x += vel // 2
                        personagem = LARGURA // 2
                    elif personagem_x > 0:
                        personagem_x -= vel // 2
                    else:
                        move_x = True

                    # Controle eixo Y (cima)
                    if pos_chao_y < 0 and personagem_y <= ALTURA // 2:
                        for obj in gerenciador_colisao.todos_objetos:
                            obj.y += vel // 2
                        pos_chao_y += vel // 2
                        personagem = ALTURA // 2
                    elif personagem_y > 0:
                        personagem_y -= vel // 2
                    else:
                        move_y = True

            # Movimento diagonal (D + W)
            elif key[pygame.K_d] and key[pygame.K_w] and not gerenciador_colisao.colide(personagem.move(vel, -vel)):
                novo_personagem = personagem.move(vel, -vel)
                if not gerenciador_colisao.colide(novo_personagem):

                    # Controle eixo X (direita)
                    if pos_chao_x > -(MAPA_LARGURA - LARGURA) and personagem_x >= LARGURA // 2:
                        for obj in gerenciador_colisao.todos_objetos:
                            obj.x -= vel // 2
                        pos_chao_x -= vel // 2
                        personagem = LARGURA // 2
                    elif personagem_x < LARGURA:
                        personagem_x += vel // 2

                    # Controle eixo Y (cima)
                    if pos_chao_y < 0 and personagem_y <= ALTURA // 2:
                        for obj in gerenciador_colisao.todos_objetos:
                            obj.y += vel // 2
                        pos_chao_y += vel // 2
                        personagem = ALTURA // 2
                    elif personagem_y > 0:
                        personagem_y -= vel // 2

            # Movimento diagonal (A + S)
            elif key[pygame.K_a] and key[pygame.K_s] and not gerenciador_colisao.colide(personagem.move(-vel, vel)):
                novo_personagem = personagem.move(-vel, vel)
                if not gerenciador_colisao.colide(novo_personagem):

                    # Controle eixo X (esquerda)
                    if pos_chao_x < 0 and personagem_x <= LARGURA // 2:
                        for obj in gerenciador_colisao.todos_objetos:
                            obj.x += vel // 2
                        pos_chao_x += vel // 2
                        personagem = LARGURA // 2
                    elif personagem_x > 0:
                        personagem_x -= vel // 2

                    # Controle eixo Y (baixo)
                    if pos_chao_y > -(MAPA_ALTURA - ALTURA) and personagem_y >= ALTURA // 2:
                        for obj in gerenciador_colisao.todos_objetos:
                            obj.y -= vel // 2
                        pos_chao_y -= vel // 2
                        personagem = ALTURA // 2
                    elif personagem_y < ALTURA:
                        personagem_y += vel // 2

            # Movimento diagonal (D + S)
            elif key[pygame.K_d] and key[pygame.K_s] and not gerenciador_colisao.colide(personagem.move(vel, vel)):
                novo_personagem = personagem.move(vel, vel)
                if not gerenciador_colisao.colide(novo_personagem):

                    # Controle eixo X (direita)
                    if pos_chao_x > -(MAPA_LARGURA - LARGURA) and personagem_x >= LARGURA // 2:
                        for obj in gerenciador_colisao.todos_objetos:
                            obj.x -= vel // 2
                        pos_chao_x -= vel // 2
                        personagem = LARGURA // 2
                    elif personagem_x < LARGURA:
                        personagem_x += vel // 2

                    # Controle eixo Y (baixo)
                    if pos_chao_y > -(MAPA_ALTURA - ALTURA) and personagem_y >= ALTURA // 2:
                        for obj in gerenciador_colisao.todos_objetos:
                            obj.y -= vel // 2
                        pos_chao_y -= vel // 2
                        personagem = ALTURA // 2
                    elif personagem_y < ALTURA:
                        personagem_y += vel // 2

            # ---------------------------
            # Movimento direita (D)
            elif key[pygame.K_d] and not gerenciador_colisao.colide(personagem.move(vel, 0)):
                novo_personagem = personagem.move(vel, 0)
                if not gerenciador_colisao.colide(novo_personagem):

                    if pos_chao_x > -(MAPA_LARGURA - LARGURA) and personagem_x >= LARGURA // 2:
                        for obj in gerenciador_colisao.todos_objetos:
                            obj.x -= vel // 1.5
                        pos_chao_x -= vel // 1.5
                        personagem = LARGURA // 2
                    elif personagem_x <= LARGURA:
                        personagem_x += vel // 1.5

            # Movimento esquerda (A)
            elif key[pygame.K_a] and not gerenciador_colisao.colide(personagem.move(-vel, 0)):
                novo_personagem = personagem.move(-vel, 0)
                if not gerenciador_colisao.colide(novo_personagem):

                    if pos_chao_x < 0 and personagem_x <= LARGURA // 2:
                        for obj in gerenciador_colisao.todos_objetos:
                            obj.x += vel // 1.5
                        pos_chao_x += vel // 1.5
                        personagem = LARGURA // 2
                    elif personagem_x >= 0:
                        personagem_x -= vel // 1.5

            # Movimento cima (W)
            elif key[pygame.K_w] and not gerenciador_colisao.colide(personagem.move(0, -vel)):
                novo_personagem = personagem.move(0, -vel)
                if not gerenciador_colisao.colide(novo_personagem):

                    if pos_chao_y < 0 and personagem_y <= ALTURA // 2:
                        for obj in gerenciador_colisao.todos_objetos:
                            obj.y += vel // 1.5
                        pos_chao_y += vel // 1.5
                        personagem = ALTURA // 2
                    elif personagem_y >= 0:
                        personagem_y -= vel // 1.5

            # Movimento baixo (S)
            elif key[pygame.K_s] and not gerenciador_colisao.colide(personagem.move(0, vel)):
                novo_personagem = personagem.move(0, vel)
                if not gerenciador_colisao.colide(novo_personagem):

                    if pos_chao_y > -(MAPA_ALTURA - ALTURA) and personagem_y >= ALTURA // 2:
                        for obj in gerenciador_colisao.todos_objetos:
                            obj.y -= vel // 1.5
                        pos_chao_y -= vel // 1.5
                        personagem = ALTURA // 2
                    elif personagem_y <= ALTURA:
                        personagem_y += vel // 1.5


            # ESCAPE → abre opções
            if key[pygame.K_ESCAPE] and not click:
                click = True
                contador = 0
                estado = OPCOES
            if not key[pygame.K_ESCAPE]:
                click = False

            # INVENTÁRIO → abre inventário
            if key[inventario] and not click_e:
                click_e = True
                contador = 0
                estado = INVENTARIO
            if not key[inventario]:
                click_e = False

            if key[mapa] and not travar_mapa:
                travar_mapa = True
                contador = 0
                estado = MAPA
            if not key[mapa]:
                travar_mapa = False

        
            if dados["progresso"]["missao"] <= 1 and estrucao == 0:
                texto = font_estrucao.render("pricione a tecla E", True, (200, 110, 110))
                largura_texto, altura_texto = font_estrucao.size("pricione a tecla E")
                quadrado_estrucao = pygame.Surface((largura_texto + 20, altura_texto + 20), pygame.SRCALPHA)
                quadrado_estrucao.fill((*(0, 0, 0), 150))
                screen.blit(quadrado_estrucao, ((LARGURA // 2) - (largura_texto // 2) - 10, 1000 - 10))
                screen.blit(texto, ((LARGURA // 2) - (largura_texto // 2), 1000))
                if tamanho_estrucao <= 36:
                    vel_letra = 0.5
                if tamanho_estrucao >= 40:
                    vel_letra = -0.5
                tamanho_estrucao += vel_letra
                if key[inventario]:
                    estrucao += 1



        if estado == COMBATE:
            anterior = COMBATE
            screen.blit(cenario_combate, (posição, 0))
            if dados["progresso"]["missao"] == 1 and not dados_obtidos:
                inimigo_local = [("parado", slime.posição_x), ("parado", slime.posição_x + 1200), ("parado", slime.posição_x + 1200 * 2)]
                status_inimigo = [[slime.dano_base, slime.velocidade_base, slime.defesa_base, slime.vida_base],
                                  [slime.dano_base, slime.velocidade_base, slime.defesa_base, slime.vida_base],
                                  [slime.dano_base, slime.velocidade_base, slime.defesa_base, slime.vida_base]]
                status_inimigo_inicial = [[slime.dano_base, slime.velocidade_base, slime.defesa_base, slime.vida_base],
                                         [slime.dano_base, slime.velocidade_base, slime.defesa_base, slime.vida_base],
                                         [slime.dano_base, slime.velocidade_base, slime.defesa_base, slime.vida_base]]
                inimigos_pachs_parado = slime_parado
                inimigos_pachs_direita = slime_direita
                inimigos_pachs_morto = slime_morto
                dados_obtidos = True
                inimigo_contato = [False, False, False]

                frame_inimigo_parado = [0, 0, 0]
                frame_inimigo_direita = [0, 0, 0]
                frame_inimigo_esquerda = [0, 0, 0]
                frame_inimigo_morto = [0, 0, 0]
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
                            screen.blit(inimigos_pachs_parado[int(frame_inimigo_parado[i])], (posicao_x, 735 - 180))
                            frame_inimigo_parado[i] += len(inimigos_pachs_parado) * 0.08
                            if frame_inimigo_parado[i] >= len(inimigos_pachs_parado):
                                frame_inimigo_parado[i] = 0
                        

                        elif diresao_adiversario == "direita":
                            screen.blit(inimigos_pachs_direita[int(frame_inimigo_direita[i])], (posicao_x, 735 - 180))
                            frame_inimigo_direita[i] += len(inimigos_pachs_direita) * 0.08
                            posicao_x = posicao_x + 6 * LARGURA // 1980
                            if frame_inimigo_direita[i] >= len(inimigos_pachs_direita):
                                frame_inimigo_direita[i] = 0

                        elif diresao_adiversario == "esquerda":
                            screen.blit(inimigos_pachs_direita[int(frame_inimigo_direita[i])], (posicao_x, 735 - 180))
                            frame_inimigo_direita[i] += len(inimigos_pachs_direita) * 0.08
                            posicao_x = posicao_x - 6 * LARGURA // 1980
                            if frame_inimigo_direita[i] >= len(inimigos_pachs_direita):
                                frame_inimigo_direita[i] = 0

                        elif diresao_adiversario == "soco":
                            screen.blit(inimigos_pachs_direita[int(frame_inimigo_direita[i])], (posicao_x, 735 - 180))
                            frame_inimigo_direita[i] += len(inimigos_pachs_direita) * 0.08
                            if cooldown_dano <= contador_cooldown:
                                vida_atual -= status_inimigo[i][0] - jogador.defesa_base if status_inimigo[i][0] - jogador.defesa_base > 0 else 1
                                diresao = "dano"
                                contador_cooldown = 0
                            else:
                                contador_cooldown += 0.2
                            if frame_inimigo_direita[i] >= len(inimigos_pachs_direita):
                                frame_inimigo_direita[i] = 0

                        porcentagem_vida_adiversario = font_vida.render(str(status_inimigo[i][3] * 100 // status_inimigo_inicial[i][3]) + "%", True, cor_usada_adiversario)
                        screen.blit(porcentagem_vida_adiversario, (posicao_x + 60, 735 - 170))

                        inimigo_local[i] = (diresao_adiversario, posicao_x)

                    else:
                        derrotados += 1
                        if frame_inimigo_morto[i] <= len(inimigos_pachs_morto) - len(inimigos_pachs_morto) * 0.05:
                            screen.blit(inimigos_pachs_morto[int(frame_inimigo_morto[i])], (posicao_x, 735 - 150))
                            frame_inimigo_morto[i] += len(inimigos_pachs_morto) * 0.05
                        else:
                            screen.blit(inimigos_pachs_morto[len(inimigos_pachs_morto) - 1], (posicao_x, 735 - 150))

                if diresao != "dano":
                    cor_usada = cor_normal
                    
                if derrotados >= len(inimigo_local):
                    dados["progresso"]["missao"] += 1
                    salvar(teclas, dados)
                    dados_obtidos = False
                    estado = JOGO
                
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
            screen.blit(chao, (pos_chao_x, pos_chao_y))
            rect.x = personagem_x - (len(list(primeiro_nome)) * 6)
            nome_rect.x = personagem_x - (len(list(primeiro_nome)) * 2)
            nome_rect.y = personagem_y - 40

            buff_vida = 0
            buff_estamina = 0
            buff_dano = 0
            buff_defesa = 0

            quadrado_7.fill((0, 200, 0))
            personagem = pygame.Rect(personagem_x, personagem_y, 50, 50)
            for obj in pach_objects_intamgible:
                screen.blit(obj.imagem_pach, (obj.x, obj.y))
            screen.blit(quadrado_7, (personagem_x, personagem_y))
            for obj in pach_objects:
                screen.blit(obj.imagem_pach, (obj.x, obj.y))
                    
            # Desenha o retângulo cinza atrás do nome
            pygame.draw.rect(screen, (100, 100, 100), rect, border_radius=5)

            # Desenha o texto do nome por cima do retângulo
            screen.blit(nome, nome_rect)

            item_x = 1800
            item_y = 250
            # icon do inventario
            screen.blit(inventario_icon, (1800, 250))
            screen.blit(inventario_icon, (1800, 370))
            screen.blit(inventario_icon, (1800, 490))
            screen.blit(inventario_icon, (1800, 610))
            screen.blit(inventario_icon, (1800, 730))

            for equipamento in dados["inventario"]["equipado"]:
                for i, item in enumerate(itens):
                    if item.nome == equipamento[0] and item.raridade == equipamento[1] and item.type != "comum" and item.type != "defesa":
                        screen.blit(itens_icons[i], (1800, item_y))
                        item_y += 120

            quadrado_3.fill((*(0, 0, 0), 150))
            screen.blit(quadrado_3, (0, 0))
            screen.blit(inventario_pach, (LARGURA // 2 - (1344 * LARGURA // 1920) // 2, ALTURA // 2 - (966  * ALTURA // 1080) // 2))

            for item in itens:
                if not (item.type == "defesa") or item.nome not in (equipamento[0] for equipamento in dados["inventario"]["equipado"]):
                    item.x = 912 * LARGURA // 1920
                    item.y = 147 * ALTURA // 1080
            mesma_linha = 0
            item_hover = None  # <- guarda qual item o mouse está em cima
            pos_x, pos_y = item.x, item.y

            for recurso in dados["inventario"]["item"]:
                for i, item in enumerate(itens):
                    if recurso[0][0] == item.nome and recurso[0][1] == (item.raridade if item.type != "comum" else recurso[0][1]):
                        pos_x, pos_y = item.x, item.y
                        mesma_linha += 1
                        objeto_rect = pygame.Rect(item.rect())

                        # Desenha o item
                        if item.type == "defesa" and item.nome in (equipamento[0] for equipamento in dados["inventario"]["equipado"]):
                            if item.nome.split()[0] == "Capacete":
                                item.x = 594
                                item.y =210
                                pos_x = item.x
                                pos_y = item.y
                            elif item.nome.split()[0] == "Bota":
                                item.x = 594
                                item.y =430
                            elif item.nome.split()[0] == "Peitoral":
                                item.x = 594
                                item.y =320
                        screen.blit(item.imagem_pach, (item.x, item.y))

                        if item.nome in (equipamento[0] for equipamento in dados["inventario"]["equipado"]) and item.type != "comum":
                            if not (item.type == "defesa") or item.nome not in (equipamento[0] for equipamento in dados["inventario"]["equipado"]):
                                pygame.draw.rect(screen, (100, 255, 100), objeto_rect, 6)
                            elif item.nome.split()[0] == "Capacete":
                                objeto_rect = pygame.Rect((624, 243, 84, 84))
                                pygame.draw.rect(screen, (100, 255, 100), objeto_rect, 6)
                            elif item.nome.split()[0] == "Bota":
                                objeto_rect = pygame.Rect((624, 459, 84, 84))
                                pygame.draw.rect(screen, (100, 255, 100), objeto_rect, 6)
                            elif item.nome.split()[0] == "Peitoral":
                                objeto_rect = pygame.Rect((624, 351, 84, 84))
                                pygame.draw.rect(screen, (100, 255, 100), objeto_rect, 6)

                        # Se o mouse está em cima, marca o item
                        if objeto_rect.collidepoint(mouse_pos):
                            item_hover = item_hover = (item, pos_x, pos_y)
                            if not (item.type == "defesa") or item.nome not in (equipamento[0] for equipamento in dados["inventario"]["equipado"]):
                                pygame.draw.rect(screen, (230, 230, 230), objeto_rect, 6)
                            if botoes[0]:
                                pygame.draw.rect(screen, (100, 180, 100), objeto_rect, 6)
                                if not precionado:
                                    precionado = True
                                    if item.nome not in (equipamento[0] for equipamento in dados["inventario"]["equipado"]) and item.type != "comum":
                                        dados["inventario"]["equipado"].append([item.nome, item.raridade])
                                    elif item.type != "comum":
                                        dados["inventario"]["equipado"].remove([item.nome, item.raridade])
                                        buff_vida -= item.vida
                                        buff_estamina -= item.peso
                                        buff_dano -= item.ataque
                                        buff_defesa -= item.defesa
                            else:
                                precionado = False


                        # Quantidade do item
                        if not (item.type == "defesa") or item.nome not in (equipamento[0] for equipamento in dados["inventario"]["equipado"]):
                            quantidade_itens = font_nome.render(str(recurso[1]), True, (100, 100, 100))
                            screen.blit(quantidade_itens, (item.x + 5, item.y + 120))

                        # Atualiza posições
                        for item2 in itens:
                            item2.x = item2.x + 174 * LARGURA // 1920 if item2.x == 912 * LARGURA // 1920 or item2.x == 1254 * LARGURA // 1920 else item2.x + 168 * LARGURA // 1920
                            if mesma_linha % 4 == 0:
                                item2.x = 912 * LARGURA // 1920
                                if item2.y == 147 * ALTURA // 1080:
                                    item2.y += 174 * ALTURA // 1080
                                elif item2.y == 321 * ALTURA // 1080 or item2.y == 489 * ALTURA // 1080:
                                    item2.y += 168 * ALTURA // 1080
                                elif item2.y == 657 * ALTURA // 1080:
                                    item2.y += 162 * ALTURA // 1080

            # 2️⃣ Só agora desenha a tooltip por cima de tudo
            if item_hover:
                if item_hover[0].type == "comum":
                    if len(item_hover[0].descricao) >= 13:
                        frases_descriacao = item_hover[0].descricao.split()
                        for i, linha in enumerate(frases_descriacao):
                            if len(frases_descriacao) > i + 1:
                                
                                if len(linha + frases_descriacao[i + 1]) <= 13:
                                    linha = f"{linha} {frases_descriacao[i + 1]}"
                                    frases_descriacao.pop(i + 1)
                                    
                                    if len(frases_descriacao) > i + 1:
                                        if len(linha + frases_descriacao[i + 1]) <= 13:
                                            linha = f"{linha} {frases_descriacao[i + 1]}"
                                            frases_descriacao.pop(i + 1)
                                            
                    quantidade_linhas = len(frases_descriacao)
                    descricao_rect = pygame.Rect(item_hover[1] + 110, item_hover[2] - 40, 300 * LARGURA // 1920, 10)
                    descricao_rect.height = 130 + (quantidade_linhas * 25)
                    if descricao_rect.bottom > ALTURA:
                        descricao_rect.top = item_hover[2] - 340
                    pygame.draw.rect(screen, (50, 50, 50), descricao_rect, border_radius=10)   # fundo
                    pygame.draw.rect(screen, (230, 230, 230), descricao_rect, 2, border_radius=10)  # borda
                    pygame.draw.line(screen, (230, 230, 230), (descricao_rect.x, descricao_rect.y + 60), (descricao_rect.x + descricao_rect.width, descricao_rect.y + 60), 2)

                    if len(item_hover[0].nome) >= 13:
                        frases = item_hover[0].nome.split()
                        for i, linha in enumerate(frases):
                            if len(frases) > i + 1:
                                if len(linha + frases[i + 1]) <= 13:
                                    linha = f"{linha} {frases[i + 1]}"
                                    frases.pop(i + 1)
                            texto = font_nome.render(linha, True, (255, 180, 180))
                            screen.blit(texto, (descricao_rect.x + 10, descricao_rect.y + 10 + i * 20))
                    else:
                        texto = font_nome.render(item_hover[0].nome, True, (255, 180, 180))
                        screen.blit(texto, (descricao_rect.x + 10, descricao_rect.y + 10))
                    if len(item_hover[0].descricao) >= 13:
                        frases_descriacao = item_hover[0].descricao.split()
                        for i, linha in enumerate(frases_descriacao):
                            if len(frases_descriacao) > i + 1:
                                if len(linha + frases_descriacao[i + 1]) <= 13:
                                    linha = f"{linha} {frases_descriacao[i + 1]}"
                                    frases_descriacao.pop(i + 1)
                                    if len(frases_descriacao) > i + 1:
                                        if len(linha + frases_descriacao[i + 1]) <= 13:
                                            linha = f"{linha} {frases_descriacao[i + 1]}"
                                            frases_descriacao.pop(i + 1)
                            texto = font_nome.render(linha, True, (255, 255, 255))
                            screen.blit(texto, (descricao_rect.x + 10, descricao_rect.y + 100 + i * 30))



                elif item_hover[0].type == "ataque":

                    descricao_rect = pygame.Rect(item_hover[1] + 110, item_hover[2] - 40, 300 * LARGURA // 1920, 10)
                    descricao_rect.height = 130 + (4 * 25)
                    if descricao_rect.bottom > ALTURA:
                        descricao_rect.top = item_hover[2] - 340
                    pygame.draw.rect(screen, (50, 50, 50), descricao_rect, border_radius=10)   # fundo
                    pygame.draw.rect(screen, (230, 230, 230), descricao_rect, 2, border_radius=10)  # borda
                    pygame.draw.line(screen, (230, 230, 230), (descricao_rect.x, descricao_rect.y + 60), (descricao_rect.x + descricao_rect.width, descricao_rect.y + 60), 2)

                    if len(item_hover[0].nome) >= 13:
                        frases = item_hover[0].nome.split()
                        for i, linha in enumerate(frases):
                            if len(frases) > i + 1:
                                if len(linha + frases[i + 1]) <= 13:
                                    linha = f"{linha} {frases[i + 1]}"
                                    frases.pop(i + 1)
                            texto = font_nome.render(linha, True, (255, 180, 180))
                            screen.blit(texto, (descricao_rect.x + 10, descricao_rect.y + 10 + i * 20))
                    else:
                        texto = font_nome.render(item_hover[0].nome, True, (255, 180, 180))
                        screen.blit(texto, (descricao_rect.x + 10, descricao_rect.y + 10))
                    
                    dano, peso, raridade = (item_hover[0].ataque, item_hover[0].peso, item_hover[0].raridade)
                    status_arma = [f"Dano: {dano}", f"Peso: {peso}", f"Raridade: {raridade}"]
                    for i, status in enumerate(status_arma):
                        if len(status) >= 13:
                            status = status.split()
                            for i2, status2 in enumerate(status):
                                texto = font_nome.render(status2, True, (255, 255, 255))
                                screen.blit(texto, (descricao_rect.x + 10, descricao_rect.y + 80 + (i + i2) * 40))
                        else:
                            texto = font_nome.render(status, True, (255, 255, 255))
                            screen.blit(texto, (descricao_rect.x + 10, descricao_rect.y + 80 + i * 40))

                elif item_hover[0].type == "ataque e defesa" or item_hover[0].type == "defesa":

                    descricao_rect = pygame.Rect(item_hover[1] + 110, item_hover[2] - 40, 300 * LARGURA // 1920, 10)
                    descricao_rect.height = 130 + (6 * 25)
                    if descricao_rect.bottom > ALTURA:
                        descricao_rect.top = item_hover[2] - 340
                    pygame.draw.rect(screen, (50, 50, 50), descricao_rect, border_radius=10)   # fundo
                    pygame.draw.rect(screen, (230, 230, 230), descricao_rect, 2, border_radius=10)  # borda
                    pygame.draw.line(screen, (230, 230, 230), (descricao_rect.x, descricao_rect.y + 60), (descricao_rect.x + descricao_rect.width, descricao_rect.y + 60), 2)

                    if len(item_hover[0].nome) >= 13:
                        frases = item_hover[0].nome.split()
                        for i, linha in enumerate(frases):
                            if len(frases) > i + 1:
                                if len(linha + frases[i + 1]) <= 13:
                                    linha = f"{linha} {frases[i + 1]}"
                                    frases.pop(i + 1)
                            texto = font_nome.render(linha, True, (255, 180, 180))
                            screen.blit(texto, (descricao_rect.x + 10, descricao_rect.y + 10 + i * 20))
                    else:
                        texto = font_nome.render(item_hover[0].nome, True, (255, 180, 180))
                        screen.blit(texto, (descricao_rect.x + 10, descricao_rect.y + 10))
                    
                    dano, peso, raridade, defesa = (item_hover[0].ataque, item_hover[0].peso, item_hover[0].raridade, item_hover[0].defesa)
                    status_arma = [f"Dano: {dano}", f"Peso: {peso}", f"Defesa: {defesa}", f"Raridade: {raridade}"]
                    for i, status in enumerate(status_arma):
                        if len(status) >= 13:
                            status = status.split()
                            for i2, status2 in enumerate(status):
                                texto = font_nome.render(status2, True, (255, 255, 255))
                                screen.blit(texto, (descricao_rect.x + 10, descricao_rect.y + 80 + (i + i2) * 40))
                        else:
                            texto = font_nome.render(status, True, (255, 255, 255))
                            screen.blit(texto, (descricao_rect.x + 10, descricao_rect.y + 80 + i * 40))

            for equipamento in dados["inventario"]["equipado"]:
                for item in itens:
                    if equipamento[0] == item.nome and equipamento[1] == item.raridade:
                        buff_vida += item.vida
                        buff_estamina += item.peso
                        buff_dano += item.ataque
                        buff_defesa += item.defesa


            vida_text = font_vida.render(str(dados["status"]["vida"] * 5 + buff_vida), True, (240, 100, 100))
            estamina_text = font_vida.render(str(dados["status"]["dano"] * 2 - buff_estamina), True, (140, 255, 140))
            dano_text = font_vida.render(str(dados["status"]["dano"] + buff_dano), True, (240, 100, 100))
            defesa_text = font_vida.render(str(dados["status"]["defesa"] + buff_defesa), True, (160, 160, 255))
            dinheiro_text = font_vida.render(str(dados["inventario"]["dinheiro"]), True, (255, 255, 150))


            screen.blit(vida_text, (420, 740))
            screen.blit(estamina_text, (670, 740))
            screen.blit(dano_text, (430, 830))
            screen.blit(defesa_text, (600, 830))
            screen.blit(dinheiro_text, (410, 665))
                        
                                    
                        
                                    

                        

                

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

            if key[mapa] and not travar_mapa:
                travar_mapa = True
                contador = 0
                estado = MAPA
            if not key[mapa]:
                travar_mapa = False

        if estado == MAPA:
            screen.blit(chao, (pos_chao_x, pos_chao_y))
            rect.x = personagem_x - (len(list(primeiro_nome)) * 6)
            nome_rect.x = personagem_x - (len(list(primeiro_nome)) * 2)
            nome_rect.y = personagem_y - 40

            buff_vida = 0
            buff_estamina = 0
            buff_dano = 0
            buff_defesa = 0

            quadrado_7.fill((0, 200, 0))
            personagem = pygame.Rect(personagem_x, personagem_y, 50, 50)
            for obj in pach_objects_intamgible:
                screen.blit(obj.imagem_pach, (obj.x, obj.y))
            screen.blit(quadrado_7, (personagem_x, personagem_y))
            for obj in pach_objects:
                screen.blit(obj.imagem_pach, (obj.x, obj.y))
                    
            # Desenha o retângulo cinza atrás do nome
            pygame.draw.rect(screen, (100, 100, 100), rect, border_radius=5)

            # Desenha o texto do nome por cima do retângulo
            screen.blit(nome, nome_rect)


            item_x = 1800
            item_y = 250
            # icon do inventario
            screen.blit(inventario_icon, (1800, 250))
            screen.blit(inventario_icon, (1800, 370))
            screen.blit(inventario_icon, (1800, 490))
            screen.blit(inventario_icon, (1800, 610))
            screen.blit(inventario_icon, (1800, 730))

            for equipamento in dados["inventario"]["equipado"]:
                for i, item in enumerate(itens):
                    if item.nome == equipamento[0] and item.raridade == equipamento[1] and item.type != "comum" and item.type != "defesa":
                        screen.blit(itens_icons[i], (1800, item_y))
                        item_y += 120

            
            quadrado_3.fill((*(0, 0, 0), 150))
            screen.blit(quadrado_3, (0, 0))
            pygame.draw.rect(screen, (200, 200, 200), (350, 50, 1220, 980), border_radius=20)
            screen.blit(mapa_img, (500, 100))

            if botoes[0] and not botao_segurado:  # clique esquerdo
                botao_segurado = True
                if not marcado:
                    pos_atual_mouse = pygame.mouse.get_pos()
                    marcado = True
                else:
                    marcado = False
            
            if not botoes[0]:
                botao_segurado = False
            
            if marcado and pos_atual_mouse[0] in range(500, 1380) and pos_atual_mouse[1] in range(100, 980):
                pygame.draw.circle(screen, (140, 20, 20), pos_atual_mouse, 10)
                loc_marcado = pos_atual_mouse
            loc_personagem = (
                            (( (personagem_x - pos_chao_x) * (1380 - 500)) // 19200 + 500),
                            (( (personagem_y - pos_chao_y) * (980 - 100)) // 10800 + 100)
                             )
            pygame.draw.circle(screen, (20, 20, 90), (loc_personagem[0], loc_personagem[1]), 10)

            

            for item in itens:
                if not (item.type == "defesa") or item.nome not in (equipamento[0] for equipamento in dados["inventario"]["equipado"]):
                    item.x = 912 * LARGURA // 1920
                    item.y = 147 * ALTURA // 1080
            mesma_linha = 0
            item_hover = None  # <- guarda qual item o mouse está em cima
            pos_x, pos_y = item.x, item.y




            # ESCAPE → abre opções
            if key[pygame.K_ESCAPE] and not click:
                click = True
                contador = 0
                estado = JOGO
            if not key[pygame.K_ESCAPE]:
                click = False

            # INVENTÁRIO → abre inventário
            if key[inventario] and not click_e:
                click_e = True
                contador = 0
                estado = INVENTARIO
            if not key[inventario]:
                click_e = False

            
            if key[mapa] and not travar_mapa:
                travar_mapa = True
                contador = 0
                estado = JOGO
            if not key[mapa]:
                travar_mapa = False
                
            

            
        pygame.display.flip()
        clock.tick(32)

    pygame.quit()