from random import randint, choice

def monstros_comum():
    lista_de_monstros = []

    def goblin():
        atributos = randint(0, 0)
        return {
            "nome": "goblin",
            "nível": atributos,
            "ataque": 0 * atributos,
            "velocidade": 0 * atributos,
            "defesa": 0 * atributos,
            "vida": 0 * atributos,
            "arma": "adaga"
        }

    def esqueleto():
        atributos = randint(0, 80)
        return {
            "nome": "esqueleto",
            "nível": atributos,
            "ataque": 0 * atributos,
            "velocidade": 0 * atributos,
            "defesa": 0 * atributos,
            "vida": 0 * atributos,
            "arma": "espada básica"
        }

    def lobo():
        atributos = randint(0, 0)
        return {
            "nome": "lobo",
            "nível": atributos,
            "ataque": 0 * atributos,
            "velocidade": 0 * atributos,
            "defesa": 0 * atributos,
            "vida": 0 * atributos,
            "arma": "nenhuma"
        }

    def zumbi():
        atributos = randint(0, 0)
        return {
            "nome": "zumbi",
            "nível": atributos,
            "ataque": 0 * atributos,
            "velocidade": 0 * atributos,
            "defesa": 0 * atributos,
            "vida": 0 * atributos,
            "arma": "espada básica"
        }
    
    def cão_selvagem():
        atributos = randint(0, 80)
        return {
            "nome": "cão selvagem",
            "nível": atributos,
            "ataque": 0 * atributos,
            "velocidade": 0 * atributos,
            "defesa": 0 * atributos,
            "vida": 0 * atributos,
            "arma": "nenhuma"
        }
    
    def rato_saqueador():
        atributos = randint(0, 0)
        return {
            "nome": "rato_saqueador",
            "nível": atributos,
            "ataque": 0 * atributos,
            "velocidade": 0 * atributos,
            "defesa": 0 * atributos,
            "vida": 0 * atributos,
            "arma": "nenhuma"
        }

    def gorila_raivoso():
        atributos = randint(0, 0)
        return {
            "nome": "gorila_raivoso",
            "nível": atributos,
            "ataque": 0 * atributos,
            "velocidade": 0 * atributos,
            "defesa": 0 * atributos,
            "vida": 0 * atributos,
            "arma": "nenhuma"
        }

def monstros_icomum():
    lista_de_monstros = []

    def orc():
        atributos = randint(0, 0)
        return {
            "nome": "orc",
            "nível": atributos,
            "ataque": 0 * atributos,
            "velocidade": 0 * atributos,
            "defesa": 0 * atributos,
            "vida": 0 * atributos,
            "arma": "lábris"
        }

    def troll():
        atributos = randint(0, 0)
        return {
            "nome": "troll",
            "nível": atributos,
            "ataque": 0 * atributos,
            "velocidade": 0 * atributos,
            "defesa": 0 * atributos,
            "vida": 0 * atributos,
            "arma": "cutelo"
        }

    def goblin_sombrio():
        atributos = randint(0, 0)
        return {
            "nome": "goblin sombrio",
            "nível": atributos,
            "ataque": 0 * atributos,
            "velocidade": 0 * atributos,
            "defesa": 0 * atributos,
            "vida": 0 * atributos,
            "arma": "adagas duplas"
        }

    def javali_mutante():
        atributos = randint(0, 0)
        return {
            "nome": "javali mutante",
            "nível": atributos,
            "ataque": 0 * atributos,
            "velocidade": 0 * atributos,
            "defesa": 0 * atributos,
            "vida": 0 * atributos,
            "arma": "nenhuma"
        }

    def goblin_arqueiro():
        atributos = randint(0, 0)
        return {
            "nome": "goblin arqueiro",
            "nível": atributos,
            "ataque": 0 * atributos,
            "velocidade": 0 * atributos,
            "defesa": 0 * atributos,
            "vida": 0 * atributos,
            "arma": "arco"
        }
    
