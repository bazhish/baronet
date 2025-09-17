import pygame
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from frontend.recursos.imagens.cenario.cenario_explorar import arbusto_0, arbusto_2, arbusto_1, arbusto_3, arvore_grande_0, arvore_grande_1, arvore_pequena_0, arvore_pequena_1, arvore_pequena_2, arvore_pequena_3, barril_0, barril_1, barril_2, cogumelo_0, pedras_0, pedras_1, pedras_2, pedras_3, LArgura, casa_pequena0

class arvore_pequena:
    def __init__(self, x, y, largura, altura, imagem_pach, pos_chao_x, pos_chao_y):
        self.x = x * LArgura // 1920
        self.y = y * LArgura // 1920
        self.pos_chao_x = pos_chao_x
        self.pos_chao_y = pos_chao_y
        self.largura =  largura * LArgura // 1920
        self.altura = altura * LArgura // 1920
        self.imagem_pach = imagem_pach
        self.bottom_left = 150
        self.bottom_rith = 33
    
    def rect(self):
        """Retorna um pygame.Rect para usar na colisão"""
        return pygame.Rect(32 * LArgura // 1920 + (((self.x - 500) * 19200) // (1380 - 500) + self.pos_chao_x),
                            156 * LArgura // 1920 + (((self.y - 100) * 19200) // (980 - 100) + self.pos_chao_y),
                              60 * LArgura // 1920, 20 * LArgura // 1920)
    
class arvore_grande:
    def __init__(self, x, y, largura, altura, imagem_pach, pos_chao_x, pos_chao_y):
        self.x = x * LArgura // 1920
        self.y = y * LArgura // 1920
        self.pos_chao_x = pos_chao_x
        self.pos_chao_y = pos_chao_y
        self.largura =  largura * LArgura // 1920
        self.altura = altura * LArgura // 1920
        self.imagem_pach = imagem_pach
        self.bottom_left = 300
        self.bottom_rith = 30
    
    def rect(self):
        """Retorna um pygame.Rect para usar na colisão"""
        return pygame.Rect(30 * LArgura // 1920 + (((self.x - 500) * 19200) // (1380 - 500) + self.pos_chao_x),
                            300 * LArgura // 1920 + (((self.y - 100) * 19200) // (980 - 100) + self.pos_chao_y),
                              200 * LArgura // 1920, 60 * LArgura // 1920)
    
class barril:
    def __init__(self, x, y, largura, altura, imagem_pach, pos_chao_x, pos_chao_y):
        self.x = x * LArgura // 1920
        self.y = y * LArgura // 1920
        self.pos_chao_x = pos_chao_x
        self.pos_chao_y = pos_chao_y
        self.largura =  largura * LArgura // 1920
        self.altura = altura * LArgura // 1920
        self.imagem_pach = imagem_pach
        self.bottom_left = 48
        self.bottom_rith = 0
    
    def rect(self):
        """Retorna um pygame.Rect para usar na colisão"""
        return pygame.Rect(0 + (((self.x - 500) * 19200) // (1380 - 500) + self.pos_chao_x),
                            45 * LArgura // 1920 + (((self.y - 100) * 19200) // (980 - 100) + self.pos_chao_y),
                            40 * LArgura // 1920, 15 * LArgura // 1920)

class casa_pequena:
    def __init__(self, x, y, largura, altura, imagem_pach, pos_chao_x, pos_chao_y):
        self.x = x * LArgura // 1920
        self.y = y * LArgura // 1920
        self.pos_chao_x = pos_chao_x
        self.pos_chao_y = pos_chao_y
        self.largura =  largura * LArgura // 1920
        self.altura = altura * LArgura // 1920
        self.imagem_pach = imagem_pach
        self.bottom_left = 170
        self.bottom_rith = 25
    
    def rect(self):
        """Retorna um pygame.Rect para usar na colisão"""
        return pygame.Rect(20 * LArgura // 1920 + (((self.x - 500) * 19200) // (1380 - 500) + self.pos_chao_x),
                            170 * LArgura // 1920 + (((self.y - 100) * 19200) // (980 - 100) + self.pos_chao_y),
                              243 * LArgura // 1920, 90 * LArgura // 1920)


#--------------------------------------------------- ÁRVORES PEQUENAS ---------------------------------------------------------------------------------
    
arvores_pequenas = [arvore_pequena(300, 200, 60 * LArgura // 1920, 20 * LArgura // 1920, arvore_pequena_0, -3500, -3500),
                    arvore_pequena(500, 400, 60 * LArgura // 1920, 20 * LArgura // 1920, arvore_pequena_1, -3500, -3500),
                    arvore_pequena(700, 300, 60 * LArgura // 1920, 20 * LArgura // 1920, arvore_pequena_2, -3500, -3500),
                    arvore_pequena(900, 500, 60 * LArgura // 1920, 20 * LArgura // 1920, arvore_pequena_3, -3500, -3500)]

arvores_pequenas_rects = [arvore.rect() for arvore in arvores_pequenas]

#--------------------------------------------------- ÁRVORES GRANDES ---------------------------------------------------------------------------------

arvores_grandes = [arvore_grande(200, 400, 200 * LArgura // 1920, 60 * LArgura // 1920, arvore_grande_0, -3500, -3500),
                   arvore_grande(600, 400, 200 * LArgura // 1920, 60 * LArgura // 1920, arvore_grande_1, -3500, -3500)]

arvores_grandes_rects = [arvore.rect() for arvore in arvores_grandes]

#--------------------------------------------------- BARRIS ---------------------------------------------------------------------------------

barris = [barril(400, 550, 40 * LArgura // 1920, 15 * LArgura // 1920, barril_0, -3500, -3500),
          barril(800, 450, 40 * LArgura // 1920, 15 * LArgura // 1920, barril_1, -3500, -3500),
          barril(1000, 350, 40 * LArgura // 1920, 15 * LArgura // 1920, barril_2, -3500, -3500)]

barris_rects = [barril.rect() for barril in barris]


#--------------------------------------------------- CASA PEQUENA ---------------------------------------------------------

casas_pequena = [casa_pequena(800, 500, 243 * LArgura // 1920, 90 * LArgura // 1920, casa_pequena0, -3500, -3500)]  # Exemplo de posição e tamanho

casas_pequena_rect = [casa.rect() for casa in casas_pequena]
#--------------------------------------------------- TODOS OS OBJETOS COM COLISAO ---------------------------------------------------------------------------------

pach_objects_colision = barris + arvores_pequenas + arvores_grandes + casas_pequena
pach_objects_rects_colision = arvores_pequenas_rects + arvores_grandes_rects + barris_rects + casas_pequena_rect

#--------------------------------------------------- COM LENTIDAO ---------------------------------------------------------------------------------

class arbusto:
    def __init__(self, x, y, largura, altura, imagem_pach, pos_chao_x, pos_chao_y):
        self.x = x * LArgura // 1920
        self.y = y * LArgura // 1920
        self.pos_chao_x = pos_chao_x
        self.pos_chao_y = pos_chao_y
        self.largura =  largura * LArgura // 1920
        self.altura = altura * LArgura // 1920
        self.imagem_pach = imagem_pach
        self.bottom_left = 48
        self.bottom_rith = 30
    
    def rect(self):
        """Retorna um pygame.Rect para usar na colisão"""
        return pygame.Rect(0 + (((self.x - 500) * 19200) // (1380 - 500) + self.pos_chao_x),
                            0 + (((self.y - 100) * 19200) // (980 - 100) + self.pos_chao_y),
                            48 * LArgura // 1920, 48 * LArgura // 1920)
    
#--------------------------------------------------- ARBUSTOS ---------------------------------------------------------------------------------

arbustos = [arbusto(350, 250, 50, 50, arbusto_0, -3500, -3500),
            arbusto(750, 350, 50, 50, arbusto_1, -3500, -3500),
            arbusto(550, 450, 50, 50, arbusto_2, -3500, -3500),
            arbusto(950, 250, 50, 50, arbusto_3, -3500, -3500)]

arbustos_rects = [arbusto.rect() for arbusto in arbustos]

#--------------------------------------------------- TODOS OS OBJETOS COM LENTIDAO ---------------------------------------------------------------------------------

pach_objects_colision_lentidao = arbustos
pach_objects_rects_colision_lentidao = arbustos_rects

#--------------------------------------------------- Sem interação ---------------------------------------------------------------------------------

class cogumelo:
    def __init__(self, x, y, largura, altura, imagem_pach):
        self.x = x * LArgura // 1920
        self.y = y * LArgura // 1920
        self.largura =  largura * LArgura // 1920
        self.altura = altura * LArgura // 1920
        self.imagem_pach = imagem_pach

class pedra:
    def __init__(self, x, y, largura, altura, imagem_pach):
        self.x = x * LArgura // 1920
        self.y = y * LArgura // 1920
        self.largura =  largura * LArgura // 1920
        self.altura = altura * LArgura // 1920
        self.imagem_pach = imagem_pach

#--------------------------------------------------- COGUMELOS ---------------------------------------------------------------------------------

cogumelos = [cogumelo(450, 150, 50, 50, cogumelo_0)]

#--------------------------------------------------- PEDRAS ---------------------------------------------------------------------------------

pedras = [pedra(250, 350, 50, 50, pedras_0),
          pedra(850, 400, 50, 50, pedras_1),
          pedra(1050, 200, 50, 50, pedras_2),
          pedra(1050, 40, 50, 50, pedras_3)]

#--------------------------------------------------- TODOS OS OBJETOS SEM INTERAÇÃO ---------------------------------------------------------------------------------

pach_objects_sem_interação = cogumelos + pedras

#--------------------------------------------------- TODOS OS OBJETOS DO CENÁRIO ---------------------------------------------------------------------------------

pach_objects = pach_objects_colision_lentidao + pach_objects_colision
pach_objects_intamgible = pach_objects_sem_interação

class GerenciadorDeColisao:
    def __init__(self, arvores_pequenas, arvores_grandes, barris, casas_pequenas, arbustos, cogumelos, pedras):
        self.arvores_pequenas = arvores_pequenas
        self.arvores_grandes = arvores_grandes
        self.barris = barris
        self.arbustos = arbustos
        self.cogumelos = cogumelos
        self.pedras = pedras
        self.casas_pequenas = casas_pequenas

        self.objetos_colisao = []
        self.objetos_lentidao = []
        self.objetos_sem_interacao = []
        self.todos_objetos = []

    def atualizar(self, pos_chao_x, pos_chao_y):
        """Atualiza listas de objetos a cada frame"""
        self.objetos_colisao = self.arvores_pequenas + self.arvores_grandes + self.barris + self.casas_pequenas
        self.objetos_lentidao = self.arbustos
        self.objetos_sem_interacao = self.cogumelos + self.pedras
        self.todos_objetos = self.objetos_sem_interacao + self.objetos_lentidao + self.objetos_colisao

    def colide(self, rect, pos_chao_x, pos_chao_y):
        """Verifica colisão com objetos sólidos"""
        return any(rect.colliderect((((obj.x - 500) * 19200) // (1380 - 500) + pos_chao_x) + obj.bottom_rith,
                                         (((obj.y - 100) * 19200) // (980 - 100) + pos_chao_y) + obj.bottom_left,
                                         obj.largura, obj.altura) for obj in self.objetos_colisao)

    def colide_lentidao(self, rect):
        """Verifica colisão com objetos que reduzem velocidade"""
        return any(rect.colliderect(obj.rect()) for obj in self.objetos_lentidao)
    
gerenciador_colisao = GerenciadorDeColisao(arvores_pequenas, arvores_grandes, barris, casas_pequena ,arbustos, cogumelos, pedras)
gerenciador_colisao.atualizar(-3500, -3500)