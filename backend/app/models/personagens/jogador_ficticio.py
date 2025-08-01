# app/models/personagens/jogador_ficticio.py
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../..')))
from backend.app.models.personagens.personagem_principal import Usuario

jogador = Usuario("nome")