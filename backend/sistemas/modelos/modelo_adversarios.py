# backend\sistemas\modelos\modelo_adversarios.py
from random import randint

class AdversarioDemiHumano:
    def __init__(self, nome, nível, experiência, queda, taxa_de_queda):
        
        # DADOS PESSOAIS
        self.nome = nome

        # NÍVEL
        self.nível_atual = nível

        # EXPERIÊNCIA QUEDADA
        self.experiência = experiência

        # QUEDA
        self.queda = queda
        self.taxa_de_queda = taxa_de_queda

        # ATRIBUTOS BASE
        self.dano_base = 0
        self.velocidade_base = 0
        self.defesa_base = 0
        self.vida_base = 0
        self.estamina_base = 0

        # ATRIBUTOS
        self.vida_atual = 0
        self.vida_máxima = 0
        self.estamina_atual = 0
        self.estamina_máxima = 0

        # BONUS DE ATRIBUTOS
        self.dano_bonus = 0
        self.velocidade_bonus = 0
        self.defesa_bonus = 0
        self.vida_bonus = 0
        self.estamina_bonus = 0

        # ARMA
        self.nome_da_arma = "nenhuma"
        self.arma = None

        # ESCUDO
        self.nome_do_escudo = "nenhum"
        self.escudo = None

        # CLASSE
        self.nome_da_classe = "nenhuma"
        self.classe = None

        # HABILIDADES
        self.primeira_habilidade_passiva = None
        self.segunda_habilidade_passiva = None
        self.terceira_habilidade_passiva = None
        self.habilidade_ativa = None
        self.habilidade_especial = None

        self.nome_da_primeira_habilidade_passiva = "nenhuma"
        self.nome_da_segunda_habilidade_passiva = "nenhuma"
        self.nome_da_terceira_habilidade_passiva = "nenhuma"
        self.nome_da_habilidade_ativa = "nenhuma"
        self.nome_da_habilidade_especial = "nenhuma"

        # ARMADURA
        self.elmo = None
        self.peitoral = None
        self.calça = None
        self.botas = None

        self.nome_do_elmo = "nenhum"
        self.nome_do_peitoral = "nenhum"
        self.nome_da_calça = "nenhuma"
        self.nome_das_botas = "nenhuma"

        # DESCRÇÃO
        self.descrição = "nenhuma"

        # ATRIBUTOS DE POSICIONAMENTO E COMBATE
        self.posição_x = 0
        self.posição_y = 0

        self.estado = "normal"

        self.pode_atacar = True
        self.pode_mover = True
        self.bloqueio_ativo = False
        self.precisao_bonus = 0
        self.critico_bonus = 0
        self.resistencia_empurrao = False
        self.multiplicador_de_experiência = 0

    def post_init(self):
        self.atualizar_atributos()
        self.atualizar_descrição()

    def tentar_queda_de_itens(self):
        tentativa = randint(0, 100)
        if tentativa >= self.taxa_de_queda:
            return self.queda
        else:
            return None

    def definir_classe(self, classe):
        self.nome_da_classe = classe.nome
        self.classe = classe
        self.dano_base = classe.dano_base
        self.velocidade_base = classe.velocidade_base
        self.defesa_base = classe.defesa_base
        self.vida_base = classe.vida_base
        self.estamina_base = classe.estamina_base
        self.atualizar_atributos()

    def definir_habilidades(self):
        self.nome_da_primeira_habilidade_passiva = self.classe.primeira_habilidade_passiva.nome
        self.nome_da_segunda_habilidade_passiva = self.classe.segunda_habilidade_passiva.nome
        self.nome_da_terceira_habilidade_passiva = self.classe.terceira_habilidade_passiva.nome
        self.nome_da_habilidade_ativa = self.classe.habilidade_ativa.nome
        self.nome_da_habilidade_especial = self.classe.habilidade_especial.nome

        self.primeira_habilidade_passiva = self.classe.primeira_habilidade_passiva
        self.segunda_habilidade_passiva = self.classe.segunda_habilidade_passiva
        self.terceira_habilidade_passiva = self.classe.terceira_habilidade_passiva
        self.habilidade_ativa = self.classe.habilidade_ativa
        self.habilidade_especial = self.classe.habilidade_especial

    def atualizar_atributos(self):
            self.vida_máxima = self.vida_base * self.nível_atual + self.vida_bonus
            self.estamina_máxima = self.estamina_base * self.nível_atual + self.estamina_bonus
            self.dano_final = self.dano_base * self.nível_atual + self.dano_bonus
            self.defesa_final = self.defesa_base * self.nível_atual + self.defesa_bonus
            self.velocidade_final = self.velocidade_base * self.nível_atual + self.velocidade_bonus
            self.vida_atual = self.vida_máxima
            self.estamina_atual = self.estamina_máxima

    def equipar_arma(self, arma):
        self.nome_da_arma = f"{arma.nome} {arma.raridade} nível {arma.nível}"
        self.arma = arma 

    def remover_arma(self):
        self.arma = None
        self.dano_bonus = 0
        self.velocidade_bonus = 0

    def equipar_escudo(self, escudo):
        self.escudo = escudo.nome 
        self.defesa_bonus = escudo.defesa_final if escudo else 0

    def remover_escudo(self):
        self.escudo = None
        self.defesa_bonus = 0


    def atacar(self, alvo):
        if alvo.defesa_final >= self.dano_final:
            dano = 0
        else:
            dano = int(self.dano_final - alvo.defesa_final)
            alvo.vida_atual -= dano

    def estar_vivo(self):
        return self.vida_atual > 0

    def atualizar_descrição(self) -> None:
        self.descrição = (
            f"nome: {self.nome}\n"
            f"nível: {self.nível_atual}\n"
            f"experiência: {self.experiência}\n"
            f"dano: {self.dano_final}\n"
            f"velocidade: {self.velocidade_final}\n"
            f"defesa: {self.defesa_final}\n"
            f"vida: {self.vida_atual}/{self.vida_máxima}\n"
            f"estamina: {self.estamina_atual}/{self.estamina_máxima}\n"
            f"arma: {self.nome_da_arma}\n"
            f"escudo: {self.nome_do_escudo}\n"
            f"elmo: {self.nome_do_elmo}\n"
            f"peitoral: {self.nome_do_peitoral}\n"
            f"calça: {self.nome_da_calça}\n"
            f"botas: {self.nome_das_botas}\n"
            f"classe: {self.nome_da_classe}\n"
            f"estado: {self.estado}\n"
            f"primeira habilidade passiva: {self.nome_da_primeira_habilidade_passiva}\n"
            f"segunda habilidade passiva: {self.nome_da_segunda_habilidade_passiva}\n"
            f"terceira habilidade passiva: {self.nome_da_terceira_habilidade_passiva}\n"
            f"habilidade ativa: {self.nome_da_habilidade_ativa}\n"
            f"habilidade especial: {self.nome_da_habilidade_especial}\n"
        )

