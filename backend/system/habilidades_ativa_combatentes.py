#  backend\system\habilidades_ativa_combatentes.py
from dataclasses import dataclass, field
from random import uniform, randint
from typing import Callable, Optional, Any
import math, time, threading

@dataclass
class HabilidadeAtiva:
    name: str
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
            f"name: {self.name}\n"
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

    def iniciar_cooldown(self):
        self.tempo_de_recarga_restante = self.tempo_de_recarga

#  ASSASSINO
class GolpeMortal(HabilidadeAtiva):
    def __init__(self, range_pixel=100):
        super().__init__(
            name = "Golpe Mortal",
            efeito = self.efeito_golpe_mortal,
            tempo_de_recarga = 1,
            nivel_minimo = 1,
            duração = 1
        )
        self.descrição_do_efeito = (
            "Causa dano massivo a um único alvo próximo. "
            "Desativa após acertar ou expirar o tempo."
        )
        self.atualizar_descrição()
        self.range_pixel = range_pixel
        self.usuario = None
        self.alvo = None
        self.tempo_ativação = None
        self.ativa = False

    def ativar(self, usuario, alvo):
        self.usuario = usuario
        self.alvo = alvo
        self.tempo_ativação = time.time()
        self.ativa = True

    def esta_no_range(self):
        direção_x = self.usuario.posição_x - self.alvo.posição_x
        direção_y = self.usuario.posição_y - self.alvo.posição_y
        distancia = math.sqrt(direção_x*direção_x + direção_y*direção_y)
        return distancia <= self.range_pixel

    def atualizar(self):
        if not self.ativa:
            return

        tempo_passado = time.time() - self.tempo_ativação
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
    def __init__(self):
        super().__init__(
            name="Intangibilidade",
            tempo_de_recarga=1,
            nivel_minimo=1,
            duração=1
        )
        self.descrição_do_efeito = (
            "Torna o usuário intangível, evitando todos os danos por um curto período."
        )
        self.atualizar_descrição()
        self.usuario = None
        self.tempo_ativação = None
        self.ativa = False

    def ativar(self, usuario):
        self.usuario = usuario
        self.tempo_ativação = time.time()
        self.ativa = True
        self.usuario.estado = "intangivel"

    def atualizar(self):
        if not self.ativa:
            return

        tempo_passado = time.time() - self.tempo_ativação
        if tempo_passado > self.duração:
            self.ativa = False
            self.usuario.estado = "normal"
# ESPADACHIN
class ImpactoCruzado(HabilidadeAtiva):
    def __init__(self, range_pixel=100):
        super().__init__(
            name="Impacto Cruzado",
            efeito=self.efeito_impacto_cruzado,
            tempo_de_recarga=1,
            nivel_minimo=1,
            duração=1
        )
        self.descrição_do_efeito = (
            "Causa dano dobrado a um alvo próximo."
        )
        self.atualizar_descrição()
        self.usuario = None
        self.alvo = None
        self.range_pixel = range_pixel
        self.tempo_ativação = None
        self.ativa = False

    def ativar(self, usuario, alvo):
        self.usuario = usuario
        self.alvo = alvo
        self.tempo_ativação = time.time()
        self.ativa = True

    def esta_no_range(self):
        direção_x = self.usuario.posição_x - self.alvo.posição_x
        direção_y = self.usuario.posição_y - self.alvo.posição_y
        distancia = math.sqrt(direção_x*direção_x + direção_y*direção_y)
        return distancia <= self.range_pixel

    def atualizar(self):
        if not self.ativa:
            return

        tempo_passado = time.time() - self.tempo_ativação
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
    def __init__(self):
        super().__init__(
            name="Bloqueio de Espada",
            efeito=self.efeito_bloqueio_de_espada,
            tempo_de_recarga=1,
            nivel_minimo=1,
            duração=1
        )
        self.descrição_do_efeito = (
            "Bloqueia ataques recebidos por um curto período."
        )
        self.atualizar_descrição()
        self.alvo = None
        self.tempo_ativação = None
        self.ativa = False

    def ativar(self, alvo):
        self.alvo = alvo
        self.tempo_ativação = time.time()
        self.ativa = True
        self.alvo.bloqueio_ativo = True

    def atualizar(self):
        if not self.ativa:
            return
        tempo_passado = time.time() - self.tempo_ativação
        if tempo_passado > self.duração:
            self.ativa = False
            self.alvo.bloqueio_ativo = False

    def efeito_bloqueio_de_espada(self, alvo):
        pass

