from dataclasses import dataclass, field
from random import choice, randint
from typing import Any, Optional
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../..')))
from backend.app.models.sistema.efeitos_de_combates import (
    Queimadura, Veneno, Sangramento, Atordoamento, Silencio, Lentidao, Explosivo
)

@dataclass
class Munição:
    nome: str
    dano_base: int
    peso: int
    nível: int = 1
    raridade: str = "comum"
    efeito: Optional[Any] = None
    dano_final: float = 0.0
    descrição: str = field(default="", init=False)

    def __post_init__(self):
        self.efeitos_possiveis = [Queimadura, Veneno, Sangramento, Atordoamento, Silencio, Lentidao, Explosivo]
        self.raridades = {
            "comum": 1.0,
            "rara": 1.5,
            "épica": 2.3,
            "lendária": 2.8
        }
        self.atualizar_descrição()

    def atualizar_descrição(self):
        efeito_nome = self.efeito.nome if self.efeito else "Nenhum"
        self.descrição = (
            f"Nome: {self.nome}\n"
            f"Dano Base: {self.dano_base}\n"
            f"Dano Final: {self.dano_final}\n"
            f"Peso: {self.peso}\n"
            f"Nível: {self.nível}\n"
            f"Raridade: {self.raridade}\n"
            f"Efeito: {efeito_nome}\n"
        )

    def definir_nível_com_parametro_usuario(self, usuario) -> None:
        nível_usuario = getattr(usuario, "nível_atual", 1)
        self.nível = randint(max(1, nível_usuario - 2), min(nível_usuario + 2, 100))

    def definir_nível_manual(self, nível: int) -> None:
        self.nível = nível

    def calcular_dano(self) -> None:
        fator = self.raridades.get(self.raridade, 1.0)
        self.dano_final = (self.dano_base * self.nível) * fator

    def escolher_raridade(self, raridade: str) -> None:
        if raridade in self.raridades:
            self.raridade = raridade
        else:
            self.raridade = "comum"

    def escolher_efeito_aleatorio(self) -> None:
        self.efeito = choice(self.efeitos_possiveis)()

    def escolher_efeito_manual(self, efeito: Any) -> None:
        self.efeito = efeito

    def aplicar_efeito(self, alvo) -> None:
        if self.efeito:
            self.efeito.aplicar_efeito(alvo)

def criar_flecha(nome: str, raridade: str, usuario: Any) -> Munição:
    raridades = {
        "comum": (5, 1),
        "rara": (7, 1),
        "épica": (9, 1),
        "lendária": (13, 1)
    }
    dano, peso = raridades.get(raridade, (5, 1))
    flecha = Munição(nome, dano, peso)
    flecha.escolher_raridade(raridade)
    flecha.definir_nível_com_parametro_usuario(usuario)
    flecha.escolher_efeito_aleatorio()
    flecha.calcular_dano()
    flecha.atualizar_descrição()
    return flecha

def criar_dardo(nome: str, raridade: str, usuario: Any) -> Munição:
    raridades = {
        "comum": (4, 1),
        "rara": (6, 1),
        "épica": (8, 1),
        "lendária": (12, 1)
    }
    dano, peso = raridades.get(raridade, (4, 1))
    dardo = Munição(nome, dano, peso)
    dardo.escolher_raridade(raridade)
    dardo.definir_nível_com_parametro_usuario(usuario)
    dardo.escolher_efeito_aleatorio()
    dardo.calcular_dano()
    dardo.atualizar_descrição()
    return dardo