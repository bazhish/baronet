import sys, os
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = current_dir
while not os.path.isdir(os.path.join(project_root, ".git")) and os.path.dirname(project_root) != project_root:
    project_root = os.path.dirname(project_root)
sys.path.append(project_root)

import pygame
from backend.system.personagem_principal import Usuario
from backend.system.adversarios import AdversarioDemiHumano
from backend.system.habilidades_ativa_combatentes import golpe_mortal, impacto_cruzado

# Inicialização do pygame
pygame.init()
LARGURA, ALTURA = 1200, 600
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Arena de Combate - Baronet")

FPS = 32
clock = pygame.time.Clock()

# Cores
BRANCO = (255, 255, 255)
VERMELHO = (200, 0, 0)
AZUL = (0, 0, 200)

# Função para desenhar personagens
def desenhar_personagem(personagem, cor):
    pygame.draw.rect(TELA, cor, (personagem.posição_x, personagem.posição_y, 50, 80))

# Função de colisão simples (retângulo)
def colidiu(p1, p2):
    rect1 = pygame.Rect(p1.posição_x, p1.posição_y, 50, 80)
    rect2 = pygame.Rect(p2.posição_x, p2.posição_y, 50, 80)
    return rect1.colliderect(rect2)

# Função para desenhar o range de ataque do jogador
def desenhar_range_ataque(personagem, alcance):
    centro_x = personagem.posição_x + 25
    centro_y = personagem.posição_y + 40
    pygame.draw.circle(TELA, (100, 100, 255), (centro_x, centro_y), alcance, 1)

# Função para verificar se o adversário está dentro do alcance de ataque do jogador
def dentro_do_range(jogador, adversario, alcance):
    centro_jogador = (jogador.posição_x + 25, jogador.posição_y + 40)
    centro_adversario = (adversario.posição_x + 25, adversario.posição_y + 40)
    distancia = ((centro_jogador[0] - centro_adversario[0]) ** 2 + (centro_jogador[1] - centro_adversario[1]) ** 2) ** 0.5
    return distancia <= alcance

# Defina o alcance de ataque do jogador (em pixels)
ALCANCE_ATAQUE = 120

# Defina o alcance de ataque do adversário (em pixels)
ALCANCE_ATAQUE_ADVERSARIO = 100

# Função para desenhar o range de ataque do adversário
def desenhar_range_ataque_adversario(personagem, alcance):
    centro_x = personagem.posição_x + 25
    centro_y = personagem.posição_y + 40
    pygame.draw.circle(TELA, (255, 100, 100), (centro_x, centro_y), alcance, 1)

# Função para verificar se o jogador está dentro do alcance de ataque do adversário
def dentro_do_range_adversario(adversario, jogador, alcance):
    centro_adversario = (adversario.posição_x + 25, adversario.posição_y + 40)
    centro_jogador = (jogador.posição_x + 25, jogador.posição_y + 40)
    distancia = ((centro_adversario[0] - centro_jogador[0]) ** 2 + (centro_adversario[1] - centro_jogador[1]) ** 2) ** 0.5
    return distancia <= alcance

# Instanciando personagens
jogador = Usuario("Jogador")
jogador.posição_x, jogador.posição_y = 100, ALTURA - 100

adversario = AdversarioDemiHumano(
    nome="Inimigo",
    idade=20,
    peso=80,
    gênero="masculino",
    altura=1.8,
    nível=1,
    experiência=0,
    dano_base=2,
    velocidade_base=3,
    defesa_base=2,
    vida_base=80
)
adversario.posição_x, adversario.posição_y = 900, ALTURA - 100

# Variável para controlar o intervalo de ataque do adversário
INTERVALO_ATAQUE_ADVERSARIO = 60  # em ticks (1 segundo se FPS=60)
contador_ataque_adversario = 0

# Defina teclas para habilidades
TECLA_HABILIDADE_ATIVA = pygame.K_q
TECLA_HABILIDADE_ESPECIAL = pygame.K_e

# Exemplo de atribuição de habilidades ao jogador (ajuste conforme sua implementação)
jogador.habilidade_ativa = golpe_mortal
jogador.habilidade_especial = impacto_cruzado

