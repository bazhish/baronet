# arena.py

import json
from typing import List, Dict, Callable

class Participante:
    def __init__(self, nome: str, vida: int, mana: int):
        self.nome = nome
        self.vida = vida
        self.mana = mana
        self.posicao = (0, 0)
        self.buffs = []
        self.debuffs = []
    
    def esta_vivo(self) -> bool:
        return self.vida > 0


class Arena:
    def __init__(self, largura: int, altura: int):
        self.largura = largura
        self.altura = altura
        self.participantes: List[Participante] = []
        self.turno_atual = 0
        self.eventos: List[str] = []

    def ia_turno_npc(self):
        for npc in self.participantes.values():
            if npc.controlado_por_jogador or not npc.esta_vivo():
                continue
            
            # Escolhe o inimigo mais próximo
            inimigos = [p for p in self.participantes.values() if p.controlado_por_jogador and p.esta_vivo()]
            if not inimigos:
                return
            
            alvo = min(inimigos, key=lambda p: self.distancia(npc.posicao, p.posicao))
            
            # Se está ao lado, ataca
            if self.distancia(npc.posicao, alvo.posicao) == 1:
                dano = max(0, npc.ataque - alvo.defesa)
                alvo.vida -= dano
                self.registrar_evento(f"{npc.nome} atacou {alvo.nome} causando {dano} de dano.")
                if not alvo.esta_vivo():
                    self.registrar_evento(f"{alvo.nome} foi derrotado!")
                    self.checar_vitoria()
            else:
                # Move na direção do alvo
                nova_pos = self.mover_em_direcao(npc.posicao, alvo.posicao)
                if self.posicao_valida(nova_pos):
                    npc.posicao = nova_pos
                    self.registrar_evento(f"{npc.nome} moveu-se para {nova_pos}.")

    def ia_turno_npc_individual(self, npc):
        inimigos = [p for p in self.participantes.values() if p.controlado_por_jogador and p.esta_vivo()]
        if not inimigos:
            return
        alvo = min(inimigos, key=lambda p: self.distancia(npc.posicao, p.posicao))
        
        if self.distancia(npc.posicao, alvo.posicao) == 1:
            dano = max(0, npc.ataque - alvo.defesa)
            alvo.vida -= dano
            self.registrar_evento(f"{npc.nome} atacou {alvo.nome} causando {dano} de dano.")
            if not alvo.esta_vivo():
                self.registrar_evento(f"{alvo.nome} foi derrotado!")
        else:
            nova_pos = self.mover_em_direcao(npc.posicao, alvo.posicao)
            if self.posicao_valida(nova_pos):
                npc.posicao = nova_pos
                self.registrar_evento(f"{npc.nome} moveu-se para {nova_pos}.")
        
    def desenhar_mapa(self):
        grade = [["." for _ in range(self.largura)] for _ in range(self.altura)]
        for p in self.participantes.values():
            if p.esta_vivo():
                x, y = p.posicao
                inicial = p.nome[0].upper()
                grade[y][x] = inicial
        for linha in grade:
            print(" ".join(linha))


    
    def distancia(self, pos1, pos2):
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])
    
    def mover_em_direcao(self, origem, destino):
        x, y = origem
        dx = destino[0] - x
        dy = destino[1] - y
        if abs(dx) > abs(dy):
            x += 1 if dx > 0 else -1
        else:
            y += 1 if dy > 0 else -1
        return (x, y)
    
    def adicionar_participante(self, participante: Participante, posicao: tuple):
        participante.posicao = posicao
        self.participantes.append(participante)
        self.registrar_evento(f"{participante.nome} entrou na arena em {posicao}")
    
    def registrar_evento(self, descricao: str):
        self.eventos.append(descricao)
        print(f"[EVENTO] {descricao}")  # Para debug
    
    def avancar_turno(self):
        self.turno_atual += 1
        self.registrar_evento(f"Início do turno {self.turno_atual}")
        for hab in self.habilidades.values():
            hab.reduzir_cooldown()
        self.ia_turno_npc()

        
    
    def salvar_estado(self, arquivo: str):
        dados = {
            "turno": self.turno_atual,
            "participantes": [
                {
                    "nome": p.nome,
                    "vida": p.vida,
                    "mana": p.mana,
                    "posicao": p.posicao
                } for p in self.participantes
            ],
            "eventos": self.eventos
        }
        with open(arquivo, "w") as f:
            json.dump(dados, f, indent=4)
    
    def carregar_estado(self, arquivo: str):
        with open(arquivo, "r") as f:
            dados = json.load(f)
        self.turno_atual = dados["turno"]
        self.eventos = dados["eventos"]
        self.participantes.clear()
        for p in dados["participantes"]:
            novo = Participante(p["nome"], p["vida"], p["mana"])
            novo.posicao = tuple(p["posicao"])
            self.participantes.append(novo)

