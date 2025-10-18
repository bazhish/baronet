import pygetwindow as gw
from pyautogui import hotkey
hotkey("win", "d")

janela = gw.getWindowsWithTitle("Bloco de Notas")[0]

# Restaura e maximiza sem checar
janela.restore()
janela.maximize()