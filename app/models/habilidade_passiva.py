from dataclasses import dataclass, field
from typing import Callable, Optional

@dataclass
class HabilidadePassiva:
    nome: str
    efeito: Callable[[dict], None]
    nivel_minimo: int
    aplicar: Optional[bool] = field(default=None, init=False)

    def verificar_nivel(self, usuario: dict):
        self.aplicar = usuario.get("nível", 0) >= self.nivel_minimo

    def aplicar_habilidade(self, usuario: dict):
        if self.aplicar:
            self.efeito(usuario)


# --- ASSASSINO ---

def efeito_furtividade(usuario):
    usuario["dano"] *= 1.25
    usuario["velocidade"] *= 1.25
    usuario["defesa"] *= 0.75
    usuario["estamina"] *= 0.75
    usuario["vida"] *= 1.25

def efeito_evasao(usuario):
    usuario["velocidade"] *= 1.5
    usuario["defesa"] *= 1.5
    usuario["estamina"] *= 1.5
    usuario["vida"] *= 1.5

def efeito_sangramento(usuario):
    usuario["dano"] *= 2
    usuario["vida"] *= 0.8

# --- ESPADACHIN ---

def efeito_vontade_da_espada(usuario):
    for stat in ["dano", "velocidade", "defesa", "estamina", "vida"]:
        usuario[stat] *= 1.2
def efeito_heranca_da_espada(usuario):
    for stat in ["dano", "velocidade", "defesa", "estamina", "vida"]:
        usuario[stat] *= 1.45

def efeito_ataque_rapido(usuario):
    usuario["dano"] *= 1.85
    usuario["velocidade"] *= 1.85
    usuario["defesa"] *= 0.7
    usuario["estamina"] *= 0.9

# --- ESCUDEIRO ---

def efeito_bloqueio_de_ataque(usuario):
    usuario["defesa"] *= 2
    usuario["estamina"] *= 1.75
    usuario["vida"] *= 1.1

def efeito_repelir(adversario):
    dano = adversario["dano"] * 0.75
    adversario["defesa"] *= 0.5
    adversario["vida"] -= dano

def efeito_peso_pena(usuario):
    usuario["velocidade"] *= 1.5
    usuario["estamina"] *= 1.5
    usuario["vida"] *= 1.5

# --- LANCEIRO ---

def efeito_danca_da_lanca(usuario):
    usuario["estamina"] *= 1.3
    usuario["velocidade"] *= 1.3

def efeito_controle_passivo(usuario):
    usuario["estamina"] *= 1.2
    usuario["defesa"] *= 1.5
    usuario["velocidade"] *= 1.2
    usuario["dano"] *= 1.5
    usuario["vida"] *= 1.5

def efeito_controle_total(usuario):
    for stat in ["estamina", "defesa", "velocidade", "dano", "vida"]:
        usuario[stat] *= 1.35

# --- ARQUEIRO ---

def efeito_disparo_preciso(usuario):
    usuario["dano"] *= 1.25
    usuario["velocidade"] *= 0.75
    usuario["defesa"] *= 0.75

def efeito_passos_silenciosos(usuario):
    usuario["velocidade"] *= 1.4
    usuario["estamina"] *= 1.4
    usuario["vida"] *= 1.4
    usuario["defesa"] *= 0.6

def efeito_flecha_dupla(usuario):
    usuario["dano"] *= 1.75
    usuario["velocidade"] *= 0.8
    usuario["defesa"] *= 0.8

# --- BATEDOR ---

def efeito_ataque_silencioso(usuario):
    usuario["velocidade"] *= 1.8
    usuario["defesa"] *= 0.85
    usuario["dano"] *= 1.3

def efeito_evasao_rapida(usuario):
    usuario["velocidade"] *= 1.5
    usuario["defesa"] *= 1.2
    usuario["estamina"] *= 0.7
    usuario["vida"] *= 1.5

def efeito_exploracao_furtiva(usuario):
    usuario["velocidade"] *= 1.3
    usuario["dano"] *= 1.2
    usuario["defesa"] *= 1.1
    usuario["estamina"] *= 0.9
    usuario["vida"] *= 1.3

furtividade = HabilidadePassiva("furtividade", efeito_furtividade, 12)
evasao = HabilidadePassiva("evasão", efeito_evasao, 45)
sangramento = HabilidadePassiva("sangramento", efeito_sangramento, 70)
vontade_da_espada = HabilidadePassiva("vontade da espada", efeito_vontade_da_espada, 12)
heranca_da_espada = HabilidadePassiva("herança da espada", efeito_heranca_da_espada, 45)
ataque_rapido = HabilidadePassiva("ataque rápido", efeito_ataque_rapido, 70)
bloqueio_de_ataque = HabilidadePassiva("bloqueio de ataque", efeito_bloqueio_de_ataque, 12)
repelir = HabilidadePassiva("repelir", efeito_repelir, 45)
peso_pena = HabilidadePassiva("peso pena", efeito_peso_pena, 70)
danca_da_lanca = HabilidadePassiva("dança da lança", efeito_danca_da_lanca, 12)
controle_passivo = HabilidadePassiva("controle passivo", efeito_controle_passivo, 45)
controle_total = HabilidadePassiva("controle total", efeito_controle_total, 70)
disparo_preciso = HabilidadePassiva("disparo preciso", efeito_disparo_preciso, 12)
passos_silenciosos = HabilidadePassiva("passos silenciosos", efeito_passos_silenciosos, 45)
flecha_dupla = HabilidadePassiva("flecha dupla", efeito_flecha_dupla, 70)
ataque_silencioso = HabilidadePassiva("ataque silencioso", efeito_ataque_silencioso, 12)
evasao_rapida = HabilidadePassiva("evasão rápida", efeito_evasao_rapida, 45)
exploracao_furtiva = HabilidadePassiva("exploração furtiva", efeito_exploracao_furtiva, 70)