# MOVIMENTAÇÃO

# arena.py (continuação da etapa 1 + movimentação)

import json
from typing import List, Tuple

class Participante:
    def __init__(self, nome: str, vida: int, mana: int, ataque: int, defesa: int, velocidade: int, controlado_por_jogador=True):
        self.nome = nome
        self.vida = vida
        self.vida_max = vida
        self.mana = mana
        self.mana_max = mana
        self.ataque = ataque
        self.defesa = defesa
        self.velocidade = velocidade
        self.posicao = (0, 0)
        self.controlado_por_jogador = controlado_por_jogador
        self.buffs = []
    
    def esta_vivo(self) -> bool:
        return self.vida > 0


class Arena:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
        self.participantes = {}
        self.habilidades = {}
        self.historico = []
    
    def adicionar_participante(self, participante: Participante, posicao: Tuple[int, int]):
        if not self.posicao_valida(posicao):
            raise ValueError("Posição inválida ou ocupada!")
        participante.posicao = posicao
        self.participantes.append(participante)
        self.registrar_evento(f"{participante.nome} entrou na arena em {posicao}")
    
    def posicao_valida(self, posicao: Tuple[int, int]) -> bool:
        x, y = posicao
        # Checa se está dentro da arena
        if not (0 <= x < self.largura and 0 <= y < self.altura):
            return False
        # Checa se não está ocupada
        for p in self.participantes:
            if p.posicao == posicao and p.esta_vivo():
                return False
        return True
    
    def mover_participante(self, nome: str, nova_posicao: Tuple[int, int]):
        for p in self.participantes:
            if p.nome == nome:
                if not p.esta_vivo():
                    self.registrar_evento(f"{p.nome} não pode se mover, pois está derrotado.")
                    return False
                if self.posicao_valida(nova_posicao):
                    pos_antiga = p.posicao
                    p.posicao = nova_posicao
                    self.registrar_evento(f"{p.nome} moveu-se de {pos_antiga} para {nova_posicao}")
                    return True
                else:
                    self.registrar_evento(f"Movimento inválido para {p.nome}.")
                    return False
        return False
    
    def registrar_evento(self, descricao: str):
        self.eventos.append(descricao)
        print(f"[EVENTO] {descricao}")
    
    def avancar_turno(self):
        ordem_turno = sorted(
            [p for p in self.participantes.values() if p.esta_vivo()],
            key=lambda p: p.velocidade,
            reverse=True
        )
        
        for entidade in ordem_turno:
            if entidade.controlado_por_jogador:
                self.turno_jogador(entidade)
            else:
                self.ia_turno_npc_individual(entidade)
        
        for hab in self.habilidades.values():
            hab.reduzir_cooldown()

    def turno_jogador(self, jogador):
        print(f"\nTurno de {jogador.nome}")
        print(f"Vida: {jogador.vida}/{jogador.vida_max} | Mana: {jogador.mana}/{jogador.mana_max}")
        self.desenhar_mapa()
    
        acao = input("[A]tacar, [M]over, [H]abilidade: ").lower()
        if acao == "a":
            inimigos = [p for p in self.participantes.values() if p != jogador and p.esta_vivo()]
            for i, inimigo in enumerate(inimigos):
                print(f"{i+1}. {inimigo.nome} (Vida: {inimigo.vida})")
            escolha = int(input("Escolha inimigo: ")) - 1
            alvo = inimigos[escolha]
            dano = max(0, jogador.ataque - alvo.defesa)
            alvo.vida -= dano
            self.registrar_evento(f"{jogador.nome} atacou {alvo.nome} causando {dano} de dano.")
        elif acao == "m":
            x = int(input("Novo X: "))
            y = int(input("Novo Y: "))
            if self.posicao_valida((x, y)):
                jogador.posicao = (x, y)
                self.registrar_evento(f"{jogador.nome} moveu-se para {(x, y)}.")
        elif acao == "h":
            for nome_hab in self.habilidades:
                print(f"- {nome_hab}")
            escolha = input("Escolha habilidade: ")
            if escolha in self.habilidades:
                self.usar_habilidade(jogador.nome, escolha, None)
    
    def salvar_estado(self, arquivo: str):
        dados = {
            "turno": self.turno_atual,
            "participantes": [
                {
                    "nome": p.nome,
                    "vida": p.vida,
                    "mana": p.mana,
                    "posicao": p.posicao
                } for p in self.participantes
            ],
            "eventos": self.eventos
        }
        with open(arquivo, "w") as f:
            json.dump(dados, f, indent=4)
    
    def carregar_estado(self, arquivo: str):
        with open(arquivo, "r") as f:
            dados = json.load(f)
        self.turno_atual = dados["turno"]
        self.eventos = dados["eventos"]
        self.participantes.clear()
        for p in dados["participantes"]:
            novo = Participante(p["nome"], p["vida"], p["mana"])
            novo.posicao = tuple(p["posicao"])
            self.participantes.append(novo)

