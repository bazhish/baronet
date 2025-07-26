# app/models/adversarios.py
from dataclasses import field, dataclass
from typing import Any

@dataclass
class AdversarioDemiHumano:
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
    vida_atual: int
    vida_máxima: int

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
        self.atributos()
        self.atualizar_descrição()

    def atualizar_descrição(self) -> None:
        self.descrição = (f"nome: {self.nome}\n"
                          f"idade: {self.idade}\n"
                          f"peso: {self.peso}Kg\n"
                          f"genero: {self.gênero}\n"
                          f"altura: {self.altura}m\n"
                          f"nível: {self.nível}\n"
                          f"dano: {self.dano}\n"
                          f"velocidade: {self.velocidade}\n"
                          f"defesa: {self.defesa}\n"
                          f"vida: {self.vida_atual}/{self.vida_máxima}\n"
                          f"arma: {self.arma}\n"
                          f"escudo: {self.escudo}\n"
                          f"classe: {self.classe}\n")
        

    def atributos(self) -> None:
        self.dano *= self.nível
        self.velocidade *= self.nível
        self.defesa *= self.nível
        self.vida_atual *= self.nível

    def atacar(self, alvo) -> None:
        alvo.vida_atual -= self.dano

    def estar_vivo(self):
        while self.vida > 0:
            return True

@dataclass
class AdversarioMontro:
    nome: str
    peso: float
    altura: float

    nível: int
    experiência: int

    dano: int
    velocidade: int
    defesa: int
    vida: int

    arma: Any = None
    escudo: Any = None

    descrição: str = field(default = "", init = False)

    def __post_init__(self):
        self.atualizar_descrição()
        self.atributos()

    def atualizar_descrição(self) -> None:
        self.atributos()
        self.descrição = (f"nome: {self.nome}\n"
                          f"peso: {self.peso}Kg\n"
                          f"altura: {self.altura}m\n"
                          f"nível: {self.nível}\n"
                          f"dano: {self.dano}\n"
                          f"velocidade: {self.velocidade}\n"
                          f"defesa: {self.defesa}\n"
                          f"vida: {self.vida}\n"
                          f"arma: {self.arma}\n"
                          f"escudo: {self.escudo}\n")
        

    def atributos(self) -> None:
        self.dano *= self.nível
        self.velocidade *= self.nível
        self.defesa *= self.nível
        self.vida *= self.nível

    def atacar(self, alvo) -> None:
        alvo.vida_atual -= self.dano

    def estar_vivo(self):
        return self.vida > 0