from random import choice, randint
from typing import Any, Dict, Optional
from _efeito_munições import (
    efeito_assoviante, efeito_congelante, efeito_desintegrador,
    efeito_eletrocutante, efeito_explosivo, efeito_flamengante,
    efeito_paralisante, efeito_tranquilizante, efeito_venenoso
)

class Munição:
    efeitos_possiveis = [efeito_assoviante, efeito_congelante, efeito_desintegrador,
    efeito_eletrocutante, efeito_explosivo, efeito_flamengante,
    efeito_paralisante, efeito_tranquilizante, efeito_venenoso]
    raridades = {
        "comum": 1.0,   
        "rara": 1.5,
        "épica": 2.3,
        "lendaria": 2.8
    }

    def __init__(self, nome: str, dano_base: int, peso: int):
        self.nome = nome
        self.dano_base = dano_base
        self.peso = peso
        self.nivel = int()
        self.raridade = str()
        self.efeito: Optional[Any] = None
        self.dano_final = Any
        self.descrição = {
            "nome": self.nome,
            "Dano": self.dano_final,
            "Peso": self.peso,
            "Nível": self.nivel,
            "Raridade": self.raridade,
            "Efeito": self.efeito
        }
    def definir_nivel_com_parametro_usuario(self, usuario: Dict) -> None:
        nivel_usuario = usuario["nível"]
        self.nivel = randint(max(1, nivel_usuario - 2), min(nivel_usuario + 2, 100))

    def definir_nivel_manual(self, nivel: int) -> None:
        self.nivel = nivel

    def calcular_dano(self) -> None:
        fator = self.raridades.get(self.raridade, 1)
        self.dano_final = (self.dano_base * self.nivel) * fator

    def escolher_raridade(self, raridade: str) -> None:
        self.raridade = raridade

    def escolher_efeito_aleatorio(self) -> None:
        self.efeito = choice(self.efeitos_possiveis)

    def escolher_efeito_manual(self, efeito: Any) -> None:
        self.efeito = efeito

    def aplicar_efeito(self, alvo: Dict) -> None:
        if self.efeito:
            self.efeito.aplicar_efeito(alvo)


def criar_flecha(nome, raridade, usuario: Dict):
    raridades = {
        "comum": (5, 1),
        "rara": (7, 1),
        "épica": (9, 1),
        "lendaria": (13, 1)
    }
    dano, peso = raridades[raridade]
    flecha = Munição(nome, dano, peso)
    flecha.escolher_raridade(raridade)
    flecha.definir_nivel_com_parametro_usuario(usuario)
    flecha.escolher_efeito_aleatorio()
    flecha.calcular_dano()
    flecha.descrição.update({
        "Dano": flecha.dano_final,
        "Nível": flecha.nivel,
        "Raridade": flecha.raridade,
        "Efeito": flecha.efeito.nome,
    })
    return flecha

def criar_dardo(nome, raridade, usuario: Dict):
    raridades = {
        "comum": (4,1),
        "raro": (6,1),
        "epico": (8,1),
        "lendario": (12,1)
    }

    dano, peso = raridades[raridade]
    dardo = Munição(nome, dano, peso)
    dardo.escolher_raridade(raridade)
    dardo.definir_nivel_com_parametro_usuario(usuario)
    dardo.escolher_efeito_aleatorio()
    dardo.calcular_dano()
    dardo.descrição.update({
        "Dano": dardo.dano_final,
        "Nível": dardo.nivel,
        "Raridade": dardo.raridade,
        "Efeito": dardo.efeito.nome,
    })
    return dardo