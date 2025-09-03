import pygame

pygame.init()

class arvore_pequena:
    def __init__(self, x, y, largura, altura, imagem_pach):
        self.x = x
        self.y = y
        self.largura =  largura
        self.altura = altura
        self.imagem_pach = imagem_pach

    def hit_box(self, top_left, top_right, bottom_left, bottom_right):
        self.top_left = (self.x, self.y)
        self.top_right = (self.x + self.largura, self.y)
        self.bottom_left = (self.x, self.y + self.altura)
        self.bottom_right = (self.x + self.largura, self.y + self.altura)
        return (self.top_left, self.top_right, self.bottom_left, self.bottom_right)
    
