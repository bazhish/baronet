# backend\sistemas\classes\habilidades_passiva_de_suporte.py
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
def efeito_benção_da_lua(usuario):
    usuario.vida_bonus += usuario.vida_base * 0.5
    usuario.defesa_bonus += usuario.defesa_base * 0.3
    usuario.velocidade_bonus += usuario.velocidade_base * 0.2

def efeito_benção_do_sol(usuario):
    usuario.vida_base += 5
    usuario.estamina_base += 5
    usuario.defesa_base += 5
    usuario.velocidade_base += 5
    usuario.dano_base += 5

def efeito_eclipse(time):
    for personagen in time:
        personagen.vida_base *= 1.5
        personagen.estamina_base *= 1.5
        personagen.defesa_base *= 1.5
        personagen.velocidade_base *= 1.5
        personagen.dano_base *= 1.5

# BARDO
def efeito_canção_de_suporte(time):
    for personagen in time:
        personagen.vida_base *= 1.25
        personagen.estamina_base *= 1.25
        personagen.defesa_base *= 1.25
        personagen.velocidade_base *= 1.25
        personagen.dano_base *= 1.25

def efeito_canção_da_ferida(adversarios):
    for adversario in adversarios:
        adversario.defesa_final = adversario.defesa_base * 0.7

def efeito_canção_ardente(usuario, time):
    usuario.dano_final = 0
    usuario.vida_máxima *= 2

    for personagen in time:
        personagen.vida_base += usuario.vida_atual * 0.5
        personagen.estamina_base += usuario.vida_atual * 0.5
        personagen.defesa_base += usuario.vida_atual * 0.5
        personagen.velocidade_base += usuario.vida_atual * 0.5
        personagen.dano_base += usuario.vida_atual * 0.5

# ILUSIONISTA
def efeito_velocista(usuario):
    usuario.velocidade_bonus *= 2

def efeito_guardador(usuario):
    usuario.defesa_bonus *= 2

def efeito_engano(adversario):
    adversario.vida_máxima *= 2

# ESCUDEIRO
bloqueio_de_ataque = HabilidadePassiva("bloqueio de ataque", efeito_bloqueio_de_ataque, 12)
repelir = HabilidadePassiva("repelir", efeito_repelir, 45)
peso_pena = HabilidadePassiva("peso pena", efeito_peso_pena, 70)
# CURANDEIRO
beção_da_lua = HabilidadePassiva("benção da lua", efeito_benção_da_lua, 12)
benção_do_sol = HabilidadePassiva("benção do sol", efeito_benção_do_sol, 45)
eclipse = HabilidadePassiva("eclipse",efeito_eclipse,70)
# ILUSIONISTA
velocista = HabilidadePassiva("velocista", efeito_velocista, 12)
guardador = HabilidadePassiva("guardador", efeito_guardador, 45)
engano = HabilidadePassiva("engano", efeito_engano, 70)
# BARDO
canção_de_suporte = HabilidadePassiva("canção de suporte", efeito_canção_de_suporte, 12)
canção_da_ferida = HabilidadePassiva("canção da ferida", efeito_canção_da_ferida, 45)
canção_ardente = HabilidadePassiva("canção ardente", efeito_canção_ardente, 70)