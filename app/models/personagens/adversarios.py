# app/models/inimigo.py

class Inimigo:
    def __init__(self, nome: str, nivel: int, vida: int, dano: int):
        self.nome = nome
        self.nivel = nivel
        self.vida = vida
        self.dano = dano

