import subprocess
import sys
import os



def atualizar_pip():
    print("Atualizando pip...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
    print("Pip atualizado com sucesso!\n")

def instalar_pygame():
    try:
        import pygame
        print("Pygame já está instalado.")
    except ImportError:
        print("Instalando Pygame...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pygame"])
        print("Pygame instalado com sucesso!\n")


atualizar_pip()
instalar_pygame()