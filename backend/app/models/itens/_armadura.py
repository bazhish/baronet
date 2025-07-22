from random import choice
from typing import Dict, Any

# CLASSE PARA CRIAR UMA PEÇA DO CONJUNTO DA ARMADURA
class PeçaArmadura:
    # INICIALIZA O BLOCO DE CÓDIGO COM ATRIBUTOS OBRIGATÓRIOS A SEREM PASSADOSE DEFINE ALGUNS A SEREM CARACTERIZADOS ADIANTE
    def __init__(self, nome_da_peça, tipo, defesa, material, durabilidade): # ATRIBUTOS OBRIGATORIOS A SEREM PASSADOS PARA A CLASSE INICIALIZAR
        self.nome_da_peça = nome_da_peça # NOME DA PEÇA
        self.tipo = tipo # TIPO DA PEÇA(ATAQUE OU DEFESA)
        self.defesa = defesa # QUANTO DE DEFESA A PEÇA FORNCE
        self.material = material # MATERIAL QUE A PEÇA É FEITA
        self.efeitos = ["dano", "velocidade", "vida", "defesa", "bonus_de_experiencia"] # LISTA COM POSSIVEIS EFEITO QUE A PEÇA PODE FORNECER
        self.equipada = False # INIDCA SE A PEÇA ESTÁ EQUIPADA(POR PADRÃO É "FALSO")
        self.raridade = "comum" # INDICA A RARIDADE DA PEÇA(POR PADRÃO É "COMUM")
        self.durabilidade = durabilidade # O QUANTO DE DANO QUE A PEÇA AGUENTA ANTES DE QUEBRAR
        self.efeito_aplicado = None # INIDCA SE A PEÇA TEM UM EFEITO APLICADO(POR PADRÃO É "NENHUM")
        self.descrição = (f"nome da peça: {self.nome_da_peça}\n"
                          f"tipo da peça: {self.tipo}\n"
                          f"defesa da peça: {self.defesa}\n"
                          f"material da peça: {self.material}\n"
                          f"raridade da peça: {self.raridade}\n"
                          f"durabilidade da peça: {self.durabilidade}")
        
    # MÉTODO PARA EQUIPAR A PEÇA NO USUÁRIO
    def equipar(self, usuario: Dict[str, Any]):
        usuario["defesa"] += self.defesa
        self.equipada = True

    # MÉTODO PARA ESCOLHER A RARIDADE DA PEÇA MANUALMENTE
    def escolher_raridade(self, raridade: str):
        self.raridade = raridade

    # MÉTODO PARA ATRIBUIR UM EFEITO ALEATÓRIO A PEÇA E APLICAR AO USUÁRIO
    def aplicar_efeito_aleatorio(self, usuario: Dict[str, Any]):
        efeito = choice(self.efeitos)
        self.aplicar_efeito(usuario, efeito)
        self.efeito_aplicado = efeito  # ARMAZENA O EFEITO APLICADO PARA FUTURAS REFERÊNCIAS

    # MÉTODO PARA REMOVER OS BENEFÍCIOS DA PEÇA DO USUÁRIO AO QUEBRAR
    def remover_beneficios(self, usuario: Dict[str, Any]):
        # REMOVE A DEFESA CONCEDIDA PELA PEÇA
        usuario["defesa"] = max(0, usuario["defesa"] - self.defesa)

        # REMOVER EFEITO CONCEDIDO AO USUARIO
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

    # MÉTODO PARA DIMINUIR A DURABILIDADE DA PEÇA
    def diminuir_durabilidade(self, adversário: dict, usuario: Dict[str, Any]):
        if self.durabilidade > 0: # VERIFICA SE A DURABILIDADE É MAIOR QUE ZERO
            self.durabilidade -= adversário["dano"] // 3 # DIMINUI A DURABILIDADE CONFORME O DANO DO ADVERSÁRIO
 
        if self.durabilidade <= 0: # VERIFICA SE A DURABILIDADE É MENOR OU IGUAL A ZERO
            self.remover_beneficios(usuario)  # QUEBRA A PEÇA E REMOVE OS BENEFÍCIOS DO USUÁRIO

    # MÉTODO PARA ATRIBUIR UM EFEITO MANUAL A PEÇA E APLICAR AO USUÁRIO
    def aplicar_efeito(self, usuario: Dict[str, Any], efeito: str):
        # VALORES BASE PARA SER ESCALADO CONFORME A RARIDADE
        base = {
            "dano": 4,
            "velocidade": 2,
            "vida": 10,
            "defesa": 3,
            "bonus_de_experiencia": 5
        }
        # VALORES DAS RARIDADES A SEREM ESCALADOS
        fatores = {
            "comum": 1,
            "rara": 1.5,
            "epica": 2,
            "lendario": 2.5
        }

        # OPERAÇÃO REALIZADA PARA ESCALAR O VALOR BASE
        fator = fatores.get(self.raridade, 1)
        valor = int(base[efeito] * fator)

        # CONDIÇÃO PARA ATRIBUIR O EFEITO AO USUÁRIO
        if not self.equipada and efeito in usuario:
            usuario[efeito] += valor
            self.efeito_aplicado = efeito  # ARMAZENA O EFEITO APLICADO PARA FUTURAS REFERÊNCIAS

