# backend/app/models/personagens/personagem_principal.py
from dataclasses import field, dataclass
from typing import Any

@dataclass
class Usuario:
    
    idade: int
    peso: float
    nome: str
    genero: str
    altura: float

    tentativas_restantes: int = 3
    tentativas: int = 3

    nível_atual: int = 1
    nível_máximo: int = 100
    
    experiência_atual: int = 0
    experiência_máxima: int = 100

    dano_base: int = 2
    velocidade_base: int = 4
    defesa_base: int = 5
    vida_base: int = 100
    estamina_base: int = 150

    arma: Any = None
    escudo: Any = None

    vida_atual: int = field(init=False)
    vida_máxima: int = field(init=False)
    estamina_atual: int = field(init=False)
    estamina_máxima: int = field(init=False)

    classe_do_usuário: Any = None

    primeira_habilidade_passiva: Any = None
    segunda_habilidade_passiva: Any = None
    terceira_habilidade_passiva: Any = None

    habilidade_ativa: Any = None
    habilidade_especial: Any = None

    descrição: str = field(default = "", init = False)

    def __post_init__(self):
        self.vida_máxima = self.vida_base
        self.vida_atual = self.vida_máxima
        self.estamina_máxima = self.estamina_base
        self.estamina_atual = self.estamina_máxima
        self.limites()

    def limites(self):
        if not (70 <= self.peso <= 110):
            raise ValueError("peso deve estar entre 70kg e 110kg")
        if not (1.5 <= self.altura <= 2.5):
            raise ValueError("altura deve estar entre 1.5m e 2.5m")
        if not (16 <= self.idade <= 25):
            raise ValueError("idade deve estar entre 16 e 25 anos")

    @property
    def dano_final(self):
        return self.dano_base + self.dano_bonus

    @property
    def velocidade_final(self):
        return self.velocidade_base + self.velocidade_bonus

    @property
    def defesa_final(self):
        return self.defesa_base + self.defesa_bonus

    def equipar_arma(self, arma):
        self.arma = arma
        self.dano_bonus = arma.dano if arma else 0
        self.velocidade_bonus = arma.velocidade if arma else 0

    def remover_arma(self):
        self.arma = None
        self.dano_bonus = 0
        self.velocidade_bonus = 0

    def equipar_escudo(self, escudo):
        self.escudo = escudo
        self.defesa_bonus = escudo.defesa if escudo else 0

    def remover_escudo(self):
        self.escudo = None
        self.defesa_bonus = 0

    def subir_nivel(self):
        if self.nível_atual < self.nível_máximo:
            self.nível_atual += 1
            self.dano_base += 1
            self.velocidade_base += 1
            self.defesa_base += 1
            self.vida_base += 10
            self.estamina_base += 10
            self.vida_máxima = self.vida_base
            self.vida_atual = self.vida_máxima
            self.estamina_máxima = self.estamina_base
            self.estamina_atual = self.estamina_máxima
            self.atualizar_experiencia_maxima()

    def atualizar_experiencia_maxima(self):
        multiplicador = 1.0
        if self.nível_atual <= 25:
            multiplicador = 1.25
        elif self.nível_atual <= 50:
            multiplicador = 1.5
        elif self.nível_atual <= 75:
            multiplicador = 1.75
        else:
            multiplicador = 2.0
        self.experiência_máxima = int(self.experiência_máxima * multiplicador)

    def atualizar_atributos(self) -> None:
        self.dano_base *= self.nível_atual
        self.velocidade_base *= self.nível_atual
        self.defesa_base *= self.nível_atual
        self.vida_máxima *= self.nível_atual
        self.vida_atual = self.vida_máxima
        self.estamina_máxima *= self.nível_atual
        self.estamina_atual = self.estamina_máxima
        self.atualizar_descrição()

    def receber_experiencia(self, xp: int):
        self.experiência_atual += xp
        while self.experiência_atual >= self.experiência_máxima and self.nível_atual < self.nível_máximo:
            self.experiência_atual -= self.experiência_máxima
            self.subir_nivel()
    
    def diminuir_tentativas(self) -> None:
        if self.vida_atual <= 0:
            self.tentativas_restantes -= 1
            self.vida_atual = self.vida_máxima
            print("você perdeu uma tentativa!")

        if self.tentativas_restantes == 0:
            raise SystemExit("suas tentativas acabaram, você perdeu o jogo")

    def atacar(self, alvo):
        alvo.vida -= self.dano_final

    def atualizar_descrição(self) -> None:
        self.descrição = (f"nome: {self.nome}\n"
                          f"idade: {self.idade}\n"
                          f"peso: {self.peso}Kg\n"
                          f"genero: {self.genero}\n"
                          f"altura: {self.altura}m\n"
                          f"experiência: {self.experiência_atual}/{self.experiência_máxima}\n"
                          f"nível: {self.nível_atual}/{self.nível_máximo}\n"
                          f"dano: {self.dano_final}\n"
                          f"velocidade: {self.velocidade_final}\n"
                          f"defesa: {self.defesa_final}\n"
                          f"vida: {self.vida_atual}/{self.vida_máxima}\n"
                          f"estamina: {self.estamina_atual}/{self.estamina_máxima}\n"
                          f"arma: {self.arma}\n"
                          f"escudo: {self.escudo}\n"
                          f"tentativas: {self.tentativas_restantes}\n"
                          f"classe: {self.classe_do_usuário}\n")