# ESCUDEIRO
class AtaqueComEscudo(HabilidadeAtiva):
    def __init__(self):
        super().__init__(
            name="Ataque com Escudo",
            efeito=self.efeito_ataque_com_escudo,
            tempo_de_recarga=1,
            nivel_minimo=1,
            duração=1
        )
        self.descrição_do_efeito = (
            "Permite atacar com o escudo, causando dano baseado na defesa."
        )
        self.atualizar_descrição()
        self.usuario = None
        self.alvo = None
        self.tempo_ativação = None
        self.ativa = False

    def ativar(self, usuario, alvo):
        self.usuario = usuario
        self.alvo = alvo
        self.tempo_ativação = time.time()
        self.ativa = True
        self.usuario.pode_atacar = True

    def atualizar(self):
        if not self.ativa:
            return

        tempo_passado = time.time() - self.tempo_ativação
        if tempo_passado > self.duração:
            self.ativa = False
            self.usuario.pode_atacar = False

    def efeito_ataque_com_escudo(self, usuario, alvo):
        if alvo:
            dano = int(max(0, (usuario.defesa_final * 2) - (alvo.defesa_final * 0.75)))
            alvo.vida -= dano

class DefesaReforçada(HabilidadeAtiva):
    def __init__(self, raio, duração=5):
        super().__init__(
            name="Defesa Reforçada",
            efeito=self.efeito_defesa_reforcada,
            tempo_de_recarga=1,
            nivel_minimo=1,
            duração=duração
        )
        self.descrição_do_efeito = (
            f"Aumenta a defesa dos aliados dentro de um raio de {raio} por {duração} segundos."
        )
        self.atualizar_descrição()
        self.usuario = None
        self.centro_x = None
        self.centro_y = None
        self.raio = raio
        self.tempo_ativação = None
        self.ativa = False
        self.personagens_no_campo = set()

    def ativar(self, usuario, centro_x, centro_y):
        self.usuario = usuario
        self.centro_x = centro_x
        self.centro_y = centro_y
        self.tempo_ativação = time.time()
        self.ativa = True

    def esta_dentro_campo(self, personagem):
        direção_x = personagem.posição_x - self.centro_x
        direção_y = personagem.posição_y - self.centro_y
        distancia = math.sqrt(direção_x*direção_x + direção_y*direção_y)
        return distancia <= self.raio

    def atualizar(self, personagens): 
        if not self.ativa:
            return

        tempo_passado = time.time() - self.tempo_ativação
        if tempo_passado > self.duração:
            self.ativa = False
            for personagem in self.personagens_no_campo:
                personagem.defesa_bonus -= int(personagem.defesa_base * 1.1)
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
    def __init__(self, raio=100, duração=3):
        super().__init__(
            name="Giro de Lança",
            efeito=self.efeito_giro_de_lanca,
            tempo_de_recarga=1,
            nivel_minimo=1,
            duração=duração
        )
        self.descrição_do_efeito = (
            f"Causa dano em área girando a lança, atingindo inimigos em um raio de {raio}."
        )
        self.atualizar_descrição()
        self.usuario = None
        self.alvos = []
        self.raio = raio
        self.tempo_ativação = None
        self.ativa = False

    def ativar(self, usuario, alvos):
        self.usuario = usuario
        self.alvos = alvos
        self.tempo_ativação = time.time()
        self.ativa = True
        self.usuario.pode_mover = False

    def esta_dentro_area(self, inimigo):
        direção_x = inimigo.posição_x - self.usuario.posição_x
        direção_y = inimigo.posição_y - self.usuario.posição_y
        distancia = math.sqrt(direção_x*direção_x + direção_y*direção_y)
        return distancia <= self.raio

    def atualizar(self):
        if not self.ativa:
            return

        tempo_passado = time.time() - self.tempo_ativação
        if tempo_passado > self.duração:
            self.ativa = False
            self.usuario.pode_mover = True
            self.iniciar_cooldown()
            return

        for inimigo in self.alvos:
            if self.esta_dentro_area(inimigo):
                dano = int(max(0, (self.usuario.dano_final * 4) - (inimigo.defesa_final * uniform(0.5, 0.75))))
                inimigo.vida -= dano