# CLASSE PARA JUNTAR E COMPLETAR O CONJUNTO DA ARMADURA
class ConjuntoArmadura:
    # INICIALIZA O BLOCO DE CÓDIGO COM ATRIBUTOS OBRIGATÓRIOS A SEREM PASSADOSE DEFINE ALGUNS A SEREM CARACTERIZADOS ADIANTE
    def __init__(self, nome_do_conjunto, tipo_de_conjunto): # ATRIBUTOS OBRIGATORIOS A SEREM PASSADOS PARA A CLASSE INICIALIZAR
        self.nome_do_conjunto = nome_do_conjunto # NOME DADO AO CONJUNTO COMPLETO DE ARMADURAS
        self.tipo_de_conjunto = tipo_de_conjunto  # DEFINE SE A ARMADURA É UM TIPO "ATAQUE" OU "DEFESA"
        self.armaduras: list[PeçaArmadura] = [] # RECEBE A LISTA DE PEÇAS E ARMAZENA
        self.conjunto_completo = "incompleto" # INDICA O STATUS DO CONJUNTO (POR PADRÃO É "INCOMPLETO")  
        self.status_do_conjunto = False # INDICA SE O CONJUNTO DE PEÇAS ESTÁ COMPLETO (POR PADRÃO É "FALSO")
        self.bonus = "nenhum" # INDICA O BONUS QUE O CONJUNTO FORNECE (POR PADRÃO É "NENHUM")
        self.status_do_bonus = False # SE O CONJUNTO ESTIVER COMPLETO ATIVA UM BONUS UNICO DA ARMADURA (POR PADRÃO É "FALSO")
        self.peças_obrigatorias = ["elmo", "peitoral", "calça", "bota"] # PEÇAS OBRIGATÓRIAS PARA O CONJUNTO ESTÁ COMPLETA
        self.descrição = "" # DESCRIÇÃO DO CONJUNTO
        self.atualizar_descricao()  # CHAMA O MÉTODO PARA ATUALIZAR A DESCRIÇÃO DO CONJUNTO

    # MÉTODO QUE ADICONA AS PEÇAS AO CONJUNTO
    def adicionar_peça(self, peça: PeçaArmadura):
        if len(self.armaduras) < 4: # VERIFICA SE FALTA PEÇAS NO CONJUNTO
            self.armaduras.append(peça) # ADICONA A PEÇA
        self.verificar_se_o_conjunto_esta_completo() # CHAMA UM OUTRO MÉTODO QUE VERIFICA SE O CONJUNTO ESTÁ COMPLETO
        self.atualizar_descricao()  # CHAMA O MÉTODO PARA ATUALIZAR A DESCRIÇÃO DO CONJUNTO

    # MÉTODO QUE VERIFICA SE O CONJUNTO ESTÁ COMPLETO
    def verificar_se_o_conjunto_esta_completo(self):
        if len(self.armaduras) == 4: # VERIFICA SE TODAS AS PEÇAS DO CONJUNTO ESTÃO EQUIPADAS
            self.status_do_conjunto = True # ATRIBUI QUE AS PEÇAS ESTÃO EQUIPADAS
            self.conjunto_completo = "completo" # ATRIBUI O STATUS DO CONJUNTO COMO "COMPLETO"
            self.status_do_bonus = True # ATRIBUI QUE É POSSIVEL USAR O BONUS

    # MÉTODO QUE APLICA O BONUS DO CONJUNTO
    def aplicar_bonus_do_conjunto(self, usuario: Dict[str, Any]):
        if not self.status_do_bonus: # VERIFICA SE O BONUS PODE SER APLICADO
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
        self.exibir_bonus()  # CHAMA O MÉTODO PARA EXIBIR O BONUS DO CONJUNTO

    def exibir_bonus(self): # MÉTODO PARA EXIBIR O BONUS DO CONJUNTO
        if self.tipo_de_conjunto == "ataque":
            self.bonus = "mais 80% de dano\nmais 60% de defesa\nmais 40% de velocidade\nmais 20% de vida"
        elif self.tipo_de_conjunto == "defesa":
            self.bonus = "mais 30% de dano\nmais 80% de defesa\nmais 20% de velocidade\nmais 60% de vida"
    
    def atualizar_descricao(self): # MÉTODO PARA ATUALIZAR A DESCRIÇÃO DO CONJUNTO
        self.descrição = (
            f"nome do conjunto: {self.nome_do_conjunto}\n"
            f"tipo do conjunto: {self.tipo_de_conjunto}\n"
            f"status do conjunto: {self.conjunto_completo}\n"
            f"peças do conjunto: {', '.join([peça.nome_da_peça for peça in self.armaduras])}\n"
            f"status do bônus: {self.bonus}\n"
        )

