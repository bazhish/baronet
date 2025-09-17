from dataclasses import dataclass, field
import sys, os
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = current_dir
while not os.path.isdir(os.path.join(project_root, ".git")) and os.path.dirname(project_root) != project_root:
    project_root = os.path.dirname(project_root)
sys.path.append(project_root)

labirinto_mental = LabirintoMental()
from backend.sistemas.modelos.habilidades_ativa_de_suporte import (ataque_com_escudo, defesa_reforcada,bençao_vital,milagre_da_vida,melodia_da_fraqueza,sinfonia_estatica,miragem_sombria,)
from backend.sistemas.modelos.habilidades_passiva_de_suporte import (bloqueio_de_ataque, repelir, peso_pena, cura,remover_debuff,remendo,buff_grupo,debuff_inimigo,clones,espelho,engano)

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

class Escudeiro(Classe):
    def __init__(self):
        super().__init__(
            nome = "Escudeiro",
            dano_base = 2,
            velocidade_base = 3,
            defesa_base = 5,
            vida_base = 150,
            estamina_base = 100,
            multiplicador_de_experiência = 1.0,
            arma = "Escudo",
            primeira_habilidade_passiva = bloqueio_de_ataque,
            segunda_habilidade_passiva = repelir,
            terceira_habilidade_passiva = peso_pena,
            habilidade_ativa = ataque_com_escudo,
            habilidade_especial = defesa_reforcada
        )
        self.atualizar_descrição()

escudeiro = Escudeiro()
#Curandeiro
class Curandeiro(Classe):
    def __init__(self):
        super().__init__(
            nome = "Curandeiro",
            dano_base = 1,
            velocidade_base = 3,
            defesa_base = 6,
            vida_base = 130,
            estamina_base = 120,
            multiplicador_de_experiência = 1.0,
            arma = "Cajado",
            primeira_habilidade_passiva = cura,
            segunda_habilidade_passiva =remover_debuff,
            terceira_habilidade_passiva = remendo,
            habilidade_ativa = bençao_vital,
            habilidade_especial = milagre_da_vida
        )
        self.atualizar_descrição()


# Bardo
class Bardo(Classe):
    def __init__(self):
        super().__init__(
            nome = "Bardo",
            dano_base = 2,
            velocidade_base = 4,
            defesa_base = 3,
            vida_base = 120,
            estamina_base = 110,
            multiplicador_de_experiência = 1.0,
            arma = "Lira",
            primeira_habilidade_passiva = buff_grupo,
            segunda_habilidade_passiva = debuff_inimigo,
            terceira_habilidade_passiva = peso_pena,  # Pode ser substituído por outra habilidade passiva
            habilidade_ativa = melodia_da_fraqueza,
            habilidade_especial = sinfonia_estatica
        )
        self.atualizar_descrição()

bardo = Bardo()

# Ilusionista
class Ilusionista(Classe):
    def __init__(self):
        super().__init__(
            nome = "Ilusionista",
            dano_base = 3,
            velocidade_base = 5,
            defesa_base = 2,
            vida_base = 100,
            estamina_base = 90,
            multiplicador_de_experiência = 1.0,
            arma = "Varinha de Ilusões",
            primeira_habilidade_passiva = clones,
            segunda_habilidade_passiva = espelho,
            terceira_habilidade_passiva = engano,
            habilidade_ativa = miragem_sombria,
            habilidade_especial = labirinto_mental  # Pode ser substituído por outra habilidade especial
        )
        self.atualizar_descrição()

ilusionista = Ilusionista()
