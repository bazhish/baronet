import pygame
import os

endereço = os.path.dirname(os.path.abspath(__file__))

pygame.init()

personagem_parado = pygame.image.load(f"{endereço}/personagem_principal/personagem_principal.png")
personagem_parado = pygame.transform.scale(personagem_parado, (200, 200))  # Ajusta o tamanho da imagem

personagem_andando0 = pygame.image.load(f"{endereço}/personagem_principal/personagem_principal0.png")
personagem_andando0 = pygame.transform.scale(personagem_andando0, (200, 200))

personagem_andando1 = pygame.image.load(f"{endereço}/personagem_principal/personagem_principal1.png")
personagem_andando1 = pygame.transform.scale(personagem_andando1, (200, 200))

personagem_andando2 = pygame.image.load(f"{endereço}/personagem_principal/personagem_principal2.png")
personagem_andando2 = pygame.transform.scale(personagem_andando2, (200, 200))

personagem_andando3 = pygame.image.load(f"{endereço}/personagem_principal/personagem_principal3.png")
personagem_andando3 = pygame.transform.scale(personagem_andando3, (200, 200))

personagem_andando4 = pygame.image.load(f"{endereço}/personagem_principal/personagem_principal4.png")
personagem_andando4 = pygame.transform.scale(personagem_andando4, (200, 200))

personagem_andando5 = pygame.image.load(f"{endereço}/personagem_principal/personagem_principal5.png")
personagem_andando5 = pygame.transform.scale(personagem_andando5, (200, 200))

personagem_andando6 = pygame.image.load(f"{endereço}/personagem_principal/personagem_principal6.png")
personagem_andando6 = pygame.transform.scale(personagem_andando6, (200, 200))

personagem_andando7 = pygame.image.load(f"{endereço}/personagem_principal/personagem_principal7.png")
personagem_andando7 = pygame.transform.scale(personagem_andando7, (200, 200))

personagem_andando8 = pygame.image.load(f"{endereço}/personagem_principal/personagem_principal8.png")
personagem_andando8 = pygame.transform.scale(personagem_andando8, (200, 200))

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