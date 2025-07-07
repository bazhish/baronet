# app/main.py

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.models.personagem import Personagem
from app.models.inimigo import Inimigo

# exemplo de uso
jogador = Personagem("Max", "Espadachim")
inimigo = Inimigo("Goblin", 1, 30, 10)
inimigo.atacar(jogador)
