import subprocess
import sys

# Lista de pacotes externos necessários
pacotes = [
    "pygame",
    "pygetwindow",
    "pyautogui",
    "pillow"
]

def instalar(pacote):
    """Instala um pacote com pip."""
    subprocess.check_call([sys.executable, "-m", "pip", "install", pacote])

if __name__ == "__main__":
    for pacote in pacotes:
        try:
            __import__(pacote if pacote != "pillow" else "PIL")  # pillow é importado como PIL
            print(f"✅ {pacote} já está instalado.")
        except ImportError:
            print(f"📦 Instalando {pacote}...")
            instalar(pacote)