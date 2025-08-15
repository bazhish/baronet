# backend\sistemas\modelos\adversarios.py
class AdversarioDemiHumano:
    def __init__(self, nome, idade, peso, gênero, altura, nível, experiência, dano_base, velocidade_base, defesa_base, vida_base, estamina_base):
        # DADOS PESSOAIS
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.gênero = gênero
        self.altura = altura
        # NÍVEL
        self.nível = nível
        # EXPERIÊNCIA DROPADA
        self.experiência = experiência
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
        # -------------------------------------------------
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
        # ---------------------------------
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
        # BONUS DE ATRIBUTOS
        self.dano_bonus = 0
        self.velocidade_bonus = 0
        self.defesa_bonus = 0
        self.vida_bonus = 0
        self.estamina_bonus = 0

    def __post_init__(self):
        # ATUALIZAÇÕES
        self.atributos()
        self.atualizar_descrição()

    @property
    def dano_final(self):
        return self.dano_base * self.nível + self.dano_bonus

    @property
    def velocidade_final(self):
        return self.velocidade_base * self.nível + self.velocidade_bonus

    @property
    def defesa_final(self):
        return self.defesa_base * self.nível + self.defesa_bonus

    @property
    def vida_máxima(self):
        return self.vida_máxima

    @property
    def estamina_máxima(self):
        return self.estamina_máxima
    
    def definir_classe(self, classe):
        self.nome_da_classe = classe.nome
        self.classe = classe
        self.dano_base = classe.dano_base
        self.velocidade_base = classe.velocidade_base
        self.defesa_base = classe.defesa_base
        self.vida_base = classe.vida_base
        self.estamina_base = classe.estamina_base
        self.multiplicador_de_experiência = classe.multiplicador_de_experiência
        self.atualizar_status_com_bonus()

    def definir_habilidades(self):
        self.nome_da_primeira_habilidade_passiva = self.classe.primeira_habilidade_passiva.nome
        self.nome_da_segunda_habilidade_passiva = self.classe.segunda_habilidade_passiva.nome
        self.nome_da_terceira_habilidade_passiva = self.classe.terceira_habilidade_passiva.nome
        self.nome_da_habilidade_ativa = self.classe.habilidade_ativa.nome
        self.nome_da_habilidade_especial = self.classe.habilidade_especial.nome
        # ---------------------------------------------------------------------
        self.primeira_habilidade_passiva = self.classe.primeira_habilidade_passiva
        self.segunda_habilidade_passiva = self.classe.segunda_habilidade_passiva
        self.terceira_habilidade_passiva = self.classe.terceira_habilidade_passiva
        self.habilidade_ativa = self.classe.habilidade_ativa
        self.habilidade_especial = self.classe.habilidade_especial

    def atualizar_status_com_bonus(self):
        self.vida_máxima = self.vida_final
        self.estamina_máxima = self.estamina_final
        self.vida_atual = self.vida_máxima
        self.estamina_atual = self.estamina_máxima

    def atributos(self):
        self.vida_máxima = self.vida_base * self.nível + self.vida_bonus
        self.estamina_máxima = self.estamina_base * self.nível + self.estamina_bonus

    def atualizar_status_com_bonus(self):
        self.vida_máxima = self.vida_base * self.nível + self.vida_bonus
        self.estamina_máxima = self.estamina_base * self.nível + self.estamina_bonus
        self.vida_atual = self.vida_máxima
        self.estamina_atual = self.estamina_máxima

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
            f"idade: {self.idade}\n"
            f"peso: {self.peso}Kg\n"
            f"genero: {self.gênero}\n"
            f"altura: {self.altura}m\n"
            f"nível: {self.nível}\n"
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
    def __init__(self, nome, peso, altura, nível, experiência, dano_base, defesa_base, vida_base, estamina_base, velocidade_base):
        # DADOS PESSOAIS
        self.nome = nome
        self.peso = peso
        self.altura = altura
        # NÍVEL
        self.nível = nível
        # EXPERIÊNCIA DROPADA
        self.experiência = experiência
        # ATRIBUTOS BASE
        self.dano_base = dano_base
        self.velocidade_base = velocidade_base
        self.defesa_base = defesa_base
        self.vida_base = vida_base
        self.estamina_base = estamina_base
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
        # ATRIBUTOS FINAIS
        self.vida_final = 0
        self.estamina_final = 0
        self.dano_final = 0
        self.defesa_final = 0
        self.velocidade_final = 0
        # BONUS DE ATRIBUTOS
        self.vida_atual = 0
        self.vida_máxima = 0
        self.estamina_atual = 0
        self.estamina_máxima = 0

    def __post_init__(self):
        self.atributos()
        self.atualizar_descrição()

    def atualizar_atributos(self):
        self.dano_final = self.dano_base * self.nível
        self.velocidade_final = self.velocidade_base * self.nível
        self.defesa_final = self.defesa_base * self.nível
        self.vida_final = self.vida_base * self.nível
        self.estamina_final = self.estamina_base * self.nível
        self.vida_máxima = self.vida_final
        self.vida_atual = self.vida_máxima
        self.estamina_máxima = self.estamina_final
        self.estamina_atual = self.estamina_máxima

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
            f"peso: {self.peso}Kg\n"
            f"altura: {self.altura}m\n"
            f"nível: {self.nível}\n"
            f"dano: {self.dano_final}\n"
            f"velocidade: {self.velocidade_final}\n"
            f"defesa: {self.defesa_final}\n"
            f"vida: {self.vida_atual}/{self.vida_máxima}\n"
            f"estamina: {self.estamina_atual}/{self.estamina_máxima}\n"
            f"estado: {self.estado}\n"
        )