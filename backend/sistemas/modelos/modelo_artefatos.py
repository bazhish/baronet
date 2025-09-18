from random import randint, choice
from dataclasses import dataclass, field
import sys, os, time

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = current_dir
while not os.path.isdir(os.path.join(project_root, ".git")) and os.path.dirname(project_root) != project_root:
    project_root = os.path.dirname(project_root)
sys.path.append(project_root)

@dataclass
class Escudo:
    nome: str
    defesa_base: int
    peso_base: int
    raridade: str = field(default  ="nenhuma")
    nivel: int = field(default = 1)
    defesa_final: float = field(default = 0)
    peso: float = field(default = 0)
    atributo_adicional: str = field(default = "nenhum")
    dano_acumulado: int = field(default = 0)
    em_cooldown: bool = field(default = False)
    cooldown_fim: float = field(default =0)
    descrição: str = field(default = "nenhuma", init = False)

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
    atributos_possiveis = ["defesa", "vida", "velocidade"]

    def pode_usar(self, usuario) -> bool:
        return True

    def definir_nivel_com_base_no_usuario(self, usuario):
        nivel_usuario = usuario.nível_atual
        self.nivel = randint(max(1, nivel_usuario - 3), min(nivel_usuario + 3, 100))

    def definir_nivel_manual(self, nivel):
        self.nivel = nivel

    def escolher_raridade(self, raridade):
        self.raridade = raridade

    def calcular_defesa(self):
        fator = self.raridades.get(self.raridade, 1.0)
        self.defesa_final = self.defesa_base * self.nivel * fator
        self.peso = self.peso_base * self.nivel * fator

    def escolher_atributo_adicional_aleatorio(self):
        self.atributo_adicional = choice(self.atributos_possiveis)

    def aplicar_bonus_no_usuario(self, usuario):
        valores_base = {"defesa": 2, "vida": 10, "velocidade": 3}
        fator = self.raridades.get(self.raridade, 1.0)
        valor = valores_base[self.atributo_adicional] * self.nivel * fator
        chave = f"{self.atributo_adicional}_bonus"
        if hasattr(usuario, chave):
            atual = getattr(usuario, chave)
            setattr(usuario, chave, atual + valor)
        else:
            setattr(usuario, chave, valor)

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

    def atualizar_descrição(self):
        self.descrição = (
            f"Escudo: {self.nome}\n"
            f"Raridade: {self.raridade}\n"
            f"Nível: {self.nivel}\n"
            f"Defesa: {round(self.defesa_final, 1)}\n"
            f"Peso: {round(self.peso, 1)}\n"
            f"Atributo adicional: {self.atributo_adicional}\n"
            f"Cooldown ativo: {self.em_cooldown}, "
            f"Tempo restante cooldown: {max(0, int(self.cooldown_fim - time.time())) if self.em_cooldown else 0}"
        )

def criar_escudo(nome: str, raridade: str, usuario):
    tabela_escudos = {
        "comum": (5, 3),
        "raro": (7, 3),
        "epico": (10, 2),
        "lendario": (15, 2)
    }
    defesa, peso = tabela_escudos[raridade]
    escudo = Escudo(nome, defesa, peso)
    escudo.escolher_raridade(raridade)
    escudo.definir_nivel_com_base_no_usuario(usuario)
    escudo.calcular_defesa()
    escudo.escolher_atributo_adicional_aleatorio()
    escudo.aplicar_bonus_no_usuario(usuario)
    escudo.atualizar_descrição()
    return escudo

@dataclass
class Cajado:
    nome: str
    poder_base: int
    raridade: str = field(default = "nenhuma")
    nivel: int = field(default = 1)
    poder_final: float = field(default = 0)
    atributo_adicional: str = field(default = "nenhum")
    descrição: str = field(default = "nenhuma", init = False)

    raridades = {
        "comum": 1.0,
        "raro": 1.5,
        "epico": 2.3,
        "lendario": 2.8
    }
    atributos_possiveis = ["cura", "defesa", "estamina"]

    def definir_nivel_com_base_no_usuario(self, usuario):
        nivel_usuario = usuario.nível_atual
        self.nivel = randint(max(1, nivel_usuario - 3), min(nivel_usuario + 3, 100))

    def escolher_raridade(self, raridade):
        self.raridade = raridade

    def calcular_poder(self):
        fator = self.raridades.get(self.raridade, 1.0)
        self.poder_final = self.poder_base * self.nivel * fator

    def escolher_atributo_adicional_aleatorio(self):
        self.atributo_adicional = choice(self.atributos_possiveis)

    def aplicar_bonus_no_usuario(self, usuario):
        valores_base = {"defesa": 5, "estamina": 10}
        fator = self.raridades.get(self.raridade, 1.0)
        valor = valores_base[self.atributo_adicional] * self.nivel * fator
        chave = f"{self.atributo_adicional}_bonus"
        if hasattr(usuario, chave):
            atual = getattr(usuario, chave)
            setattr(usuario, chave, atual + valor)
        else:
            setattr(usuario, chave, valor)

    def atualizar_descrição(self):
        self.descrição = (
            f"Cajado: {self.nome}\n"
            f"Raridade: {self.raridade}\n"
            f"Nível: {self.nivel}\n"
            f"Poder: {round(self.poder_final, 1)}\n"
            f"Atributo adicional: {self.atributo_adicional}\n"
        )

