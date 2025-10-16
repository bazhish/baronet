from pygame import image, init, transform, display
from pyautogui import size
from os import path

init()
LArgura , Altura = size()
endereço = path.dirname(path.abspath(__file__))

screen = display.set_mode((1, 1))
display.iconify()

arvore_pequena_0 = image.load(fr"{endereço}\arvore_P_0.png").convert_alpha()
arvore_pequena_0 = transform.scale(arvore_pequena_0, (128 * LArgura // 1920, 180 * LArgura // 1920))

arvore_pequena_1 = image.load(fr"{endereço}\arvore_P_1.png").convert_alpha()
arvore_pequena_1 = transform.scale(arvore_pequena_1, (128 * LArgura // 1920, 180 * LArgura // 1920))

arvore_pequena_2 = image.load(fr"{endereço}\arvore_P_2.png").convert_alpha()
arvore_pequena_2 = transform.scale(arvore_pequena_2, (158 * LArgura // 1920, 210 * LArgura // 1920))

arvore_pequena_3 = image.load(fr"{endereço}\arvore_P_3.png").convert_alpha()
arvore_pequena_3 = transform.scale(arvore_pequena_3, (128 * LArgura // 1920, 180 * LArgura // 1920))

arvore_grande_0 = image.load(fr"{endereço}\arvore_G_0.png").convert_alpha()
arvore_grande_0 = transform.scale(arvore_grande_0, (256 * LArgura // 1920, 360 * LArgura // 1920))

arvore_grande_1 = image.load(fr"{endereço}\arvore_G_1.png").convert_alpha()
arvore_grande_1 = transform.scale(arvore_grande_1, (256 * LArgura // 1920, 360 * LArgura // 1920))

arbusto_0 = image.load(fr"{endereço}\arbusto_0.png").convert_alpha()
arbusto_0 = transform.scale(arbusto_0, (60 * LArgura // 1920, 60 * LArgura // 1920))

arbusto_1 = image.load(fr"{endereço}\arbusto_1.png").convert_alpha()
arbusto_1 = transform.scale(arbusto_1, (48 * LArgura // 1920, 36 * LArgura // 1920))  

arbusto_2 = image.load(fr"{endereço}\arbusto_2.png").convert_alpha()
arbusto_2 = transform.scale(arbusto_2, (52 * LArgura // 1920, 52 * LArgura // 1920))

arbusto_3 = image.load(fr"{endereço}\arbusto_3.png").convert_alpha()
arbusto_3 = transform.scale(arbusto_3, (56 * LArgura // 1920, 56 * LArgura // 1920))

barril_0 = image.load(fr"{endereço}\barril 0.png").convert_alpha()
barril_0 = transform.scale(barril_0, (40 * LArgura // 1920, 65 * LArgura // 1920))

barril_1 = image.load(fr"{endereço}\barril 1.png").convert_alpha()
barril_1 = transform.scale(barril_1, (40 * LArgura // 1920, 65 * LArgura // 1920))

barril_2 = image.load(fr"{endereço}\barril 2.png").convert_alpha()
barril_2 = transform.scale(barril_2, (40 * LArgura // 1920, 65 * LArgura // 1920))

cogumelo_0 = image.load(fr"{endereço}\cogumelo 0.png").convert_alpha()
cogumelo_0 = transform.scale(cogumelo_0, (28 * LArgura // 1920, 32 * LArgura // 1920))

cogumelo_1 = image.load(fr"{endereço}\cogumelo 1.png").convert_alpha()
cogumelo_1 = transform.scale(cogumelo_1, (25 * LArgura // 1920, 32 * LArgura // 1920))

cogumelo_2 = image.load(fr"{endereço}\cogumelo 2.png").convert_alpha()
cogumelo_2 = transform.scale(cogumelo_2, (28 * LArgura // 1920, 38 * LArgura // 1920))

flor_0 = image.load(fr"{endereço}\flor 0.png").convert_alpha()
flor_0 = transform.scale(flor_0, (32 * LArgura // 1920, 50 * LArgura // 1920))

flor_1 = image.load(fr"{endereço}\flor 1.png").convert_alpha()
flor_1 = transform.scale(flor_1, (30 * LArgura // 1920, 49 * LArgura // 1920))

flor_2 = image.load(fr"{endereço}\flor 2.png").convert_alpha()
flor_2 = transform.scale(flor_2, (33 * LArgura // 1920, 47 * LArgura // 1920))

flor_3 = image.load(fr"{endereço}\flor 3.png").convert_alpha()
flor_3 = transform.scale(flor_3, (39 * LArgura // 1920, 53 * LArgura // 1920))

flor_4 = image.load(fr"{endereço}\flor 4.png").convert_alpha()
flor_4 = transform.scale(flor_4, (30 * LArgura // 1920, 49 * LArgura // 1920))

folhas = image.load(fr"{endereço}\folhas.png").convert_alpha()
folhas = transform.scale(folhas, (60 * LArgura // 1920, 60 * LArgura // 1920))

pedras_0 = image.load(fr"{endereço}\pedras 0.png").convert_alpha()
pedras_0 = transform.scale(pedras_0, (40 * LArgura // 1920, 60 * LArgura // 1920))

pedras_1 = image.load(fr"{endereço}\pedras 1.png").convert_alpha()
pedras_1 = transform.scale(pedras_1, (48 * LArgura // 1920, 36 * LArgura // 1920))

pedras_2 = image.load(fr"{endereço}\pedras 2.png").convert_alpha()
pedras_2 = transform.scale(pedras_2, (36 * LArgura // 1920, 16 * LArgura // 1920))

pedras_4 = image.load(fr"{endereço}\pedra 4.png").convert_alpha()
pedras_4 = transform.scale(pedras_4, (48 * LArgura // 1920, 36 * LArgura // 1920))

pedras_5 = image.load(fr"{endereço}\pedra 5.png").convert_alpha()
pedras_5 = transform.scale(pedras_5, (58 * LArgura // 1920, 37 * LArgura // 1920))

pedras_6 = image.load(fr"{endereço}\pedra 6.png").convert_alpha()
pedras_6 = transform.scale(pedras_6, (42 * LArgura // 1920, 30 * LArgura // 1920))

casa_pequena0 = image.load(fr"{endereço}\casa_pequena0.png").convert_alpha()
casa_pequena0 = transform.scale(casa_pequena0, (572 * LArgura // 1920, 536 * LArgura // 1920))

casa_pequena1 = image.load(fr"{endereço}\casa_pequena1.png").convert_alpha()
casa_pequena1 = transform.scale(casa_pequena1, (572 * LArgura // 1920, 536 * LArgura // 1920))

rocha_0 = image.load(fr"{endereço}\Rocha.png").convert_alpha()
rocha_0 = transform.scale(rocha_0, (90 * LArgura // 1920, 100 * LArgura // 1920))

inventario_pach = image.load(fr"{endereço}\inventario_final.png").convert_alpha()
inventario_pach = transform.scale(inventario_pach, (1344 * LArgura // 1920, 966 * LArgura // 1920))

inventario_icon = image.load(fr"{endereço}\inventario_icon.png").convert()
inventario_icon = transform.scale(inventario_icon, (100 * LArgura // 1920, 100 * LArgura // 1920))

mapa_img = image.load(fr"{endereço}\mapa.png").convert()
mapa_img = transform.scale(mapa_img, (880 * LArgura // 1920, 880 * LArgura // 1920))

taverna_P = image.load(fr"{endereço}\taverna.png").convert_alpha()
taverna_P = transform.scale(taverna_P, (1244 * LArgura // 1920, 2596 * LArgura // 1920))

castelo_1 = image.load(fr"{endereço}\castelo.png").convert_alpha()
castelo_1 = transform.scale(castelo_1, (1877 * LArgura // 1920, 1833 * LArgura // 1920))

castelo_2 = image.load(fr"{endereço}\castelo_2.png").convert_alpha()
castelo_2 = transform.scale(castelo_2, (1221 * LArgura // 1920, 1156 * LArgura // 1920))

barraca_H0 = image.load(fr"{endereço}\barraca_0.png").convert_alpha()
barraca_H0 = transform.scale(barraca_H0, (415 * LArgura // 1920, 240 * LArgura // 1920))

barraca_H1 = image.load(fr"{endereço}\barraca_1.png").convert_alpha()
barraca_H1 = transform.scale(barraca_H1, (415 * LArgura // 1920, 240 * LArgura // 1920))

barraca_H2 = image.load(fr"{endereço}\barraca_2.png").convert_alpha()
barraca_H2 = transform.scale(barraca_H2, (415 * LArgura // 1920, 240 * LArgura // 1920))

barraca_H3 = image.load(fr"{endereço}\barraca_3.png").convert_alpha()
barraca_H3 = transform.scale(barraca_H3, (415 * LArgura // 1920, 240 * LArgura // 1920))

barraca_V0 = image.load(fr"{endereço}\barraca_V0.png").convert_alpha()
barraca_V0 = transform.scale(barraca_V0, (240 * LArgura // 1920, 415 * LArgura // 1920))

barraca_V1 = image.load(fr"{endereço}\barraca_V1.png").convert_alpha()
barraca_V1 = transform.scale(barraca_V1, (240 * LArgura // 1920, 415 * LArgura // 1920))

barraca_V2 = image.load(fr"{endereço}\barraca_V2.png").convert_alpha()
barraca_V2 = transform.scale(barraca_V2, (240 * LArgura // 1920, 415 * LArgura // 1920))

barraca_V3 = image.load(fr"{endereço}\barraca_V3.png").convert_alpha()
barraca_V3 = transform.scale(barraca_V3, (240 * LArgura // 1920, 415 * LArgura // 1920))

sem_colisao = [pedras_0, pedras_1, pedras_2, pedras_4, pedras_5, pedras_6, cogumelo_0, cogumelo_1, cogumelo_2, flor_0, flor_1, flor_2, flor_3, flor_4, folhas]

