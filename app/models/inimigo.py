# app/models/inimigo.py

class Inimigo:
    def __init__(self, nome: str, nivel: int, vida: int, dano: int):
        self.nome = nome
        self.nivel = nivel
        self.vida = vida
        self.dano = dano

    def atacar(self, alvo):
        print(f"{self.nome} ataca {alvo.nome} causando {self.dano} de dano.")
        alvo.receber_dano(self.dano)