class LancaArremessada:
    def __init__(self, usuario, direção, alcance_maximo, dano_inicial, redução_por_inimigo, duração_maxima):
        self.usuario = usuario
        self.posição_x = usuario.posição_x
        self.posição_y = usuario.posição_y
        self.dano = dano_inicial
        self.redução_por_inimigo = redução_por_inimigo
        self.direção = direção
        self.alcance_maximo = alcance_maximo
        self.velocidade = 15  
        self.distancia_percorrida = 0
        self.tempo_ativação = time.time()
        self.duração_maxima = duração_maxima
        self.ativa = True
        self.colidiu = False

    def mover(self):
        if not self.ativa:
            return

        direção_x = self.direção[0] * self.velocidade
        direção_y = self.direção[1] * self.velocidade

        self.posição_x += direção_x
        self.posição_y += direção_y

        self.distancia_percorrida += math.sqrt(direção_x*direção_x + direção_y*direção_y)

        if self.distancia_percorrida >= self.alcance_maximo or (time.time() - self.tempo_ativação) > self.duração_maxima:
            self.retornar()

    def verificar_colisao(self, inimigos, obstaculos):
        if not self.ativa:
            return

        for obstaculo in obstaculos:
            if self.colidiu_com(obstaculo):
                self.colidiu = True
                self.retornar()
                return

        for inimigo in inimigos:
            if self.colidiu_com(inimigo):
                inimigo.vida -= int(max(0, self.dano - inimigo.defesa_final * 0.9))
                self.dano *= (1 - self.redução_por_inimigo) 
                if self.dano <= 0:
                    self.retornar()
                    return

    def colidiu_com(self, objeto):
        direção_x = self.posição_x - objeto.posição_x
        direção_y = self.posição_y - objeto.posição_y
        distancia = math.sqrt(direção_x*direção_x + direção_y*direção_y)
        return distancia < (objeto.raio + 5)

    def retornar(self):
        self.ativa = False

class ArremessoDeLanca(HabilidadeAtiva):
    def __init__(self):
        super().__init__(
            name="Arremesso de Lança",
            efeito=self.efeito_arremesso_de_lanca,
            tempo_de_recarga=1,
            nivel_minimo=1,
            duração=5
        )
        self.descrição_do_efeito = (
            "Arremessa uma lança que atravessa inimigos e obstáculos, causando dano reduzido a cada acerto."
        )
        self.atualizar_descrição()
        self.usuario = None
        self.lanca = None
        self.inimigos = []
        self.obstaculos = []

    def ativar(self, usuario, direção, inimigos, obstaculos):
        self.usuario = usuario
        dano_inicial = self.usuario.dano_final * 2 
        redução_por_inimigo = 0.2  
        alcance_maximo = 300
        duração_maxima = self.duração

        self.lanca = LancaArremessada(self.usuario, direção, alcance_maximo, dano_inicial, redução_por_inimigo, duração_maxima)
        self.ativa = True
        self.inimigos = inimigos
        self.obstaculos = obstaculos
        self.tempo_ativação = time.time()

    def atualizar(self):
        if not self.ativa or self.lanca is None:
            return

        self.lanca.mover()
        self.lanca.verificar_colisao(self.inimigos, self.obstaculos)

        if not self.lanca.ativa:
            self.ativa = False
            self.iniciar_cooldown()