# Loop principal de combate
rodando = True
while rodando:
    clock.tick(FPS)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

        # Ataque com o botão esquerdo do mouse
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            if dentro_do_range(jogador, adversario, ALCANCE_ATAQUE):
                jogador.atacar(adversario)

        # Usar habilidade ativa (Q)
        if evento.type == pygame.KEYDOWN and evento.key == TECLA_HABILIDADE_ATIVA:
            if hasattr(jogador, "habilidade_ativa") and jogador.habilidade_ativa:
                if dentro_do_range(jogador, adversario, ALCANCE_ATAQUE):
                    jogador.habilidade_ativa.ativar(jogador, adversario)

        # Usar habilidade especial (E)
        if evento.type == pygame.KEYDOWN and evento.key == TECLA_HABILIDADE_ESPECIAL:
            if hasattr(jogador, "habilidade_especial") and jogador.habilidade_especial:
                if dentro_do_range(jogador, adversario, ALCANCE_ATAQUE):
                    jogador.habilidade_especial.ativar(jogador, adversario)

    # Controles do jogador (setas OU teclas W A S D)
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
        jogador.posição_x -= 5
    if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
        jogador.posição_x += 5
    if teclas[pygame.K_UP] or teclas[pygame.K_w]:
        jogador.posição_y -= 5
    if teclas[pygame.K_DOWN] or teclas[pygame.K_s]:
        jogador.posição_y += 5

    # Colisão do jogador com as bordas da tela
    if jogador.posição_x < 0:
        jogador.posição_x = 0
    if jogador.posição_x > LARGURA - 50:
        jogador.posição_x = LARGURA - 50
    if jogador.posição_y < 0:
        jogador.posição_y = 0
    if jogador.posição_y > ALTURA - 80:
        jogador.posição_y = ALTURA - 80

    # Colisão do adversário com as bordas da tela
    if adversario.posição_x < 0:
        adversario.posição_x = 0
    if adversario.posição_x > LARGURA - 50:
        adversario.posição_x = LARGURA - 50
    if adversario.posição_y < 0:
        adversario.posição_y = 0
    if adversario.posição_y > ALTURA - 80:
        adversario.posição_y = ALTURA - 80

    # Movimento simples do adversário (segue o jogador)
    if adversario.posição_x > jogador.posição_x and not dentro_do_range_adversario(adversario, jogador, ALCANCE_ATAQUE_ADVERSARIO):
        adversario.posição_x -= 2
    elif adversario.posição_x < jogador.posição_x and not dentro_do_range_adversario(adversario, jogador, ALCANCE_ATAQUE_ADVERSARIO):
        adversario.posição_x += 2

    # Ataque do adversário em intervalo de ticks se o jogador estiver dentro do range
    if dentro_do_range_adversario(adversario, jogador, ALCANCE_ATAQUE_ADVERSARIO):
        contador_ataque_adversario += 1
        if contador_ataque_adversario >= 5:
            adversario.atacar(jogador)
            contador_ataque_adversario = 0
    else:
        contador_ataque_adversario = 0

    # Fim de combate
    if jogador.vida_atual <= 0 or adversario.vida_atual <= 0:
        rodando = False

    # Desenho
    TELA.fill(BRANCO)
    desenhar_personagem(jogador, AZUL)
    desenhar_personagem(adversario, VERMELHO)
    desenhar_range_ataque(jogador, ALCANCE_ATAQUE)
    desenhar_range_ataque_adversario(adversario, ALCANCE_ATAQUE_ADVERSARIO)

    # Exibir vida
    fonte = pygame.font.SysFont(None, 36)
    vida_jogador = fonte.render(f"Vida Jogador: {jogador.vida_atual}", True, AZUL)
    vida_adversario = fonte.render(f"Vida Inimigo: {adversario.vida_atual}", True, VERMELHO)
    TELA.blit(vida_jogador, (20, 20))
    TELA.blit(vida_adversario, (LARGURA - 250, 20))

    pygame.display.flip()
    clock.tick(32)

pygame.quit()