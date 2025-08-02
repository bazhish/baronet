import pygame
import os


endereço = os.path.dirname(os.path.abspath(__file__))
pygame.init()
pygame.mixer.init()
#configuraçao de diretorios

#Criação de Janela principal
LARGURA_JANELA = 800
ALTURA_JANELA = 500
tela = pygame.display.set_mode((LARGURA_JANELA,ALTURA_JANELA))
pygame.display.set_caption("Inventario")

#Carregamento de recursos
try:
    textura_fundo = pygame.image.load(rf"{endereço}\inventario_img\inv.png")
    textura_fundo = pygame.transform.scale(textura_fundo, (LARGURA_JANELA, ALTURA_JANELA))

except pygame.error as e:
    exit()  # Preencher com vermelho se a imagem não puder ser carregada

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    


    # Desenhar fundo
    tela.blit(textura_fundo, (0, 0))


    # Atualizar a tela
    pygame.display.flip()