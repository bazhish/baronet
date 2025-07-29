import pygame
import sys
import os
from random import choice
from tela_criacao_personagem import desenhar_botao, font_title, TEXTO_S, obter_id_usuario_por_nome
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

# Cores
COR_ATIVA = (0, 120, 215)
COR_INATIVA = (150, 150, 150)
COR_TEXTO = (0, 0, 0)
COR_BG = (255, 255, 255)

# Fontes
fonte_input = pygame.font.SysFont("arial", LARGURA // 40)

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

input_boxes = [
                {"label": "Inventario", "rect": pygame.Rect(LARGURA // 1.8, ALTURA // 4, LARGURA // 18, ALTURA // 16), "text": f"{dados["keys"]["inventario"]}", "active": False, "peritido": TEXTO_S},
                {"label": "Correr", "rect": pygame.Rect(LARGURA // 1.8, ALTURA // 4 + ALTURA // 10, LARGURA // 18, ALTURA // 16), "text": f"{dados["keys"]["correr"]}", "active": False, "peritido": TEXTO_S},
                {"label": "Habilidades", "rect": pygame.Rect(LARGURA // 1.8, ALTURA // 4 + ALTURA // 10 + ALTURA // 10, LARGURA // 18, ALTURA // 16), "text": f"{dados["keys"]["habilidade"]}", "active": False, "peritido": TEXTO_S},
                {"label": "Habilidade 1", "rect": pygame.Rect(LARGURA // 1.8, ALTURA // 4 + ALTURA // 10 + ALTURA // 10 + ALTURA // 10, LARGURA // 18, ALTURA // 16), "text": f"{dados["keys"]["habilidade_1"]}", "active": False, "peritido": TEXTO_S},
                {"label": "Habilidade 2", "rect": pygame.Rect(LARGURA // 1.8, ALTURA // 4 + ALTURA // 10 + ALTURA // 10 + ALTURA // 10 + ALTURA // 10, LARGURA // 18, ALTURA // 16), "text": f"{dados["keys"]["habilidade_2"]}", "active": False, "peritido": TEXTO_S},
                {"label": "Habilidade 3", "rect": pygame.Rect(LARGURA // 1.8, ALTURA // 4 + ALTURA // 10 + ALTURA // 10 + ALTURA // 10 + ALTURA // 10 + ALTURA // 10, LARGURA // 18, ALTURA // 16), "text": f"{dados["keys"]["habilidade_3"]}", "active": False, "peritido": TEXTO_S},
                {"label": "Mapa", "rect": pygame.Rect(LARGURA // 1.8, ALTURA // 4 + ALTURA // 10 + ALTURA // 10 + ALTURA // 10 + ALTURA // 10 + ALTURA // 10 + ALTURA // 10, LARGURA // 18, ALTURA // 16), "text": f"{dados["keys"]["mapa"]}", "active": False, "peritido": TEXTO_S},
            ]

id_usuario = obter_id_usuario_por_nome(dados["usuario"])

def salvar():
    global id_usuario
    dados["keys"] = teclas
    with open(rf"{endereço}\usuario.json", "w") as arquivo:
        json.dump(dados, arquivo, indent=4)
    conexao = sqlite3.connect(endereco_banco_de_dados)
    cursor = conexao.cursor()

    cursor.execute("""
        UPDATE usuarios
        SET nome = ?, idade = ?, altura = ?, peso = ?, genero = ?, classe = ?
        WHERE id = ?
    """, (dados["usuario"], dados["dados_pessoais"]["Idade"], dados["dados_pessoais"]["Altura"], dados["dados_pessoais"]["Peso"], dados["dados_pessoais"]["Genero"], dados["dados_pessoais"]["Classe"], id_usuario))

    cursor.execute("""
        UPDATE status
        SET nivel = ?, dano = ?, velocidade = ?, defesa = ?, vida = ?, experiencia = ?
        WHERE usuario_id = ?
    """, (dados["status"]["nivel"], dados["status"]["dano"], dados["status"]["velocidade"], dados["status"]["defesa"], dados["status"]["vida"], dados["status"]["experiencia"], id_usuario))

    cursor.execute("""
        UPDATE progresso
        SET capitulo = ?, missao = ?
        WHERE usuario_id = ?
    """, (dados["progresso"]["capitulo"], dados["progresso"]["missao"], id_usuario))

    cursor.execute("""
        UPDATE inventario
        SET item = ?, quantidade = ?
        WHERE usuario_id = ?
    """, (dados["inventario"][0][0], dados["inventario"][0][1], id_usuario))

    cursor.execute("""
        UPDATE keys
        SET inventario = ?, correr = ?, habilidades = ?, habilidade_1 = ?, habilidade_2 = ?, habilidade_3 = ?, mapa = ?
        WHERE usuario_id = ?
    """, (
        teclas["inventario"],
        teclas["correr"],
        teclas["habilidade"],
        teclas["habilidade_1"],
        teclas["habilidade_2"],
        teclas["habilidade_3"],
        teclas["mapa"],
        id_usuario
    ))

    conexao.commit()
    conexao.close()

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
                        box["text"] = ""
                        if evento.key == pygame.K_BACKSPACE:
                            box["text"] = box["text"][:-1]
                        elif evento.key == pygame.K_RETURN:
                            box["active"] = False
                        else:
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
                Popen([sys.executable, rf'{endereço}\jogo.py'])
                sys.exit()
            
        if estado == OPCOES:
            screen.blit(imagem_fundo_secundario, (0, 0))

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
                estado = MENU
            
            rect_box = pygame.Rect(LARGURA // 2.7, ALTURA // 4.5, LARGURA // 3.9, ALTURA // 1.4)
            pygame.draw.rect(screen, (210, 210, 210), rect_box, border_radius=15)

            if input_boxes[0]["text"] != teclas["inventario"] or input_boxes[1]["text"] != teclas["correr"] or input_boxes[2]["text"] != teclas["habilidade"] or input_boxes[3]["text"] != teclas["habilidade_1"] or input_boxes[4]["text"] != teclas["habilidade_2"] or input_boxes[5]["text"] != teclas["habilidade_3"] or input_boxes[6]["text"] != teclas["mapa"] and input_boxes[6]["text"] != "" and input_boxes[5]["text"] != "" and input_boxes[4]["text"] != "" and input_boxes[3]["text"] != "" and input_boxes[2]["text"] != "" and input_boxes[1]["text"] != "" and input_boxes[0]["text"] != "":
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

                
        


        pygame.display.flip()
        clock.tick(16)

    sys.exit()