# ATAQUES

# arena.py (continuação das etapas anteriores)

import json
from typing import List, Tuple

class Participante:
    def __init__(self, nome: str, vida: int, mana: int, ataque: int = 10, defesa: int = 5):
        self.nome = nome
        self.vida = vida
        self.mana = mana
        self.ataque_base = ataque
        self.defesa_base = defesa
        self.posicao: Tuple[int, int] = (0, 0)
        self.buffs = []
        self.debuffs = []
    
    def esta_vivo(self) -> bool:
        return self.vida > 0
    
    def receber_dano(self, quantidade: int):
        self.vida = max(0, self.vida - quantidade)
    
    def calcular_dano(self, alvo: "Participante") -> int:
        dano = self.ataque_base - alvo.defesa_base
        return max(1, dano)  # garante pelo menos 1 de dano


class Arena:
    def __init__(self, largura: int, altura: int):
        self.largura = largura
        self.altura = altura
        self.participantes: List[Participante] = []
        self.turno_atual = 0
        self.eventos: List[str] = []
        self.partida_finalizada = False
    
    # --- GESTÃO DE PARTICIPANTES ---
    def adicionar_participante(self, participante: Participante, posicao: Tuple[int, int]):
        if not self.posicao_valida(posicao):
            raise ValueError("Posição inválida ou ocupada!")
        participante.posicao = posicao
        self.participantes.append(participante)
        self.registrar_evento(f"{participante.nome} entrou na arena em {posicao}")
    
    def posicao_valida(self, posicao: Tuple[int, int]) -> bool:
        x, y = posicao
        if not (0 <= x < self.largura and 0 <= y < self.altura):
            return False
        for p in self.participantes:
            if p.posicao == posicao and p.esta_vivo():
                return False
        return True
    
    # --- MOVIMENTAÇÃO ---
    def mover_participante(self, nome: str, nova_posicao: Tuple[int, int]):
        if self.partida_finalizada:
            self.registrar_evento("A partida já terminou.")
            return False
        for p in self.participantes:
            if p.nome == nome:
                if not p.esta_vivo():
                    self.registrar_evento(f"{p.nome} não pode se mover, pois está derrotado.")
                    return False
                if self.posicao_valida(nova_posicao):
                    pos_antiga = p.posicao
                    p.posicao = nova_posicao
                    self.registrar_evento(f"{p.nome} moveu-se de {pos_antiga} para {nova_posicao}")
                    return True
                else:
                    self.registrar_evento(f"Movimento inválido para {p.nome}.")
                    return False
        return False
    
    # --- ATAQUE ---
    def atacar(self, atacante_nome: str, alvo_nome: str):
        if self.partida_finalizada:
            self.registrar_evento("A partida já terminou.")
            return False
        
        atacante = self.get_participante(atacante_nome)
        alvo = self.get_participante(alvo_nome)
        
        if not atacante or not alvo:
            self.registrar_evento("Atacante ou alvo não encontrado.")
            return False
        if not atacante.esta_vivo():
            self.registrar_evento(f"{atacante.nome} está derrotado e não pode atacar.")
            return False
        if not alvo.esta_vivo():
            self.registrar_evento(f"{alvo.nome} já está derrotado.")
            return False
        
        dano = atacante.calcular_dano(alvo)
        alvo.receber_dano(dano)
        self.registrar_evento(f"{atacante.nome} atacou {alvo.nome} causando {dano} de dano. Vida restante do alvo: {alvo.vida}")
        
        if not alvo.esta_vivo():
            self.registrar_evento(f"{alvo.nome} foi derrotado!")
            self.checar_vitoria()
        return True
    
    def get_participante(self, nome: str) -> Participante:
        for p in self.participantes:
            if p.nome == nome:
                return p
        return None
    
    # --- CONDIÇÕES DE VITÓRIA ---
    def checar_vitoria(self):
        vivos = [p for p in self.participantes if p.esta_vivo()]
        if len(vivos) <= 1:
            self.partida_finalizada = True
            if vivos:
                self.registrar_evento(f"{vivos[0].nome} venceu a partida!")
            else:
                self.registrar_evento("Todos foram derrotados! Empate.")
    
    # --- EVENTOS E ESTADO ---
    def registrar_evento(self, descricao: str):
        self.eventos.append(descricao)
        print(f"[EVENTO] {descricao}")
    
    def avancar_turno(self):
        if not self.partida_finalizada:
            self.turno_atual += 1
            self.registrar_evento(f"Início do turno {self.turno_atual}")
    
    def salvar_estado(self, arquivo: str):
        dados = {
            "turno": self.turno_atual,
            "participantes": [
                {
                    "nome": p.nome,
                    "vida": p.vida,
                    "mana": p.mana,
                    "posicao": p.posicao
                } for p in self.participantes
            ],
            "eventos": self.eventos
        }
        with open(arquivo, "w") as f:
            json.dump(dados, f, indent=4)
    
    def carregar_estado(self, arquivo: str):
        with open(arquivo, "r") as f:
            dados = json.load(f)
        self.turno_atual = dados["turno"]
        self.eventos = dados["eventos"]
        self.participantes.clear()
        for p in dados["participantes"]:
            novo = Participante(p["nome"], p["vida"], p["mana"])
            novo.posicao = tuple(p["posicao"])
            self.participantes.append(novo)

