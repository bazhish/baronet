from dataclasses import dataclass, field
import sys, os
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = current_dir
while not os.path.isdir(os.path.join(project_root, ".git")) and os.path.dirname(project_root) != project_root:
    project_root = os.path.dirname(project_root)
sys.path.append(project_root)

from backend.system.habilidades_ativa_combatentes import (
    death_blow, intangibility, cross_impact, sword_block, shield_attack, reinforced_defense,
    spear_swing, spear_throwing, armor_piercing_shot, camouflage, surprise_attack,
    quick_escape, ghost_step, sand, lightning_combo, iron_posture
)
from backend.system.habilidades_passiva_combatentes import (
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
    estamina_base: int
    multiplicador_de_experiência: float
    arma: None = field(default = "nenhuma", init = False)
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
            f"arma inicial: {self.arma}\n"
            f"multiplicador de experiência: {self.multiplicador_de_experiência}\n"
            f"primeira habilidade passiva: {self.primeira_habilidade_passiva}\n"
            f"segunda habilidade passiva: {self.segunda_habilidade_passiva}\n"
            f"terceira habilidade passiva: {self.terceira_habilidade_passiva}\n"
            f"habilidade ativa: {self.habilidade_ativa}\n"
            f"habilidade especial: {self.habilidade_especial}\n"
        )

class Assassino(Classe):
    def __init__(self):
        super().__init__("Assassino", 100, 5, 2, 10, 130 , 1.5,
            furtividade, evasao, sangramento, death_blow, intangibility)
        self.atualizar_descrição()

class Espadachim(Classe):
    def __init__(self):
        super().__init__(
            "Espadachim", 120, 4, 3, 12, 150 , 1.2,
            vontade_da_espada, heranca_da_espada,
            ataque_rapido, cross_impact, sword_block)
        self.atualizar_descrição()

class Escudeiro(Classe):
    def __init__(self):
        super().__init__(
            "Escudeiro", 80, 3, 5, 15, 100 , 1.0,
            bloqueio_de_ataque, repelir,
            peso_pena, shield_attack, reinforced_defense)
        self.atualizar_descrição()


class Lanceiro(Classe):
    def __init__(self):
        super().__init__(
            "Lanceiro", 11, 4, 4, 13, 110 , 1.3,
            danca_da_lanca, controle_passivo,
            controle_total,  spear_swing, spear_throwing)
        self.atualizar_descrição()

class Arqueiro(Classe):
    def __init__(self):
        super().__init__(
            "Arqueiro", 90, 6, 2, 11, 110 , 1.4,
            disparo_preciso, passos_silenciosos,
            flecha_dupla, armor_piercing_shot, camouflage)
        self.atualizar_descrição()

class Batedor(Classe):
    def __init__(self):
        super().__init__(
            "Batedor", 70, 5, 3, 14, 120 , 1.1,
            ataque_silencioso, evasao_rapida,
            exploracao_furtiva, surprise_attack,
    quick_escape)
        self.atualizar_descrição()

class Artilheiro(Classe):
    def __init__(self):
        super().__init__(
            "Artilheiro", 150, 3, 2, 90 , 20,
            foco_interno, tecnica_perfeita, golpe_fatal, ghost_step, sand)
        self


class ArtistaMarcial(Classe):
    def __init__(self):
        super().__init__(
            "Artista Marcial", 100, 6, 4, 18, 90 , 1.5,
            mira_aprimorada, arsenal_tatico, fogo_sucessivo,
            lightning_combo, iron_posture)
        self.atualizar_descrição()

assassino = Assassino()
espadachim = Espadachim()
escudeiro = Escudeiro()
lanceiro = Lanceiro()
arqueiro = Arqueiro()
batedor = Batedor()
artilheiro = Artilheiro()
artista_marcial = ArtistaMarcial()
print(artilheiro.descrição)
print()
print(artista_marcial.descrição)