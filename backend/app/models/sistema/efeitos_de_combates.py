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
        super().__init__("uueimadura", 1,1,1,1,1)

    def aplicar_efeito(self, alvo):
        for segundos in range(self.duração):
            alvo.vida_atual -= self.dano
            alvo.velocidade = max(0, alvo.velocidade - self.velocidade)
            alvo.defesa = max(0, alvo.defesa - self.defesa)

    def atualizar_descrição(self):
        super().atualizar_descrição()

class Veneno(Base):
    def __init__(self):
        super().__init__("veneno", 1,1,1,1,1)

    def aplicar_efeito(self, alvo):
        for segundos in range(self.duração):
            alvo.vida_atual -= self.dano
            alvo.velocidade = max(0, alvo.velocidade - self.velocidade)
            alvo.defesa = max(0, alvo.defesa - self.defesa)

    def atualizar_descrição(self):
        super().atualizar_descrição()

class Sangramento(Base):
    def __init__(self):
        super().__init__("sangramento", 1,1,1,1,1)

    def aplicar_efeito(self, alvo):
        for segundos in range(self.duração):
            alvo.vida_atual -= self.dano
            alvo.velocidade = max(0, alvo.velocidade - self.velocidade)
            alvo.defesa = max(0, alvo.defesa - self.defesa)

    def atualizar_descrição(self):
        super().atualizar_descrição()

class Atordoamento(Base):
    def __init__(self):
        super().__init__("atordoamento", 1,1,1,1,1)

    def aplicar_efeito(self, alvo):
        for segundos in range(self.duração):
            alvo.velocidade = max(0, alvo.velocidade - self.velocidade)
            alvo.defesa = max(0, alvo.defesa - self.defesa)

    def atualizar_descrição(self):
        return super().atualizar_descrição()
    
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
        else:
            pass

    def atualizar_descrição(self):
        return super().atualizar_descrição()
    
class Lentidao(Base):
    def __init__(self):
        super().__init__("Lentidão",1,1,1,1,1)

    def aplicar_efeito(self, alvo):
        for segundos in range(self.duração):
            alvo.velocidade = max(0, alvo.velocidade - self.velocidade)
            alvo.defesa = max(0, alvo.defesa - self.defesa)

    def atualizar_descrição(self):
        return super().atualizar_descrição()
    
class Explosivo(Base):
    def __init__(self):
        super().__init__("Explosivo",1,1,1,1,1)

    def aplicar_efeito(self, alvo):
        for segundos in range(self.duração)

# vantagens

@dataclass
class Defesa():
    porcentagem: float

    def vantagem(self, usuario):
        self.valor = usuario.defesa * self.porcentagem
        usuario.defesa_bonus = self.valor
@dataclass
class Velocidade():
    porcentagem: float

    def vantagem(self, usuario):
        self.valor = usuario.velocidade * self.porcentagem
        usuario.velocidade_bonus = self.valor
@dataclass
class Vida():
    porcentagem: float

    def vantagem(self, usuario):
        self.valor = usuario.vida * self.porcentagem
        usuario.vida_bonus = self.valor
@dataclass
class Estamina():
    porcentagem: float

    def vantagem(self, usuario):
        self.valor = usuario.estamina * self.porcentagem
        usuario.estamina_bonus = self.valor
@dataclass
class Dano():
    porcentagem: float

    def vantagem(self, usuario):
        self.valor = usuario.dano * self.porcentagem
        usuario.dano_bonus = self.valor
@dataclass
class BonusDeExperiencia():
    porcentagem: float

    def vantagem(self, usuario):
        usuario.bonus_de_experiência = self.porcentagem



