from dataclasses import dataclass
from habilidade_ativa import (
    golpe_mortal, intangibilidade, impacto_cruzado, bloqueio_de_espada,
    ataque_com_escudo, defesa_reforcada, giro_de_lanca, arremesso_de_lanca,
    disparo_perfurante, camuflagem, ataque_surpresa, fuga_rapida
)
from habilidade_passiva import (
    furtividade, evasao, sangramento, vontade_da_espada, heranca_da_espada,
    ataque_rapido, bloqueio_de_ataque, repelir, peso_pena, danca_da_lanca,
    controle_passivo, controle_total, disparo_preciso, passos_silenciosos,
    flecha_dupla, ataque_silencioso, evasao_rapida, exploracao_furtiva
)
from armas_iniciais import (
    espada, adaga, lanca, arco, flecha, manopla, escudo
)

@dataclass
class Classe:
    nome: str
    dano: int
    velocidade: int
    defesa: int
    vida_max: int
    arma_inicial: object
    multiplicador_xp: float
    passiva1: object
    passiva2: object
    passiva3: object
    ativa1: object
    ativa2: object

    def dicionario_classe(self):
        dict = {
            "nome": self.nome,
            "dano base": self.dano,
            "velocidade base": self.velocidade,
            "defesa base": self.defesa,
            "vida máxima base": self.vida_max,
            "arma inicial": self.arma_inicial,
            "multiplicador de experiência": self.multiplicador_xp,
            "habilidade passiva 1": self.passiva1,
            "habilidade passiva 2": self.passiva2,
            "habilidade passiva 3": self.passiva3,
            "habilidade ativa 1": self.ativa1,
            "habilidade ativa 2": self.ativa2
        }

        return dict

class Assassino(Classe):
    def __init__(self, usuario: dict):
        super().__init__("Assassino", 10, 5, 2, 10, adaga(usuario), 1.5,
            furtividade, evasao, sangramento, golpe_mortal, intangibilidade
        )
        
    def dicionario_classe(self):
        super().dicionario_classe()

class Espadachim(Classe):
    def __init__(self, usuario: dict):
        super().__init__(
            "Espadachim", 12, 4, 3, 12, espada(usuario), 1.2,
            vontade_da_espada, heranca_da_espada, ataque_rapido, impacto_cruzado, bloqueio_de_espada
        )

    def dicionario_classe(self):
        super().dicionario_classe()

class Escudeiro(Classe):
    def __init__(self, usuario: dict):
        super().__init__(
            "Escudeiro", 8, 3, 5, 15, escudo(usuario), 1.0,
            bloqueio_de_ataque, repelir, peso_pena, ataque_com_escudo, defesa_reforcada
        )

    def dicionario_classe(self):
        super().dicionario_classe()

class Lanceiro(Classe):
    def __init__(self, usuario: dict):
        super().__init__(
            "Lanceiro", 11, 4, 4, 13, lanca(usuario), 1.3,
            danca_da_lanca, controle_passivo, controle_total, giro_de_lanca, arremesso_de_lanca
        )

    def dicionario_classe(self):
        super().dicionario_classe()

class Arqueiro(Classe):
    def __init__(self, usuario: dict):
        super().__init__(
            "Arqueiro", 9, 6, 2, 11, (arco(usuario), flecha()), 1.4,
            disparo_preciso, passos_silenciosos, flecha_dupla, disparo_perfurante, camuflagem
        )

    def dicionario_classe(self):
        super().dicionario_classe()

class Batedor(Classe):
    def __init__(self, usuario: dict):
        super().__init__(
            "Batedor", 7, 5, 3, 14, manopla(usuario), 1.1,
            ataque_silencioso, evasao_rapida, exploracao_furtiva, ataque_surpresa, fuga_rapida
        )

    def dicionario_classe(self):
        super().dicionario_classe()

assassino = Assassino(usuario = {})
espadachim = Espadachim(usuario = {})
escudeiro = Escudeiro(usuario = {})
lanceiro = Lanceiro(usuario = {})
arqueiro = Arqueiro(usuario = {})
batedor = Batedor(usuario = {})