#  APLICAÇÃO DE HABILIDADES

# arena.py (continuação da etapa 3 + habilidades)

import json
from typing import List, Tuple, Callable


class Participante:
    def __init__(self, nome: str, vida: int, mana: int, ataque: int = 10, defesa: int = 5):
        self.nome = nome
        self.vida = vida
        self.mana = mana
        self.ataque_base = ataque
        self.defesa_base = defesa
        self.posicao: Tuple[int, int] = (0, 0)
        self.buffs: List[dict] = []
        self.debuffs: List[dict] = []
    
    def esta_vivo(self) -> bool:
        return self.vida > 0
    
    def receber_dano(self, quantidade: int):
        self.vida = max(0, self.vida - quantidade)
    
    def calcular_dano(self, alvo: "Participante") -> int:
        dano = self.ataque_base - alvo.defesa_base
        return max(1, dano)  # garante pelo menos 1 de dano
    
    def aplicar_buff(self, buff: dict):
        """buff: {"tipo": str, "valor": int, "duracao": int}"""
        self.buffs.append(buff)
    
    def aplicar_debuff(self, debuff: dict):
        """debuff: {"tipo": str, "valor": int, "duracao": int}"""
        self.debuffs.append(debuff)
    
    def processar_efeitos(self):
        # Buffs
        for buff in list(self.buffs):
            if buff["tipo"] == "ataque":
                self.ataque_base += buff["valor"]
            elif buff["tipo"] == "defesa":
                self.defesa_base += buff["valor"]
            buff["duracao"] -= 1
            if buff["duracao"] <= 0:
                self.buffs.remove(buff)
        
        # Debuffs
        for debuff in list(self.debuffs):
            if debuff["tipo"] == "ataque":
                self.ataque_base -= debuff["valor"]
            elif debuff["tipo"] == "defesa":
                self.defesa_base -= debuff["valor"]
            debuff["duracao"] -= 1
            if debuff["duracao"] <= 0:
                self.debuffs.remove(debuff)


