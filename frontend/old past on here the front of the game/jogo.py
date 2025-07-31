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

LARGURA, ALTURA = pyautogui.size()
endereço = os.path.dirname(os.path.abspath(__file__))

if __name__ == "__main__":
    if not os.path.exists(rf"{endereço}\usuario.json"):
        Popen([sys.executable, rf'{endereço}\tela_criacao_personagem.py'])
        sys.exit()

endereco_banco_de_dados = rf"{endereço}\banco_de_dados.db"

with open(rf"{endereço}\usuario.json", "r") as arquivo:
    dados = json.load(arquivo)

teclas = dados["keys"]

pygame.init()
clock = pygame.time.Clock()

# Estados
JOGO = "jogo"
OPCOES = "opcoes"
MENU = "menu"
INVENTARIO = "inventario"
estado = JOGO

quadrado = pygame.Surface((LARGURA, ALTURA), pygame.SRCALPHA)
quadrado_2 = pygame.Surface((LARGURA, ALTURA), pygame.SRCALPHA)
quadrado_3 = pygame.Surface((LARGURA, ALTURA), pygame.SRCALPHA)
contador = 0
rect_opcoes = pygame.Rect(LARGURA // 2.5, LARGURA // 1.5, ALTURA // 1.6, ALTURA // 2)
click = False
click_e = False

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
                                box["text"] = "Alt"
                            if mods & pygame.KMOD_CAPS:
                                box["text"] = "Caps"
                            if mods & pygame.KMOD_CTRL:
                                box["text"] = "Ctrl"
                            if mods & pygame.KMOD_SHIFT:
                                box["text"] = "Shift"
                            if evento.key == pygame.K_TAB:
                                box["text"] = "Tab"

        key = pygame.key.get_pressed()

        if estado == JOGO:
            screen.fill((210, 210, 210))
            if key[pygame.K_ESCAPE] and not click:
                click = True
                contador = 0
                estado = OPCOES
            if not key[pygame.K_ESCAPE]:
                click = False
            if key[pygame.K_e] and not click_e:
                click_e = True
                contador = 0
                estado = INVENTARIO
            if not key[pygame.K_e]:
                click_e = False

        if estado == OPCOES:
            if key[pygame.K_ESCAPE] and not click:
                click = True
                estado = JOGO
            if not key[pygame.K_ESCAPE]:
                click = False
            if contador == 0:
                quadrado.fill((*(0, 0, 0), 150))
                screen.blit(quadrado, (0, 0))
            contador += 1
            rect_box = pygame.Rect(LARGURA // 3, ALTURA // 6, LARGURA // 3, ALTURA // 1.4)
            pygame.draw.rect(screen, (180, 180, 180), rect_box, border_radius=15)

            if desenhar_botao("Continuar", LARGURA // 2.86, ALTURA // 4.7, LARGURA // 3.3, ALTURA // 8, ALTURA // 18, (150, 150, 150), (120, 120, 120), ALTURA // 30, fonte= ALTURA // 18):
                estado = JOGO

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
                                {"label": "Habilidade 3", "rect": pygame.Rect(LARGURA // 1.8, ALTURA // 4 + ALTURA // 10 + ALTURA // 10 + ALTURA // 10 + ALTURA // 10 + ALTURA // 10, LARGURA // 18, ALTURA // 16), "text": f"{dados["keys"]["habilidade_3"]}", "active": False, "peritido": TEXTO_S},
                                {"label": "Mapa", "rect": pygame.Rect(LARGURA // 1.8, ALTURA // 4 + ALTURA // 10 + ALTURA // 10 + ALTURA // 10 + ALTURA // 10 + ALTURA // 10 + ALTURA // 10, LARGURA // 18, ALTURA // 16), "text": f"{dados["keys"]["mapa"]}", "active": False, "peritido": TEXTO_S},
                            ]
                estado = JOGO
            
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
                input_boxes[5]["text"] != teclas["habilidade_3"] or
                input_boxes[6]["text"] != teclas["mapa"]
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
                    teclas["habilidade_3"] = input_boxes[5]["text"]
                    teclas["mapa"] = input_boxes[6]["text"]
                    salvar()
                    estado = MENU

            
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
            
            if key[pygame.K_e] and not click_e:
                click_e = True
                estado = JOGO
            if not key[pygame.K_e]:
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

        
        
