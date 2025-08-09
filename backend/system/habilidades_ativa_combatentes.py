#  backend\system\habilidades_ativa_combatentes.py
from dataclasses import dataclass, field
from random import uniform, randint
from typing import Callable, Optional, Any
import math, time, threading

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
        
        self.tempo_ativação = None
        self.ativa = False

    def ativar(self):
        self.tempo_ativação = time.time()
        self.ativa = True

    def esta_no_range(self):
        distancia_x = self.usuario.posição_x - self.alvo.posição_x
        distancia_y = self.usuario.posição_y - self.alvo.posição_y
        distancia = math.sqrt(distancia_x*distancia_x + distancia_y*distancia_y)
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
        self.tempo_ativação = None
        self.ativa = False

    def ativar(self):
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

        self.tempo_ativação = None
        self.ativa = False

    def ativar(self):
        self.tempo_ativação = time.time()
        self.ativa = True

    def esta_no_range(self):
        distancia_x = self.usuario.posição_x - self.alvo.posição_x
        distancia_y = self.usuario.posição_y - self.alvo.posição_y
        distancia = math.sqrt(distancia_x*distancia_x + distancia_y*distancia_y)
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
    def __init__(self, alvo):
        super().__init__(
            nome="Bloqueio de Espada",
            efeito=self.efeito_bloqueio_de_espada,
            tempo_de_recarga=1,
            nivel_minimo=1,
            duração=1
        )
        self.alvo = alvo
        self.tempo_ativação = None
        self.ativa = False

    def ativar(self):
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

        self.tempo_ativação = None
        self.ativa = False

    def ativar(self):
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
        self.tempo_ativação = None
        self.ativa = False

        self.personagens_no_campo = set()

    def ativar(self):
        self.tempo_ativação = time.time()
        self.ativa = True

    def esta_dentro_campo(self, personagem):
        distancia_x = personagem.posição_x - self.centro_x
        distancia_y = personagem.posição_y - self.centro_y
        distancia = math.sqrt(distancia_x*distancia_x + distancia_y*distancia_y)
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
    def __init__(self, usuario, alvos, raio=100, duração=3):
        super().__init__(
            nome="Giro de Lança",
            efeito=self.efeito_giro_de_lanca,
            tempo_de_recarga=1,
            nivel_minimo=1,
            duração=duração
        )
        self.usuario = usuario
        self.alvos = alvos 
        self.raio = raio

        self.tempo_ativação = None
        self.ativa = False

    def ativar(self):
        self.tempo_ativação = time.time()
        self.ativa = True
        self.usuario.pode_mover = False

    def esta_dentro_area(self, inimigo):
        distancia_x = inimigo.posição_x - self.usuario.posição_x
        distancia_y = inimigo.posição_y - self.usuario.posição_y
        distancia = math.sqrt(distancia_x*distancia_x + distancia_y*distancia_y)
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

        distancia_x = self.direção[0] * self.velocidade
        distancia_y = self.direção[1] * self.velocidade

        self.posição_x += distancia_x
        self.posição_y += distancia_y

        self.distancia_percorrida += math.sqrt(distancia_x*distancia_x + distancia_y*distancia_y)

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
        distancia_x = self.posição_x - objeto.posição_x
        distancia_y = self.posição_y - objeto.posição_y
        distancia = math.sqrt(distancia_x*distancia_x + distancia_y*distancia_y)
        return distancia < (objeto.raio + 5)

    def retornar(self):
        self.ativa = False

class ArremessoDeLanca(HabilidadeAtiva):
    def __init__(self, usuario):
        super().__init__(
            nome="Arremesso de Lança",
            efeito=self.efeito_arremesso_de_lanca,
            tempo_de_recarga=1,
            nivel_minimo=1,
            duração=5
        )
        self.usuario = usuario
        self.lanca = None

    def ativar(self, direção, inimigos, obstaculos):
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
    def __init__(self, usuario, inimigos, obstaculos, alcance=400):
        super().__init__(
            nome="Disparo Perfurante",
            efeito=self.efeito_disparo_perfurante,
            tempo_de_recarga=5,
            nivel_minimo=1,
            duração=10 
        )
        self.usuario = usuario
        self.inimigos = inimigos
        self.obstaculos = obstaculos
        self.alcance = alcance

        self.disparo_ativo = False
        self.projetil = None
        self.tempo_ativacao = None

    def ativar(self):
        self.disparo_ativo = True
        self.tempo_ativacao = time.time()

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

        if self.disparo_ativo and (time.time() - self.tempo_ativacao) > self.duração:
            self.disparo_ativo = False

class Camuflagem(HabilidadeAtiva):
    def __init__(self):
        super().__init__(
            nome="Camuflagem",
            efeito=self.efeito_camuflagem,
            tempo_de_recarga=5, 
            nivel_minimo=1,
            duração=10 
        )

    def efeito_camuflagem(self, usuario):
        usuario.estado = "camuflado"

        self.agendar_desativacao(usuario)

    def agendar_desativacao(self, usuario):
        import threading

        def desativar():
            usuario.estado = "normal"

        timer = threading.Timer(self.duração, desativar)
        timer.start()

