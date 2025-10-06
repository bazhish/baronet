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

pedras_0 = image.load(fr"{endereço}\pedras 0.png").convert_alpha()
pedras_0 = transform.scale(pedras_0, (40 * LArgura // 1920, 60 * LArgura // 1920))

pedras_1 = image.load(fr"{endereço}\pedras 1.png").convert_alpha()
pedras_1 = transform.scale(pedras_1, (48 * LArgura // 1920, 36 * LArgura // 1920))

pedras_2 = image.load(fr"{endereço}\pedras 2.png").convert_alpha()
pedras_2 = transform.scale(pedras_2, (36 * LArgura // 1920, 16 * LArgura // 1920))

pedras_3 = image.load(fr"{endereço}\pedras 3.png").convert_alpha()
pedras_3 = transform.scale(pedras_3, (52 * LArgura // 1920, 120 * LArgura // 1920))

casa_pequena0 = image.load(fr"{endereço}\casa_pequena0.png").convert_alpha()
casa_pequena0 = transform.scale(casa_pequena0, (572 * LArgura // 1920, 900 * LArgura // 1920))

casa_pequena1 = image.load(fr"{endereço}\casa_pequena1.png").convert_alpha()
casa_pequena1 = transform.scale(casa_pequena1, (572 * LArgura // 1920, 900 * LArgura // 1920))

rocha_0 = image.load(fr"{endereço}\Rocha.png").convert_alpha()
rocha_0 = transform.scale(rocha_0, (90 * LArgura // 1920, 100 * LArgura // 1920))

inventario_pach = image.load(fr"{endereço}\inventario_final.png").convert_alpha()
inventario_pach = transform.scale(inventario_pach, (1344 * LArgura // 1920, 966 * LArgura // 1920))

inventario_icon = image.load(fr"{endereço}\inventario_icon.png").convert()
inventario_icon = transform.scale(inventario_icon, (100 * LArgura // 1920, 100 * LArgura // 1920))

mapa_img = image.load(fr"{endereço}\mapa.png").convert()
mapa_img = transform.scale(mapa_img, (880 * LArgura // 1920, 880 * LArgura // 1920))

