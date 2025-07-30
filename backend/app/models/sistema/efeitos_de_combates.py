#backend/app/models/sistema/efeitos_de_combates.py
import sys, os
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from ..personagens.adversarios import AdversarioDemiHumano
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../..')))

@dataclass
class Base(ABC):
    nome: str
    alcance: int = 0
    duração: int = 0
    dano: int = 0
    velocidade: int = 0
    defesa: int = 0
    descrição: str = field(default = "", init = False)

    def __post_init__(self):
        self.atualizar_descrição()

    @abstractmethod
    def aplicar_efeito(self, alvo):
        pass

    def atualizar_descrição(self):
        self.descrição = (
            f"nome: {self.nome} "
            f"alcance: {self.alcance} "
            f"duração: {self.duração} "
            f"dano: {self.dano} "
            f"velocidade: {self.velocidade} "
            f"defesa: {self.defesa}"
        )

# desvantagens

class Queimadura(Base):
    def __init__(self):
        super().__init__("queimadura", 1,1,1,1,1)

    def aplicar_efeito(self, alvo):
        for segundos in range(self.duração):
            alvo.vida_atual -= self.dano
            alvo.velocidade = max(0, alvo.velocidade - self.velocidade)
            alvo.defesa = max(0, alvo.defesa - self.defesa)

class Veneno(Base):
    def __init__(self):
        super().__init__("veneno", 1,1,1,1,1)

    def aplicar_efeito(self, alvo):
        for segundos in range(self.duração):
            alvo.vida_atual -= self.dano
            alvo.velocidade = max(0, alvo.velocidade - self.velocidade)
            alvo.defesa = max(0, alvo.defesa - self.defesa)

class Sangramento(Base):
    def __init__(self):
        super().__init__("sangramento", 1,1,1,1,1)

    def aplicar_efeito(self, alvo):
        for segundos in range(self.duração):
            alvo.vida_atual -= self.dano
            alvo.velocidade = max(0, alvo.velocidade - self.velocidade)
            alvo.defesa = max(0, alvo.defesa - self.defesa)

class Atordoamento(Base):
    def __init__(self):
        super().__init__("atordoamento", 1,1,1,1,1)

    def aplicar_efeito(self, alvo):
        for segundos in range(self.duração):
            alvo.velocidade = max(0, alvo.velocidade - self.velocidade)
            alvo.defesa = max(0, alvo.defesa - self.defesa)

class Silencio(Base):
    def __init__(self):
        super().__init__("silêncio")

    def aplicar_efeito(self, alvo):
        if isinstance(alvo, AdversarioDemiHumano):
            for segundos in range(self.duração):
                alvo.primeira_habilidade_passiva = None
                alvo.segunda_habilidade_passiva = None
                alvo.terceira_habilidade_passiva = None
                alvo.habilidade_ativa = None
                alvo.habilidade_especial = None

class Lentidao(Base):
    def __init__(self):
        super().__init__("Lentidão",1,1,1,1,1)

    def aplicar_efeito(self, alvo):
        for segundos in range(self.duração):
            alvo.velocidade = max(0, alvo.velocidade - self.velocidade)
            alvo.defesa = max(0, alvo.defesa - self.defesa)

class Explosivo(Base):
    def __init__(self):
        super().__init__("Explosivo",1,1,1,1,1)

    def aplicar_efeito(self, alvo):
        alvo.vida_atual -= self.dano

# vantagens

@dataclass
class VantagemBase:
    porcentagem: float
    atributo: str
    descricao: str = ""

    def vantagem(self, usuario):
        valor_base = getattr(usuario, self.atributo)
        valor_bonus = valor_base * self.porcentagem
        setattr(usuario, f"{self.atributo}_bonus", valor_bonus)

@dataclass
class Defesa(VantagemBase):
    def __init__(self, porcentagem: float):
        descricao = f"Aumenta a defesa em {porcentagem*100:.0f}%."
        super().__init__(porcentagem, "defesa", descricao)

@dataclass
class Velocidade(VantagemBase):
    def __init__(self, porcentagem: float):
        descricao = f"Aumenta a velocidade em {porcentagem*100:.0f}%."
        super().__init__(porcentagem, "velocidade", descricao)

@dataclass
class Vida(VantagemBase):
    def __init__(self, porcentagem: float):
        descricao = f"Aumenta a vida máxima em {porcentagem*100:.0f}%."
        super().__init__(porcentagem, "vida", descricao)

@dataclass
class Estamina(VantagemBase):
    def __init__(self, porcentagem: float):
        descricao = f"Aumenta a estamina em {porcentagem*100:.0f}%."
        super().__init__(porcentagem, "estamina", descricao)

@dataclass
class Dano(VantagemBase):
    def __init__(self, porcentagem: float):
        descricao = f"Aumenta o dano em {porcentagem*100:.0f}%."
        super().__init__(porcentagem, "dano", descricao)

@dataclass
class BonusDeExperiencia:
    porcentagem: float
    descricao: str = ""

    def __post_init__(self):
        self.descricao = f"Aumenta o ganho de experiência em {self.porcentagem*100:.0f}%."

    def vantagem(self, usuario):
        usuario.bonus_de_experiência = self.porcentagem