# ARQUEIRO
class ProjétilPerfurante:
    def __init__(self, usuario, direção, alcance_maximo, inimigos, obstaculos):
        self.usuario = usuario
        self.posição_x = usuario.posição_x
        self.posição_y = usuario.posição_y
        self.direção = direção  
        self.velocidade = 20  
        self.alcance_max = alcance_maximo
        self.distancia_percorrida = 0
        self.ativa = True
        self.inimigos = inimigos
        self.obstaculos = obstaculos

    def mover(self):
        if not self.ativa:
            return

        direção_x = self.direção[0] * self.velocidade
        direção_y = self.direção[1] * self.velocidade
        self.posição_x += direção_x
        self.posição_y += direção_y
        self.distancia_percorrida += math.sqrt(direção_x*direção_x + direção_y*direção_y)

        if self.distancia_percorrida >= self.alcance_max:
            self.ativa = False

    def verificar_colisao(self):
        if not self.ativa:
            return

        for obstaculo in self.obstaculos:
            if self.colidiu_com(obstaculo):
                self.ativa = False
                return

        for inimigo in self.inimigos:
            if self.colidiu_com(inimigo):
                inimigo.vida_atual *= 0.1 

    def colidiu_com(self, obj):
        direção_x = self.posição_x - obj.posição_x
        direção_y = self.posição_y - obj.posição_y
        distancia = math.sqrt(direção_x*direção_x + direção_y*direção_y)
        return distancia < (obj.raio + 5) 

class DisparoPerfurante(HabilidadeAtiva):
    def __init__(self, alcance=400):
        super().__init__(
            name="Disparo Perfurante",
            efeito=self.efeito_disparo_perfurante,
            tempo_de_recarga=5,
            nivel_minimo=1,
            duração=10 
        )
        self.descrição_do_efeito = (
            f"Dispara uma flecha que perfura inimigos em linha reta até {alcance} de alcance."
        )
        self.atualizar_descrição()
        self.usuario = None
        self.inimigos = []
        self.obstaculos = []
        self.alcance = alcance
        self.disparo_ativo = False
        self.projetil = None
        self.tempo_de_ativação = None

    def ativar(self, usuario, inimigos, obstaculos):
        self.usuario = usuario
        self.inimigos = inimigos
        self.obstaculos = obstaculos
        self.disparo_ativo = True
        self.tempo_de_ativação = time.time()

    def atacar(self, direção):
        if not self.disparo_ativo:
            return False

        self.projetil = ProjétilPerfurante(self.usuario, direção, self.alcance, self.inimigos, self.obstaculos)
        self.disparo_ativo = False
        return True

    def atualizar(self):
        if self.projetil and self.projetil.ativa:
            self.projetil.mover()
            self.projetil.verificar_colisao()
        else:
            self.projetil = None

        if self.disparo_ativo and (time.time() - self.tempo_de_ativação) > self.duração:
            self.disparo_ativo = False

class Camuflagem(HabilidadeAtiva):
    def __init__(self):
        super().__init__(
            name="Camuflagem",
            efeito=self.efeito_camuflagem,
            tempo_de_recarga=5, 
            nivel_minimo=1,
            duração=10 
        )
        self.descrição_do_efeito = (
            "Torna o usuário invisível por um tempo limitado."
        )
        self.atualizar_descrição()
        self.timer = None

    def ativar(self, usuario):
        self.efeito_camuflagem(usuario)

