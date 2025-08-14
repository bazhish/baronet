import pygame
from backend.configuracoes import FPS
from backend.nucleo.gerenciador_cenas import executar_cena

def iniciar_jogo():
    pygame.init()
    executar_cena("menu")  # Cena inicial
    pygame.quit()
