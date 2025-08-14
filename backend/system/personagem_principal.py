# backend\app\models\personagens\personagem_principal.py
from dataclasses import field, dataclass
from typing import Any

class Usuario:
    def __init__(self, nome):
        # DADOS PESSOAIS
        self.nome = nome
        self.idade = 17
        self.peso = 80
        self.genero = "feminino"
        self.altura = 1.76
        # TENTATIVAS
        self.tentativas_restantes = 3
        self.tentativas = 3
        # NÍVEL
        self.nível_atual = 1
        self.nível_máximo = 100
        #  EXPERIÊNCIA
        self.experiência_atual = 0
        self.experiência_máxima = 100
        # ATRIBUTOS
        self.dano_base = 0
        self.velocidade_base = 0
        self.defesa_base = 0
        self.vida_base = 0
        self.estamina_base = 0
        self.multiplicador_de_experiência = 1.0
        # ESTADO
        self.estado = "normal"
        # CLASSE 
        self.nome_da_classe_do_usuário = "nenhuma"
        self.classe_do_usuário = None
        # ATRIBUTOS
        self.vida_atual = 0
        self.vida_máxima = 0
        self.estamina_atual = 0
        self.estamina_máxima = 0
        # ARMADURA
        self.elmo = "nenhum"
        self.peitoral= "nenhum"
        self.calça = "nenhuma"
        self.botas = "nenhuma"
        # DESCRIÇÃO
        self.descrição = "nenhuma"
        # HABLIDIDADES
        self.primeira_habilidade_passiva = None
        self.segunda_habilidade_passiva = None
        self.terceira_habilidade_passiva = None
        self.habilidade_ativa = None
        self.habilidade_especial = None
        # --------------------------------------------
        self.nome_da_primeira_habilidade_passiva = str
        self.nome_da_segunda_habilidade_passiva = str
        self.nome_da_terceira_habilidade_passiva = str
        self.nome_da_habilidade_ativa = str
        self.nome_da_habilidade_especial = str
        # ITENS
        self.arma = "nenhuma"
        self.escudo = "nenhum"
        # BONUS DE ATRIBUTOS
        self.dano_bonus = 0
        self.velocidade_bonus = 0
        self.defesa_bonus = 0
        self.vida_bonus = 0
        self.estamina_bonus = 0
        # DEFINIÇÕES
        self.vida_máxima = self.vida_base
        self.vida_atual = self.vida_máxima
        self.estamina_máxima = self.estamina_base
        self.estamina_atual = self.estamina_máxima
        # ATRIBUTOS DE POSICIONAMENTO E COMBATE
        self.posição_x = 0
        self.posição_y = 0
        self.pode_atacar = True
        self.pode_mover = True
        self.bloqueio_ativo = False
        self.precisao_bonus = 0
        self.critico_bonus = 0
        self.resistencia_empurrao = False
    def __post_init__(self):
        # ATUALIZAÇÕES
        self.atualizar_atributos()
        self.atualizar_descrição()

    @property
    def dano_final(self):
        return self.dano_base + self.dano_bonus

    @property
    def velocidade_final(self):
        return self.velocidade_base + self.velocidade_bonus

    @property
    def defesa_final(self):
        return self.defesa_base + self.defesa_bonus
    
    @property
    def vida_final(self):
        return self.vida_base + self.vida_bonus
    
    @property
    def estamina_final(self):
        return self.estamina_base + self.estamina_bonus

    def definir_classe(self, classe):
        self.nome_da_classe_do_usuário = classe.nome
        self.classe_do_usuário = classe
        self.dano_base = classe.dano_base
        self.velocidade_base = classe.velocidade_base
        self.defesa_base = classe.defesa_base
        self.vida_base = classe.vida_base
        self.estamina_base = classe.estamina_base
        self.multiplicador_de_experiência = classe.multiplicador_de_experiência
        self.arma = classe.arma
        self.atualizar_status_com_bonus()

    def definir_habilidades(self):
        self.nome_da_primeira_habilidade_passiva = self.classe_do_usuário.primeira_habilidade_passiva.nome
        self.nome_da_segunda_habilidade_passiva = self.classe_do_usuário.segunda_habilidade_passiva.nome
        self.nome_da_terceira_habilidade_passiva = self.classe_do_usuário.terceira_habilidade_passiva.nome
        self.nome_da_habilidade_ativa = self.classe_do_usuário.habilidade_ativa.nome
        self.nome_da_habilidade_especial = self.classe_do_usuário.habilidade_especial.nome
        # ---------------------------------------------------------------------
        self.primeira_habilidade_passiva = self.classe_do_usuário.primeira_habilidade_passiva
        self.segunda_habilidade_passiva = self.classe_do_usuário.segunda_habilidade_passiva
        self.terceira_habilidade_passiva = self.classe_do_usuário.terceira_habilidade_passiva
        self.habilidade_ativa = self.classe_do_usuário.habilidade_ativa
        self.habilidade_especial = self.classe_do_usuário.habilidade_especial

    def atualizar_status_com_bonus(self):
        self.vida_máxima = self.vida_final
        self.estamina_máxima = self.estamina_final
        self.vida_atual = self.vida_máxima
        self.estamina_atual = self.estamina_máxima

    def equipar_arma(self, arma):
        self.arma = arma.nome
        self.dano_bonus = arma.dano if arma else 0
        self.velocidade_bonus = arma.velocidade if arma else 0

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

    def receber_experiencia(self, experiência: int):
        experiência *= self.multiplicador_de_experiência

        self.experiência_atual += experiência
        while self.experiência_atual >= self.experiência_máxima and self.nível_atual < self.nível_máximo:
            self.experiência_atual -= self.experiência_máxima
            self.subir_nivel()
    
    def atualizar_experiencia_maxima(self):
        multiplicador = 1.0
        if self.nível_atual <= 25:
            multiplicador = 1.25
        elif self.nível_atual <= 50:
            multiplicador = 1.5
        elif self.nível_atual <= 75:
            multiplicador = 1.75
        else:
            multiplicador = 2.0
        
        self.experiência_máxima = int(self.experiência_máxima * multiplicador)

    def subir_nivel(self):
        if self.nível_atual < self.nível_máximo:
            self.nível_atual += 1
            self.dano_base += 1
            self.velocidade_base += 1
            self.defesa_base += 1
            self.vida_base += 10
            self.estamina_base += 10
            self.vida_máxima = self.vida_base
            self.vida_atual = self.vida_máxima
            self.estamina_máxima = self.estamina_base
            self.estamina_atual = self.estamina_máxima
            self.atualizar_experiencia_maxima()
            self.atualizar_atributos()

    def atualizar_atributos(self) -> None:
        self.dano_base *= self.nível_atual
        self.velocidade_base *= self.nível_atual
        self.defesa_base *= self.nível_atual
        self.vida_máxima *= self.nível_atual
        self.vida_atual = self.vida_máxima
        self.estamina_máxima *= self.nível_atual
        self.estamina_atual = self.estamina_máxima

    def diminuir_tentativas(self) -> None:
        if self.vida_atual <= 0:
            self.tentativas_restantes -= 1
            self.vida_atual = self.vida_máxima
            print("você perdeu uma tentativa!")

        if self.tentativas_restantes == 0:
            raise SystemExit("suas tentativas acabaram, você perdeu o jogo")

    def atacar(self, alvo):
        if alvo.defesa_final >= self.dano_final:
            dano = 0
        else:
            dano = int(self.dano_final - alvo.defesa_final)
            alvo.vida_atual -= dano

    def atualizar_descrição(self) -> None:
        self.descrição = (f"nome: {self.nome}\n"
                          f"idade: {self.idade}\n"
                          f"peso: {self.peso}Kg\n"
                          f"genero: {self.genero}\n"
                          f"altura: {self.altura}m\n"
                          f"experiência: {self.experiência_atual}/{self.experiência_máxima}\n"
                          f"multiplicador de experiência: {self.multiplicador_de_experiência}\n"
                          f"nível: {self.nível_atual}/{self.nível_máximo}\n"
                          f"dano: {self.dano_final}\n"
                          f"velocidade: {self.velocidade_final}\n"
                          f"defesa: {self.defesa_final}\n"
                          f"vida: {self.vida_atual}/{self.vida_máxima}\n"
                          f"estamina: {self.estamina_atual}/{self.estamina_máxima}\n"
                          f"estado: {self.estado}\n"
                          f"arma: {self.arma}\n"
                          f"escudo: {self.escudo}\n"
                          f"tentativas: {self.tentativas_restantes}\n"
                          f"classe: {self.nome_da_classe_do_usuário}\n"
                          f"primeira habilidade passiva: {self.nome_da_primeira_habilidade_passiva}\n"
                          f"segunda habilidade passiva: {self.nome_da_segunda_habilidade_passiva}\n"
                          f"terceira habilidade passiva: {self.nome_da_terceira_habilidade_passiva}\n"
                          f"habilidade especial: {self.nome_da_habilidade_especial}\n"
                          f"habilidade ativa: {self.nome_da_habilidade_ativa}\n")