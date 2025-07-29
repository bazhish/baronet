#backend/app/models/sistema/efeitos_de_combates.py
import sys, os
from abc import ABC, abstractmethod
from ..personagens.adversarios import AdversarioDemiHumano
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../..')))


class Base(ABC):
    def __init__(self, nome, alcance = 0, duração = 0, dano = 0, velocidade = 0, defesa = 0):
        self.nome = nome
        self.alcance = alcance
        self.duração = duração
        self.dano = dano
        self.velocidade = velocidade
        self.defesa = defesa
        self.descrição = ""
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