# FUNÇÃO DE GERAR PEÇA E ADICIONAR AO CONJUNTO
def gerar_peça_do_conjunto(conjunto: ConjuntoArmadura, nome_da_peça: str, defesa: int, material: str, raridade: str, usuario: Dict[str, Any], durabilidade: int):
    tipo = conjunto.tipo_de_conjunto # ATRIBUI O TIPO DO CONJUNTO  UMA VARIVAEL
    peça = PeçaArmadura(nome_da_peça, tipo, defesa, material, durabilidade) # CRIA UMA VARIAVEL PESSA E ATRIBUI OS PARAMENTROS OBRIGATORIOS
    peça.escolher_raridade(raridade) # ESCOLHE A RARIDADE DA PEÇA
    peça.aplicar_efeito_aleatorio(usuario) # APLICA O EFEITO NO USUARIO
    peça.equipar(usuario) # EQUIPA A PEÇA
    conjunto.adicionar_peça(peça) # CRIA UM CONJUNTO E ADICIONA A PEÇA A ELE
    return peça

"""# exemplo de uso:

usuario = {
    "dano": 10,
    "defesa": 10,
    "velocidade": 10,
    "vida": 100,
    "bonus_de_experiencia": 0
}

conjunto = ConjuntoArmadura("Armadura da besta celestial", "ataque")
gerar_peça_do_conjunto(conjunto, "Elmo da besta celestial", 5, "escamas da besta celestial", "lendario", usuario, 200)
gerar_peça_do_conjunto(conjunto, "Peitoral da besta celestial", 8, "escamas da besta celestial", "lendario", usuario, 500)
gerar_peça_do_conjunto(conjunto, "Calça da besta celestial", 4, "escamas da besta celestial", "lendario", usuario, 400)
gerar_peça_do_conjunto(conjunto, "Botas da besta celestial", 3, "escamas da besta celestial", "lendario", usuario, 150)
conjunto.verificar_se_o_conjunto_esta_completo()  
conjunto.aplicar_bonus_do_conjunto(usuario)

print(usuario)
print(conjunto.descrição)
"""