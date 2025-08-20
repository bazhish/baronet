# backend\sistemas\modelos\habilidades_passiva_combatentes.py
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

# ASSASSINO
def efeito_furtividade(usuario):
    usuario.dano_bonus += usuario.dano_base * 0.25
    usuario.velocidade_bonus += usuario.velocidade_base * 0.25
    usuario.defesa_bonus += usuario.defesa_base * 0.75
    usuario.estamina_bonus += usuario.estamina_base * 0.75
    usuario.vida_bonus += usuario.vida_base * 0.25

def efeito_evasao(usuario):
    usuario.velocidade_bonus += usuario.velocidade_base * 0.5
    usuario.defesa_bonus += usuario.defesa_base * 0.5
    usuario.estamina_bonus += usuario.estamina_base * 0.5
    usuario.vida_bonus += usuario.vida_base * 0.5

def efeito_sangramento(usuario):
    usuario.dano_bonus += usuario.dano_base * 2
    usuario.vida_bonus += usuario.vida_base * 0.8

# ESPADACHIN
def efeito_vontade_da_espada(usuario):
    for status in ["dano_base", "velocidade_base", "defesa_base", "estamina_base", "vida_base"]:
        valor = getattr(usuario, status)
    setattr(usuario, status, valor * 0.2)


def efeito_heranca_da_espada(usuario):
    for status in ["dano_base", "velocidade_base", "defesa_base", "estamina_base", "vida_base"]:
        valor = getattr(usuario, status)
        setattr(usuario, status, valor * 0.6)

def efeito_ataque_rapido(usuario):
    usuario.dano_bonus += usuario.dano_base * 0.85
    usuario.velocidade_bonus += usuario.velocidade_base * 0.85
    usuario.defesa_bonus += usuario.defesa_base * 0.7
    usuario.estamina_bonus += usuario.estamina_base * 0.9

# LANCEIRO
def efeito_danca_da_lanca(usuario):
    usuario.estamina_bonus += usuario.estamina_base * 0.3
    usuario.velocidade_bonus += usuario.velocidade_base * 0.3

def efeito_controle_passivo(usuario):
    usuario.estamina_bonus += usuario.estamina_base * 0.2
    usuario.defesa_bonus += usuario.defesa_base * 0.5
    usuario.velocidade_bonus += usuario.velocidade_base * 0.2
    usuario.dano_bonus += usuario.dano_base * 0.5
    usuario.vida_bonus += usuario.vida_base * 0.5

def efeito_controle_total(usuario):
    for status in ["dano", "velocidade", "defesa", "estamina", "vida"]:
        valor = getattr(usuario, status)
        setattr(usuario, status, valor * 0.35)

#  ARQUEIRO
def efeito_disparo_preciso(usuario):
    usuario.dano_bonus += usuario.dano_base * 0.25
    usuario.velocidade_bonus += usuario.velocidade_base * 0.75
    usuario.defesa_bonus += usuario.defesa_base * 0.75

def efeito_passos_silenciosos(usuario):
    usuario.velocidade_bonus += usuario.velocidade_base * 0.4
    usuario.estamina_bonus += usuario.estamina_base * 0.4
    usuario.vida_bonus += usuario.vida_base *01.4
    usuario.defesa_bonus += usuario.defesa_base * 0.6

def efeito_flecha_dupla(usuario):
    usuario.dano_bonus += usuario.dano_base * 0.75
    usuario.velocidade_bonus += usuario.velocidade_base * 0.8
    usuario.defesa_bonus += usuario.defesa_base * 0.8

# BATEDOR
def efeito_ataque_silencioso(usuario):
    usuario.velocidade_bonus += usuario.velocidade_base * 0.8
    usuario.defesa_bonus += usuario.defesa_base * 0.85
    usuario.dano_bonus += usuario.dano_base * 0.3

def efeito_evasao_rapida(usuario):
    usuario.velocidade_bonus += usuario.velocidade_base * 0.5
    usuario.defesa_bonus += usuario.defesa_base * 1.2
    usuario.estamina_bonus += usuario.estamina_base * 0.7
    usuario.vida_bonus += usuario.vida_base * 0.5

