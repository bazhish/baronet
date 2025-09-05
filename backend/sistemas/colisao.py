import pygame
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from frontend.recursos.imagens.cenario.cenario_explorar import arbusto_0, arbusto_2, arbusto_1, arbusto_3, arvore_grande_0, arvore_grande_1, arvore_pequena_0, arvore_pequena_1, arvore_pequena_2, arvore_pequena_3, barril_0, barril_1, barril_2, cogumelo_0, pedras_0, pedras_1, pedras_2, LArgura

class arvore_pequena:
    def __init__(self, x, y, largura, altura, imagem_pach):
        self.x = x * LArgura // 1920
        self.y = y * LArgura // 1920
        self.largura =  largura * LArgura // 1920
        self.altura = altura * LArgura // 1920
        self.imagem_pach = imagem_pach

    def hit_box(self):
        self.top_left = 32 * LArgura // 1920 + self.x, 156 * LArgura // 1920 + self.y
        self.top_right = 92 * LArgura // 1920 + self.x, 156 * LArgura // 1920 + self.y
        self.bottom_left = 32 * LArgura // 1920 + self.x, 176 * LArgura // 1920 + self.y
        self.bottom_right = 92 * LArgura // 1920 + self.x, 176 * LArgura // 1920 + self.y
        return (self.top_left, self.top_right, self.bottom_left, self.bottom_right)
    
    def rect(self):
        """Retorna um pygame.Rect para usar na colisão"""
        return pygame.Rect(32 * LArgura // 1920 + self.x, 156 * LArgura // 1920 + self.y, 60 * LArgura // 1920, 20 * LArgura // 1920)
    
class arvore_grande:
    def __init__(self, x, y, largura, altura, imagem_pach):
        self.x = x * LArgura // 1920
        self.y = y * LArgura // 1920
        self.largura =  largura * LArgura // 1920
        self.altura = altura * LArgura // 1920
        self.imagem_pach = imagem_pach

    def hit_box(self):
        self.top_left = 20 * LArgura // 1920 + self.x, 136 * LArgura // 1920 + self.y
        self.top_right = 160 * LArgura // 1920 + self.x, 136 * LArgura // 1920 + self.y
        self.bottom_left = 20 * LArgura // 1920 + self.x, 172 * LArgura // 1920 + self.y
        self.bottom_right = 160 * LArgura // 1920 + self.x, 172 * LArgura // 1920 + self.y
        return (self.top_left, self.top_right, self.bottom_left, self.bottom_right)
    
    def rect(self):
        """Retorna um pygame.Rect para usar na colisão"""
        return pygame.Rect(30 * LArgura // 1920 + self.x, 300 * LArgura // 1920 + self.y, 200 * LArgura // 1920, 60 * LArgura // 1920)
    
class barril:
    def __init__(self, x, y, largura, altura, imagem_pach):
        self.x = x * LArgura // 1920
        self.y = y * LArgura // 1920
        self.largura =  largura * LArgura // 1920
        self.altura = altura * LArgura // 1920
        self.imagem_pach = imagem_pach

    def hit_box(self):
        self.top_left = 0 + self.x, 18 * LArgura // 1920 + self.y
        self.top_right = 23 * LArgura // 1920 + self.x, 18 * LArgura // 1920 + self.y
        self.bottom_left = 0 + self.x, 28 * LArgura // 1920 + self.y
        self.bottom_right = 23 * LArgura // 1920 + self.x, 28 * LArgura // 1920 + self.y
        return (self.top_left, self.top_right, self.bottom_left, self.bottom_right)
    
    def rect(self):
        """Retorna um pygame.Rect para usar na colisão"""
        return pygame.Rect(0 + self.x, 82 * LArgura // 1920 + self.y, 92 * LArgura // 1920, 30 * LArgura // 1920)



#--------------------------------------------------- ÁRVORES PEQUENAS ---------------------------------------------------------------------------------
    
arvores_pequenas = [arvore_pequena(300, 200, 50, 50, arvore_pequena_0),
                    arvore_pequena(500, 400, 50, 50, arvore_pequena_1),
                    arvore_pequena(700, 300, 50, 50, arvore_pequena_2),
                    arvore_pequena(900, 500, 50, 50, arvore_pequena_3)]

arvores_pequenas_hit_boxes = [arvore.hit_box() for arvore in arvores_pequenas]

arvores_pequenas_rects = [arvore.rect() for arvore in arvores_pequenas]

#--------------------------------------------------- ÁRVORES GRANDES ---------------------------------------------------------------------------------

arvores_grandes = [arvore_grande(200, 400, 100, 100, arvore_grande_0),
                   arvore_grande(600, 400, 100, 100, arvore_grande_1)]

arvores_grandes_hit_boxes = [arvore.hit_box() for arvore in arvores_grandes]

arvores_grandes_rects = [arvore.rect() for arvore in arvores_grandes]

#--------------------------------------------------- BARRIS ---------------------------------------------------------------------------------

barris = [barril(400, 300, 50, 50, barril_0),
          barril(800, 450, 50, 50, barril_1),
          barril(1000, 350, 50, 50, barril_2)]

barris_hit_boxes = [barril.hit_box() for barril in barris]

barris_rects = [barril.rect() for barril in barris]

#--------------------------------------------------- TODOS OS OBJETOS COM COLISAO ---------------------------------------------------------------------------------

pach_objects_colision = barris + arvores_pequenas + arvores_grandes
pach_objects_hit_boxes_colision = arvores_pequenas_hit_boxes + arvores_grandes_hit_boxes + barris_hit_boxes
pach_objects_rects_colision = arvores_pequenas_rects + arvores_grandes_rects + barris_rects

#--------------------------------------------------- COM LENTIDAO ---------------------------------------------------------------------------------

class arbusto:
    def __init__(self, x, y, largura, altura, imagem_pach):
        self.x = x * LArgura // 1920
        self.y = y * LArgura // 1920
        self.largura =  largura * LArgura // 1920
        self.altura = altura * LArgura // 1920
        self.imagem_pach = imagem_pach

    def hit_box(self):
        self.top_left = 0 + self.x, 0 + self.y
        self.top_right = 48 * LArgura // 1920 + self.x, 0 + self.y
        self.bottom_left = 0 + self.x, 48 * LArgura // 1920 + self.y
        self.bottom_right = 48 * LArgura // 1920 + self.x, 48 * LArgura // 1920 + self.y
        return (self.top_left, self.top_right, self.bottom_left, self.bottom_right)
    
    def rect(self):
        """Retorna um pygame.Rect para usar na colisão"""
        return pygame.Rect(0 + self.x, 0 + self.y, 48 * LArgura // 1920, 48 * LArgura // 1920)
    
#--------------------------------------------------- ARBUSTOS ---------------------------------------------------------------------------------

arbustos = [arbusto(350, 250, 50, 50, arbusto_0),
            arbusto(750, 350, 50, 50, arbusto_1),
            arbusto(550, 450, 50, 50, arbusto_2),
            arbusto(950, 250, 50, 50, arbusto_3)]

arbustos_hit_boxes = [arbusto.hit_box() for arbusto in arbustos]

arbustos_rects = [arbusto.rect() for arbusto in arbustos]

#--------------------------------------------------- TODOS OS OBJETOS COM LENTIDAO ---------------------------------------------------------------------------------

pach_objects_colision_lentidao = arbustos
pach_objects_hit_boxes_colision_lentidao = arbustos_hit_boxes
pach_objects_rects_colision_lentidao = arbustos_rects

#--------------------------------------------------- Sem interação ---------------------------------------------------------------------------------

class cogumelo:
    def __init__(self, x, y, largura, altura, imagem_pach):
        self.x = x * LArgura // 1920
        self.y = y * LArgura // 1920
        self.largura =  largura * LArgura // 1920
        self.altura = altura * LArgura // 1920
        self.imagem_pach = imagem_pach

class pedras:
    def __init__(self, x, y, largura, altura, imagem_pach):
        self.x = x * LArgura // 1920
        self.y = y * LArgura // 1920
        self.largura =  largura * LArgura // 1920
        self.altura = altura * LArgura // 1920
        self.imagem_pach = imagem_pach

#--------------------------------------------------- COGUMELOS ---------------------------------------------------------------------------------

cogumelos = [cogumelo(450, 150, 50, 50, cogumelo_0)]

#--------------------------------------------------- PEDRAS ---------------------------------------------------------------------------------

pedras = [pedras(250, 350, 50, 50, pedras_0),
               pedras(850, 400, 50, 50, pedras_1),
                pedras(1050, 200, 50, 50, pedras_2)]

#--------------------------------------------------- TODOS OS OBJETOS SEM INTERAÇÃO ---------------------------------------------------------------------------------

pach_objects_sem_interação = cogumelos + pedras

#--------------------------------------------------- TODOS OS OBJETOS DO CENÁRIO ---------------------------------------------------------------------------------

pach_objects = pach_objects_colision_lentidao + pach_objects_colision
pach_objects_intamgible = pach_objects_sem_interação

class GerenciadorDeColisao:
    def __init__(self, arvores_pequenas, arvores_grandes, barris, arbustos, cogumelos, pedras):
        self.arvores_pequenas = arvores_pequenas
        self.arvores_grandes = arvores_grandes
        self.barris = barris
        self.arbustos = arbustos
        self.cogumelos = cogumelos
        self.pedras = pedras

        self.objetos_colisao = []
        self.objetos_lentidao = []
        self.objetos_sem_interacao = []
        self.todos_objetos = []

    def atualizar(self):
        """Atualiza listas de objetos a cada frame"""
        self.objetos_colisao = self.arvores_pequenas + self.arvores_grandes + self.barris
        self.objetos_lentidao = self.arbustos
        self.objetos_sem_interacao = self.cogumelos + self.pedras
        self.todos_objetos = self.objetos_sem_interacao + self.objetos_lentidao + self.objetos_colisao

    def colide(self, rect):
        """Verifica colisão com objetos sólidos"""
        return any(rect.colliderect(obj.rect()) for obj in self.objetos_colisao)

    def colide_lentidao(self, rect):
        """Verifica colisão com objetos que reduzem velocidade"""
        return any(rect.colliderect(obj.rect()) for obj in self.objetos_lentidao)
    
gerenciador_colisao = GerenciadorDeColisao(arvores_pequenas, arvores_grandes, barris, arbustos, cogumelos, pedras)
gerenciador_colisao.atualizar()