class Habilidade:
    def __init__(self, nome: str, custo_mana: int, efeito: Callable, area: int = 0):
        self.nome = nome
        self.custo_mana = custo_mana
        self.efeito = efeito  # função que recebe (arena, usuario, alvo)
        self.area = area      # raio de alcance em área


class Arena:
    def __init__(self, largura: int, altura: int):
        self.largura = largura
        self.altura = altura
        self.participantes: List[Participante] = []
        self.habilidades: dict = {}
        self.turno_atual = 0
        self.eventos: List[str] = []
        self.partida_finalizada = False
    
    # --- GESTÃO ---
    def adicionar_participante(self, participante: Participante, posicao: Tuple[int, int]):
        if not self.posicao_valida(posicao):
            raise ValueError("Posição inválida ou ocupada!")
        participante.posicao = posicao
        self.participantes.append(participante)
        self.registrar_evento(f"{participante.nome} entrou na arena em {posicao}")
    
    def posicao_valida(self, posicao: Tuple[int, int]) -> bool:
        x, y = posicao
        if not (0 <= x < self.largura and 0 <= y < self.altura):
            return False
        for p in self.participantes:
            if p.posicao == posicao and p.esta_vivo():
                return False
        return True
    
    def get_participante(self, nome: str) -> Participante:
        for p in self.participantes:
            if p.nome == nome:
                return p
        return None
    
    # --- MOVIMENTAÇÃO ---
    def mover_participante(self, nome: str, nova_posicao: Tuple[int, int]):
        if self.partida_finalizada:
            self.registrar_evento("A partida já terminou.")
            return False
        p = self.get_participante(nome)
        if p:
            if not p.esta_vivo():
                self.registrar_evento(f"{p.nome} não pode se mover, pois está derrotado.")
                return False
            if self.posicao_valida(nova_posicao):
                pos_antiga = p.posicao
                p.posicao = nova_posicao
                self.registrar_evento(f"{p.nome} moveu-se de {pos_antiga} para {nova_posicao}")
                return True
            else:
                self.registrar_evento(f"Movimento inválido para {p.nome}.")
        return False
    
    # --- ATAQUES ---
    def atacar(self, atacante_nome: str, alvo_nome: str):
        if self.partida_finalizada:
            self.registrar_evento("A partida já terminou.")
            return False
        
        atacante = self.get_participante(atacante_nome)
        alvo = self.get_participante(alvo_nome)
        
        if not atacante or not alvo:
            self.registrar_evento("Atacante ou alvo não encontrado.")
            return False
        if not atacante.esta_vivo():
            self.registrar_evento(f"{atacante.nome} está derrotado e não pode atacar.")
            return False
        if not alvo.esta_vivo():
            self.registrar_evento(f"{alvo.nome} já está derrotado.")
            return False
        
        dano = atacante.calcular_dano(alvo)
        alvo.receber_dano(dano)
        self.registrar_evento(f"{atacante.nome} atacou {alvo.nome} causando {dano} de dano. Vida restante do alvo: {alvo.vida}")
        
        if not alvo.esta_vivo():
            self.registrar_evento(f"{alvo.nome} foi derrotado!")
            self.checar_vitoria()
        return True
    
    # --- HABILIDADES ---
    def registrar_habilidade(self, nome: str, habilidade: Habilidade):
        self.habilidades[nome] = habilidade
    
    def usar_habilidade(self, usuario_nome: str, habilidade_nome: str, alvo_nome: str):
        usuario = self.get_participante(usuario_nome)
        habilidade = self.habilidades.get(habilidade_nome)
        
        if not usuario or not habilidade:
            self.registrar_evento("Usuário ou habilidade não encontrada.")
            return False
        if usuario.mana < habilidade.custo_mana:
            self.registrar_evento(f"{usuario.nome} não tem mana suficiente para usar {habilidade.nome}.")
            return False
        
        usuario.mana -= habilidade.custo_mana
        habilidade.efeito(self, usuario, self.get_participante(alvo_nome))
        return True
    
    # --- CONDIÇÕES DE VITÓRIA ---
    def checar_vitoria(self):
        vivos = [p for p in self.participantes if p.esta_vivo()]
        if len(vivos) <= 1:
            self.partida_finalizada = True
            if vivos:
                self.registrar_evento(f"{vivos[0].nome} venceu a partida!")
            else:
                self.registrar_evento("Todos foram derrotados! Empate.")
    
    # --- EVENTOS E ESTADO ---
    def registrar_evento(self, descricao: str):
        self.eventos.append(descricao)
        print(f"[EVENTO] {descricao}")
    
    def avancar_turno(self):
        if not self.partida_finalizada:
            self.turno_atual += 1
            self.registrar_evento(f"Início do turno {self.turno_atual}")
            # Processar buffs/debuffs
            for p in self.participantes:
                if p.esta_vivo():
                    p.processar_efeitos()
    
    def salvar_estado(self, arquivo: str):
        dados = {
            "turno": self.turno_atual,
            "participantes": [
                {
                    "nome": p.nome,
                    "vida": p.vida,
                    "mana": p.mana,
                    "posicao": p.posicao
                } for p in self.participantes
            ],
            "eventos": self.eventos
        }
        with open(arquivo, "w") as f:
            json.dump(dados, f, indent=4)

