import pygame
import pyautogui
import os

LARGURA, ALTURA = pyautogui.size()
endereço = os.path.dirname(os.path.abspath(__file__))

pygame.init()

personagem_parado1 = pygame.image.load(f"{endereço}/personagem_principal/personagem_parado1.png")
personagem_parado1 = pygame.transform.scale(personagem_parado1, (200 * LARGURA // 1920, 200* LARGURA // 1920)) 

personagem_parado2 = pygame.image.load(f"{endereço}/personagem_principal/personagem_parado2.png")
personagem_parado2 = pygame.transform.scale(personagem_parado2, (200 * LARGURA // 1920, 200* LARGURA // 1920)) 

personagem_parado3 = pygame.image.load(f"{endereço}/personagem_principal/personagem_parado3.png")
personagem_parado3 = pygame.transform.scale(personagem_parado3, (200 * LARGURA // 1920, 200* LARGURA // 1920)) 

personagem_parado = [personagem_parado1,
                     personagem_parado2,
                     personagem_parado3,
                     personagem_parado2]

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

personagem_soco_d2 =pygame.image.load(f"{endereço}/personagem_principal/personagem_ataque1.png")
personagem_soco_d2 = pygame.transform.scale(personagem_soco_d2, (200 * LARGURA // 1920, 200 * LARGURA // 1920))

personagem_soco_d3 =pygame.image.load(f"{endereço}/personagem_principal/personagem_ataque2.png")
personagem_soco_d3 = pygame.transform.scale(personagem_soco_d3, (200 * LARGURA // 1920, 200 * LARGURA // 1920))

personagem_soco_d4 =pygame.image.load(f"{endereço}/personagem_principal/personagem_ataque3.png")
personagem_soco_d4 = pygame.transform.scale(personagem_soco_d4, (200 * LARGURA // 1920, 200 * LARGURA // 1920))

personagem_soco_d5 =pygame.image.load(f"{endereço}/personagem_principal/personagem_ataque4.png")
personagem_soco_d5 = pygame.transform.scale(personagem_soco_d5, (200 * LARGURA // 1920, 200 * LARGURA // 1920))

personagem_soco_d6 =pygame.image.load(f"{endereço}/personagem_principal/personagem_ataque5.png")
personagem_soco_d6 = pygame.transform.scale(personagem_soco_d6, (200 * LARGURA // 1920, 200 * LARGURA // 1920))

personagem_soco_d = [
    personagem_soco_d2,
    personagem_soco_d3,
    personagem_soco_d4,
    personagem_soco_d5,
    personagem_soco_d6,
    personagem_soco_d5,
    personagem_soco_d4,
    personagem_soco_d3,
    personagem_soco_d2]

personagem_morto1 = pygame.image.load(f"{endereço}/personagem_principal/morte_1.png")
personagem_morto1 = pygame.transform.scale(personagem_morto1, (200 * LARGURA // 1920, 200 * LARGURA // 1920))

personagem_morto2 = pygame.image.load(f"{endereço}/personagem_principal/morte_2.png")
personagem_morto2 = pygame.transform.scale(personagem_morto2, (200 * LARGURA // 1920, 200 * LARGURA // 1920))

personagem_morto3 = pygame.image.load(f"{endereço}/personagem_principal/morte_3.png")
personagem_morto3 = pygame.transform.scale(personagem_morto3, (200 * LARGURA // 1920, 200 * LARGURA // 1920))

personagem_morto4 = pygame.image.load(f"{endereço}/personagem_principal/morte_4.png")
personagem_morto4 = pygame.transform.scale(personagem_morto4, (200 * LARGURA // 1920, 200 * LARGURA // 1920))

personagem_morto5 = pygame.image.load(f"{endereço}/personagem_principal/morte_5.png")
personagem_morto5 = pygame.transform.scale(personagem_morto5, (200 * LARGURA // 1920, 200 * LARGURA // 1920))

personagem_morto6 = pygame.image.load(f"{endereço}/personagem_principal/morte_6.png")
personagem_morto6 = pygame.transform.scale(personagem_morto6, (200 * LARGURA // 1920, 200 * LARGURA // 1920))

personagem_morto7 = pygame.image.load(f"{endereço}/personagem_principal/morte_7.png")
personagem_morto7 = pygame.transform.scale(personagem_morto7, (200 * LARGURA // 1920, 200 * LARGURA // 1920))

personagem_morto = [personagem_morto1,
                    personagem_morto2,
                    personagem_morto3,
                    personagem_morto4,
                    personagem_morto5,
                    personagem_morto6,
                    personagem_morto7   ]

personagem_dano1 = pygame.image.load(f"{endereço}/personagem_principal/personagem_dano1.png")
personagem_dano1 = pygame.transform.scale(personagem_dano1, (200 * LARGURA // 1920, 200 * LARGURA // 1920))

personagem_dano2 = pygame.image.load(f"{endereço}/personagem_principal/personagem_dano2.png")
personagem_dano2 = pygame.transform.scale(personagem_dano2, (200 * LARGURA // 1920, 200 * LARGURA // 1920))

personagem_dano3 = pygame.image.load(f"{endereço}/personagem_principal/personagem_dano3.png")
personagem_dano3 = pygame.transform.scale(personagem_dano3, (200 * LARGURA // 1920, 200 * LARGURA // 1920))

personagem_dano = [personagem_dano1,
                   personagem_dano2,
                   personagem_dano3]