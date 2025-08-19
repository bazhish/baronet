import pygame
from backend.configuracoes import *
from backend.system.personagem_principal import Usuario
from backend.system.adversarios import AdversarioDemiHumano
from backend.system.habilidades_ativa_combatentes import golpe_mortal, impacto_cruzado
from backend.sistemas.colisao import dentro_do_range
from frontend.renderizacao.desenhar_entidades import desenhar_personagem, desenhar_range_ataque

def executar():
    pygame.init()
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption("Arena de Combate - Baronet")
    clock = pygame.time.Clock()

    jogador = Usuario("Jogador")
    jogador.posição_x, jogador.posição_y = 100, ALTURA - 100
    jogador.habilidade_ativa = golpe_mortal
    jogador.habilidade_especial = impacto_cruzado

    adversario = AdversarioDemiHumano("Inimigo", 20, 80, "masculino", 1.8, 1, 0, 2, 3, 2, 80)
    adversario.posição_x, adversario.posição_y = 900, ALTURA - 100

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