def criar_cajado(nome: str, raridade: str, usuario):
    tabela_cajados = {
        "comum": 8,
        "raro": 12,
        "epico": 18,
        "lendario": 25
    }
    poder = tabela_cajados[raridade]
    cajado = Cajado(nome, poder)
    cajado.escolher_raridade(raridade)
    cajado.definir_nivel_com_base_no_usuario(usuario)
    cajado.calcular_poder()
    cajado.escolher_atributo_adicional_aleatorio()
    cajado.aplicar_bonus_no_usuario(usuario)
    cajado.atualizar_descrição()
    return cajado

@dataclass
class Lira:
    nome: str
    melodia_base: int
    raridade: str = field(default = "nenhuma")
    nivel: int = field(default = 1)
    melodia_final: float = field(default = 0)
    atributo_adicional: str = field(default = "nenhum")
    descrição: str = field(default = "nenhuma", init = False)

    raridades = {
        "comum": 1.0,
        "raro": 1.5,
        "epico": 2.3,
        "lendario": 2.8
    }
    atributos_possiveis = ["dano", "velocidade", "estamina"]

    def definir_nivel_com_base_no_usuario(self, usuario):
        nivel_usuario = usuario.nível_atual
        self.nivel = randint(max(1, nivel_usuario - 3), min(nivel_usuario + 3, 100))

    def escolher_raridade(self, raridade):
        self.raridade = raridade

    def calcular_melodia(self):
        fator = self.raridades.get(self.raridade, 1.0)
        self.melodia_final = self.melodia_base * self.nivel * fator

    def escolher_atributo_adicional_aleatorio(self):
        self.atributo_adicional = choice(self.atributos_possiveis)

    def aplicar_bonus_no_usuario(self, usuario):
        valores_base = {"dano": 5, "velocidade": 7, "estamina": 10}
        fator = self.raridades.get(self.raridade, 1.0)
        valor = valores_base[self.atributo_adicional] * self.nivel * fator
        chave = f"{self.atributo_adicional}_bonus"
        if hasattr(usuario, chave):
            atual = getattr(usuario, chave)
            setattr(usuario, chave, atual + valor)
        else:
            setattr(usuario, chave, valor)

    def atualizar_descrição(self):
        self.descrição = (
            f"Lira: {self.nome}\n"
            f"Raridade: {self.raridade}\n"
            f"Nível: {self.nivel}\n"
            f"Melodia: {round(self.melodia_final, 1)}\n"
            f"Atributo adicional: {self.atributo_adicional}\n"
        )

def criar_lira(nome: str, raridade: str, usuario):
    tabela_liras = {
        "comum": 6,
        "raro": 10,
        "epico": 15,
        "lendario": 22
    }
    melodia = tabela_liras[raridade]
    lira = Lira(nome, melodia)
    lira.escolher_raridade(raridade)
    lira.definir_nivel_com_base_no_usuario(usuario)
    lira.calcular_melodia()
    lira.escolher_atributo_adicional_aleatorio()
    lira.aplicar_bonus_no_usuario(usuario)
    lira.atualizar_descrição()
    return lira

@dataclass
class VarinhaDeIlusoes:
    nome: str
    magia_base: int
    raridade: str = field(default = "nenhuma")
    nivel: int = field(default = 1)
    magia_final: float = field(default = 0)
    atributo_adicional: str = field(default = "nenhum")
    descrição: str = field(default = "nenhuma", init = False)

    raridades = {
        "comum": 1.0,
        "raro": 1.5,
        "epico": 2.3,
        "lendario": 2.8
    }
    atributos_possiveis = ["dano", "velocidade", "vida"]

    def definir_nivel_com_base_no_usuario(self, usuario):
        nivel_usuario = usuario.nível_atual
        self.nivel = randint(max(1, nivel_usuario - 3), min(nivel_usuario + 3, 100))

    def escolher_raridade(self, raridade):
        self.raridade = raridade

    def calcular_magia(self):
        fator = self.raridades.get(self.raridade, 1.0)
        self.magia_final = self.magia_base * self.nivel * fator

    def escolher_atributo_adicional_aleatorio(self):
        self.atributo_adicional = choice(self.atributos_possiveis)

    def aplicar_bonus_no_usuario(self, usuario):
        valores_base = {"dano": 7, "velocidade": 8, "vida": 12}
        fator = self.raridades.get(self.raridade, 1.0)
        valor = valores_base[self.atributo_adicional] * self.nivel * fator
        chave = f"{self.atributo_adicional}_bonus"
        if hasattr(usuario, chave):
            atual = getattr(usuario, chave)
            setattr(usuario, chave, atual + valor)
        else:
            setattr(usuario, chave, valor)

    def atualizar_descrição(self):
        self.descrição = (
            f"Varinha de Ilusões: {self.nome}\n"
            f"Raridade: {self.raridade}\n"
            f"Nível: {self.nivel}\n"
            f"Magia: {round(self.magia_final, 1)}\n"
            f"Atributo adicional: {self.atributo_adicional}\n"
        )

def criar_varinha_de_ilusoes(nome: str, raridade: str, usuario):
    tabela_varinhas = {
        "comum": 7,
        "raro": 11,
        "epico": 17,
        "lendario": 24
    }
    magia = tabela_varinhas[raridade]
    varinha = VarinhaDeIlusoes(nome, magia)
    varinha.escolher_raridade(raridade)
    varinha.definir_nivel_com_base_no_usuario(usuario)
    varinha.calcular_magia()
    varinha.escolher_atributo_adicional_aleatorio()
    varinha.aplicar_bonus_no_usuario(usuario)
    varinha.atualizar_descrição()
    return varinha