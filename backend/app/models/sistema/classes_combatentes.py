from dataclasses import dataclass, field
from backend.app.models.sistema.habilidades_ativa_combatentes import (
    golpe_mortal, intangibilidade, impacto_cruzado, bloqueio_de_espada,
    ataque_com_escudo, defesa_reforcada, giro_de_lanca, arremesso_de_lanca,
    disparo_perfurante, camuflagem, ataque_surpresa, fuga_rapida
)
from backend.app.models.sistema.habilidades_passivas_combatentes import (
    furtividade, evasao, sangramento, vontade_da_espada, heranca_da_espada,
    ataque_rapido, bloqueio_de_ataque, repelir, peso_pena, danca_da_lanca,
    controle_passivo, controle_total, disparo_preciso, passos_silenciosos,
    flecha_dupla, ataque_silencioso, evasao_rapida, exploracao_furtiva, 
    foco_interno, tecnica_perfeita, golpe_fatal, mira_aprimorada,
    arsenal_tatico, fogo_sucessivo
)

@dataclass
class Classe:
    nome: str
    dano_base: int
    velocidade_base: int
    defesa_base: int
    vida_base: int
    multiplicador_de_experiência: float
    arma_inicial: None = field(default = "nenhuma", init = False)
    primeira_habilidade_passiva: None = field(default = "nenhuma")
    segunda_habilidade_passiva: None = field(default = "nenhuma")
    terceira_habilidade_passiva: None = field(default = "nenhuma")
    habilidade_ativa: None = field(default = "nenhuma")
    habilidade_especial: None = field(default = "nenhuma")
    descrição: str = field(default = "", init = False)

    def atualizar_descrição(self):
        self.descrição = (
            f"classe: {self.nome}\n"
            f"dano base: {self.dano_base}\n"
            f"velocidade base: {self.velocidade_base}\n"
            f"defesa base: {self.defesa_base}\n"
            f"vida máxima base: {self.vida_base}\n"
            f"arma inicial: {self.arma_inicial}\n"
            f"multiplicador de experiência: {self.multiplicador_de_experiência}\n"
            f"primeira habilidade passiva: {self.primeira_habilidade_passiva}\n"
            f"segunda habilidade passiva: {self.segunda_habilidade_passiva}\n"
            f"terceira habilidade passiva: {self.terceira_habilidade_passiva}\n"
            f"habilidade ativa: {self.habilidade_ativa}\n"
            f"habilidade especial: {self.habilidade_especial}\n"
        )

class Assassino(Classe):
    def __init__(self, usuario):
        super().__init__("Assassino", 10, 5, 2, 10, 1.5,
            furtividade, evasao, sangramento, golpe_mortal,
            intangibilidade)
        self.atualizar_descrição()

class Espadachim(Classe):
    def __init__(self, usuario):
        super().__init__(
            "Espadachim", 12, 4, 3, 12, 1.2,
            vontade_da_espada, heranca_da_espada,
            ataque_rapido, impacto_cruzado, bloqueio_de_espada)
        self.atualizar_descrição()

class Escudeiro(Classe):
    def __init__(self, usuario):
        super().__init__(
            "Escudeiro", 8, 3, 5, 15, 1.0,
            bloqueio_de_ataque, repelir,
            peso_pena, ataque_com_escudo,
            defesa_reforcada)
        self.atualizar_descrição()


class Lanceiro(Classe):
    def __init__(self, usuario):
        super().__init__(
            "Lanceiro", 11, 4, 4, 13, 1.3,
            danca_da_lanca, controle_passivo,
            controle_total, giro_de_lanca,
            arremesso_de_lanca)
        self.atualizar_descrição()

class Arqueiro(Classe):
    def __init__(self, usuario):
        super().__init__(
            "Arqueiro", 9, 6, 2, 11, 1.4,
            disparo_preciso, passos_silenciosos,
            flecha_dupla, disparo_perfurante,
            camuflagem)
        self.atualizar_descrição()

class Batedor(Classe):
    def __init__(self, usuario):
        super().__init__(
            "Batedor", 7, 5, 3, 14, 1.1,
            ataque_silencioso, evasao_rapida,
            exploracao_furtiva, ataque_surpresa,
            fuga_rapida)
        self.atualizar_descrição()

class Artilheiro(Classe):
    def __init__(self, usuario):
        super().__init__(
            "Artilheiro", 15, 3, 2, 20,
            foco_interno, tecnica_perfeita, golpe_fatal, None,
            None)
        self


class ArtistaMarcial(Classe):
    def __init__(self, usuario):
        super().__init__(
            "Artista Marcial", 10, 6, 4, 18, 1.5,
            mira_aprimorada, arsenal_tatico, fogo_sucessivo,
            None, None)
        self.atualizar_descrição()

assassino = Assassino()
espadachim = Espadachim()
escudeiro = Escudeiro()
lanceiro = Lanceiro()
arqueiro = Arqueiro()
batedor = Batedor()
artilheiro = Artilheiro()
artista_marcial = ArtistaMarcial()