class AdversarioMonstro:
        def __init__(self, nome, nível, experiência,
                    dano_base, defesa_base, vida_base, estamina_base,
                    velocidade_base, queda, taxa_de_queda):
            
            # DADOS PESSOAIS
            self.nome = nome

            # NÍVEL
            self.nível = nível

            # EXPERIÊNCIA QUEDADA
            self.experiência = experiência

            # QUEDA
            self.queda = queda
            self.taxa_de_queda = taxa_de_queda

            # ATRIBUTOS BASE
            self.dano_base = dano_base
            self.velocidade_base = velocidade_base
            self.defesa_base = defesa_base
            self.vida_base = vida_base
            self.estamina_base = estamina_base

            # ATRIBUTOS
            self.vida_atual = 0
            self.vida_máxima = 0
            self.estamina_atual = 0
            self.estamina_máxima = 0

            # BONUS DE ATRIBUTOS
            self.vida_bonus = 0
            self.defesa_bonus = 0
            self.dano_bonus = 0
            self.velocidade_bonus = 0
            self.estamina_bonus = 0

            # ATRIBUTOS DE POSICIONAMENTO E COMBATE
            self.posição_x = 0
            self.posição_y = 0

            self.estado = "normal"

            self.pode_atacar = True
            self.pode_mover = True
            self.bloqueio_ativo = False
            self.precisao_bonus = 0
            self.critico_bonus = 0
            self.resistencia_empurrao = False

            # DESCRÇÃO
            self.descrição = "nenhuma"

        def post_init(self):
            self.atualizar_atributos()
            self.atualizar_descrição()

        def tentar_queda_de_itens(self):
            tentativa = randint(0, 100)
            if tentativa >= self.taxa_de_queda:
                return self.queda
            else:
                return None

        def atualizar_atributos(self):
            self.vida_máxima = self.vida_base * self.nível + self.vida_bonus
            self.estamina_máxima = self.estamina_base * self.nível + self.estamina_bonus
            self.dano_final = self.dano_base * self.nível + self.dano_bonus
            self.defesa_final = self.defesa_base * self.nível + self.defesa_bonus
            self.velocidade_final = self.velocidade_base * self.nível + self.velocidade_bonus

        def atacar(self, alvo):
            if alvo.defesa_final >= self.dano_final:
                dano = 0
            else:
                dano = int(self.dano_final - alvo.defesa_final)
                alvo.vida_atual -= dano

        def estar_vivo(self):
            return self.vida_atual > 0

        def atualizar_descrição(self) -> None:
            self.descrição = (
                f"nome: {self.nome}\n"
                f"nível: {self.nível}\n"
                f"dano: {self.dano_final}\n"
                f"velocidade: {self.velocidade_final}\n"
                f"defesa: {self.defesa_final}\n"
                f"vida: {self.vida_atual}/{self.vida_máxima}\n"
                f"estamina: {self.estamina_atual}/{self.estamina_máxima}\n"
                f"estado: {self.estado}\n"
            )