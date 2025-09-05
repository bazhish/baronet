import pygame
from sys import path
from os import path as path_os
path.append(path_os.abspath(path_os.join(path_os.dirname(__file__), '..', '..')))
from frontend.recursos.imagens.itens.drops import *

class item_ataque:
    def __init__(self, x, y, nome, ataque, defesa, velocidade, descricao, imagem_path):
        self.posicao_x = x
        self.posicao_y = y
        self.nome = nome
        self.ataque = ataque
        self.defesa = defesa
        self.velocidade = velocidade
        self.descricao = descricao
        self.imagem = pygame.image.load(imagem_path)
    
    def rect(self):
        return self.imagem.get_rect()
    
class item:
    def __init__(self, x, y, nome, descricao, imagem_path):
        self.posicao_x = x
        self.posicao_y = y
        self.nome = nome
        self.descricao = descricao
        self.imagem = pygame.image.load(imagem_path)

    def rect(self):
        return self.imagem.get_rect()
    
class item_utilizavel:
    def __init__(self, x, y, nome, descricao, efeito, imagem_path):
        self.posicao_x = x
        self.posicao_y = y
        self.nome = nome
        self.descricao = descricao
        self.efeito = efeito
        self.imagem = pygame.image.load(imagem_path)

    def rect(self):
        return self.imagem.get_rect()
    
endereço = path_os.abspath(path_os.join(path_os.dirname(__file__), '..', '..'))
endereço = endereço + "\frontend\recursos\imagens\itens"

itens = []


