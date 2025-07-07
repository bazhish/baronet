import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.models.personagem import Personagem
from app.models.inimigo import Inimigo

jogador = Personagem(nome="Max", classe="Espadachim")
goblin = Inimigo(nome="Goblin", nivel=1, vida=30, dano=8)

goblin.atacar(jogador)
jogador.subir_nivel()