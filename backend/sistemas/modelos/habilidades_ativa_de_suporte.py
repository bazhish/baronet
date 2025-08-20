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
            f"nome: {self.nome}\n"
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

# ESCUDEIRO
class AtaqueComEscudo(HabilidadeAtiva):
    def __init__(self):
        super().__init__(
            nome="Ataque com Escudo",
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
            nome="Defesa Reforçada",
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

# CURANDEIRO
class BencaoVital(HabilidadeAtiva):
    def __init__(self):
        super().__init__(
            nome="Bênção Vital",
            efeito=self.efeito_bencao,
            tempo_de_recarga=10,
            nivel_minimo=1,
            duração=6  # tempo total do efeito
        )
        self.thread = None
        self.ativa = False

    def efeito_bencao(self, usuario, aliados):
        if self.ativa:
            return  # evita reativar antes de acabar

        self.ativa = True
        inicio = time.time()

        def loop_cura():
            while time.time() - inicio < self.duração:
                for aliado in aliados:
                    cura = int(usuario.poder_magico * 0.8)
                    aliado.vida = min(aliado.vida_maxima, aliado.vida + cura)
                time.sleep(2)  # intervalo entre curas
            self.ativa = False
            self.iniciar_cooldown()

        self.thread = threading.Thread(target=loop_cura, daemon=True)
        self.thread.start()

class MilagreDaVida(HabilidadeAtiva):
    def __init__(self):
        super().__init__(
            nome="Milagre da Vida",
            efeito=self.efeito_milagre,
            tempo_de_recarga=20,  # maior cooldown porque é muito forte
            nivel_minimo=1,
            duração=0  # efeito imediato
        )

    def efeito_milagre(self, usuario, alvo):
        if alvo:
            alvo.vida = alvo.vida_maxima
            self.iniciar_cooldown()

# BARDO
class MelodiaDaFraqueza(HabilidadeAtiva):
    def __init__(self, usuario, inimigos, raio=150, duracao=6):
        super().__init__(
            nome="Melodia da Fraqueza",
            efeito=self.efeito_melodia,
            tempo_de_recarga=12,
            nivel_minimo=1,
            duração=duracao
        )
        self.usuario = usuario
        self.inimigos = inimigos
        self.raio = raio
        self.afetados = []

    def esta_no_raio(self, inimigo):
        dx = inimigo.posição_x - self.usuario.posição_x
        dy = inimigo.posição_y - self.usuario.posição_y
        return math.sqrt(dx*dx + dy*dy) <= self.raio

    def efeito_melodia(self, usuario, _=None):
        self.afetados = [i for i in self.inimigos if self.esta_no_raio(i)]

        # aplica redução de atributos
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
    def __init__(self, usuario, inimigos, raio=150, duracao=4):
        super().__init__(
            nome="Sinfonia Estática",
            efeito=self.efeito_sinfonia,
            tempo_de_recarga=15,
            nivel_minimo=1,
            duração=duracao
        )
        self.usuario = usuario
        self.inimigos = inimigos
        self.raio = raio
        self.afetados = []

    def esta_no_raio(self, inimigo):
        dx = inimigo.posição_x - self.usuario.posição_x
        dy = inimigo.posição_y - self.usuario.posição_y
        return math.sqrt(dx*dx + dy*dy) <= self.raio

    def efeito_sinfonia(self, usuario, _=None):
        self.afetados = [i for i in self.inimigos if self.esta_no_raio(i)]

        for inimigo in self.afetados:
            inimigo.estado = "paralisado"

        def restaurar():
            for inimigo in self.afetados:
                inimigo.estado = "normal"
            self.afetados.clear()
            self.iniciar_cooldown()

        threading.Timer(self.duração, restaurar).start()

# ILUSIONISTA
class MiragemSombria(HabilidadeAtiva):
    def __init__(self, usuario, inimigos, quantidade=3, duracao=6):
        super().__init__(
            nome="Miragem Sombria",
            efeito=self.efeito_miragem,
            tempo_de_recarga=14,
            nivel_minimo=1,
            duração=duracao
        )
        self.usuario = usuario
        self.inimigos = inimigos
        self.quantidade = quantidade
        self.ilusoes = []

    def efeito_miragem(self, usuario, _=None):
        # cria ilusões
        for i in range(self.quantidade):
            ilusão = {
                "posição_x": usuario.posição_x + i * 20,
                "posição_y": usuario.posição_y + i * 20,
                "é_ilusão": True
            }
            self.ilusoes.append(ilusão)

        # aplica bônus de esquiva
        usuario.esquiva += 30

        def encerrar():
            self.ilusoes.clear()
            usuario.esquiva -= 30
            self.iniciar_cooldown()

        threading.Timer(self.duração, encerrar).start()

class LabirintoMental(HabilidadeAtiva):
    def __init__(self, usuario, inimigos, raio=200, duracao=5):
        super().__init__(
            nome="Labirinto Mental",
            efeito=self.efeito_labirinto,
            tempo_de_recarga=18,
            nivel_minimo=1,
            duração=duracao
        )
        self.usuario = usuario
        self.inimigos = inimigos
        self.raio = raio
        self.afetados = []

    def esta_no_raio(self, inimigo):
        dx = inimigo.posição_x - self.usuario.posição_x
        dy = inimigo.posição_y - self.usuario.posição_y
        return math.sqrt(dx*dx + dy*dy) <= self.raio

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

ataque_com_escudo = AtaqueComEscudo()
defesa_reforcada = DefesaReforçada()
bençao_vital = BencaoVital()
milagre_da_vida = MilagreDaVida()
melodia_da_fraqueza = MelodiaDaFraqueza()
sinfonia_estatica = SinfoniaEstatica()
miragem_sombria = MiragemSombria()
labirinto_mental = LabirintoMental()