# backend/app/models/personagens/adversarios.py
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

    dano_base: int
    velocidade_base: int
    defesa_base: int
    vida_base: int

    arma: Any = None
    escudo: Any = None

    classe: Any = None

    primeira_habilidade_passiva: Any = None
    segunda_habilidade_passiva: Any = None
    terceira_habilidade_passiva: Any = None

    habilidade_ativa: Any = None
    habilidade_especial: Any = None

    descrição: str = field(default = "", init = False)

    vida_atual: int = field(init = False)
    vida_máxima: int = field(init = False)

    def __post_init__(self):
        self.atributos()
        self.dano_bonus = 0
        self.velocidade_bonus = 0
        self.defesa_bonus = 0
        self.vida_bonus = 0
        self.estamina_bonus = 0
        self.vida_atual = self.vida_máxima
        self.atualizar_descrição()

    def atualizar_descrição(self) -> None:
        self.descrição = (f"nome: {self.nome}\n"
                          f"idade: {self.idade}\n"
                          f"peso: {self.peso}Kg\n"
                          f"genero: {self.gênero}\n"
                          f"altura: {self.altura}m\n"
                          f"nível: {self.nível}\n"
                          f"dano: {self.dano_final}\n"
                          f"velocidade: {self.velocidade_final}\n"
                          f"defesa: {self.defesa_final}\n"
                          f"vida: {self.vida_atual}/{self.vida_máxima}\n"
                          f"arma: {self.arma}\n"
                          f"escudo: {self.escudo}\n"
                          f"classe: {self.classe}\n")
        
    @property
    def dano_final(self):
        self.dano_base + self.dano_bonus

    @property
    def velocidade_final(self):
        self.velocidade_base + self.velocidade_bonus

    @property
    def defesa_final(self):
        self.defesa_base + self.defesa_bonus

    @property
    def vida_máxima(self):
        self.vida_máxima + self.vida_bonus

    def atacar(self, alvo) -> None:
        alvo.vida_atual -= self.dano

    def estar_vivo(self):
        return self.vida_atual > 0

@dataclass
class AdversarioMonstro:
    nome: str
    peso: float
    altura: float

    nível: int
    experiência: int

    dano_base: int
    velocidade_base: int
    defesa_base: int
    vida_base: int

    arma: Any = None
    escudo: Any = None

    descrição: str = field(default = "", init = False)

    dano_bonus: int = field(default=0, init=False)
    velocidade_bonus: int = field(default=0, init=False)
    defesa_bonus: int = field(default=0, init=False)
    vida_bonus: int = field(default=0, init=False)

    vida_atual: int = field(init=False)
    vida_máxima: int = field(init=False)

    def __post_init__(self):
        self.atributos()
        self.vida_atual = self.vida_máxima
        self.atualizar_descrição()

    def atualizar_descrição(self) -> None:
        self.descrição = (f"nome: {self.nome}\n"
                          f"peso: {self.peso}Kg\n"
                          f"altura: {self.altura}m\n"
                          f"nível: {self.nível}\n"
                          f"dano: {self.dano_final}\n"
                          f"velocidade: {self.velocidade_final}\n"
                          f"defesa: {self.defesa_final}\n"
                          f"vida: {self.vida_atual}/{self.vida_máxima}\n"
                          f"arma: {self.arma}\n"
                          f"escudo: {self.escudo}\n")

    @property
    def dano_final(self):
        return self.dano_base * self.nível + self.dano_bonus

    @property
    def velocidade_final(self):
        return self.velocidade_base * self.nível + self.velocidade_bonus

    @property
    def defesa_final(self):
        return self.defesa_base * self.nível + self.defesa_bonus

    @property
    def vida_máxima(self):
        return self.vida_base * self.nível + self.vida_bonus

    def atributos(self) -> None:
        self.dano_bonus = 0
        self.velocidade_bonus = 0
        self.defesa_bonus = 0
        self.vida_bonus = 0
        self.vida_máxima = self.vida_base * self.nível + self.vida_bonus

    def atacar(self, alvo) -> None:
        alvo.vida_atual -= self.dano_final

    def estar_vivo(self):
        return self.vida_atual > 0