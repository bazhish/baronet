from dataclasses import dataclass, field
from random import uniform, randint
from typing import Callable, Optional

@dataclass
class HabilidadeAtiva:
    nome: str
    efeito: Callable  
    custo: int
    tempo_de_recarga: int
    nivel_minimo: int
    duracao: int
    tempo_de_recarga_restante: int = field(default=0, init=False)
    duracao_restante: int = field(default=0, init=False)
    uso: Optional[bool] = field(default=None, init=False)

    def verificar_nivel(self, usuario: dict):
        self.uso = usuario.get("nível", 0) >= self.nivel_minimo

    def aplicar_habilidade(self, usuario: dict, alvo: Optional[dict] = None):
        if self.uso and usuario.get("estamina", 0) >= self.custo and self.tempo_de_recarga_restante == 0:
            usuario["estamina"] -= self.custo
            self.efeito(usuario, alvo)
            self.duracao_restante = self.duracao
            self.tempo_de_recarga_restante = self.tempo_de_recarga

    def atualizar_turno(self):
        if self.duracao_restante > 0:
            self.duracao_restante -= 1
        if self.tempo_de_recarga_restante > 0:
            self.tempo_de_recarga_restante -= 1

def efeito_golpe_mortal(usuario, alvo):
    if alvo:
        dano_base = usuario["dano"]
        reducao_defesa = alvo["defesa"] * uniform(0.6, 0.8)
        dano_final = max(0, (dano_base * 3) - reducao_defesa)
        alvo["vida"] -= dano_final

def efeito_intangibilidade(usuario, alvo):
    if alvo:
        alvo["dano"] = 0

def efeito_impacto_cruzado(usuario, alvo):
    if alvo:
        dano_base = usuario["dano"]
        reducao_defesa = alvo["defesa"] * 0.5
        dano_final = max(0, (dano_base * 2) - reducao_defesa)
        alvo["vida"] -= dano_final

def efeito_bloqueio_de_espada(usuario, alvo):
    if alvo:
        alvo["dano"] *= 0.3

def efeito_ataque_com_escudo(usuario, alvo):
    if alvo:
        dano_base = usuario["defesa"]
        reducao_defesa = alvo["defesa"] * 0.75
        dano_final = max(0, (dano_base * 2) - reducao_defesa)
        alvo["vida"] -= dano_final

def efeito_defesa_reforcada(usuario, alvo):
    if alvo:
        alvo["dano"] *= 0.1

def efeito_giro_de_lanca(usuario, alvo):
    if alvo:
        dano_base = usuario["dano"]
        reducao_defesa = alvo["defesa"] * uniform(0.5, 0.75)
        dano_final = max(0, (dano_base * 4) - reducao_defesa)
        alvo["vida"] -= dano_final

def efeito_arremesso_de_lanca(usuario, alvo):
    if alvo:
        dano_base = usuario["dano"]
        reducao_defesa = alvo["defesa"] * 0.9
        dano_final = max(0, (dano_base * randint(2, 3)) - reducao_defesa)
        alvo["vida"] -= dano_final

def efeito_disparo_perfurante(usuario, alvo):
    if alvo:
        alvo["vida"] *= 0.1

def efeito_camuflagem(usuario, alvo):
    if alvo:
        alvo["dano"] = 0

def efeito_ataque_surpresa(usuario, alvo):
    if alvo:
        dano_base = usuario["dano"]
        reducao_defesa = alvo["defesa"] * 0.1
        dano_final = max(0, (dano_base * 2) - reducao_defesa)
        alvo["vida"] -= dano_final

def efeito_fuga_rapida(usuario, alvo):
    if alvo:
        dano_base = alvo["dano"]
        aumento_defesa = usuario["velocidade"] + usuario["defesa"]
        dano_final = max(0, (dano_base * 5) - aumento_defesa)
        usuario["vida"] -= dano_final

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
