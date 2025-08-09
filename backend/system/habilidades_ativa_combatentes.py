from dataclasses import dataclass, field
from random import uniform, randint
from typing import Callable, Optional, Any
import math, time

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
            f"Nome: {self.nome}\n"
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

    def atualizar_atualizar_tempo(self):
        while self.duração_restante > 0:
            self.duração_restante -= 1
        while self.tempo_de_recarga_restante > 0:
            self.tempo_de_recarga_restante -= 1

#  ASSASSINO
class GolpeMortal(HabilidadeAtiva):
    def __init__(self, usuario, alvo, range_pixel=100):
        super().__init__(
            nome = "Golpe Mortal",
            efeito = self.efeito_golpe_mortal,
            tempo_de_recarga = 1,
            nivel_minimo = 1,
            duração = 1
        )
        self.descrição_do_efeito = (
            "Causa dano massivo a um único alvo. "
            "A habilidade é desativada após o ataque acertar um alvo "
            "ou acabar o tempo."
        )
        self.atualizar_descrição()

        self.usuario = usuario
        self.alvo = alvo
        self.range_pixel = range_pixel
        
        self.tempo_ativacao = None
        self.ativa = False

    def ativar(self):
        self.tempo_ativacao = time.time()
        self.ativa = True

    def esta_no_range(self):
        distancia_x = self.usuario.posição_x - self.alvo.posição_x
        distancia_y = self.usuario.posição_y - self.alvo.posição_y
        distancia = math.sqrt(distancia_x*distancia_x + distancia_y*distancia_y)
        return distancia <= self.range_pixel

    def atualizar(self):
        if not self.ativa:
            return

        tempo_passado = time.time() - self.tempo_ativacao
        if tempo_passado > self.duração:
            self.ativa = False
            self.iniciar_cooldown()
            return

        if self.alvo and self.esta_no_range():
            self.efeito(self.usuario, self.alvo)
            self.ativa = False
            self.iniciar_cooldown()

    def efeito_golpe_mortal(self, usuario, alvo):
        dano = int(max(0, (usuario.dano_final * 3) - (alvo.defesa_final * uniform(0.6, 0.8))))
        alvo.vida -= dano


class Intangibilidade(HabilidadeAtiva):
    def __init__(self, usuario):
        super().__init__(
            nome="Intangibilidade",
            efeito=self.efeito_intangibilidade,
            tempo_de_recarga=1,
            nivel_minimo=1,
            duração=1
        )
        self.descrição_do_efeito = (
            f"O usuário se torna intangível, evitando todos os danos por {self.duração}."
        )
        self.atualizar_descrição()
        self.usuario = usuario
        self.tempo_ativacao = None
        self.ativa = False

    def ativar(self):
        self.tempo_ativacao = time.time()
        self.ativa = True
        self.usuario.estado = "intangivel"

    def atualizar(self):
        if not self.ativa:
            return

        tempo_passado = time.time() - self.tempo_ativacao
        if tempo_passado > self.duração:
            self.ativa = False
            self.usuario.estado = "normal"

    def efeito_intangibilidade(self, usuario):
        pass

# ESPADACHIN
class ImpactoCruzado(HabilidadeAtiva):
    def __init__(self, usuario, alvo, range_pixel=100):
        super().__init__(
            nome="Impacto Cruzado",
            efeito=self.efeito_impacto_cruzado,
            tempo_de_recarga=1,
            nivel_minimo=1,
            duração=1
        )
        self.usuario = usuario
        self.alvo = alvo
        self.range_pixel = range_pixel

        self.tempo_ativacao = None
        self.ativa = False

    def ativar(self):
        self.tempo_ativacao = time.time()
        self.ativa = True

    def esta_no_range(self):
        distancia_x = self.usuario.posição_x - self.alvo.posição_x
        distancia_y = self.usuario.posição_y - self.alvo.posição_y
        distancia = math.sqrt(distancia_x*distancia_x + distancia_y*distancia_y)
        return distancia <= self.range_pixel

    def atualizar(self):
        if not self.ativa:
            return

        tempo_passado = time.time() - self.tempo_ativacao
        if tempo_passado > self.duração:
            self.ativa = False
            self.iniciar_cooldown()
            return

        if self.alvo and self.esta_no_range():
            self.efeito(self.usuario, self.alvo)
            self.ativa = False
            self.iniciar_cooldown()

    def efeito_impacto_cruzado(self, usuario, alvo):
        dano = int(max(0, (usuario.dano_final * 2) - (alvo.defesa_final * 0.5)))
        alvo.vida -= dano

class BloqueioDeEspada(HabilidadeAtiva):
    def __init__(self, alvo):
        super().__init__(
            nome="Bloqueio de Espada",
            efeito=self.efeito_bloqueio_de_espada,
            tempo_de_recarga=1,
            nivel_minimo=1,
            duração=1
        )
        self.alvo = alvo
        self.tempo_ativacao = None
        self.ativa = False

    def ativar(self):
        self.tempo_ativacao = time.time()
        self.ativa = True
        self.alvo.bloqueio_ativo = True

    def atualizar(self):
        if not self.ativa:
            return
        tempo_passado = time.time() - self.tempo_ativacao
        if tempo_passado > self.duração:
            self.ativa = False
            self.alvo.bloqueio_ativo = False

    def efeito_bloqueio_de_espada(self, alvo):
        pass

