from random import randint, choice
from typing import Any, Dict
from dataclasses import dataclass, field
import sys, os
import time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../..')))
from backend.app.models.personagens.jogador_ficticio import jogador 

@dataclass
class Escudo:
    nome: str
    defesa: int
    peso: int

    raridades = {
        "comum": 1.0,
        "raro": 1.5,
        "epico": 2.3,
        "lendario": 2.8
    }

    cooldowns_por_raridade = {
        "comum": 10,      
        "raro": 7,
        "epico": 5,
        "lendario": 3
    }
    dano_para_cooldown = 50

    descrição: str = field(default="", init=False)

    def __post_init__(self):
        self.nivel = int
        self.raridade = str
        self.atributo_adicional = Any
        self.defesa_final = Any
        self.dano_acumulado = 0
        self.em_cooldown = False
        self.cooldown_fim = 0

    def atualizar_descrição(self):
        self.descrição = (
            f"Nome: {self.nome}, "
            f"Nível: {self.nivel}, "
            f"Raridade: {self.raridade}, "
            f"Defesa: {self.defesa_final}, "
            f"Peso: {self.peso}, "
            f"Atributo adicional: {self.atributo_adicional}, "
            f"Cooldown ativo: {self.em_cooldown}, "
            f"Tempo restante cooldown: {max(0, int(self.cooldown_fim - time.time())) if self.em_cooldown else 0}"
        )

    def definir_nivel_com_base_no_usuario(self, usuario):
        nivel_usuario = usuario.nível_atual
        self.nivel = randint(max(1, nivel_usuario - 3), min(nivel_usuario + 3, 100))

    def definir_nivel_manual(self, nivel):
        self.nivel = nivel

    def escolher_raridade(self, raridade):
        self.raridade = raridade

    def calcular_defesa(self):
        fator = self.raridades.get(self.raridade, 1.0)
        self.defesa_final = self.defesa * self.nivel * fator
        self.peso = self.peso * self.nivel * fator
        
    def escolher_atributo_adicional_aleatorio(self):
        atributos = ["defesa", "vida", "velocidade"]
        self.atributo_adicional = choice(atributos)

    def aplicar_bonus_no_usuario(self, usuario):
        defesa_bonus = 2
        vida_bonus = 10
        velocidade_bonus = 3

        fator = self.raridades.get(self.raridade, 1.0)
        defesa_bonus *= self.nivel * fator
        vida_bonus *= self.nivel * fator
        velocidade_bonus *= self.nivel * fator

        if self.atributo_adicional == "defesa":
            usuario.defesa_bonus += defesa_bonus
        elif self.atributo_adicional == "vida":
            usuario.vida_bonus += vida_bonus
        elif self.atributo_adicional == "velocidade":
            usuario.velocidade_bonus += velocidade_bonus

    def receber_dano(self, dano: int):
        if self.em_cooldown:
            return False

        self.dano_acumulado += dano
        if self.dano_acumulado >= self.dano_para_cooldown:
            self.ativar_cooldown()
            self.dano_acumulado = 0
        return True

    def ativar_cooldown(self):
        tempo_cooldown = self.cooldowns_por_raridade.get(self.raridade, 10)
        self.em_cooldown = True
        self.cooldown_fim = time.time() + tempo_cooldown

    def atualizar_cooldown(self):
        if self.em_cooldown and time.time() >= self.cooldown_fim:
            self.em_cooldown = False

    def gerar_escudo(self):
        self.atualizar_cooldown()
        self.calcular_defesa()
        return {
            "Nome": self.nome,
            "Nível": self.nivel,
            "Raridade": self.raridade,
            "Defesa": self.defesa_final,
            "Peso": self.peso,
            "Atributo adicional": self.atributo_adicional,
            "Cooldown ativo": self.em_cooldown,
            "Tempo restante cooldown": max(0, int(self.cooldown_fim - time.time())) if self.em_cooldown else 0,
        }

def criar_escudo(nome: str, raridade, usuario):
    raridades = {
        "comum": (5,3),
        "raro": (7,3),
        "epico": (10,2),
        "lendario": (15,2)
    }

    defesa, peso = raridades[raridade]
    escudo = Escudo(nome, defesa, peso)
    escudo.definir_nivel_com_base_no_usuario(usuario)
    escudo.escolher_raridade(raridade)
    escudo.calcular_defesa()
    escudo.escolher_atributo_adicional_aleatorio()
    escudo.aplicar_bonus_no_usuario(usuario)
    return escudo.gerar_escudo()

escudo_titanico = criar_escudo("Escudo Titânico", "lendario", jogador)

print(escudo_titanico.descrição)