def efeito_exploracao_furtiva(usuario):
    usuario.velocidade_bonus += usuario.velocidade_base * 0.3
    usuario.dano_bonus += usuario.dano_base * 0.2
    usuario.defesa_bonus += usuario.defesa_base *01.1
    usuario.estamina_bonus += usuario.estamina_base * 0.9
    usuario.vida_bonus += usuario.vida_base * 0.3

# ARTILHEIRO
def efeito_mira_aprimorada(usuario):
    usuario.dano_bonus += usuario.dano_base * 0.6
    usuario.velocidade_bonus += usuario.velocidade_base * 0.1
    usuario.estamina_bonus += usuario.estamina_base * 0.9

def efeito_arsenal_tatico(usuario):
    usuario.dano_bonus += usuario.dano_base * 0.3
    usuario.defesa_bonus += usuario.defesa_base * 0.3
    usuario.vida_bonus += usuario.vida_base * 0.2

def efeito_fogo_sucessivo(usuario):
    usuario.velocidade_bonus += usuario.velocidade_base * 0.5
    usuario.dano_bonus += usuario.dano_base * 0.4
    usuario.estamina_bonus += usuario.estamina_base * 0.8
    usuario.defesa_bonus += usuario.defesa_base * 0.85

# ARTISTA MARCIAL
def efeito_foco_interno(usuario):
    usuario.estamina_bonus += usuario.estamina_base * 0.6
    usuario.velocidade_bonus += usuario.velocidade_base * 0.2
    usuario.dano_bonus += usuario.dano_base * 0.1

def efeito_tecnica_perfeita(usuario):
    usuario.dano_bonus += usuario.dano_base * 0.4
    usuario.defesa_bonus += usuario.defesa_base * 0.4
    usuario.estamina_bonus += usuario.estamina_base * 0.1

def efeito_golpe_fatal(usuario):
    usuario.dano_bonus += usuario.dano_base * 0.0
    usuario.vida_bonus += usuario.vida_base * 0.75
    usuario.defesa_bonus += usuario.defesa_base * 0.85

foco_interno = HabilidadePassiva("foco interno", efeito_foco_interno, 12)
tecnica_perfeita = HabilidadePassiva("técnica perfeita", efeito_tecnica_perfeita, 45)
golpe_fatal = HabilidadePassiva("golpe fatal", efeito_golpe_fatal, 70)
furtividade = HabilidadePassiva("furtividade", efeito_furtividade, 12)
evasao = HabilidadePassiva("evasão", efeito_evasao, 45)
sangramento = HabilidadePassiva("sangramento", efeito_sangramento, 70)
vontade_da_espada = HabilidadePassiva("vontade da espada", efeito_vontade_da_espada, 12)
heranca_da_espada = HabilidadePassiva("herança da espada", efeito_heranca_da_espada, 45)
ataque_rapido = HabilidadePassiva("ataque rápido", efeito_ataque_rapido, 70)
danca_da_lanca = HabilidadePassiva("dança da lança", efeito_danca_da_lanca, 12)
controle_passivo = HabilidadePassiva("controle passivo", efeito_controle_passivo, 45)
controle_total = HabilidadePassiva("controle total", efeito_controle_total, 70)
disparo_preciso = HabilidadePassiva("disparo preciso", efeito_disparo_preciso, 12)
passos_silenciosos = HabilidadePassiva("passos silenciosos", efeito_passos_silenciosos, 45)
flecha_dupla = HabilidadePassiva("flecha dupla", efeito_flecha_dupla, 70)
ataque_silencioso = HabilidadePassiva("ataque silencioso", efeito_ataque_silencioso, 12)
evasao_rapida = HabilidadePassiva("evasão rápida", efeito_evasao_rapida, 45)
mira_aprimorada = HabilidadePassiva("mira aprimorada", efeito_mira_aprimorada, 12)
arsenal_tatico = HabilidadePassiva("arsenal tático", efeito_arsenal_tatico, 45)
fogo_sucessivo = HabilidadePassiva("fogo sucessivo", efeito_fogo_sucessivo, 70)
exploracao_furtiva = HabilidadePassiva("exploração furtiva", efeito_exploracao_furtiva, 70)