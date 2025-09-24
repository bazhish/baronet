# backend\sistemas\classes\habilidades_ativa_de_suporte.py
# from friendly import install
# install(lang="pt")
from dataclasses import dataclass, field
from random import uniform, randint
from typing import Callable, Optional, Any
import math, time, threading

@dataclass
class HabilidadeAtiva:
    nome: str
    efeito: Callable[[Any, Optional[Any]], None]
    tempo_de_recarga: int
    tempo_de_duração: int
    nível_minimo: int

    def __post_init__(self):
        self.descrição_do_efeito = "nenhuma"
        self.descrição = "nenhuma"
        self.tempo_de_recarga_restante = 0
        self.duração_restante = 0
        self.uso = None

    def atualizar_descrição(self):
        self.descrição = (
            f"nome: {self.nome}\n"
            f"Tempo de recarga: {self.tempo_de_recarga}\n"
            f"Duração: {self.tempo_de_duração}\n"
            f"Efeito: {self.descrição_do_efeito}\n"
        )

    def verificar_nivel(self, usuario):
        self.uso = usuario.nível_atual >= self.nível_minimo

    def aplicar_habilidade(self, usuario, alvo):
        if self.uso == True and self.tempo_de_recarga_restante == 0:
            self.efeito(usuario, alvo)
            self.duração_restante = self.duração
            self.tempo_de_recarga_restante = self.tempo_de_recarga

    def iniciar_cooldown(self):
        self.tempo_de_recarga_restante = self.tempo_de_recarga

# ESCUDEIRO
class AtaqueComEscudo(HabilidadeAtiva):
    def __init__(self, raio_maximo=100):
        super().__init__(
            nome="Ataque com Escudo",
            efeito=self.efeito_ataque_com_escudo,
            tempo_de_recarga=3,
            tempo_de_duração=5,
            nível_minimo=16
        )
        self.descrição_do_efeito = (
            f"Permite atacar com o escudo, causando dano baseado na defesa. Alcance máximo: {raio_maximo} pixels."
        )
        self.atualizar_descrição()
        self.usuario = None
        self.alvo = None
        self.tempo_ativação = None
        self.ativa = False
        self.raio_maximo = raio_maximo

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

    def dentro_do_raio(self, usuario, alvo):
        distância_x = alvo.posição_x - usuario.posição_x
        distância_y = alvo.posição_y - usuario.posição_y
        return math.sqrt(distância_x*distância_x + distância_y*distância_y) <= self.raio_maximo

    def efeito_ataque_com_escudo(self, usuario, alvo):
        if alvo and self.dentro_do_raio(usuario, alvo):
            dano = int(max(0, (usuario.defesa_final * 2) - (alvo.defesa_final * 0.75)))
            alvo.vida -= dano