# ESCUDEIRO
class AtaqueComEscudo(HabilidadeAtiva):
    def __init__(self, usuario, alvo):
        super().__init__(
            nome="Ataque com Escudo",
            efeito=self.efeito_ataque_com_escudo,
            tempo_de_recarga=1,
            nivel_minimo=1,
            duração=1
        )
        self.usuario = usuario
        self.alvo = alvo

        self.tempo_ativacao = None
        self.ativa = False

    def ativar(self):
        self.tempo_ativacao = time.time()
        self.ativa = True
        self.usuario.pode_atacar = True

    def atualizar(self):
        if not self.ativa:
            return

        tempo_passado = time.time() - self.tempo_ativacao
        if tempo_passado > self.duração:
            self.ativa = False
            self.usuario.pode_atacar = False

    def efeito_ataque_com_escudo(self, usuario, alvo):
        if alvo:
            dano = int(max(0, (usuario.defesa_final * 2) - (alvo.defesa_final * 0.75)))
            alvo.vida -= dano

class DefesaReforçada(HabilidadeAtiva):
    def __init__(self, usuario, centro_x, centro_y, raio, duração=5):
        super().__init__(
            nome="Defesa Reforçada",
            efeito=self.efeito_defesa_reforcada,
            tempo_de_recarga=1,
            nivel_minimo=1,
            duração=duração
        )
        self.usuario = usuario
        self.centro_x = centro_x
        self.centro_y = centro_y
        self.raio = raio
        self.tempo_ativacao = None
        self.ativa = False

        self.personagens_no_campo = set()

    def ativar(self):
        self.tempo_ativacao = time.time()
        self.ativa = True

    def esta_dentro_campo(self, personagem):
        dx = personagem.pos_x - self.centro_x
        dy = personagem.pos_y - self.centro_y
        distancia = math.sqrt(dx*dx + dy*dy)
        return distancia <= self.raio

    def atualizar(self, personagens): 
        if not self.ativa:
            return

        tempo_passado = time.time() - self.tempo_ativacao
        if tempo_passado > self.duração:
            self.ativa = False
            for p in self.personagens_no_campo:
                p.defesa_bonus -= int(p.defesa_base * 1.1)
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
# LANCEIRO
class GiroDeLanca(HabilidadeAtiva):
    def __init__(self):
        super().__init__(
            nome = "Giro de Lança",
            efeito = self.efeito_giro_de_lanca,
            tempo_de_recarga = 1,
            nivel_minimo = 1,
            duração = 1
        )

    def efeito_giro_de_lanca(self, usuario, alvos):
        for inimigo in alvos:
            inimigo.vida -= int(max(0, (usuario.dano_final * 4) - (inimigo.defesa_final * uniform(0.5, 0.75))))

class ArremessoDeLanca(HabilidadeAtiva):
    def __init__(self):
        super().__init__(
            nome = "Arremesso de Lança",
            efeito = self.efeito_arremesso_de_lanca,
            tempo_de_recarga = 1,
            nivel_minimo = 1,
            duração = 1
        )

    def efeito_arremesso_de_lanca(self, usuario, alvo):
        if alvo:
            alvo.vida -= int(max(0, ((usuario.dano_final) * randint(2, 3)) - (alvo.defesa_final * 0.9)))

# ARQUEIRO
class DisparoPerfurante(HabilidadeAtiva):
    def __init__(self):
        super().__init__(
            nome = "Disparo Perfurante",
            efeito = self.efeito_disparo_perfurante,
            tempo_de_recarga = 1,
            nivel_minimo = 1,
            duração = 1
        )

    def efeito_disparo_perfurante(self, alvo):
        if alvo:
            alvo.vida_atual *= 0.1

class Camuflagem(HabilidadeAtiva):
    def __init__(self):
        super().__init__(
            nome = "Camuflagem",
            efeito = self.efeito_camuflagem,
            tempo_de_recarga = 1,
            nivel_minimo = 1,
            duração = 1
        )

    def efeito_camuflagem(self, usuario):
        usuario.estado = "camuflado"

# BATEDOR
class AtaqueSurpresa(HabilidadeAtiva):
    def __init__(self):
        super().__init__(
            nome = "Ataque Surpresa",
            efeito = self.efeito_ataque_surpresa,
            tempo_de_recarga = 1,
            nivel_minimo = 1,
            duração = 1
        )

    def efeito_ataque_surpresa(self, usuario, alvo):
        if alvo:
            alvo.vida -= int(max(0, ((usuario.dano_final) * 2) - (alvo.defesa_final * 0.1)))

class FugaRapida(HabilidadeAtiva):
    def __init__(self):
        super().__init__(
            nome = "Fuga Rápida",
            efeito = self.efeito_fuga_rapida,
            tempo_de_recarga = 1,
            nivel_minimo = 1,
            duração = 1
        )

    def efeito_fuga_rapida(self, usuario, alvo):
        if alvo:
            usuario.vida -= int(max(0, (alvo.dano_final * 5) - (usuario.velocidade_final + usuario.defesa_final)))
            usuario.velocidade_bonus = int(usuario.velocidade_base + usuario.defesa_base)
            usuario.defesa_bonus = int(usuario.velocidade_base + usuario.defesa_base)

