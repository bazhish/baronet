from random import randint, choice
from typing import Any, Dict

class Escudo:
    raridades = {
        "comum": 1.0,
        "raro": 1.5,
        "epico": 2.3,
        "lendario": 2.8
    }

    def __init__(self, nome, defesa, peso):
        self.nome = nome
        self.defesa = defesa
        self.peso = peso
        self.nivel = int()
        self.raridade = str()
        self.atributo_adicional = Any
        self.defesa_final = Any

    def definir_nivel_com_base_no_usuario(self, usuario: Dict):
        nivel_usuario = usuario["nível"]
        self.nivel = randint(max(1, nivel_usuario - 3), min(nivel_usuario + 3, 100))

    def definir_nivel_manual(self, nivel):
        self.nivel = nivel

    def escolher_raridade(self, raridade):
        self.raridade = raridade

    def calcular_defesa(self):
        fator = self.raridades.get(self.raridade, 1.0)
        self.defesa_final = self.defesa * self.nivel * fator

    def escolher_atributo_adicional_aleatorio(self):
        atributos = ["defesa", "vida", "velocidade"]
        self.atributo_adicional = choice(atributos)

    def aplicar_bonus_no_usuario(self, usuario: Dict):
        defesa_bonus = 2
        vida_bonus = 10
        velocidade_bonus = 3

        fator = self.raridades.get(self.raridade, 1.0)
        defesa_bonus *= self.nivel * fator
        vida_bonus *= self.nivel * fator
        velocidade_bonus *= self.nivel * fator

        if self.atributo_adicional == "defesa":
            usuario["defesa"] += defesa_bonus
        elif self.atributo_adicional == "vida":
            usuario["vida"] += vida_bonus
        elif self.atributo_adicional == "velocidade":
            usuario["velocidade"] += velocidade_bonus

    def gerar_escudo(self):
        self.calcular_defesa()
        return {
            "Nome": self.nome,
            "Nível": self.nivel,
            "Raridade": self.raridade,
            "Defesa": self.defesa_final,
            "Peso": self.peso,
            "Atributo adicional": self.atributo_adicional,
        }

def criar_escudo(nome: str, raridade, usuario: Dict):
    raridades = {
        "comum": (5,3),
        "raro": (7,3),
        "epico": (10,2),
        "lendario": (15,2)
    }

    defesa, peso = raridades[raridade]
    escudo = Escudo(nome, defesa, peso)
    escudo.definir_nivel_com_base_no_usuario(usuario)
    escudo.escolher_raridade(raridade)
    escudo.calcular_defesa()
    escudo.escolher_atributo_adicional_aleatorio()
    escudo.aplicar_bonus_no_usuario(usuario)
    return escudo.gerar_escudo()