class DefesaReforçada(HabilidadeAtiva):
    def __init__(self, raio = 300, duração=5):
        super().__init__(
            nome="Defesa Reforçada",
            efeito=self.efeito_defesa_reforcada,
            tempo_de_recarga=10,
            tempo_de_duração=duração,
            nível_minimo=50
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

    def efeito_defesa_reforcada(self):
        pass

# CURANDEIRO
class BencaoVital(HabilidadeAtiva):
    def __init__(self):
        super().__init__(
            nome="Bênção Vital",
            efeito=self.efeito_bencao,
            tempo_de_recarga=7,
            tempo_de_duração=6,
            nível_minimo=16,
        )
        self.thread = None
        self.ativa = False

    def efeito_bencao(self, usuario, aliados):
        if self.ativa:
            return 

        self.ativa = True
        inicio = time.time()

        def loop_cura():
            while time.time() - inicio < self.duração:
                for aliado in aliados:
                    cura = int(usuario.vida_máxima * 0.8)
                    aliado.vida_atual = min(aliado.vida_maxima, aliado.vida_atual + cura)
                threading.Event().wait(2)
            self.ativa = False
            self.iniciar_cooldown()

        self.thread = threading.Thread(target=loop_cura, daemon=True)
        self.thread.start()

class MilagreDaVida(HabilidadeAtiva):
    def __init__(self):
        super().__init__(
            nome="Milagre da Vida",
            efeito=self.efeito_milagre,
            tempo_de_recarga=10,  
            tempo_de_duração=9,
            nível_minimo=50,
        )

    def efeito_milagre(self, alvo):
        if alvo:
            alvo.vida_atual = alvo.vida_maxima
            self.iniciar_cooldown()

# BARDO
class MelodiaDaFraqueza(HabilidadeAtiva):
    def __init__(self, usuario=None, inimigos=None, raio=150, duracao=6):
        super().__init__(
            nome="Melodia da Fraqueza",
            efeito=self.efeito_melodia,
            tempo_de_recarga=8,
            tempo_de_duração=duracao,
            nível_minimo=16,
        )
        self.usuario = usuario
        self.inimigos = inimigos
        self.raio = raio
        self.afetados = []

    def esta_no_raio(self, inimigo):
        distância_x = inimigo.posição_x - self.usuario.posição_x
        distância_y = inimigo.posição_y - self.usuario.posição_y
        return math.sqrt(distância_x*distância_x + distância_y*distância_y) <= self.raio

    def efeito_melodia(self, usuario, _=None):
        self.afetados = [i for i in self.inimigos if self.esta_no_raio(i)]

        for inimigo in self.afetados:
            inimigo.forca //= 2
            inimigo.defesa //= 2
            inimigo.agilidade //= 2
            inimigo.inteligencia //= 2

        def restaurar():
            for inimigo in self.afetados:
                inimigo.forca *= 2
                inimigo.defesa *= 2
                inimigo.agilidade *= 2
                inimigo.inteligencia *= 2
            self.afetados.clear()
            self.iniciar_cooldown()

        threading.Timer(self.duração, restaurar).start()

class SinfoniaEstatica(HabilidadeAtiva):
    def __init__(self, usuario=None, inimigos=None, raio=150, duracao=4):
        super().__init__(
            nome="Sinfonia Estática",
            efeito=self.efeito_sinfonia,
            tempo_de_recarga=15,
            tempo_de_duração=duracao,
            nível_minimo=50,
        )
        self.usuario = usuario
        self.inimigos = inimigos
        self.raio = raio
        self.afetados = []

    def esta_no_raio(self, inimigo):
        distância_x = inimigo.posição_x - self.usuario.posição_x
        distãncia_y = inimigo.posição_y - self.usuario.posição_y
        return math.sqrt(distância_x*distância_x + distãncia_y*distãncia_y) <= self.raio

    def efeito_sinfonia(self, usuario, _=None):
        self.afetados = [i for i in self.inimigos if self.esta_no_raio(i)]

        for inimigo in self.afetados:
            inimigo.pode_mover = False

        def restaurar():
            for inimigo in self.afetados:
                inimigo.pode_mover = True
            self.afetados.clear()
            self.iniciar_cooldown()

        threading.Timer(self.duração, restaurar).start()

# ILUSIONISTA
class MiragemSombria(HabilidadeAtiva):
    def __init__(self, usuario=None, inimigos=None, quantidade=3, duracao=6):
        super().__init__(
            nome="Miragem Sombria",
            efeito=self.efeito_miragem,
            tempo_de_recarga=14,
            tempo_de_duração=duracao,
            nível_minimo=16,
        )
        self.usuario = usuario
        self.inimigos = inimigos
        self.quantidade = quantidade
        self.ilusoes = []

    def efeito_miragem(self, usuario, _=None):
        for i in range(self.quantidade):
            ilusão = {
                "posição_x": usuario.posição_x + i * 20,
                "posição_y": usuario.posição_y + i * 20,
                "é_ilusão": True
            }
            self.ilusoes.append(ilusão)

        def encerrar():
            self.iniciar_cooldown()

        threading.Timer(self.duração, encerrar).start()

class LabirintoMental(HabilidadeAtiva):
    def __init__(self, usuario=None, inimigos=None, raio=200, duracao=5):
        super().__init__(
            nome="Labirinto Mental",
            efeito=self.efeito_labirinto,
            tempo_de_recarga=18,
            tempo_de_duração=duracao,
            nível_minimo=50,
        )
        self.usuario = usuario
        self.inimigos = inimigos
        self.raio = raio
        self.afetados = []

    def esta_no_raio(self, inimigo):
        distância_x = inimigo.posição_x - self.usuario.posição_x
        distãncia_y = inimigo.posição_y - self.usuario.posição_y
        return math.sqrt(distância_x*distância_x + distãncia_y*distãncia_y) <= self.raio

    def efeito_labirinto(self, usuario, _=None):
        self.afetados = [i for i in self.inimigos if self.esta_no_raio(i)]

        for inimigo in self.afetados:
            inimigo.estado = "confuso"

        def restaurar():
            for inimigo in self.afetados:
                inimigo.estado = "normal"
            self.afetados.clear()
            self.iniciar_cooldown()

        threading.Timer(self.duração, restaurar).start()

# ESCUDEIRO
ataque_com_escudo = AtaqueComEscudo()
defesa_reforcada = DefesaReforçada()
# CURANDEIRO
bençao_vital = BencaoVital()
milagre_da_vida = MilagreDaVida()
# BARDO
melodia_da_fraqueza = MelodiaDaFraqueza()
sinfonia_estatica = SinfoniaEstatica()
# ILUSIONISTA
miragem_sombria = MiragemSombria()
labirinto_mental = LabirintoMental()