def usar_habilidade(self, usuario_nome: str, habilidade_nome: str, alvo_nome: str):
    usuario = self.get_participante(usuario_nome)
    habilidade = self.habilidades.get(habilidade_nome)
    
    if not usuario or not habilidade:
        self.registrar_evento("Usuário ou habilidade não encontrada.")
        return False
    if not habilidade.pode_usar(usuario_nome):
        self.registrar_evento(f"{habilidade.nome} ainda está em recarga para {usuario.nome}.")
        return False
    if usuario.mana < habilidade.custo_mana:
        self.registrar_evento(f"{usuario.nome} não tem mana suficiente para usar {habilidade.nome}.")
        return False
    
    usuario.mana -= habilidade.custo_mana
    habilidade.efeito(self, usuario, self.get_participante(alvo_nome))
    
    if habilidade.cooldown_max > 0:
        habilidade.cooldowns[usuario_nome] = habilidade.cooldown_max
    return True

class Participante:
    def __init__(self, nome: str, vida: int, mana: int, ataque: int, defesa: int, controlado_por_jogador=True):
        self.nome = nome
        self.vida = vida
        self.vida_max = vida
        self.mana = mana
        self.mana_max = mana
        self.ataque = ataque
        self.defesa = defesa
        self.posicao = (0, 0)
        self.controlado_por_jogador = controlado_por_jogador
        self.buffs = []
    
    def esta_vivo(self) -> bool:
        return self.vida > 0

if __name__ == "__main__":
    arena = Arena(5, 5)
    jogador = Participante("Alice", 40, 20, ataque=7, defesa=3, velocidade=5, controlado_por_jogador=True)
    goblin = Participante("Goblin", 20, 10, ataque=5, defesa=2, velocidade=3, controlado_por_jogador=False)
    orc = Participante("Orc", 25, 8, ataque=6, defesa=3, velocidade=4, controlado_por_jogador=False)
    
    arena.adicionar_participante(jogador, (0, 0))
    arena.adicionar_participante(goblin, (2, 0))
    arena.adicionar_participante(orc, (4, 0))
    
    while True:
        arena.avancar_turno()
