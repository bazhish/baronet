import pygame
import pyautogui
import os

LARGURA, ALTURA = pyautogui.size()
endereço = os.path.dirname(os.path.abspath(__file__))

pygame.init()

personagem_parado = pygame.image.load(f"{endereço}/personagem_principal/personagem_principal.png")
personagem_parado = pygame.transform.scale(personagem_parado, (200 * LARGURA // 1920, 200* LARGURA // 1920))  # Ajusta o tamanho da imagem

personagem_andando0 = pygame.image.load(f"{endereço}/personagem_principal/personagem_principal0.png")
personagem_andando0 = pygame.transform.scale(personagem_andando0, (200 * LARGURA // 1920, 200 * LARGURA // 1920))

personagem_andando1 = pygame.image.load(f"{endereço}/personagem_principal/personagem_principal1.png")
personagem_andando1 = pygame.transform.scale(personagem_andando1, (200 * LARGURA // 1920, 200 * LARGURA // 1920))

personagem_andando2 = pygame.image.load(f"{endereço}/personagem_principal/personagem_principal2.png")
personagem_andando2 = pygame.transform.scale(personagem_andando2, (200 * LARGURA // 1920, 200 * LARGURA // 1920))

personagem_andando3 = pygame.image.load(f"{endereço}/personagem_principal/personagem_principal3.png")
personagem_andando3 = pygame.transform.scale(personagem_andando3, (200 * LARGURA // 1920, 200 * LARGURA // 1920))

personagem_andando4 = pygame.image.load(f"{endereço}/personagem_principal/personagem_principal4.png")
personagem_andando4 = pygame.transform.scale(personagem_andando4, (200 * LARGURA // 1920, 200 * LARGURA // 1920))

personagem_andando5 = pygame.image.load(f"{endereço}/personagem_principal/personagem_principal5.png")
personagem_andando5 = pygame.transform.scale(personagem_andando5, (200 * LARGURA // 1920, 200 * LARGURA // 1920))

personagem_andando6 = pygame.image.load(f"{endereço}/personagem_principal/personagem_principal6.png")
personagem_andando6 = pygame.transform.scale(personagem_andando6, (200 * LARGURA // 1920, 200 * LARGURA // 1920))

personagem_andando7 = pygame.image.load(f"{endereço}/personagem_principal/personagem_principal7.png")
personagem_andando7 = pygame.transform.scale(personagem_andando7, (200 * LARGURA // 1920, 200 * LARGURA // 1920))

personagem_andando8 = pygame.image.load(f"{endereço}/personagem_principal/personagem_principal8.png")
personagem_andando8 = pygame.transform.scale(personagem_andando8, (200 * LARGURA // 1920, 200 * LARGURA // 1920))

personagem_andando_D = [
    personagem_andando0,
    personagem_andando1,
    personagem_andando2,
    personagem_andando3,
    personagem_andando4,
    personagem_andando5,
    personagem_andando6,
    personagem_andando7,
    personagem_andando8]

personagem_soco_d2 =pygame.image.load(f"{endereço}/personagem_principal/soco_2.png")
personagem_soco_d2 = pygame.transform.scale(personagem_soco_d2, (200 * LARGURA // 1920, 200 * LARGURA // 1920))

personagem_soco_d3 =pygame.image.load(f"{endereço}/personagem_principal/soco_3.png")
personagem_soco_d3 = pygame.transform.scale(personagem_soco_d3, (200 * LARGURA // 1920, 200 * LARGURA // 1920))

personagem_soco_d4 =pygame.image.load(f"{endereço}/personagem_principal/soco_4.png")
personagem_soco_d4 = pygame.transform.scale(personagem_soco_d4, (200 * LARGURA // 1920, 200 * LARGURA // 1920))

personagem_soco_d5 =pygame.image.load(f"{endereço}/personagem_principal/soco_5.png")
personagem_soco_d5 = pygame.transform.scale(personagem_soco_d5, (200 * LARGURA // 1920, 200 * LARGURA // 1920))

personagem_soco_d6 =pygame.image.load(f"{endereço}/personagem_principal/soco_6.png")
personagem_soco_d6 = pygame.transform.scale(personagem_soco_d6, (200 * LARGURA // 1920, 200 * LARGURA // 1920))

personagem_soco_d7 =pygame.image.load(f"{endereço}/personagem_principal/soco_7.png")
personagem_soco_d7 = pygame.transform.scale(personagem_soco_d7, (200 * LARGURA // 1920, 200 * LARGURA // 1920))

personagem_soco_d8 =pygame.image.load(f"{endereço}/personagem_principal/soco_8.png")
personagem_soco_d8 = pygame.transform.scale(personagem_soco_d8, (200 * LARGURA // 1920, 200 * LARGURA // 1920))

personagem_soco_d = [
    personagem_soco_d2,
    personagem_soco_d3,
    personagem_soco_d4,
    personagem_soco_d5,
    personagem_soco_d6,
    personagem_soco_d7,
    personagem_soco_d8,
    personagem_soco_d7,
    personagem_soco_d6,
    personagem_soco_d5,
    personagem_soco_d4,
    personagem_soco_d3,
    personagem_soco_d2]

