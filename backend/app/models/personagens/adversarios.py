# app/models/inimigo.py
from dataclasses import field, dataclass
from typing import Any

@dataclass
class AdversarioHumano:
    nome: str 
    idade: int
    peso: int
    gênero: str
    altura: float

    nível: int
    experiência: int

    dano: int
    velocidade: int
    defesa: int
    vida: int

    arma: Any
    escudo: Any

    classe: Any

    primeira_habilidade_passiva: Any = None
    segunda_habilidade_passiva: Any = None
    terceira_habilidade_passiva: Any = None

    primeira_habilidade_ativa: Any = None
    segunda_habilidade_ativa: Any = None

    descrição: str = field(default = "", init = False)

    def __post_init__(self):
        self.atualizar_descrição()
        self.atributos()

    def atualizar_descrição(self) -> None:
        self.atributos()
        self.descrição = (f"nome: {self.nome}\n"
                          f"idade: {self.idade}\n"
                          f"peso: {self.peso}Kg\n"
                          f"genero: {self.gênero}\n"
                          f"altura: {self.altura}m\n"
                          f"nível: {self.nível}\n"
                          f"dano: {self.dano}\n"
                          f"velocidade: {self.velocidade}\n"
                          f"defesa: {self.defesa}\n"
                          f"vida: {self.vida}\n"
                          f"arma: {self.arma}\n"
                          f"escudo: {self.escudo}\n"
                          f"classe: {self.classe}\n")
        

    def atributos(self) -> None:
        self.dano *= self.nível
        self.velocidade *= self.nível
        self.defesa *= self.nível
        self.vida *= self.nível

    def receber_dano(self, quantidade) -> None:
        self.vida -= quantidade
        if self.vida < 0:
            self.vida = 0

    def atacar(self, alvo: dict) -> None:
        alvo["vida"] -= self.dano

    def estar_vivo(self):
        while self.vida > 0:
            return True


class AdversarioDemiHumano:
    pass

class AdversarioMontro:
    pass

