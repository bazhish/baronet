from dataclasses import dataclass, field
from random import uniform, randint
from typing import Callable, Optional, Any, Union

@dataclass
class HabilidadeAtiva:
    nome: str
    efeito: Callable[[Any, Optional[Any]], None]

    tempo_de_recarga: int
    nivel_minimo: int
    duração: int
    def __post_init__(self):
        self.tempo_de_recarga_restante = 0
        self.duração_restante = 0
        self.uso = None

    def verificar_nivel(self, usuario):
        self.uso = usuario.nível_atual >= self.nivel_minimo

    def aplicar_habilidade(self, usuario, alvo):
        if self.uso == True and self.tempo_de_recarga_restante == 0:
            self.efeito(usuario, alvo)
            self.duração_restante = self.duração
            self.tempo_de_recarga_restante = self.tempo_de_recarga

    def atualizar_atualizar_tempo(self):
        while self.duração_restante > 0:
            self.duração_restante -= 1
        while self.tempo_de_recarga_restante > 0:
            self.tempo_de_recarga_restante -= 1

#  ASSASSINO
def efeito_golpe_mortal(usuario, alvo):
    if alvo:
        alvo.vida -= max(0, ((usuario.dano_final) * 3) - (alvo.defesa_final* uniform(0.6, 0.8)))

def efeito_intangibilidade(usuario):
    usuario.estado = "intangivel"

# ESPADACHIN
def efeito_impacto_cruzado(usuario, alvo):
    if alvo:
        alvo.vida -= max(0, ((usuario.dano_final) * 2) - (alvo.defesa_final * 0.5))

def efeito_bloqueio_de_espada(alvo):
    if alvo:
        alvo.dano_final *= 0.3

# ESCUDEIRO
def efeito_ataque_com_escudo(usuario, alvo):
    if alvo:
        alvo.vida -= max(0, ((usuario.defesa_final) * 2) - (alvo.defesa_final * 0.75))

def efeito_defesa_reforcada(usuario):
    usuario.defesa_bonus += int(usuario.defesa_base * 1.1)

# LANCEIRO
def efeito_giro_de_lanca(usuario, alvos):
    for inimigo in alvos:
        dano = max(0, (usuario.dano_final * 4) - (inimigo.defesa_final * uniform(0.5, 0.75)))
        inimigo.vida -= dano

def efeito_arremesso_de_lanca(usuario, alvo):
    if alvo:
        alvo.vida -= max(0, ((usuario.dano_final) * randint(2, 3)) - (alvo.defesa_final * 0.9))

# ARQUEIRO
def efeito_disparo_perfurante(usuario, alvo):
    if alvo:
        alvo["vida"] *= 0.1

def efeito_camuflagem(usuario, alvo):
    if alvo:
        alvo["dano"] = 0

# BATEDOR
def efeito_ataque_surpresa(usuario, alvo):
    if alvo:
        alvo.vida -= max(0, ((usuario.dano_final) * 2) - (alvo.defesa_final * 0.1))

def efeito_fuga_rapida(usuario, alvo):
    if alvo:
        usuario.vida -= max(0, (alvo.dano_final * 5) - (usuario.velocidade + usuario.defesa))

golpe_mortal = HabilidadeAtiva("Golpe mortal", efeito_golpe_mortal, 100, 2, 50, 1)
intangibilidade = HabilidadeAtiva("Intangibilidade", efeito_intangibilidade, 70, 1, 80, 1)
impacto_cruzado = HabilidadeAtiva("Impacto cruzado", efeito_impacto_cruzado, 90, 2, 50, 1)
bloqueio_de_espada = HabilidadeAtiva("Bloqueio de espada", efeito_bloqueio_de_espada, 85, 1, 80, 1)
ataque_com_escudo = HabilidadeAtiva("Ataque com escudo", efeito_ataque_com_escudo, 100, 1, 50, 1)
defesa_reforcada = HabilidadeAtiva("Defesa reforçada", efeito_defesa_reforcada, 75, 2, 80, 1)
giro_de_lanca = HabilidadeAtiva("Giro de lança", efeito_giro_de_lanca, 250, 2, 50, 1)
arremesso_de_lanca = HabilidadeAtiva("Arremesso de lança", efeito_arremesso_de_lanca, 30, 1, 80, 1)
disparo_perfurante = HabilidadeAtiva("Disparo perfurante", efeito_disparo_perfurante, 200, 2, 50, 1)
camuflagem = HabilidadeAtiva("Camuflagem", efeito_camuflagem, 70, 1, 80, 1)
ataque_surpresa = HabilidadeAtiva("Ataque surpresa", efeito_ataque_surpresa, 160, 2, 50, 1)
fuga_rapida = HabilidadeAtiva("Fuga rápida", efeito_fuga_rapida, 90, 1, 80, 1)
