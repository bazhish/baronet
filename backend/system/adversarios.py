# backend/app/models/personagens/adversarios.py
from dataclasses import dataclass, field
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
    estamina_base: int

    arma: Any = None
    escudo: Any = None
    classe: Any = None

    primeira_habilidade_passiva: Any = None
    segunda_habilidade_passiva: Any = None
    terceira_habilidade_passiva: Any = None

    habilidade_ativa: Any = None
    habilidade_especial: Any = None

    elmo: Any = None
    peitoral: Any = None
    calça: Any = None
    botas: Any = None

    posição_x: int = 0
    posição_y: int = 0

    estado: str = field(default="normal", init=False)
    pode_atacar: bool = field(default=True, init=False)
    pode_mover: bool = field(default=True, init=False)
    bloqueio_ativo: bool = field(default=False, init=False)
    precisao_bonus: int = field(default=0, init=False)
    critico_bonus: int = field(default=0, init=False)
    resistencia_empurrao: bool = field(default=False, init=False)

    descrição: str = field(default="", init=False)

    dano_bonus: int = field(default=0, init=False)
    velocidade_bonus: int = field(default=0, init=False)
    defesa_bonus: int = field(default=0, init=False)
    vida_bonus: int = field(default=0, init=False)
    estamina_bonus: int = field(default=0, init=False)

    vida_atual: int = field(init=False)
    _vida_máxima: int = field(init=False, repr=False)
    estamina_atual: int = field(init=False)
    _estamina_máxima: int = field(init=False, repr=False)

    def __post_init__(self):
        self.atributos()
        self.vida_atual = self.vida_máxima
        self.estamina_atual = self.estamina_máxima
        self.atualizar_descrição()

    def atributos(self):
        self.dano_bonus = 0
        self.velocidade_bonus = 0
        self.defesa_bonus = 0
        self.vida_bonus = 0
        self.estamina_bonus = 0
        self._vida_máxima = self.vida_base * self.nível + self.vida_bonus
        self._estamina_máxima = self.estamina_base * self.nível + self.estamina_bonus

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
        return self._vida_máxima

    @property
    def estamina_máxima(self):
        return self._estamina_máxima

    def atualizar_status_com_bonus(self):
        self._vida_máxima = self.vida_base * self.nível + self.vida_bonus
        self._estamina_máxima = self.estamina_base * self.nível + self.estamina_bonus
        self.vida_atual = self._vida_máxima
        self.estamina_atual = self._estamina_máxima

    def aplicar_habilidades_passivas(self):
        if self.primeira_habilidade_passiva:
            self.primeira_habilidade_passiva.aplicar_habilidade(self)
        if self.segunda_habilidade_passiva:
            self.segunda_habilidade_passiva.aplicar_habilidade(self)
        if self.terceira_habilidade_passiva:
            self.terceira_habilidade_passiva.aplicar_habilidade(self)

    def aplicar_habilidade_ativa(self, alvo=None):
        if self.habilidade_ativa:
            if alvo:
                self.habilidade_ativa.aplicar_habilidade(self, alvo)
            else:
                self.habilidade_ativa.aplicar_habilidade(self)

    def atualizar_descrição(self) -> None:
        self.descrição = (
            f"nome: {self.nome}\n"
            f"idade: {self.idade}\n"
            f"peso: {self.peso}Kg\n"
            f"genero: {self.gênero}\n"
            f"altura: {self.altura}m\n"
            f"nível: {self.nível}\n"
            f"dano: {self.dano_final}\n"
            f"velocidade: {self.velocidade_final}\n"
            f"defesa: {self.defesa_final}\n"
            f"vida: {self.vida_atual}/{self.vida_máxima}\n"
            f"estamina: {self.estamina_atual}/{self.estamina_máxima}\n"
            f"arma: {self.arma}\n"
            f"escudo: {self.escudo}\n"
            f"elmo: {self.elmo}\n"
            f"peitoral: {self.peitoral}\n"
            f"calça: {self.calça}\n"
            f"botas: {self.botas}\n"
            f"classe: {self.classe}\n"
            f"estado: {self.estado}\n"
            f"primeira habilidade passiva: {getattr(self.primeira_habilidade_passiva, 'nome', None)}\n"
            f"segunda habilidade passiva: {getattr(self.segunda_habilidade_passiva, 'nome', None)}\n"
            f"terceira habilidade passiva: {getattr(self.terceira_habilidade_passiva, 'nome', None)}\n"
            f"habilidade ativa: {getattr(self.habilidade_ativa, 'nome', None)}\n"
            f"habilidade especial: {getattr(self.habilidade_especial, 'nome', None)}\n"
            f"posição: ({self.posição_x}, {self.posição_y})\n"
        )

    def atacar(self, alvo) -> None:
        dano = max(1, self.dano_final - getattr(alvo, 'defesa_final', 0))
