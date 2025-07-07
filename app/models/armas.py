from random import choice, randint, uniform
from typing import Dict, Any
from dataclasses import dataclass
from classes_permitidas import definir_classes_permitidas

@dataclass
class Arma:
    def __init__(self, tipo: str, nome: str, dano: int, peso: int,
                durabilidade: int, experiência_máxima_inicial: int,
                crescimento_de_experiência: float, porcentagem_de_reparo: float,
                porcentagem_de_evolução: float):
        self.tipo_da_arma = tipo
        self.nome = nome
        self.raridades = ["comum", "rara", "épica", "lendaria"]
        self.raridade: str
        self.dano_base = dano
        self.dano: int
        self.bonus = float(uniform(1.1, 1.9) - 1)
        self.peso = peso
        self.atributos = ["dano", "vida", "velocidade", "defesa"]
        self.atributo: Any
        self.nível: Any
        self.durabilidade = durabilidade 
        self.descrição: str
        self.experiência_atual = 0
        self.experiência_máxima = experiência_máxima_inicial
        self.crescimento_de_experiência = crescimento_de_experiência
        self.porcentagem_de_reparo = porcentagem_de_reparo
        self.porcentagem_de_evolução = porcentagem_de_evolução
        self.classes_permitidas = definir_classes_permitidas(tipo)  
        self.níveis_raridade = {
            "comum": (0, 25),
            "rara": (25, 50),
            "épica": (50, 75),
            "lendaria": (75, 100)
        }       

    def pode_usar(self, usuario: Dict[str, Any]) -> bool:
        nível_minimo, nível_máximo = self.níveis_raridade.get(self.raridade, (0, 100))
        classe = usuario.get("classe", None)
        classe = classe is not None and self.classes_permitidas is not None and classe in self.classes_permitidas
        return nível_minimo <= usuario["nível"] < nível_máximo and classe

    def nivel_da_arma_com_parametro_do_usuario(self, usuario: Dict[str, Any]):
        self.nível = randint(max(1, usuario["nível"] - 3), min(usuario["nível"] + 3, 100))

    def nivel_com_parametro_manual(self, nível: int):
        self.nível = nível

    def dano_da_arma(self):
        self.dano = self.dano_base * self.nível

    def velocidade_que_o_usuario_ira_perder(self, usuario: Dict[str, Any]):
        usuario["velocidade"] -= self.peso

    def escolha_de_raridade(self, raridade_escolhida: str):
        self.raridade = raridade_escolhida

    def aplicar_bonus_atributo(self, usuario: Dict[str, Any], atributo: str):
        valores_base = {"dano": 2, "vida": 10, "velocidade": 3, "defesa": 1}
        multiplicador = {"comum": 1, "rara": 1.5, "épica": 2.3, "lendaria": 2.8}.get(self.raridade, 1)
        valor = valores_base[atributo] * multiplicador * self.nível
        usuario[atributo] += valor

    def atributo_adicional_aleatorio(self, usuario: Dict[str, Any]):
        self.atributo_escolhido = choice(self.atributos)
        self.atributo = self.atributo_escolhido
        self.aplicar_bonus_atributo(usuario, self.atributo)

    def atributo_adicional_manual(self, atributo: str, usuario: Dict[str, Any]):
        self.atributo = atributo
        self.aplicar_bonus_atributo(usuario, self.atributo)

    def checar_e_remover_se_quebrada(self, usuario: Dict[str, Any]):
         if self.durabilidade <= 0:
            usuario["arma"] = "nenhuma"

    def usar(self, usuario: Dict[str, Any], alvo: Dict[str, Any]):
        dano_final = self.dano * {"comum": 1, "rara": 1.5, "épica": 2.3, "lendaria": 2.8}.get(self.raridade, 1)
        alvo["vida"] -= dano_final
        self.aplicar_bonus_atributo(usuario, self.atributo)
        self.durabilidade -= 1
        self.checar_e_remover_se_quebrada(usuario)

    def receber_xp(self, experiência_dropada: int):
        ganho = int(experiência_dropada * self.porcentagem_de_evolução)
        experiência_de_reparo = int(experiência_dropada * self.porcentagem_de_reparo)
        self.experiência_atual += ganho
        self.durabilidade += experiência_de_reparo
        while self.experiência_atual >= self.experiência_máxima and self.nível < 100:
            self.experiência_atual -= self.experiência_máxima
            self.nível += 1
            self.experiência_máxima = int(self.experiência_máxima * (1 + self.crescimento_de_experiência))
        
        if self.nível >= 100:
            self.nível = "nível máximo"
            self.experiência_atual = 0

    def descrição_da_arma(self):
        raridades = {"comum": 1, "rara": 1.5, "épica": 2.3, "lendaria": 2.8}
        multiplicador = raridades.get(self.raridade, 1)
        bonus_percentual = f"{round(self.bonus * multiplicador * 10)}%"
        nivel_exibido = "nível máximo" if self.nível >= 100 else self.nível
        info = (
            f"Arma: {self.nome}\n"
            f"Raridade: {self.raridade}\n"
            f"Nível: {nivel_exibido}\n"
            f"Dano: {round(self.dano * multiplicador, 1)}\n"
            f"Bônus de experiência: {bonus_percentual}\n"
            f"Peso: {self.peso}\n"
            f"Durabilidade: {self.durabilidade}\n"
            f"Atributo adicional: {self.atributo}\n"
            f"experiência: {self.experiência_atual}/{self.experiência_máxima}\n"
        )
        return info
    
