from random import choice
from typing import Dict, Any

class PeçaArmadura:
    def __init__(self, nome_da_peça, tipo, defesa, material, durabilidade): 
        self.nome_da_peça = nome_da_peça 
        self.tipo = tipo 
        self.defesa = defesa 
        self.material = material 
        self.efeitos = ["dano", "velocidade", "vida", "defesa", "bonus_de_experiencia"]
        self.equipada = False 
        self.raridade = "comum" 
        self.durabilidade = durabilidade 
        self.efeito_aplicado = None 
        self.descrição = (f"nome da peça: {self.nome_da_peça}\n"
                          f"tipo da peça: {self.tipo}\n"
                          f"defesa da peça: {self.defesa}\n"
                          f"material da peça: {self.material}\n"
                          f"raridade da peça: {self.raridade}\n"
                          f"durabilidade da peça: {self.durabilidade}")
        
    
    def equipar(self, usuario: Dict[str, Any]):
        usuario["defesa"] += self.defesa
        self.equipada = True

    def escolher_raridade(self, raridade: str):
        self.raridade = raridade

    def aplicar_efeito_aleatorio(self, usuario: Dict[str, Any]):
        efeito = choice(self.efeitos)
        self.aplicar_efeito(usuario, efeito)
        self.efeito_aplicado = efeito

    def remover_beneficios(self, usuario: Dict[str, Any]):
        usuario["defesa"] = max(0, usuario["defesa"] - self.defesa)

        base = {
            "dano": 4,
            "velocidade": 2,
            "vida": 10,
            "defesa": 3,
            "bonus_de_experiencia": 5
        }

        fatores = {
            "comum": 1,
            "rara": 1.5,
            "epica": 2,
            "lendario": 2.5
        }

        fator = fatores.get(self.raridade, 1)
        if self.efeito_aplicado:
            efeito = self.efeito_aplicado.replace("bonus", "")
            if efeito in usuario:
                valor = int(base.get(efeito, 0) * fator)
                usuario[efeito] -= valor
        self.equipada = False
        self.efeito_aplicado = None

    def diminuir_durabilidade(self, adversário: dict, usuario: Dict[str, Any]):
        if self.durabilidade > 0: 
            self.durabilidade -= adversário["dano"] // 3 
 
        if self.durabilidade <= 0: 
            self.remover_beneficios(usuario)  

    def aplicar_efeito(self, usuario: Dict[str, Any], efeito: str):
        base = {
            "dano": 4,
            "velocidade": 2,
            "vida": 10,
            "defesa": 3,
            "bonus_de_experiencia": 5
        }

        fatores = {
            "comum": 1,
            "rara": 1.5,
            "epica": 2,
            "lendario": 2.5
        }

        fator = fatores.get(self.raridade, 1)
        valor = int(base[efeito] * fator)

        if not self.equipada and efeito in usuario:
            usuario[efeito] += valor
            self.efeito_aplicado = efeito 

class ConjuntoArmadura:

    def __init__(self, nome_do_conjunto, tipo_de_conjunto):
        self.nome_do_conjunto = nome_do_conjunto
        self.tipo_de_conjunto = tipo_de_conjunto 
        self.armaduras: list[PeçaArmadura] = [] 
        self.conjunto_completo = "incompleto" 
        self.status_do_conjunto = False 
        self.bonus = "nenhum" 
        self.status_do_bonus = False 
        self.peças_obrigatorias = ["elmo", "peitoral", "calça", "bota"] 
        self.descrição = "nenhuma"
        self.atualizar_descricao() 

    def adicionar_peça(self, peça: PeçaArmadura):
        if len(self.armaduras) < 4: 
            self.armaduras.append(peça) 
        self.verificar_se_o_conjunto_esta_completo() 
        self.atualizar_descricao()  

    def verificar_se_o_conjunto_esta_completo(self):
        if len(self.armaduras) == 4: 
            self.status_do_conjunto = True 
            self.conjunto_completo = "completo" 
            self.status_do_bonus = True 

    def aplicar_bonus_do_conjunto(self, usuario: Dict[str, Any]):
        if not self.status_do_bonus: 
            return

        if self.tipo_de_conjunto == "ataque":
            usuario["dano"] *= 1.8
            usuario["defesa"] *= 1.6
            usuario["velocidade"] *= 1.4
            usuario["vida"] *= 1.2
        elif self.tipo_de_conjunto == "defesa":
            usuario["dano"] *= 1.3
            usuario["defesa"] *= 1.8
            usuario["velocidade"] *= 1.2
            usuario["vida"] *= 1.6
        self.exibir_bonus()  

    def exibir_bonus(self):
        if self.tipo_de_conjunto == "ataque":
            self.bonus = "mais 80% de dano\nmais 60% de defesa\nmais 40% de velocidade\nmais 20% de vida"
        elif self.tipo_de_conjunto == "defesa":
            self.bonus = "mais 30% de dano\nmais 80% de defesa\nmais 20% de velocidade\nmais 60% de vida"
    
    def atualizar_descricao(self):
        self.descrição = (
            f"nome do conjunto: {self.nome_do_conjunto}\n"
            f"tipo do conjunto: {self.tipo_de_conjunto}\n"
            f"status do conjunto: {self.conjunto_completo}\n"
            f"peças do conjunto: {', '.join([peça.nome_da_peça for peça in self.armaduras])}\n"
            f"status do bônus: {self.bonus}\n"
        )

def gerar_peça_do_conjunto(conjunto: ConjuntoArmadura, nome_da_peça: str, defesa: int, material: str, raridade: str, usuario: Dict[str, Any], durabilidade: int):
    tipo = conjunto.tipo_de_conjunto 
    peça = PeçaArmadura(nome_da_peça, tipo, defesa, material, durabilidade)
    peça.escolher_raridade(raridade) 
    peça.aplicar_efeito_aleatorio(usuario) 
    peça.equipar(usuario) 
    conjunto.adicionar_peça(peça) 
    return peça