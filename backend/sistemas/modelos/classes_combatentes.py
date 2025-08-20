from dataclasses import dataclass, field
import sys, os
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = current_dir
while not os.path.isdir(os.path.join(project_root, ".git")) and os.path.dirname(project_root) != project_root:
    project_root = os.path.dirname(project_root)
sys.path.append(project_root)

from backend.sistemas.modelos.habilidades_ativa_combatentes import (
    golpe_mortal, intangibilidade, impacto_cruzado, bloqueio_de_espada,
    giro_de_lanca, arremesso_de_lanca,
    disparo_perfurante, camuflagem, ataque_surpresa, fuga_rapida,
    passo_fantasma, areia, combo_relampago, postura_de_ferro 
)
from backend.sistemas.modelos.habilidades_passiva_combatentes import (
    furtividade, evasao, sangramento, vontade_da_espada, heranca_da_espada,
    ataque_rapido, danca_da_lanca,
    controle_passivo, controle_total, disparo_preciso, passos_silenciosos,
    flecha_dupla, ataque_silencioso, evasao_rapida, exploracao_furtiva, 
    foco_interno, tecnica_perfeita, golpe_fatal, mira_aprimorada,
    arsenal_tatico, fogo_sucessivo
)

@dataclass
class Classe:
    def __init__(self, nome, dano_base, velocidade_base, defesa_base, vida_base,
                estamina_base, multiplicador_de_experiência, arma, primeira_habilidade_passiva,
                segunda_habilidade_passiva, terceira_habilidade_passiva,
                habilidade_ativa, habilidade_especial):
        self.nome = nome
        self.dano_base = dano_base
        self.velocidade_base = velocidade_base
        self.defesa_base = defesa_base
        self.vida_base = vida_base
        self.estamina_base = estamina_base
        self.multiplicador_de_experiência = multiplicador_de_experiência
        self.arma = arma
        self.primeira_habilidade_passiva = primeira_habilidade_passiva
        self.segunda_habilidade_passiva = segunda_habilidade_passiva
        self.terceira_habilidade_passiva = terceira_habilidade_passiva
        self.habilidade_ativa = habilidade_ativa
        self.habilidade_especial = habilidade_especial
        self.descrição = "nenhuma"

    def atualizar_descrição(self):
        self.descrição = (
            f"classe: {self.nome}\n"
            f"dano base: {self.dano_base}\n"
            f"velocidade base: {self.velocidade_base}\n"
            f"defesa base: {self.defesa_base}\n"
            f"vida máxima base: {self.vida_base}\n"
            f"arma inicial: {self.arma}\n"
            f"multiplicador de experiência: {self.multiplicador_de_experiência}\n"
            f"primeira habilidade passiva: {self.primeira_habilidade_passiva.nome}\n"
            f"segunda habilidade passiva: {self.segunda_habilidade_passiva.nome}\n"
            f"terceira habilidade passiva: {self.terceira_habilidade_passiva.nome}\n"
            f"habilidade ativa: {self.habilidade_ativa.nome}\n"
            f"habilidade especial: {self.habilidade_especial.nome}\n"
        )

class Assassino(Classe):
    def __init__(self):
        super().__init__(
            nome = "Assassino",
            dano_base = 3,
            velocidade_base = 5,
            defesa_base = 2,
            vida_base = 100,
            estamina_base = 130,
            multiplicador_de_experiência = 1.5,
            arma = "Adaga",
            primeira_habilidade_passiva = furtividade,
            segunda_habilidade_passiva = evasao,
            terceira_habilidade_passiva = sangramento,
            habilidade_ativa = golpe_mortal,
            habilidade_especial = intangibilidade
        )
        self.atualizar_descrição()

class Espadachim(Classe):
    def __init__(self):
        super().__init__(
            nome = "Espadachim",
            dano_base = 4,
            velocidade_base = 4,
            defesa_base = 3,
            vida_base = 120,
            estamina_base = 150,
            multiplicador_de_experiência = 1.2,
            arma = "Espada Longa",
            primeira_habilidade_passiva = vontade_da_espada,
            segunda_habilidade_passiva = heranca_da_espada,
            terceira_habilidade_passiva = ataque_rapido,
            habilidade_ativa = impacto_cruzado,
            habilidade_especial = bloqueio_de_espada
        )
        self.atualizar_descrição()

class Lanceiro(Classe):
    def __init__(self):
        super().__init__(
            nome = "Lanceiro",
            dano_base = 3,
            velocidade_base = 4,
            defesa_base = 4,
            vida_base = 130,
            estamina_base = 110,
            multiplicador_de_experiência = 1.3,
            arma = "Lança",
            primeira_habilidade_passiva = danca_da_lanca,
            segunda_habilidade_passiva = controle_passivo,
            terceira_habilidade_passiva = controle_total,
            habilidade_ativa = giro_de_lanca,
            habilidade_especial = arremesso_de_lanca
        )
        self.atualizar_descrição()

class Arqueiro(Classe):
    def __init__(self):
        super().__init__(
            nome = "Arqueiro",
            dano_base = 2,
            velocidade_base = 6,
            defesa_base = 2,
            vida_base = 110,
            estamina_base = 110,
            multiplicador_de_experiência = 1.4,
            arma = "Arco",
            primeira_habilidade_passiva = disparo_preciso,
            segunda_habilidade_passiva = passos_silenciosos,
            terceira_habilidade_passiva = flecha_dupla,
            habilidade_ativa = disparo_perfurante,
            habilidade_especial = camuflagem
        )
        self.atualizar_descrição()

class Batedor(Classe):
    def __init__(self):
        super().__init__(
            nome = "Batedor",
            dano_base = 3,
            velocidade_base = 5,
            defesa_base = 3,
            vida_base = 140,
            estamina_base = 120,
            multiplicador_de_experiência = 1.1,
            arma = "Adaga",
            primeira_habilidade_passiva = ataque_silencioso,
            segunda_habilidade_passiva = evasao_rapida,
            terceira_habilidade_passiva = exploracao_furtiva,
            habilidade_ativa = ataque_surpresa,
            habilidade_especial = fuga_rapida
        )
        self.atualizar_descrição()

class Artilheiro(Classe):
    def __init__(self):
        super().__init__(
            nome = "Artilheiro",
            dano_base = 5,
            velocidade_base = 3,
            defesa_base = 2,
            vida_base = 90,
            estamina_base = 130,
            multiplicador_de_experiência = 1.6,
            arma = "Arma de Fogo",
            primeira_habilidade_passiva = foco_interno,
            segunda_habilidade_passiva = tecnica_perfeita,
            terceira_habilidade_passiva = golpe_fatal,
            habilidade_ativa = passo_fantasma,
            habilidade_especial = areia
        )
        self.atualizar_descrição()

class ArtistaMarcial(Classe):
    def __init__(self):
        super().__init__(
            nome = "Artista Marcial",
            dano_base = 4,
            velocidade_base = 6,
            defesa_base = 4,
            vida_base = 180,
            estamina_base = 90,
            multiplicador_de_experiência = 1.5,
            arma = "Punhos",
            primeira_habilidade_passiva = mira_aprimorada,
            segunda_habilidade_passiva = arsenal_tatico,
            terceira_habilidade_passiva = fogo_sucessivo,
            habilidade_ativa = combo_relampago,
            habilidade_especial = postura_de_ferro
        )
        self.atualizar_descrição()

assassino = Assassino()
espadachim = Espadachim()
lanceiro = Lanceiro()
arqueiro = Arqueiro()
batedor = Batedor()
artilheiro = Artilheiro()
artista_marcial = ArtistaMarcial()
