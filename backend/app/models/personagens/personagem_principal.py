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

    tentativas_restantes = 3
    tentativas = 3

    nível_atual = 1
    nível_máximo = 100
    
    experiência_atual = 0
    experiência_máxima = 100

    dano_base = 2
    dano_final: int = dano_base

    velocidade_base = 4
    velocidade_final: int = velocidade_base

    defesa_base = 5
    defesa_final: int = velocidade_base

    vida_base = 100
    vida_atual: int = vida_base
    vida_máxima = 100

    estamina_base = 150
    estamina_atual: int = estamina_base
    estamina_máxima = 150

    arma: Any = None
    escudo: Any = None

    classe_do_usuário: Any = None

    primeira_habilidade_passiva: Any = None
    segunda_habilidade_passiva: Any = None
    terceira_habilidade_passiva: Any = None

    habilidade_ativa: Any = None
    habilidade_especial: Any = None

    descrição: str = field(default = "", init = False)

    def __post_init__(self):
        self.limite_de_altura()
        self.limite_de_idade()
        self.limite_de_peso()
        self.atributos()
        self.atualizar_descrição()
        
    def limite_de_peso(self) -> None:
        if not (70 <= self.peso <= 110):
            raise ValueError("o peso do  seu personagem deve estar entre 70kg - 110kg")
 
    def limite_de_altura(self) -> None:
        if not (1.5 <= self.altura <= 2.5):
            raise ValueError("a altura do seu personagem deve estar entre 1.5m - 2.5m")
        
    def limite_de_idade(self) -> None:
        if not (16 <= self.idade <= 25):
            raise ValueError("a idade do seu personagem deve estar entre 16 anos - 25 anos")

    def multiplicador_de_experiência(self) -> None:

        multiplicador = 1
        if 0 < self.nível_atual <= 25:
            multiplicador = 1.25
        if 25 < self.nível_atual <= 50:
            multiplicador = 1.5
        if 50 < self.nível_atual <= 75:
            multiplicador = 1.75
        if 75 < self.nível_atual <= 100:
            multiplicador = 2.0

        self.experiência_máxima = int(self.experiência_máxima * multiplicador)

    def atributos(self) -> None:
        self.nível_atual += 1
        self.dano_base *= self.nível_atual
        self.velocidade_base *= self.nível_atual
        self.defesa_base *= self.nível_atual
        self.vida_máxima *= self.nível_atual
        self.vida_atual = self.vida_máxima
        self.estamina_máxima *= self.nível_atual
        self.estamina_atual = self.estamina_máxima
        self.atualizar_descrição()

    def receber_experiência(self, experiência: int) -> None:
        self.experiência_atual += experiência

        while self.experiência_atual >= self.experiência_máxima and self.nível_atual < self.nível_máximo:  
            if self.experiência_atual > self.estamina_máxima: 
                self.experiência_atual -= self.experiência_máxima
            else:
                self.experiência_atual = 0
            self.atributos()
            self.multiplicador_de_experiência()
    
    def diminuir_tentativas(self) -> None:
        if self.vida_atual <= 0:
            self.tentativas_restantes -= 1
            self.vida_atual = self.vida_máxima
            print("você perdeu uma tentativa!")

        if self.tentativas_restantes == 0:
            raise SystemExit("suas tentativas acabaram, você perdeu o jogo")

    def atacar(self, alvo):
        alvo.vida -= self.dano_final
 
    def equipar_arma(self, arma) -> None:
        self.arma = arma

    def equipar_escudo(self, escudo) -> None:
        self.escudo = escudo

    def atualizar_descrição(self) -> None:
        self.descrição = (f"nome: {self.nome}\n"
                          f"idade: {self.idade}\n"
                          f"peso: {self.peso}Kg\n"
                          f"genero: {self.genero}\n"
                          f"altura: {self.altura}m\n"
                          f"experiência: {self.experiência_atual}/{self.experiência_máxima}\n"
                          f"nível: {self.nível_atual}/{self.nível_máximo}\n"
                          f"dano: {self.dano_final}\n"
                          f"velocidade: {self.velocidade}\n"
                          f"defesa: {self.defesa}\n"
                          f"vida: {self.vida_atual}/{self.vida_máxima}\n"
                          f"estamina: {self.estamina_atual}/{self.estamina_máxima}\n"
                          f"arma: {self.arma}\n"
                          f"escudo: {self.escudo}\n"
                          f"tentativas: {self.tentativas_restantes}\n"
                          f"classe: {self.classe_do_usuário}\n")