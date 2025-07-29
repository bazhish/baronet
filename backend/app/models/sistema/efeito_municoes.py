import sys
import os

# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../..')))

from abc import ABC, abstractmethod

class EfeitoMunição(ABC):
    def __init__(self, nome, alcance, duração, dano, velocidade, defesa):
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

class Queimadura(EfeitoMunição):
    def __init__(self):
        super().__init__("Queimadura", 1, 1, 1, 1, 1)

    def aplicar_efeito(self, alvo):
        for segundos in range(self.duração):
            alvo.vida_atual -= self.dano
            alvo.velocidade = max(0, alvo.velocidade - self.velocidade)
            alvo.defesa = max(0, alvo.defesa - self.defesa)

    def atualizar_descrição(self):
        super().atualizar_descrição()