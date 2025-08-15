import sys, os
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = current_dir
while not os.path.isdir(os.path.join(project_root, ".git")) and os.path.dirname(project_root) != project_root:
    project_root = os.path.dirname(project_root)
sys.path.append(project_root)


import pygame
from backend.configuracoes import (
    LARGURA, ALTURA, FPS, BRANCO, AZUL, VERMELHO,
    ALCANCE_ATAQUE, ALCANCE_ATAQUE_ADVERSARIO
)
from backend.entidades.jogador import Jogador
from backend.entidades.inimigo import Inimigo
from frontend.renderizacao.desenhar_entidades import desenhar_personagem, desenhar_range_ataque

def executar():
    pygame.init()
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption("Arena de Combate - Baronet")
    clock = pygame.time.Clock()

    jogador = Jogador("Jogador")
    jogador.posicao_x, jogador.posicao_y = 100, ALTURA - 100

    adversario = Inimigo("Inimigo", 20, 80, "masculino", 1.8, 1, 0, 2, 3, 2, 80)
    adversario.posicao_x, adversario.posicao_y = 900, ALTURA - 100

    rodando = True
    while rodando:
        clock.tick(FPS)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

        # Renderização
        tela.fill(BRANCO)
        desenhar_personagem(tela, jogador, AZUL)
        desenhar_personagem(tela, adversario, VERMELHO)
        desenhar_range_ataque(tela, jogador, ALCANCE_ATAQUE, (100, 100, 255))
        desenhar_range_ataque(tela, adversario, ALCANCE_ATAQUE_ADVERSARIO, (255, 100, 100))

        pygame.display.flip()

    pygame.quit()