def monstros_raros():

    def esqueleto_branco():
        atributos = randint(0, 0)
        return {
            "nome": "esqueleto negro",
            "nível": atributos,
            "ataque": 0 * atributos,
            "velocidade": 0 * atributos,
            "defesa": 0 * atributos,
            "vida": 0 * atributos,
            "arma": "espaga longa"
        }
    
    def demonio():
        atributos = randint(0, 0)
        return {
            "nome": "demonio",
            "nível": atributos,
            "ataque": 0 * atributos,
            "velocidade": 0 * atributos,
            "defesa": 0 * atributos,
            "vida": 0 * atributos,
            "arma": "manopola"
        }
    
    def besta_de_gelo():
        atributos = randint(0, 0)
        return {
            "nome": "besta de gelo",
            "nível": atributos,
            "ataque": 0 * atributos,
            "velocidade": 0 * atributos,
            "defesa": 0 * atributos,
            "vida": 0 * atributos,
            "arma": "nehuma"
        }

    def aranha_rainha():
        atributos = randint(0, 0)
        return {
            "nome": "aranha rainha",
            "nível": atributos,
            "ataque": 0 * atributos,
            "velocidade": 0 * atributos,
            "defesa": 0 * atributos,
            "vida": 0 * atributos,
            "arma": "nenhuma"
        }

    def lobo_alfa():
        atributos = randint(0, 0)
        return {
            "nome": "lobo alfa",
            "nível": atributos,
            "ataque": 0 * atributos,
            "velocidade": 0 * atributos,
            "defesa": 0 * atributos,
            "vida": 0 * atributos,
            "arma": "nenhuma"
        }

    def goblin_assassino():
        atributos = randint(0, 0)
        return {
            "nome": "goblin assassino",
            "nível": atributos,
            "ataque": 0 * atributos,
            "velocidade": 0 * atributos,
            "defesa": 0 * atributos,
            "vida": 0 * atributos,
            "arma": "cutelo duplo"
        }

    def esqueleto_cavalero():
        atributos = randint(0, 0)
        return {
            "nome": "esqueleto cavaleiro",
            "nível": atributos,
            "ataque": 0 * atributos,
            "velocidade": 0 * atributos,
            "defesa": 0 * atributos,
            "vida": 0 * atributos,
            "arma": "espaga longa"
        }

    def gigante_da_montanha():
        atributos = randint(0, 0)
        return {
            "nome": "gigante da montanha",
            "nível": atributos,
            "ataque": 0 * atributos,
            "velocidade": 0 * atributos,
            "defesa": 0 * atributos,
            "vida": 0 * atributos,
            "arma": "lança"
        }

    def esqueleto_negro():
        atributos = randint(0, 0)
        return {
            "nome": "esqueleto negro",
            "nível": atributos,
            "ataque": 0 * atributos,
            "velocidade": 0 * atributos,
            "defesa": 0 * atributos,
            "vida": 0 * atributos,
            "arma": "espaga longa"
        }

    def serpente_gigante():
        atributos = randint(0, 0)
        return {
            "nome": "serpente gigante",
            "nível": atributos,
            "ataque": 0 * atributos,
            "velocidade": 0 * atributos,
            "defesa": 0 * atributos,
            "vida": 0 * atributos,
            "arma": "nenhuma"
        }

def montros_lendario():

    def colosso_cego():
        atributos = randint(0, 0)
        return {
            "nome": "colosso cego",
            "nível": atributos,
            "ataque": 0 * atributos,
            "velocidade": 0 * atributos,
            "defesa": 0 * atributos,
            "vida": 0 * atributos,
            "arma": "manopola   "
        }
    
    def rei_carniceiro():
        atributos = randint(0, 0)
        return {
            "nome": "rei carniceiro",
            "nível": atributos,
            "ataque": 0 * atributos,
            "velocidade": 0 * atributos,
            "defesa": 0 * atributos,
            "vida": 0 * atributos,
            "arma": "espada dupla"
        }

    def maquina_de_guerra():
        atributos = randint(0, 0)
        return {
            "nome": "maquina de guerra",
            "nível": atributos,
            "ataque": 0 * atributos,
            "velocidade": 0 * atributos,
            "defesa": 0 * atributos,
            "vida": 0 * atributos,
            "arma": "nenhuma"
        }

def chefe_final():

    def rei_tirano():
        atributos = 666
        return {
            "nome": "rei tirano",
            "nível": atributos,
            "ataque": 0 * atributos,
            "velocidade": 0 * atributos,
            "defesa": 0 * atributos,
            "vida": 50 * atributos,
            "arma": "todas"
        }


from random import randint

class Monstro:
    def __init__(self, nome, arma, nivel_min=0, nivel_max=0, multiplicador_vida=1):
        self.nome = nome
        self.nivel = randint(nivel_min, nivel_max)
        self.ataque = 1 * self.nivel
        self.velocidade = 1 * self.nivel
        self.defesa = 1 * self.nivel
        self.vida = multiplicador_vida * self.nivel
        self.arma = arma

    def __repr__(self):
        return f"{self.nome.title()} (Nv {self.nivel}) - Arma: {self.arma}"

# Exemplos de subclasses por raridade
class Goblin(Monstro):
    def __init__(self):
        super().__init__("goblin", "adaga", 1, 5)

class Esqueleto(Monstro):
    def __init__(self):
        super().__init__("esqueleto", "espada básica", 5, 10)

class CãoSelvagem(Monstro):
    def __init__(self):
        super().__init__("cão selvagem", "nenhuma", 3, 8)

class Orc(Monstro):
    def __init__(self):
        super().__init__("orc", "lábris", 10, 15)

class EsqueletoNegro(Monstro):
    def __init__(self):
        super().__init__("esqueleto negro", "espada longa", 20, 25)

class ReiTirano(Monstro):
    def __init__(self):
        super().__init__("rei tirano", "todas", 666, 666, multiplicador_vida=50)

# Exemplo de uso:
monstros = [
    Goblin(),
    Esqueleto(),
    CãoSelvagem(),
    Orc(),
    EsqueletoNegro(),
    ReiTirano()
]

for monstro in monstros:
    print(monstro)