# BATEDOR
class AtaqueSurpresa(HabilidadeAtiva):
    def __init__(self):
        super().__init__(
            name="Ataque Surpresa",
            efeito=self.efeito_ataque_surpresa,
            tempo_de_recarga=5,
            nivel_minimo=1,
            duração=1
        )
        self.descrição_do_efeito = (
            "Ataca um alvo desprevenido, causando dano extra."
        )
        self.atualizar_descrição()

    def ativar(self, usuario, alvo):
        self.efeito_ataque_surpresa(usuario, alvo)

class FugaRapida(HabilidadeAtiva):
    def __init__(self):
        super().__init__(
            name="Fuga Rápida",
            efeito=self.efeito_fuga_rapida,
            tempo_de_recarga=5,
            nivel_minimo=1,
            duração=1
        )
        self.descrição_do_efeito = (
            "Permite escapar rapidamente de inimigos próximos."
        )
        self.atualizar_descrição()

    def ativar(self, usuario, inimigos):
        self.efeito_fuga_rapida(usuario, inimigos)

# ANDARILHO
class PassoFantasma(HabilidadeAtiva):
    def __init__(self, distancia=150):
        super().__init__(
            name="Passo Fantasma",
            efeito=self.efeito_passo_fantasma,
            tempo_de_recarga=5,
            nivel_minimo=1,
            duração=0.5
        )
        self.descrição_do_efeito = (
            f"Move rapidamente o usuário na direção escolhida, atravessando obstáculos por {distancia} unidades."
        )
        self.atualizar_descrição()
        self.usuario = None
        self.distancia = distancia
        self.tempo_ativação = None
        self.ativa = False
        self.direcao = (0, 0)

    def ativar(self, usuario, direcao):
        self.usuario = usuario
        self.direcao = direcao
        self.tempo_ativação = time.time()
        self.ativa = True
        self.usuario.estado = "intangivel"

    def atualizar(self):
        if not self.ativa:
            return

        self.usuario.posição_x += self.direcao[0] * self.distancia
        self.usuario.posição_y += self.direcao[1] * self.distancia

        if (time.time() - self.tempo_ativação) > self.duração:
            self.usuario.estado = "normal"
            self.ativa = False
            self.iniciar_cooldown()

    def efeito_passo_fantasma(self, usuario):
        pass

class Areia(HabilidadeAtiva):
    def __init__(self, duração_efeito=3):
        super().__init__(
            name="Areia nos Olhos",
            efeito=self.efeito_areia_nos_olhos,
            tempo_de_recarga=6,
            nivel_minimo=1,
            duração=1
        )
        self.descrição_do_efeito = (
            f"Cega o alvo, reduzindo sua precisão por {duração_efeito} segundos."
        )
        self.atualizar_descrição()
        self.duração_efeito = duração_efeito

    def ativar(self, usuario, alvo):
        self.efeito_areia_nos_olhos(usuario, alvo)

# ARTISTA MARCIAL
class ComboRelampago(HabilidadeAtiva):
    def __init__(self):
        super().__init__(
            name="Combo Relâmpago",
            efeito=self.efeito_combo_relampago,
            tempo_de_recarga=8,
            nivel_minimo=1,
            duração=1
        )
        self.descrição_do_efeito = (
            "Executa uma sequência rápida de ataques contra um alvo."
        )
        self.atualizar_descrição()

    def ativar(self, usuario, alvo):
        self.efeito_combo_relampago(usuario, alvo)

class PosturaDeFerro(HabilidadeAtiva):
    def __init__(self, duração_efeito=5):
        super().__init__(
            name="Postura de Ferro",
            efeito=self.efeito_postura_de_ferro,
            tempo_de_recarga=12,
            nivel_minimo=1,
            duração=1
        )
        self.descrição_do_efeito = (
            f"Aumenta drasticamente a defesa do usuário por {duração_efeito} segundos."
        )
        self.atualizar_descrição()

    def ativar(self, usuario):
        self.efeito_postura_de_ferro(usuario)
