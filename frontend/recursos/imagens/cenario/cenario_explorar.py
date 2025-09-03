from pygame import image, init, transform
from pyautogui import size
from os import path

init()
LArgura , Altura = size()
endereço = path.dirname(path.abspath(__file__))

arvore_pequena_0 = image.load(fr"{endereço}\arvore_P_0.png")
arvore_pequena_0 = transform.scale(arvore_pequena_0, (128 * LArgura // 1920, 180 * LArgura // 1920))

arvore_pequena_1 = image.load(fr"{endereço}\arvore_P_1.png")
arvore_pequena_1 = transform.scale(arvore_pequena_1, (128 * LArgura // 1920, 180 * LArgura // 1920))

arvore_pequena_2 = image.load(fr"{endereço}\arvore_P_2.png")
arvore_pequena_2 = transform.scale(arvore_pequena_2, (128 * LArgura // 1920, 180 * LArgura // 1920))

arvore_pequena_3 = image.load(fr"{endereço}\arvore_P_3.png")
arvore_pequena_3 = transform.scale(arvore_pequena_3, (128 * LArgura // 1920, 180 * LArgura // 1920))

arvore_grande_0 = image.load(fr"{endereço}\arvore_G_0.png")
arvore_grande_0 = transform.scale(arvore_grande_0, (256 * LArgura // 1920, 360 * LArgura // 1920))

arvore_grande_1 = image.load(fr"{endereço}\arvore_G_1.png")
arvore_grande_1 = transform.scale(arvore_grande_1, (256 * LArgura // 1920, 360 * LArgura // 1920))

arbusto_0 = image.load(fr"{endereço}\arbusto_0.png")
arbusto_0 = transform.scale(arbusto_0, (60 * LArgura // 1920, 60 * LArgura // 1920))

arbusto_1 = image.load(fr"{endereço}\arbusto_1.png")
arbusto_1 = transform.scale(arbusto_1, (48 * LArgura // 1920, 36 * LArgura // 1920))  

arbusto_2 = image.load(fr"{endereço}\arbusto_2.png")
arbusto_2 = transform.scale(arbusto_2, (52 * LArgura // 1920, 52 * LArgura // 1920))

arbusto_3 = image.load(fr"{endereço}\arbusto_3.png")
arbusto_3 = transform.scale(arbusto_3, (56 * LArgura // 1920, 56 * LArgura // 1920))


