from dataclasses import dataclass, field
from typing import Callable, Optional

@dataclass
class HabilidadePassiva:
    nome: str
    efeito: Callable[[dict], None]
    nivel_minimo: int
    aplicar: Optional[bool] = field(default = None, init = False)
    descrição: str = field(default = "", init = False)

    def verificar_nivel(self, usuario):
        self.aplicar = usuario.nível_atual >= self.nivel_minimo

    def aplicar_habilidade(self, usuario):
        if self.aplicar:
            self.efeito(usuario)

    def atualizar_descrição(self):
        self.descrição = (
            f"Habilidade Passiva: {self.nome}\n"
            f"Nível Mínimo: {self.nivel_minimo}\n"
            f"Efeito: {self.efeito}\n"
        )

# ESCUDEIRO
def efeito_bloqueio_de_ataque(usuario):
    usuario.defesa_bonus += usuario.defesa_base * 2
    usuario.estamina_bonus += usuario.estamina_base * 0.75
    usuario.vida_bonus += usuario.vida_base * 0.1

def efeito_repelir(adversario):
    dano = adversario.dano_final * 0.75
    adversario.defesa_final *= 0.5
    adversario.vida_atual -= dano

def efeito_peso_pena(usuario):
    usuario.velocidade_bonus += usuario.velocidade_base * 0.5
    usuario.estamina_bonus += usuario.estamina_base * 0.5
    usuario.vida_bonus += usuario.vida_base * 0.5

# CURANDEIRO
def benção_da_lua(usuario):
    usuario.vida_bonus

def efeito_remover_debuff(usuario):
    usuario.debuffs.clear()

def efeito_remendo(adversario):
    adversario.dano_final *= 0.5

# Bardo
def efeito_buff_grupo(usuario):
    for aliado in usuario.grupo:
        aliado.ataque_bonus += aliado.ataque_base * 0.1
        aliado.defesa_bonus += aliado.defesa_base * 0.1

def efeito_debuff_inimigo(adversario):
    adversario.defesa_final -= adversario.defesa_base * 0.1

# Ilusionista
def efeito_clones(adversario):
    adversario.defesa -= 0.5 

def efeito_espelho(usuario):
    usuario.defesa_bonus += usuario.defesa_base * 0.3  

def efeito_engano(adversario):
    adversario.ataque_final *= 0.8 

# ESCUDEIRO
bloqueio_de_ataque = HabilidadePassiva("bloqueio de ataque", efeito_bloqueio_de_ataque, 12)
repelir = HabilidadePassiva("repelir", efeito_repelir, 45)
peso_pena = HabilidadePassiva("peso pena", efeito_peso_pena, 70)
# CURANDEIRO
cura = HabilidadePassiva("cura", efeito_cura, 5)
remover_debuff = HabilidadePassiva("remover debuff", efeito_remover_debuff, 25)
remendo = HabilidadePassiva("Remendo",efeito_remendo,50)
# ILUSIONISTA
clones = HabilidadePassiva("clones", efeito_clones, 18)
espelho = HabilidadePassiva("espelho", efeito_espelho, 30)
engano = HabilidadePassiva("engano", efeito_engano, 40)
# BARDO
buff_grupo = HabilidadePassiva("buff grupo", efeito_buff_grupo, 15)
debuff_inimigo = HabilidadePassiva("debuff inimigo", efeito_debuff_inimigo, 25)
