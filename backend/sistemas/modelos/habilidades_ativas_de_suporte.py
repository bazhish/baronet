from dataclasses import dataclass, field
from random import uniform, randint
from typing import Callable, Optional, Any
import math, time, threading

@dataclass
class HabilidadeAtiva:
    nome: str
    efeito: Callable[[Any, Optional[Any]], None]
    tempo_de_recarga: int
    nivel_minimo: int
    duração: int
    descrição_do_efeito: str = field(default = "", init = False)
    descrição: str = field(default = "", init = False)
    def __post_init__(self):
        self.tempo_de_recarga_restante = 0
        self.duração_restante = 0
        self.uso = None

    def atualizar_descrição(self):
        self.descrição = (
            f"nome: {self.nome}\n"
            f"Tempo de recarga: {self.tempo_de_recarga}\n"
            f"Nível mínimo para uso: {self.nivel_minimo}\n"
            f"Duração: {self.duração}\n"
            f"Efeito: {self.efeito}\n"
        )

    def verificar_nivel(self, usuario):
        self.uso = usuario.nível_atual >= self.nivel_minimo

    def aplicar_habilidade(self, usuario, alvo):
        if self.uso == True and self.tempo_de_recarga_restante == 0:
            self.efeito(usuario, alvo)
            self.duração_restante = self.duração
            self.tempo_de_recarga_restante = self.tempo_de_recarga

    def iniciar_cooldown(self):
        self.tempo_de_recarga_restante = self.tempo_de_recarga


# ESCUDEIRO
class AtaqueComEscudo(HabilidadeAtiva):
    def __init__(self):
        super().__init__(
            nome="Ataque com Escudo",
            efeito=self.efeito_ataque_com_escudo,
            tempo_de_recarga=1,
            nivel_minimo=1,
            duração=1
        )
        self.descrição_do_efeito = (
            "Permite atacar com o escudo, causando dano baseado na defesa."
        )
        self.atualizar_descrição()
        self.usuario = None
        self.alvo = None
        self.tempo_ativação = None
        self.ativa = False

    def ativar(self, usuario, alvo):
        self.usuario = usuario
        self.alvo = alvo
        self.tempo_ativação = time.time()
        self.ativa = True
        self.usuario.pode_atacar = True

    def atualizar(self):
        if not self.ativa:
            return

        tempo_passado = time.time() - self.tempo_ativação
        if tempo_passado > self.duração:
            self.ativa = False
            self.usuario.pode_atacar = False

    def efeito_ataque_com_escudo(self, usuario, alvo):
        if alvo:
            dano = int(max(0, (usuario.defesa_final * 2) - (alvo.defesa_final * 0.75)))
            alvo.vida -= dano

class DefesaReforçada(HabilidadeAtiva):
    def __init__(self, raio, duração=5):
        super().__init__(
            nome="Defesa Reforçada",
            efeito=self.efeito_defesa_reforcada,
            tempo_de_recarga=1,
            nivel_minimo=1,
            duração=duração
        )
        self.descrição_do_efeito = (
            f"Aumenta a defesa dos aliados dentro de um raio de {raio} por {duração} segundos."
        )
        self.atualizar_descrição()
        self.usuario = None
        self.centro_x = None
        self.centro_y = None
        self.raio = raio
        self.tempo_ativação = None
        self.ativa = False
        self.personagens_no_campo = set()

    def ativar(self, usuario, centro_x, centro_y):
        self.usuario = usuario
        self.centro_x = centro_x
        self.centro_y = centro_y
        self.tempo_ativação = time.time()
        self.ativa = True

    def esta_dentro_campo(self, personagem):
        direção_x = personagem.posição_x - self.centro_x
        direção_y = personagem.posição_y - self.centro_y
        distancia = math.sqrt(direção_x*direção_x + direção_y*direção_y)
        return distancia <= self.raio

    def atualizar(self, personagens): 
        if not self.ativa:
            return

        tempo_passado = time.time() - self.tempo_ativação
        if tempo_passado > self.duração:
            self.ativa = False
            for personagem in self.personagens_no_campo:
                personagem.defesa_bonus -= int(personagem.defesa_base * 1.1)
            self.personagens_no_campo.clear()
            return

        personagens_atuais = set()
        for personagem in personagens:
            if self.esta_dentro_campo(personagem):
                personagens_atuais.add(personagem)
                if personagem not in self.personagens_no_campo:
                    personagem.defesa_bonus += int(personagem.defesa_base * 1.1)
            else:
                if personagem in self.personagens_no_campo:
                    personagem.defesa_bonus -= int(personagem.defesa_base * 1.1)

        self.personagens_no_campo = personagens_atuais

    def efeito_defesa_reforcada(self, usuario):
        pass

ataque_com_escudo = AtaqueComEscudo()
defesa_reforcada = DefesaReforçada()