from typing import Any

class Personagem:
    def __init__(self, nome: str, classe: Any, nivel: int, vida: int, stamina: int = 100):
        self.nome = nome
        self.classe = classe
        self.nivel = nivel
        self.vida = vida
        self.stamina = stamina
        self.experiencia = 0
        self.habilidades = []

    def subir_nivel(self):
        self.nivel += 1
        self.vida += 10
        self.stamina += 5
        print(f"{self.nome} subiu para o nível {self.nivel}!")

    def receber_dano(self, dano: int):
        self.vida -= dano
        if self.vida <= 0:
            self.vida = 0
            print(f"{self.nome} foi derrotado.")
        else:
            print(f"{self.nome} recebeu {dano} de dano. Vida restante: {self.vida}")
