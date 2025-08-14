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
        import spritesheet
        print("Pygame já está instalado.")
    except ImportError:
        print("Instalando Pygame...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pygame"])
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pygame-spritesheet"])
        print("Pygame instalado com sucesso!\n")

def instalar_pyautogui():
    try:
        import pyautogui
        print("Pyautogui já está instalado.")
    except ImportError:
        print("Instalando Pyautogui...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyautogui"])
        print("Pyautogui instalado com sucesso!\n")


atualizar_pip()
instalar_pygame()
instalar_pyautogui()