# BATEDOR
class AtaqueSurpresa(HabilidadeAtiva):
    def __init__(self):
        super().__init__(
            nome="Ataque Surpresa",
            efeito=self.efeito_ataque_surpresa,
            tempo_de_recarga=5,
            nivel_minimo=1,
            duração=1
        )

    def efeito_ataque_surpresa(self, usuario, alvo):
        if alvo:
            defesa_original = alvo.defesa_final
            alvo.defesa_final = defesa_original * 0.1
            
            def aplicar_dano():
                dano = int(max(0, (usuario.dano_final * 2) - alvo.defesa_final))
                alvo.vida -= dano
                alvo.defesa_final = defesa_original
            
            timer = threading.Timer(self.duração, aplicar_dano)
            timer.start()

class FugaRapida(HabilidadeAtiva):
    def __init__(self):
        super().__init__(
            nome="Fuga Rápida",
            efeito=self.efeito_fuga_rapida,
            tempo_de_recarga=5,
            nivel_minimo=1,
            duração=1
        )

    def efeito_fuga_rapida(self, usuario, inimigos):
        if not inimigos:
            return
        
        media_dano_inimigos = sum(inimigo.dano_final for inimigo in inimigos) / len(inimigos)
        dano = int(max(0, (media_dano_inimigos * 5) - (usuario.defesa_final + usuario.velocidade_final)))

        usuario.vida -= dano

        usuario.velocidade_bonus = usuario.velocidade_base + usuario.defesa_base
        usuario.defesa_bonus = usuario.velocidade_base + usuario.defesa_base

# ANDARILHO
class PassoFantasma(HabilidadeAtiva):
    def __init__(self, usuario, distancia=150):
        super().__init__(
            nome="Passo Fantasma",
            efeito=self.efeito_passo_fantasma,
            tempo_de_recarga=5,
            nivel_minimo=1,
            duração=0.5
        )
        self.usuario = usuario
        self.distancia = distancia
        self.tempo_ativacao = None
        self.ativa = False
        self.direcao = (0, 0)

    def ativar(self, direcao):
        self.direcao = direcao
        self.tempo_ativacao = time.time()
        self.ativa = True
        self.usuario.estado = "intangivel"

    def atualizar(self):
        if not self.ativa:
            return

        self.usuario.posição_x += self.direcao[0] * self.distancia
        self.usuario.posição_y += self.direcao[1] * self.distancia

        if (time.time() - self.tempo_ativacao) > self.duração:
            self.usuario.estado = "normal"
            self.ativa = False
            self.iniciar_cooldown()

    def efeito_passo_fantasma(self, usuario):
        pass


class AreiaNosOlhos(HabilidadeAtiva):
    def __init__(self, usuario, alvo, duração_efeito=3):
        super().__init__(
            nome="Areia nos Olhos",
            efeito=self.efeito_areia_nos_olhos,
            tempo_de_recarga=6,
            nivel_minimo=1,
            duração=1
        )
        self.usuario = usuario
        self.alvo = alvo
        self.duração_efeito = duração_efeito

    def efeito_areia_nos_olhos(self, usuario, alvo):
        if alvo:
            alvo.precisao_bonus -= 50  
            alvo.critico_bonus -= 50  

            def restaurar():
                alvo.precisao_bonus += 50
                alvo.critico_bonus += 50

            timer = threading.Timer(self.duração_efeito, restaurar)
            timer.start()

# ARTISTA MARCIAL
class ComboRelampago(HabilidadeAtiva):
    def __init__(self, usuario, alvo):
        super().__init__(
            nome="Combo Relâmpago",
            efeito=self.efeito_combo_relampago,
            tempo_de_recarga=8,
            nivel_minimo=1,
            duração=1
        )
        self.usuario = usuario
        self.alvo = alvo

    def efeito_combo_relampago(self, usuario, alvo):
        if alvo:
            for _ in range(3):
                dano = int(max(0, (usuario.dano_final * 1.2) - (alvo.defesa_final * 0.5)))
                alvo.vida -= dano

class PosturaDeFerro(HabilidadeAtiva):
    def __init__(self, usuario, duração_efeito=5):
        super().__init__(
            nome="Postura de Ferro",
            efeito=self.efeito_postura_de_ferro,
            tempo_de_recarga=12,
            nivel_minimo=1,
            duração=1
        )
        self.usuario = usuario
        self.duração_efeito = duração_efeito

    def efeito_postura_de_ferro(self, usuario):
        usuario.defesa_bonus += int(usuario.defesa_base * 1.5)
        usuario.resistencia_empurrao = True  

        def restaurar():
            usuario.defesa_bonus -= int(usuario.defesa_base * 1.5)
            usuario.resistencia_empurrao = False

        timer = threading.Timer(self.duração_efeito, restaurar)
        timer.start()


