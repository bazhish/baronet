# app/models/personagens/jogador_ficticio.py
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../..')))
from backend.app.models.personagens.personagem_principal import Usuario

jogador = Usuario("jaseh", 21, 98.7, "masculino", 2.1)
jogador.receber_experiencia(400)
jogador.atualizar_descrição()