import pygame
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from menus import desenhar_botao, font_title, TEXTO_S, obter_id_usuario_por_nome
import sqlite3
import pyautogui
from subprocess import Popen
import json
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from recursos.imagens.telas.telas import telas


LARGURA, ALTURA = pyautogui.size()
endereço = os.path.dirname(os.path.abspath(__file__))
endereco_frontend = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

if __name__ == "__main__":
    if not os.path.exists(rf"{endereco_frontend}\ui\usuario.json"):
        Popen([sys.executable, rf'{endereco_frontend}\ui\menus.py'])
        sys.exit()

endereco_banco_de_dados = rf"{endereco_frontend}\ui\banco_de_dados.db"

imagem_personagem = pygame.image.load(rf"{endereco_frontend}\recursos\Imagens\classes\personagem_parado1.png")
imagem_personagem = pygame.transform.scale(imagem_personagem, (LARGURA // 4, ALTURA // 3))

imagem_fundo = pygame.image.load(rf"{endereco_frontend}\recursos\Imagens\classes\fundo.png")
imagem_fundo = pygame.transform.scale(imagem_fundo, (LARGURA, ALTURA))
font_title = pygame.font.Font(rf"{endereco_frontend}\recursos\fontes\Minha fonte.ttf", 100)
font_nome = pygame.font.Font(rf"{endereco_frontend}\recursos\fontes\Minha fonte.ttf", 27)

with open(rf"{endereco_frontend}\ui\usuario.json", "r") as arquivo:
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
fonte_input = pygame.font.Font(f"{endereco_frontend}/recursos/fontes/Minha fonte.ttf", 25)
fonte_T_input = pygame.font.Font(f"{endereco_frontend}/recursos/fontes/Minha fonte.ttf", 27)

nome = font_nome.render(f"{primeiro_nome}", True, (230, 230, 230))

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
                                {"label": "Inventario", "rect": pygame.Rect(446, 414, 472, 135), "text": f"{dados["keys"]["inventario"]}", "active": False, "peritido": TEXTO_S},
                                {"label": "Correr", "rect": pygame.Rect(446, 599, 473, 139), "text": f"{dados["keys"]["correr"]}", "active": False, "peritido": TEXTO_S},
                                {"label": "Habilidades", "rect": pygame.Rect(446, 794, 473, 136), "text": f"{dados["keys"]["habilidade"]}", "active": False, "peritido": TEXTO_S},
                                {"label": "Habilidade 1", "rect": pygame.Rect(1002, 414, 471, 135), "text": f"{dados["keys"]["habilidade_1"]}", "active": False, "peritido": TEXTO_S},
                                {"label": "Habilidade 2", "rect": pygame.Rect(1002, 597, 478, 138), "text": f"{dados["keys"]["habilidade_2"]}", "active": False, "peritido": TEXTO_S},
                                {"label": "Mapa", "rect": pygame.Rect(1002, 794, 472, 136), "text": f"{dados["keys"]["mapa"]}", "active": False, "peritido": TEXTO_S},
                            ]

id_usuario = obter_id_usuario_por_nome(dados["usuario"])
def salvar(teclas, dado=dados):
    global id_usuario
    dado["keys"] = teclas

    # Converte inventário para JSON se for lista
    if isinstance(dado["inventario"]["item"], list):
        dado["inventario"]["item"] = json.dumps(dado["inventario"]["item"], ensure_ascii=False)
        
    if isinstance(dado["inventario"]["equipado"], list):
        dado["inventario"]["equipado"] = json.dumps(dado["inventario"]["equipado"], ensure_ascii=False)

    # Salva no arquivo JSON
    with open(rf"{endereço}\usuario.json", "w", encoding="utf-8") as arquivo:
        json.dump(dado, arquivo, indent=4, ensure_ascii=False)

    # Conecta no SQLite
    conexao = sqlite3.connect(endereco_banco_de_dados)
    cursor = conexao.cursor()

    # Atualiza dado do usuário
    cursor.execute("""
        UPDATE usuarios
        SET nome = ?, classe = ?
        WHERE id = ?
    """, (dado["usuario"], dado["dados_pessoais"]["Classe"], id_usuario))

    # Atualiza status
    cursor.execute("""
        UPDATE status
        SET nivel = ?, dano = ?, velocidade = ?, defesa = ?, vida = ?, experiencia = ?
        WHERE usuario_id = ?
    """, (
        dado["status"]["nivel"],
        dado["status"]["dano"],
        dado["status"]["velocidade"],
        dado["status"]["defesa"],
        dado["status"]["vida"],
        dado["status"]["experiencia"],
        id_usuario
    ))

    # Atualiza progresso
    cursor.execute("""
        UPDATE progresso
        SET capitulo = ?, missao = ?
        WHERE usuario_id = ?
    """, (dado["progresso"]["capitulo"], dado["progresso"]["missao"], id_usuario))

    # Atualiza inventário
    cursor.execute("""
        UPDATE inventario
        SET item = ?, item_equipado = ?, dinheiro = ?
        WHERE usuario_id = ?
    """, (dado["inventario"]["item"], dado["inventario"]["equipado"], dado["inventario"]["dinheiro"], id_usuario))

    # Atualiza teclas
    cursor.execute("""
        UPDATE keys
        SET inventario = ?, correr = ?, habilidades = ?, habilidade_1 = ?, habilidade_2 = ?, mapa = ?
        WHERE usuario_id = ?
    """, (
        teclas["inventario"],
        teclas["correr"],
        teclas["habilidade"],
        teclas["habilidade_1"],
        teclas["habilidade_2"],
        teclas["mapa"],
        id_usuario
    ))

    conexao.commit()
    conexao.close()

    if isinstance(dado["inventario"]["item"], str):
        dado["inventario"]["item"] = json.loads(dado["inventario"]["item"])
        
    if isinstance(dado["inventario"]["equipado"], str):
        dado["inventario"]["equipado"] = json.loads(dado["inventario"]["equipado"])


rect_fundo = pygame.Surface((LARGURA, ALTURA), pygame.SRCALPHA)
rect_fundo.fill((*(30, 30, 30), 120))

rect_fundo2 = pygame.Surface((LARGURA, ALTURA), pygame.SRCALPHA)
rect_fundo2.fill((*(30, 30, 30), 180))

def confirmar_sair():
    while True:
        screen.blit(imagem_fundo, (0, 0))
        screen.blit(rect_fundo2, (0, 0))
        screen.blit(telas[13], (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.music.play(0)
                pygame.quit()
                sys.exit()

        if desenhar_botao(1043, 776, 368, 92):
            pygame.event.clear()
            return True

        if desenhar_botao(467, 776, 368, 92):
            pygame.event.clear()
            return False
        
        pygame.display.update()

travar = False

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
                    if not travar:
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
                            box["active"] = False
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

            elif not (evento.type ==  pygame.MOUSEBUTTONDOWN):
                travar = False
                            
        
        if estado == MENU:
            screen.blit(imagem_fundo, (0, 0))
            screen.blit(rect_fundo, (0, 0))
            screen.blit(telas[11], (0, 0))


            
            # Desenha o texto do nome por cima do retângulo
            screen.blit(nome, ((1715 - 1379) // 2 - nome.get_size()[0] // 2 + 1379, (801 - 741) // 2 - nome.get_size()[1] // 2 + 750))

            if desenhar_botao(830, 560, 394, 106):
                if confirmar_sair():
                    pygame.quit()
                    if os.path.exists(rf"{endereço}\usuario.json"):
                        os.remove(rf"{endereço}\usuario.json")
                    Popen([sys.executable, rf'{endereço}\menus.py'])
                    sys.exit()
            
            if desenhar_botao(676, 560, 145, 106):
                estado = OPCOES
                travar = True

            if desenhar_botao(676, 419, 548, 99):
                pygame.quit()
                Popen([sys.executable, rf'{endereco_frontend}\main.py'])
                sys.exit()
            
        if estado == OPCOES:
            screen.blit(imagem_fundo, (0, 0))
            screen.blit(rect_fundo, (0, 0))

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
                telas_opicao = telas[26]
            else:
                telas_opicao = telas[22]

            screen.blit(telas_opicao, (0, 0))

            if desenhar_botao(25, 996, 299, 74):
                input_boxes = [
                                {"label": "Inventario", "rect": pygame.Rect(446, 414, 472, 135), "text": f"{dados["keys"]["inventario"]}", "active": False, "peritido": TEXTO_S},
                                {"label": "Correr", "rect": pygame.Rect(446, 599, 473, 139), "text": f"{dados["keys"]["correr"]}", "active": False, "peritido": TEXTO_S},
                                {"label": "Habilidades", "rect": pygame.Rect(446, 794, 473, 136), "text": f"{dados["keys"]["habilidade"]}", "active": False, "peritido": TEXTO_S},
                                {"label": "Habilidade 1", "rect": pygame.Rect(1002, 414, 471, 135), "text": f"{dados["keys"]["habilidade_1"]}", "active": False, "peritido": TEXTO_S},
                                {"label": "Habilidade 2", "rect": pygame.Rect(1002, 597, 478, 138), "text": f"{dados["keys"]["habilidade_2"]}", "active": False, "peritido": TEXTO_S},
                                {"label": "Mapa", "rect": pygame.Rect(1002, 794, 472, 136), "text": f"{dados["keys"]["mapa"]}", "active": False, "peritido": TEXTO_S},
                            ]
                estado = MENU


            if desenhar_botao(1603, 990, 300, 74):
                if telas_opicao == telas[26]:
                    teclas["inventario"] = input_boxes[0]["text"]
                    teclas["correr"] = input_boxes[1]["text"]
                    teclas["habilidade"] = input_boxes[2]["text"]
                    teclas["habilidade_1"] = input_boxes[3]["text"]
                    teclas["habilidade_2"] = input_boxes[4]["text"]
                    teclas["mapa"] = input_boxes[5]["text"]
                    salvar(teclas)
                    estado = MENU

            
            for i, box in enumerate(input_boxes):
                box["text"] = box["text"].title()
                
                # Label
                label_surface = fonte_T_input.render(box["label"] + ":" if i <= 2 else ":" + box["label"], True, (230, 230, 230))
                screen.blit(label_surface, (box["rect"].x + 20 if i <= 2 else box["rect"].x + 120, box["rect"].y + 40))

                # Texto
                if len(box["text"]) == 4 and not box["active"]:
                    fonte_input = pygame.font.Font(f"{endereco_frontend}/recursos/fontes/Minha fonte.ttf", 22)
                elif len(box["text"]) == 5 and not box["active"]:
                    fonte_input = pygame.font.Font(f"{endereco_frontend}/recursos/fontes/Minha fonte.ttf", 18)
                else:
                    fonte_input = pygame.font.Font(f"{endereco_frontend}/recursos/fontes/Minha fonte.ttf", 25)
                texto_surface = fonte_input.render(box["text"] if not box["active"] else "_", True, (230, 230, 230))
                screen.blit(texto_surface, (box["rect"].x + 360 if i <= 2 else box["rect"].x + 30, box["rect"].y + 40))


        pygame.display.flip()
        clock.tick(16)

    sys.exit()