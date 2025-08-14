# app/models/personagens/jogador_ficticio.py
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../..')))
from backend.system.personagem_principal import Usuario

jogador = Usuario("ayala")
jogador.receber_experiencia(400)
jogador.atualizar_descrição()
