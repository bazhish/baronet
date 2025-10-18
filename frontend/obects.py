import pygame
import sys
import math

# Inicializa o pygame
pygame.init()

# Configuração da tela
LARGURA, ALTURA = 600, 400
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Barra Circular")

# Clock para controlar FPS
clock = pygame.time.Clock()

# Variáveis do círculo
centro_moita = (LARGURA // 2, ALTURA // 2)
raio_moita = 30
angulo_moita = 0
carregando_moita = False

# Loop principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.KEYDOWN:
            carregando_moita = True
        elif evento.type == pygame.KEYUP:
            carregando_moita = False
            angulo_moita = 0  # reseta quando solta a tecla

    # Atualiza progresso
    if carregando_moita:
        angulo_moita += 2.25  # velocidade de carregamento
        if angulo_moita > 360:
            angulo_moita = 360  # limite máximo

    # Fundo
    tela.fill((30, 30, 30))

    # Desenha círculo de fundo
    pygame.draw.circle(tela, (80, 80, 80), centro_moita, raio_moita, 4)

    # Desenha a barra circular (arco)
    if angulo_moita > 0:
        rect_moita = pygame.Rect(centro_moita[0]-raio_moita, centro_moita[1]-raio_moita, raio_moita*2, raio_moita*2)
        pygame.draw.arc(tela, (0, 200, 255), rect_moita, -math.pi/2, -math.pi/2 + math.radians(angulo_moita), 4)

    # Atualiza a tela
    pygame.display.flip()
    clock.tick(60)