def criar_arma(tipo: str, nome: str, raridade: str, usuario: Dict, durabilidade: int, experiência_máxima_inicial: int, crescimento_de_experiência: float, porcentagem_de_reparo: float, porcentagem_de_evolução: float ):
    tabela_armas = {
        "espada": {"comum": (6,3), "rara": (11,3), "épica": (18,2), "lendaria": (23,2)},
        "espada Curta": {"comum": (6,2), "rara": (8,2), "épica": (12,1), "lendaria": (18,1)},
        "espada Longa": {"comum": (9,4), "rara": (12,4), "épica": (16,3), "lendaria": (24,3)},
        "espada Dupla": {"comum": (10,5), "rara": (14,5), "épica": (18,3), "lendaria": (21,3)},
        "adaga": {"comum": (5,3), "rara": (8,3), "épica": (10,2), "lendaria": (13,2)},
        "adaga dupla": {"comum": (7,5), "rara": (16,5), "épica": (20,4), "lendaria": (26,4)},
        "zarabatana": {"comum": (4,3), "rara": (6,3), "épica": (8,2), "lendaria": (13,2)},
        "besta": {"comum": (6,5), "rara": (9,5), "épica": (12,4), "lendaria": (16,4)},
        "arco": {"comum": (5,3), "rara": (8,3), "épica": (10,2), "lendaria": (16,2)},
        "lança": {"comum": (6,4), "rara": (8,4), "épica": (11,3), "lendaria": (16,5)},
        "machado": {"comum": (8,4), "rara": (10,4), "épica": (16,4), "lendaria": (20,4)},
        "machado duplo": {"comum": (10,6), "rara": (18,6), "épica": (24,6), "lendaria": (26,5)},
        "cutelo": {"comum": (9,4), "rara": (12,4), "épica": (15,3), "lendaria": (18,3)},
        "cutelo duplo": {"comum": (11,6), "rara": (16,6), "épica": (20,5), "lendaria": (25,5)},
        "manopla": {"comum": (8,4), "rara": (13,4), "épica": (18,3), "lendaria": (23,3)},
        "katana": {"comum": (9,4), "rara": (15,4), "épica": (18,3), "lendaria": (20,33)},
        "sabre": {"comum": (7,4), "rara": (10,4), "épica": (15,3), "lendaria": (20,3)},
    }

    dano, peso = tabela_armas[tipo][raridade]
    nova_arma = Arma(tipo, nome, dano, peso, durabilidade, experiência_máxima_inicial, crescimento_de_experiência, porcentagem_de_reparo, porcentagem_de_evolução)
    nova_arma.escolha_de_raridade(raridade)
    nova_arma.nivel_da_arma_com_parametro_do_usuario(usuario)
    nova_arma.dano_da_arma()
    nova_arma.atributo_adicional_aleatorio(usuario)
    nova_arma.descrição = nova_arma.descrição_da_arma()
    return nova_arma

jogador = {
    "nível": 10,
    "dano": 0,
    "vida": 100,
    "velocidade": 10,
    "defesa": 5
}

apocalipse = criar_arma("espada", "apocalipse", "lendaria", jogador, 20, 100, 0.1, 0.7, 1.0)
print(apocalipse.descrição)