<<<<<<< HEAD
        alvo.vida_atual = max(0, alvo.vida_atual - dano)
=======
        alvo.vida_atual = max(1, alvo.vida_atual - dano)
>>>>>>> 9780770656b768a18468949f9c25aa48669c0930

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
    estamina_base: int = 100  # Novo atributo

    arma: Any = None
    escudo: Any = None

    elmo: Any = None
    peitoral: Any = None
    calça: Any = None
    botas: Any = None

    posição_x: int = 0
    posição_y: int = 0

    estado: str = field(default="normal", init=False)
    pode_atacar: bool = field(default=True, init=False)
    pode_mover: bool = field(default=True, init=False)
    bloqueio_ativo: bool = field(default=False, init=False)
    precisao_bonus: int = field(default=0, init=False)
    critico_bonus: int = field(default=0, init=False)
    resistencia_empurrao: bool = field(default=False, init=False)

    descrição: str = field(default="", init=False)

    dano_bonus: int = field(default=0, init=False)
    velocidade_bonus: int = field(default=0, init=False)
    defesa_bonus: int = field(default=0, init=False)
    vida_bonus: int = field(default=0, init=False)
    estamina_bonus: int = field(default=0, init=False)

    vida_atual: int = field(init=False)
    _vida_máxima: int = field(init=False, repr=False)
    estamina_atual: int = field(init=False)
    _estamina_máxima: int = field(init=False, repr=False)

    def __post_init__(self):
        self.atributos()
        self.vida_atual = self.vida_máxima
        self.estamina_atual = self.estamina_máxima
        self.atualizar_descrição()

    def atributos(self):
        self.dano_bonus = 0
        self.velocidade_bonus = 0
        self.defesa_bonus = 0
        self.vida_bonus = 0
        self.estamina_bonus = 0
        self._vida_máxima = self.vida_base * self.nível + self.vida_bonus
        self._estamina_máxima = self.estamina_base * self.nível + self.estamina_bonus

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
        return self._vida_máxima

    @property
    def estamina_máxima(self):
        return self._estamina_máxima

    def atualizar_status_com_bonus(self):
        self._vida_máxima = self.vida_base * self.nível + self.vida_bonus
        self._estamina_máxima = self.estamina_base * self.nível + self.estamina_bonus
        self.vida_atual = self._vida_máxima
        self.estamina_atual = self._estamina_máxima

    def receber_experiencia(self, experiencia: int):
        self.experiência += experiencia
        # Adapte conforme regras de evolução dos adversários

    def subir_nivel(self):
        self.nível += 1
        self.dano_base += 1
        self.velocidade_base += 1
        self.defesa_base += 1
        self.vida_base += 10
        self.estamina_base += 10
        self.atualizar_status_com_bonus()

    def atualizar_descrição(self) -> None:
        self.descrição = (
            f"nome: {self.nome}\n"
            f"peso: {self.peso}Kg\n"
            f"altura: {self.altura}m\n"
            f"nível: {self.nível}\n"
            f"dano: {self.dano_final}\n"
            f"velocidade: {self.velocidade_final}\n"
            f"defesa: {self.defesa_final}\n"
            f"vida: {self.vida_atual}/{self.vida_máxima}\n"
            f"estamina: {self.estamina_atual}/{self.estamina_máxima}\n"
            f"arma: {self.arma}\n"
            f"escudo: {self.escudo}\n"
            f"elmo: {self.elmo}\n"
            f"peitoral: {self.peitoral}\n"
            f"calça: {self.calça}\n"
            f"botas: {self.botas}\n"
            f"estado: {self.estado}\n"
            f"posição: ({self.posição_x}, {self.posição_y})\n"
        )

    def atacar(self, alvo) -> None:
        dano = max(0, self.dano_final - getattr(alvo, 'defesa_final', 0))
        alvo.vida_atual = max(0, alvo.vida_atual - dano)

    def estar_vivo(self):
        return self.vida_atual > 0