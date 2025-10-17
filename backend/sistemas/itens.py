import pygame
from pyautogui import size
from sys import path
from os import path as path_os
path.append(path_os.abspath(path_os.join(path_os.dirname(__file__), '..', '..')))
from backend.sistemas.modelos.modelos_armas import tabela_armas

LARGURA, ALTURA = size()
screen = pygame.display.set_mode((1, 1))
pygame.display.iconify()


class item_ataque:
    def __init__(self, nome, type, raridade, ataque, peso, imagem_path):
        self.x = 912 * LARGURA // 1920
        self.y = 147 * LARGURA // 1920
        self.nome = nome
        self.ataque = ataque
        self.peso = peso
        self.type = type
        self.defesa = 0
        self.vida = 0
        self.raridade = raridade
        self.imagem_pach = imagem_path
    
    def rect(self):
        return (self.x, self.y, 144 * LARGURA // 1920, 144 * LARGURA // 1920)
    
class item_atk_e_def:
    def __init__(self, nome, type, raridade, ataque, defesa, peso, imagem_path):
        self.x = 912 * LARGURA // 1920
        self.y = 147 * LARGURA // 1920
        self.nome = nome
        self.ataque = ataque
        self.peso = peso
        self.type = type
        self.defesa = defesa
        self.vida = 0
        self.raridade = raridade
        self.imagem_pach = imagem_path

    def rect(self):
        return (self.x, self.y, 144 * LARGURA // 1920, 144 * LARGURA // 1920)

class item:
    def __init__(self, nome, descricao, imagem_path):
        self.x = 912 * LARGURA // 1920
        self.y = 147 * LARGURA // 1920
        self.nome = nome
        self.type = "comum"
        self.raridade = "comum"
        self.descricao = descricao
        self.imagem_pach = imagem_path

    def rect(self):
        return (self.x, self.y, 144 * LARGURA // 1920, 144 * LARGURA // 1920)

class item_utilizavel:
    def __init__(self, nome, descricao, efeito, imagem_path):
        self.x = 912 * LARGURA // 1920
        self.y = 147 * LARGURA // 1920
        self.nome = nome
        self.descricao = descricao
        self.efeito = efeito
        self.imagem_pach = imagem_path

    def rect(self):
        return (self.x, self.y, 144 * LARGURA // 1920, 144 * LARGURA // 1920)


endereço = path_os.abspath(path_os.join(path_os.dirname(__file__), '..', '..', 'frontend', 'recursos', 'imagens', 'itens'))



itens_path = ["Carne podre.png", "Cauda.png", "cifre de Minotauro -pixilart.png", "couro.png", "dente.png","dente(1).png", "membrana de fantasma.png", "Osso.png", "tentaculo.png", "chave esqueleto.png", "escrritura antiga.png", "espada quebrada.png", "Olho especial.png",
              "Arco_flexa.png", "Espada.png", "Escudo.png", "luva.png", "lança.png", "Punho.png", "Gosma azul.png", "fruta azul.png"]
itens2 = []


for item2 in itens_path:
    itens2.append(rf"{endereço}\normal\{item2}")
itens_path.clear()

for i, item_ in enumerate(itens2):
    itens_path.append(pygame.image.load(f"{item_}").convert_alpha())
    itens_path[i] = pygame.transform.scale(itens_path[i], (144 * LARGURA // 1920, 144 * LARGURA // 1920))

del(itens2)

itens = [
    item("Carne Podre", "Um pedaço de carne estragada, cheira muito mal.", itens_path[0]),
    item("Cauda", "Uma cauda arrancada de uma criatura desconhecida.", itens_path[1]),
    item("Cifre de Minotauro", "Um chifre robusto de um minotauro lendário.", itens_path[2]),
    item("Couro", "Couro resistente, útil para fabricar armaduras.", itens_path[3]),
    item("Dente", "Um dente comum de criatura.", itens_path[4]),
    item("Dente Raro", "Um dente raro, parece ter valor especial.", itens_path[5]),
    item("Membrana de Fantasma", "Um tecido etéreo, quase transparente.", itens_path[6]),
    item("Osso", "Um osso forte, pode ser usado como material.", itens_path[7]),
    item("Tentáculo", "Um tentáculo gosmento, ainda se mexe um pouco...", itens_path[8]),
    item("Chave de Esqueleto", "Uma chave misteriosa em forma de osso, pode abrir fechaduras sombrias.", itens_path[9]),
    item("Escritura Antiga", "Um pergaminho antigo, escrito em uma língua esquecida.", itens_path[10]),
    item("Espada Quebrada", "Uma espada partida ao meio, mas ainda com um leve brilho.", itens_path[11]),
    item("Olho Especial", "Um olho mágico que parece observar tudo ao redor.", itens_path[12]),
    item("Gosma azul", "Uma substância viscosa e azulada, fria ao toque e levemente brilhante.", itens_path[19]),
    item_ataque("Arco e flexa", "ataque", "comum", tabela_armas["arco"]["comum"][0], tabela_armas["arco"]["comum"][1], itens_path[13]),
    item_ataque("Arco e flexa", "ataque", "rara", tabela_armas["arco"]["rara"][0], tabela_armas["arco"]["rara"][1], itens_path[13]),
    item_ataque("Arco e flexa", "ataque", "épica", tabela_armas["arco"]["épica"][0], tabela_armas["arco"]["épica"][1], itens_path[13]),
    item_ataque("Arco e flexa", "ataque", "lendaria", tabela_armas["arco"]["lendaria"][0], tabela_armas["arco"]["lendaria"][1], itens_path[13]),
    item_atk_e_def("Escudo", "ataque e defesa", "comum", 4, 3, 6, itens_path[15]),
    item_atk_e_def("Escudo", "ataque e defesa", "rara", 6, 4, 6, itens_path[15]),
    item_atk_e_def("Escudo", "ataque e defesa", "épica", 6, 5, 5, itens_path[15]),
    item_atk_e_def("Escudo", "ataque e defesa", "lendaria", 10, 6, 4, itens_path[15]),
    item_ataque("Espada", "ataque", "comum", tabela_armas["espada"]["comum"][0], tabela_armas["espada"]["comum"][1], itens_path[14]),
    item_ataque("Espada", "ataque", "rara", tabela_armas["espada"]["rara"][0], tabela_armas["espada"]["rara"][1], itens_path[14]),
    item_ataque("Espada", "ataque", "épica", tabela_armas["espada"]["épica"][0], tabela_armas["espada"]["épica"][1], itens_path[14]),
    item_ataque("Espada", "ataque", "lendaria", tabela_armas["espada"]["lendaria"][0], tabela_armas["espada"]["lendaria"][1], itens_path[14]),
    item_ataque("Manopla", "ataque", "comum", tabela_armas["manopla"]["comum"][0], tabela_armas["manopla"]["comum"][1], itens_path[16]),
    item_ataque("Manopla", "ataque", "rara", tabela_armas["manopla"]["rara"][0], tabela_armas["manopla"]["rara"][1], itens_path[16]),
    item_ataque("Manopla", "ataque", "épica", tabela_armas["manopla"]["épica"][0], tabela_armas["manopla"]["épica"][1], itens_path[16]),
    item_ataque("Manopla", "ataque", "lendaria", tabela_armas["manopla"]["lendaria"][0], tabela_armas["manopla"]["lendaria"][1], itens_path[16]),
    item_ataque("Lança", "ataque", "comum", tabela_armas["lança"]["comum"][0], tabela_armas["lança"]["comum"][1], itens_path[17]),
    item_ataque("Lança", "ataque", "rara", tabela_armas["lança"]["rara"][0], tabela_armas["lança"]["rara"][1], itens_path[17]),
    item_ataque("Lança", "ataque", "épica", tabela_armas["lança"]["épica"][0], tabela_armas["lança"]["épica"][1], itens_path[17]),
    item_ataque("Lança", "ataque", "lendaria", tabela_armas["lança"]["lendaria"][0], tabela_armas["lança"]["lendaria"][1], itens_path[17]),
    item_ataque("Punho", "ataque", "comum", tabela_armas["punho"]["comum"][0], tabela_armas["punho"]["comum"][1], itens_path[18]),
    item_ataque("Punho", "ataque", "rara", tabela_armas["punho"]["rara"][0], tabela_armas["punho"]["rara"][1], itens_path[18]),
    item_ataque("Punho", "ataque", "épica", tabela_armas["punho"]["épica"][0], tabela_armas["punho"]["épica"][1], itens_path[18]),
    item_ataque("Punho", "ataque", "lendaria", tabela_armas["punho"]["lendaria"][0], tabela_armas["punho"]["lendaria"][1], itens_path[18]),
    item_atk_e_def("Capacete de couro", "defesa", "comum", 0, 5, 1, itens_path[12]),
    item("Fruta azul", "Uma fruta rara que cresce na floresta Wode of Blod.", itens_path[20])
]

itens_icons = [item1.imagem_pach for item1 in itens]
for i, item1 in enumerate(itens_icons):
    itens_icons[i] = pygame.transform.scale(item1, (100 * LARGURA // 1920, 100 * LARGURA // 1920))