import pygame
import sys
import os
from random import choice
import ctypes
import sqlite3
from pyautogui import hotkey, size
import pygetwindow as gw
hotkey("win", "d")
from subprocess import Popen
import json
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from recursos.imagens.telas.telas import telas

# Tamanho da janela
WIDTH, HEIGHT = 1300, 650

# Inicia o pygame
pygame.init()
pygame.mixer.init()

# Tela
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Baronet")

janela = gw.getWindowsWithTitle("Baronet")[0]

# Restaura e maximiza sem checar
janela.restore()


# ----------------- Centralizar a janela no Windows -----------------
user32 = ctypes.windll.user32
res_x = user32.GetSystemMetrics(0)  # largura da tela
res_y = user32.GetSystemMetrics(1)  # altura da tela

hwnd = pygame.display.get_wm_info()['window']  # handle da janela Pygame
pos_x = (res_x - WIDTH) // 2
pos_y = (res_y - HEIGHT) // 2
ctypes.windll.user32.MoveWindow(hwnd, pos_x, pos_y, WIDTH, HEIGHT, True)
# -------------------------------------------------------------------

# Música de fundo
endereco_frontend = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
pygame.mixer.music.load(rf"{endereco_frontend}\recursos\sons\Menu.mp3")
pygame.mixer.music.set_volume(0.05)
pygame.mixer.music.play(-1)

botao = pygame.mixer.Sound(rf"{endereco_frontend}\recursos\sons\botao.ogg")
erro = pygame.mixer.Sound(rf"{endereco_frontend}\recursos\sons\error.ogg")

# Endereço do arquivo
endereço = os.path.dirname(os.path.abspath(__file__))
endereco_frontend = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Endereço do banco de dados
endereco_banco_de_dados = rf"{endereco_frontend}\ui\banco_de_dados.db"

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)
GREEN = (0, 255, 0)

# Fontes
font_title = pygame.font.Font(rf"{endereco_frontend}\recursos\fontes\Minha fonte.ttf", 30)

font_button = pygame.font.Font(rf"{endereco_frontend}\recursos\fontes\Minha fonte.ttf", 18)

font_sub = pygame.font.Font(rf"{endereco_frontend}\recursos\fontes\Minha fonte.ttf", 20)

fonte_input = pygame.font.Font(rf"{endereco_frontend}\recursos\fontes\Minha fonte.ttf", 17)

fonte = pygame.font.Font(rf"{endereco_frontend}\recursos\fontes\Minha fonte.ttf", 9)

fonte_alternativa = pygame.font.Font(rf"{endereco_frontend}\recursos\fontes\Minha fonte.ttf", 12)

fonte_box = pygame.font.Font(rf"{endereco_frontend}\recursos\fontes\Minha fonte.ttf", 25)


# Telas do jogo
LOGIN = "login"
COMO_SERA_ESCOLHIDO_A_CLASSE = "como sera escolhido a classe"
ESCOLHA_DE_CLASSES = "escolha de classe"
CLASSE_DE_COMBATE = "classe de combate"
CLASSE_DE_SUPORTE = "classe de suporte"
DADOS_PESSOAIS = "dados pessoais"
VERIFICAR_DADOS = "verificar dados"
ENTRAR = "entrar"
ALEATÓRIO = "aleatorio"
PERSONALIDADE = "personalidade"
PERSONALIDADE_tela_2 = "personalidade tela 2"
PERSONALIDADE_tela_3 = "personalidade tela 3"
CRIAR_E_IR = "criar e ir"
DEFINIR_CLASSE = "definir classe"
DADOS_CLASSE = "dados da classe"
estado = LOGIN

# verificar se o botão do mause esta ativo
clicou = False

# Dados que podem ser digitado
TEXTO_S = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
TEXTO = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "ç", "á", "é", "ó", "í", "ú", "ã", "õ", "â", "ê", "ô", "û", "î", " ",
         "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "I", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "Ç", "Á", "É", "Ó", "Í", "Ú", "Â", "Ô", "Â", "Ê", "Ô", "Û", "Î"]
INTEIRO = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
DECIMAIS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ","]


# Cores
COR_ATIVA = (0, 120, 215)
COR_INATIVA = (150, 150, 150)
COR_TEXTO = (0, 0, 0)
COR_BG = (255, 255, 255)

# Tempo que ira definir o FPS
clock = pygame.time.Clock()

# Imagem do fundo principal e secundario
imagem_fundo = pygame.image.load(rf"{endereco_frontend}\recursos\Imagens\classes\fundo.png")
imagem_fundo = pygame.transform.scale(imagem_fundo, (1300, 650))
fundo_x = 0
fundo_y = 0

imagem_fundo_secundario = pygame.image.load(rf"{endereco_frontend}\recursos\Imagens\classes\fundo_secundario.png")
imagem_fundo_secundario = pygame.transform.scale(imagem_fundo_secundario, (1300, 650))

rect_fundo = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
rect_fundo.fill((*(30, 30, 30), 120))

rect_fundo2 = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
rect_fundo2.fill((*(30, 30, 30), 180))


def desenhar_botao(posicao_x, posicao_y, largura, altura):
    global clicou
    
    mouse = pygame.mouse.get_pos()
    clique = pygame.mouse.get_pressed()
    quadrado_botao = pygame.Surface((largura, altura), pygame.SRCALPHA)
    quadrado_botao2 = pygame.Surface((largura, altura), pygame.SRCALPHA)
    quadrado_botao.fill((250, 250, 250, 50))
    quadrado_botao2.fill((20, 20, 20, 50))
    
    # Verifica se o mouse está em cima
    if posicao_x < mouse[0] < posicao_x + largura and posicao_y < mouse[1] < posicao_y + altura:
        if clique[0] and not clicou:  
            # Pressionou pela primeira vez
            screen.blit(quadrado_botao2, (posicao_x, posicao_y))
            botao.set_volume(0.1)
            botao.play()
            clicou = True  # marca que já clicou
            return True    # só retorna nesse momento
        
        elif not clique[0]:
            # Mouse sobre o botão mas sem pressionar
            screen.blit(quadrado_botao, (posicao_x, posicao_y))
    
    # Soltou o clique → libera para clicar novamente
    if not clique[0]:
        clicou = False

    return False


        
# Dados do texto sendo digitado na hora
tempo_por_letra = 100  # milissegundos
inicio_texto = pygame.time.get_ticks()
quantidade_letras = 0

# Caixas de texto para colocar os dados do seu usuario
input_boxes = {"label": "Nome", "rect": pygame.Rect(420, 185, 465, 82), "text": "", "active": False, "peritido": TEXTO}
    


# Caixas de texto para logar em sua conta ja criada
input_usuario = {"label": "Usuario", "rect": pygame.Rect(420, 185, 465, 82), "text": "", "active": False, "peritido": TEXTO}

# botão para confirmar a opção que esta escolhendo

def botao_de_confirmação(texto: list, title):
    fonte_title = pygame.font.Font(f"{endereco_frontend}/recursos/fontes/Minha fonte.ttf", 30)
    fonte_texto = pygame.font.Font(f"{endereco_frontend}/recursos/fontes/Minha fonte.ttf", 20)
    
    while True:
        screen.blit(imagem_fundo, (0, 0))
        screen.blit(rect_fundo2, (0, 0))
        screen.blit(telas[23], (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.music.play(0)
                pygame.quit()
                sys.exit()

        for i, text in enumerate(texto):
            texto_renderizado = fonte_texto.render(text, True, (220, 220, 220))
            screen.blit(texto_renderizado, (176, (i + 1) * 30 + 180))
        titulo_rederizado = fonte_title.render(title, True, (220, 220, 220))
        screen.blit(titulo_rederizado, (650 - titulo_rederizado.get_size()[0] // 2, 156))

        if desenhar_botao(707, 467, 249, 55):
            pygame.event.clear()
            return True

        if desenhar_botao(317, 467, 249, 55):
            pygame.event.clear()
            return False
        
        pygame.display.update()

# Mostra que algo que esta dando erro
def Mensagem_de_aviso(texto: list, title):
    fonte_title = pygame.font.Font(f"{endereco_frontend}/recursos/fontes/Minha fonte.ttf", 30)
    fonte_texto = pygame.font.Font(f"{endereco_frontend}/recursos/fontes/Minha fonte.ttf", 20)
    erro.set_volume(0.5)
    erro.play()
    while True:
        screen.blit(imagem_fundo, (0, 0))
        screen.blit(rect_fundo2, (0, 0))
        screen.blit(telas[24], (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        
        for i, text in enumerate(texto):
            texto_renderizado = fonte_texto.render(text, True, (220, 220, 220))
            screen.blit(texto_renderizado, (310, (i + 1) * 30 + 240))
        titulo_rederizado = fonte_title.render(title, True, (220, 220, 220))
        screen.blit(titulo_rederizado, (650 - titulo_rederizado.get_size()[0] // 2, 198))

        if desenhar_botao(562, 422, 172, 56):
            pygame.event.clear()
            return False
        
        pygame.display.update()

# Questão que possui alternativas para ser respondidas
def alternativas(posicao_x, posicao_y, alternativa_1, alternativa_2, selecionada, largura = 700):
    global clicou  # precisa ser global ou controlada pelo escopo externo

    mouse = pygame.mouse.get_pos()
    clique = pygame.mouse.get_pressed()

    # Coordenadas das bolinhas
    raio = 10
    bolinha1 = (posicao_x + 345, posicao_y + 15)
    bolinha2 = (posicao_x + 345, posicao_y + 50)

    if clique[0] and not clicou:
        if (bolinha1[0] - raio < mouse[0] < bolinha1[0] + raio and
            bolinha1[1] - raio < mouse[1] < bolinha1[1] + raio):
            selecionada = alternativa_1
            clicou = True

        if (bolinha2[0] - raio < mouse[0] < bolinha2[0] + raio and
            bolinha2[1] - raio < mouse[1] < bolinha2[1] + raio):
            selecionada = alternativa_2
            clicou = True

    if not clique[0]:
        clicou = False  # só volta a permitir clique depois que soltar o botão

    # Desenhar bolinhas com base na seleção
    cor_preenchida = (100, 0, 0)
    cor_vazia = (150, 150, 150)

    pygame.draw.circle(screen, cor_preenchida if selecionada == alternativa_1 else cor_vazia, bolinha1, raio)
    pygame.draw.circle(screen, cor_preenchida if selecionada == alternativa_2 else cor_vazia, bolinha2, raio)

    return selecionada

    
# Nomes das questões que possui alternativas
questao_1 = None
questao_2 = None
questao_3 = None
questao_4 = None
questao_5 = None
questao_6 = None
questao_7 = None
questao_8 = None
questao_9 = None
questao_10 = None
questao_11 = None
questao_12 = None
questao_13 = None
questao_14 = None
questao_15 = None
questao_16 = None
questao_17 = None
questao_18 = None
questao_19 = None
genero = None


# Conexão inicial e criação das tabelas
def inicializar_banco():
    conexao = sqlite3.connect(endereco_banco_de_dados)
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        classe TEXT
        
    )""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS status (
        usuario_id INTEGER PRIMARY KEY,
        nivel INTEGER,
        dano INTEGER,
        velocidade INTEGER,
        defesa INTEGER,
        vida integer,
        experiencia INTEGER,
        FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
    )""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS progresso (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario_id INTEGER,
        capitulo INTEGER,
        missao INTEGER,
        FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
    )""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS inventario (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario_id INTEGER,
        item TEXT,
        item_equipado TEXT,
        dinheiro INTEGER,
        FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
    )""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS keys (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario_id INTEGER,
        inventario TEXT,
        correr TEXT,
        habilidades TEXT,
        habilidade_1 TEXT,
        habilidade_2 TEXT,
        mapa TEXT,
        FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
    )""")

    conexao.commit()
    conexao.close()

nivel = 1
experiencia = 0
inicializar_banco()

# Função para criar personagem completo
def criar_personagem(nome, classe, dano, velocidade, defesa, vida, arma):
    global nivel, experiencia
    conexao = sqlite3.connect(endereco_banco_de_dados)
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")
    arma = [(arma, 1)]


    # Inserir usuário
    cursor.execute("""
        INSERT INTO usuarios (nome, classe) VALUES (?, ?)
    """, (nome, classe))
    usuario_id = cursor.lastrowid

    # Inserir status
    

    cursor.execute("""
        INSERT INTO status (usuario_id, nivel, dano, velocidade, defesa, vida, experiencia)
        VALUES (?, 1, ?, ?, ?, ?, 0)
    """, (usuario_id, dano, velocidade, defesa, vida))

    # Inserir progresso
    cursor.execute("""
        INSERT INTO progresso (usuario_id, capitulo, missao)
        VALUES (?, ?, ?)
    """, (usuario_id, 1, 0))

    # Inserir inventário
    cursor.execute("""
    INSERT INTO inventario (usuario_id, item, item_equipado, dinheiro)
    VALUES (?, ?, ?, ?)
""", (usuario_id,  json.dumps(arma), json.dumps([]), 100))

    cursor.execute("""
        INSERT INTO keys (usuario_id, inventario, correr, habilidades, habilidade_1, habilidade_2, mapa)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (usuario_id, "E", "lctrl", "R", "Z", "X", "M"))

    conexao.commit()
    conexao.close()

def obter_id_usuario_por_nome(nome):
    conexao = sqlite3.connect(endereco_banco_de_dados)
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id
        FROM usuarios
        WHERE nome = ?
    """, (nome,))

    resultado = cursor.fetchone()
    conexao.close()

    if resultado:
        return resultado[0]  # ID do usuário
    else:
        return None
    
def obter_inventario_do_usuario(usuario_id):
    conexao = sqlite3.connect(endereco_banco_de_dados)
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT item, item_equipado, dinheiro
        FROM inventario
        WHERE usuario_id = ?
    """, (usuario_id,))


    for item, equipado, dinheiro in cursor.fetchall():
        inventario = {
            "item": item,
            "equipado": equipado,
            "dinheiro": dinheiro
        }

    conexao.close()
    return inventario

def obter_status_do_usuario(usuario_id):
    conexao = sqlite3.connect(endereco_banco_de_dados)
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT nivel, dano, velocidade, defesa, vida, experiencia
        FROM status
        WHERE usuario_id = ?
    """, (usuario_id,))

    status = cursor.fetchall()
    conexao.close()
    return status

def obter_progresso_do_usuario(usuario_id):
    conexao = sqlite3.connect(endereco_banco_de_dados)
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT capitulo, missao
        FROM progresso
        WHERE usuario_id = ?
    """, (usuario_id,))

    progresso = cursor.fetchall()
    conexao.close()
    return progresso

def obter_keys_do_usuario(usuario_id):
    conexao = sqlite3.connect(endereco_banco_de_dados)
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT inventario, correr, habilidades, habilidade_1, habilidade_2, mapa
        FROM keys
        WHERE usuario_id = ?
    """, (usuario_id,))

    keys = cursor.fetchall()
    conexao.close()
    return keys

def ver_se_o_usuario_ja_existe(nome):
    conexao = sqlite3.connect(endereco_banco_de_dados)
    cursor = conexao.cursor()

    cursor.execute("PRAGMA foreign_keys = ON")

    cursor.execute("SELECT id, classe FROM usuarios WHERE nome = ?", (nome,))
    usuario = cursor.fetchone()

    if usuario:
        conexao.close()
        return True
    else:
        conexao.close()
        return False
    

def ver_se_o_usuario_nao_existe(nome):
    conexao = sqlite3.connect(endereco_banco_de_dados)
    cursor = conexao.cursor()

    cursor.execute("PRAGMA foreign_keys = ON")

    cursor.execute("SELECT id, classe FROM usuarios WHERE nome = ?", (nome,))
    usuario = cursor.fetchone()

    if not usuario:
        conexao.close()
        return True
    else:
        conexao.close()
        return False

def obter_dados_usuario_por_nome(nome):
    conexao = sqlite3.connect(endereco_banco_de_dados)
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT nome, classe
        FROM usuarios
        WHERE nome = ?
    """, (nome,))

    dados = cursor.fetchone()
    conexao.close()
    return dados

contador = 1


def definir_classe(respostas):
    # Dicionário de classes com pontuações iniciais
    classes = {
        "Arqueiro": 0,
        "Espadachin": 0,
        "Assassino": 0,
        "Escudeiro": 0,
        "Lanceiro": 0,
        "Artista Marcial": 0,
        "Artilheiro": 0,
        "Curandeiro": 0,
        "Bardo": 0,
        "Ilusionista": 0
    }

    # Respostas esperadas organizadas
    questao_1 = respostas.get(1)
    questao_2 = respostas.get(2)
    questao_3 = respostas.get(3)
    questao_4 = respostas.get(4)
    questao_5 = respostas.get(5)
    questao_6 = respostas.get(6)
    questao_7 = respostas.get(7)
    questao_8 = respostas.get(8)
    questao_9 = respostas.get(9)
    questao_10 = respostas.get(10)
    questao_11 = respostas.get(11)
    questao_12 = respostas.get(12)
    questao_13 = respostas.get(13)
    questao_14 = respostas.get(14)
    questao_15 = respostas.get(15)
    questao_16 = respostas.get(16)
    questao_17 = respostas.get(17)
    questao_18 = respostas.get(18)
    questao_19 = respostas.get(19)

    # ---------- BLOCO 1: Questões mentais ----------
    if questao_1 == "Planejar":
        classes["Espadachin"] += 2
        classes["Arqueiro"] += 2
        classes["Assassino"] += 2
    elif questao_1 == "Agir no momento":
        classes["Artista Marcial"] += 2
        classes["Lanceiro"] += 2
        classes["Escudeiro"] += 2

    if questao_2 == "Calmo":
        classes["Espadachin"] += 2
        classes["Arqueiro"] += 2
        classes["Assassino"] += 1
        classes["Escudeiro"] += 2
    elif questao_2 == "Estressado":
        classes["Lanceiro"] += 2
        classes["Artista Marcial"] += 2

    if questao_3 == "Sozinho":
        classes["Assassino"] += 2
        classes["Artista Marcial"] += 1
        classes["Espadachin"] += 2
    elif questao_3 == "Pedir ajuda":
        classes["Arqueiro"] += 2
        classes["Artista Marcial"] += 2
        classes["Espadachin"] += 2
        classes["Escudeiro"] += 1
        classes["Curandeiro"] += 2

    if questao_4 == "Sim":
        classes["Arqueiro"] += 2
        classes["Artista Marcial"] += 1
        classes["Lanceiro"] += 2
        classes["Assassino"] += 2
        classes["Escudeiro"] += 2
    elif questao_4 == "Não":
        classes["Espadachin"] += 2

    if questao_5 == "Lógico":
        classes["Espadachin"] += 2
        classes["Escudeiro"] += 2
        classes["Artista Marcial"] += 2
    elif questao_5 == "Criativo":
        classes["Assassino"] += 2
        classes["Arqueiro"] += 2
        classes["Lanceiro"] += 2
        classes["Ilusionista"] += 2

    # ---------- BLOCO 2: Questões físicas ----------
    if questao_6 == "Força":
        classes["Escudeiro"] += 2
        classes["Espadachin"] += 2
        classes["Artista Marcial"] += 2
    elif questao_6 == "Agilidade":
        classes["Artista Marcial"] += 2
        classes["Lanceiro"] += 2
        classes["Assassino"] += 2
        classes["Arqueiro"] += 2

    if questao_7 == "Resistência":
        classes["Escudeiro"] += 2
        classes["Espadachin"] += 2
        classes["Assassino"] += 2
    elif questao_7 == "Explosões":
        classes["Artista Marcial"] += 2
        classes["Lanceiro"] += 2
        classes["Arqueiro"] += 2

    if questao_8 == "Rápido":
        classes["Arqueiro"] += 2
        classes["Assassino"] += 2
        classes["Lanceiro"] += 2
        classes["Artista Marcial"] += 2
    elif questao_8 == "Poderoso":
        classes["Espadachin"] += 2
        classes["Artista Marcial"] += 2

    if questao_9 == "Esquivar":
        classes["Arqueiro"] += 2
        classes["Artista Marcial"] += 2
        classes["Lanceiro"] += 2
        classes["Assassino"] += 2
    elif questao_9 == "Bloquear":
        classes["Escudeiro"] += 2

    if questao_10 == "Dor":
        classes["Escudeiro"] += 2
        classes["Lanceiro"] += 2
        classes["Espadachin"] += 2
        classes["Artista Marcial"] += 2
        classes["Assassino"] += 2
    elif questao_10 == "Cansaço":
        classes["Escudeiro"] += 2
        classes["Assassino"] += 2
        classes["Espadachin"] += 2
        classes["Arqueiro"] += 2

    # ---------- BLOCO 3: Questões sociais ----------
    if questao_11 == "Liderar":
        classes["Arqueiro"] += 2
        classes["Assassino"] += 2
        classes["Lanceiro"] += 2
        classes["Bardo"] += 2
    elif questao_11 == "Seguir":
        classes["Escudeiro"] += 2
        classes["Espadachin"] += 2
        classes["Artista Marcial"] += 2

    if questao_12 == "Amigável":
        classes["Escudeiro"] += 2
        classes["Arqueiro"] += 2
        classes["Espadachin"] += 2
        classes["Curandeiro"] += 2
    elif questao_12 == "Reservado":
        classes["Artista Marcial"] += 2
        classes["Assassino"] += 2
        classes["Lanceiro"] += 2

    if questao_13 == "Sim":
        classes["Escudeiro"] += 2
        classes["Espadachin"] += 2
        classes["Arqueiro"] += 2
        classes["Curandeiro"] += 2
    elif questao_13 == "Não":
        classes["Assassino"] += 2
        classes["Lanceiro"] += 2
        classes["Artista Marcial"] += 2

    if questao_14 == "Sim":
        classes["Escudeiro"] += 2
        classes["Arqueiro"] += 2
        classes["Espadachin"] += 2
        classes["Bardo"] += 2
    elif questao_14 == "Não":
        classes["Assassino"] += 2
        classes["Artista Marcial"] += 2
        classes["Lanceiro"] += 2

    if questao_15 == "Conversa":
        classes["Espadachin"] += 2
        classes["Arqueiro"] += 2
        classes["Assassino"] += 2
        classes["Escudeiro"] += 2
        classes["Bardo"] += 2
    elif questao_15 == "Ação":
        classes["Artista Marcial"] += 2
        classes["Lanceiro"] += 2
        classes["Artilheiro"] += 2

    # ---------- BLOCO 4: Questões de combate ----------
    if questao_16 == "Furtivos":
        classes["Arqueiro"] += 2
        classes["Lanceiro"] += 2
        classes["Assassino"] += 2
        classes["Ilusionista"] += 2
    elif questao_16 == "Fortes":
        classes["Artista Marcial"] += 2
        classes["Espadachin"] += 2
        classes["Escudeiro"] += 2

    if questao_17 == "Defesa":
        classes["Escudeiro"] += 2
    elif questao_17 == "Ataque":
        classes["Lanceiro"] += 2
        classes["Espadachin"] += 2
        classes["Assassino"] += 2
        classes["Arqueiro"] += 2
        classes["Artista Marcial"] += 2
        classes["Artilheiro"] += 2

    if questao_18 == "Sozinho":
        classes["Assassino"] += 2
        classes["Artista Marcial"] += 2
        classes["Lanceiro"] += 2
    elif questao_18 == "Em time":
        classes["Arqueiro"] += 2
        classes["Espadachin"] += 2
        classes["Escudeiro"] += 2
        classes["Curandeiro"] += 2

    if questao_19 == "Corpo a corpo":
        classes["Escudeiro"] += 2
        classes["Artista Marcial"] += 2
        classes["Espadachin"] += 2
        classes["Assassino"] += 2
    elif questao_19 == "À distância":
        classes["Lanceiro"] += 2
        classes["Arqueiro"] += 2
        classes["Artilheiro"] += 2

    # Classe escolhida final
    classe_escolhida = max(classes, key=classes.get)
    return classe_escolhida

classes = [
        "Arqueiro",
        "Espadachin",
        "Assassino",
        "Escudeiro",
        "Lanceiro",
        "Artista Marcial",
        "Artilheiro",
        "Curandeiro",
        "Bardo",
        "Ilusionista"
]

timer = 0

# Loop principal
if __name__ == "__main__":
    # Vê se o usuario ja está conectado
    if not os.path.exists(rf"{endereco_frontend}\ui\usuario.json"):
        while True:
            # Eventos que tem no jogo
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.mixer.music.play(0)
                    pygame.quit()
                    sys.exit()

                if evento.type == pygame.QUIT:
                    rodando = False

                # Caixas de texto
                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    input_boxes["active"] = input_boxes["rect"].collidepoint(evento.pos)
                    input_usuario["active"] = input_usuario["rect"].collidepoint(evento.pos)

                elif evento.type == pygame.KEYDOWN:
                    if input_boxes["active"]:
                        if evento.key == pygame.K_BACKSPACE:
                            input_boxes["text"] = input_boxes["text"][:-1]
                        elif evento.key == pygame.K_RETURN:
                            input_boxes["active"] = False
                        else:
                            if evento.unicode in input_boxes["peritido"] and len(input_boxes["text"]) < 18:
                                input_boxes["text"] += evento.unicode
                    if input_usuario["active"]:
                        if evento.key == pygame.K_BACKSPACE:
                            input_usuario["text"] = input_usuario["text"][:-1]
                        elif evento.key == pygame.K_RETURN:
                            input_usuario["active"] = False
                        else:
                            if evento.unicode in input_usuario["peritido"] and len(input_usuario["text"]) < 17:
                                input_usuario["text"] += evento.unicode

            key = pygame.key.get_pressed()

            if estado == LOGIN:
                screen.blit(imagem_fundo, (0, 0))
                screen.blit(rect_fundo, (0, 0))
                screen.blit(telas[25], (0, 0))
                if desenhar_botao(220, 176, 372, 340):
                    estado = ENTRAR
                if desenhar_botao(710, 172, 371, 344):
                    estado = COMO_SERA_ESCOLHIDO_A_CLASSE
            
            # Logar na conta
            elif estado == ENTRAR:
                screen.blit(imagem_fundo, (0, 0))
                screen.blit(rect_fundo, (0, 0))
                screen.blit(telas[12], (0, 0))

                if input_usuario["active"]:
                    if timer >= 0 and timer <= 32:
                        ponteiro = "|"
                        timer += 2
                        if timer >= 31:
                            timer = 64
                    elif timer <= 64 and timer >= 32:
                        ponteiro = " "
                        timer -= 2
                        if timer <= 33:
                            timer = 0
                
                else:
                    ponteiro = ""
                    timer = 0

                # Texto
                if input_usuario["text"] != "":
                    pygame.draw.rect(screen, (5, 5, 5), (460, 225, 425, 42))
                texto_surface = fonte_box.render(input_usuario["text"].title() + ponteiro, True, (220, 220, 220))
                screen.blit(texto_surface, (input_usuario["rect"].x + 5, input_usuario["rect"].y + 30))
                usuario = input_usuario["text"]

                if desenhar_botao(720, 372, 249, 56) or key[pygame.K_KP_ENTER]:
                    if ver_se_o_usuario_nao_existe(usuario):
                        Mensagem_de_aviso([" Não encontramos nenhum usuario com", "esse nome, tente novamente."], "Nome não encontrado")
                    else:
                        with open(rf"{endereco_frontend}\ui\usuario2.json", "w") as arquivo:
                            json.dump({"usuario": usuario,
                                       "dados_pessoais": obter_dados_usuario_por_nome(usuario),
                                       "inventario": obter_inventario_do_usuario(obter_id_usuario_por_nome(usuario)),
                                       "status": obter_status_do_usuario(obter_id_usuario_por_nome(usuario)),
                                       "progresso": obter_progresso_do_usuario(obter_id_usuario_por_nome(usuario)),
                                       "keys": obter_keys_do_usuario(obter_id_usuario_por_nome(usuario))}, arquivo)
                                       
                        with open(rf"{endereco_frontend}\ui\usuario2.json", "r") as arquivo:
                            dados = json.load(arquivo)
                        with open(rf"{endereco_frontend}\ui\usuario.json", "w") as arquivo:
                            json.dump({"usuario": usuario,
                                       
                                       "dados_pessoais": {"Nome": dados["dados_pessoais"][0],
                                                          "Classe": dados["dados_pessoais"][1]},

                                       "inventario": obter_inventario_do_usuario(obter_id_usuario_por_nome(usuario)),

                                       "status": {"nivel": dados["status"][0][0],
                                                  "dano": dados["status"][0][1],
                                                  "velocidade": dados["status"][0][2],
                                                  "defesa": dados["status"][0][3],
                                                  "vida": dados["status"][0][4],
                                                  "experiencia": dados["status"][0][5]},

                                        "progresso": {"capitulo": dados["progresso"][0][0],
                                                      "missao": dados["progresso"][0][1]},

                                        "keys": {"inventario": dados["keys"][0][0],
                                                 "correr": dados["keys"][0][1],
                                                 "habilidade": dados["keys"][0][2],
                                                 "habilidade_1": dados["keys"][0][3],
                                                 "habilidade_2": dados["keys"][0][4],
                                                 "mapa": dados["keys"][0][5]
                                                 }}, arquivo, indent=4)
                        if os.path.exists(rf"{endereco_frontend}\ui\usuario2.json"):
                            os.remove(rf"{endereco_frontend}\ui\usuario2.json")
                        pygame.mixer.music.play(0)
                        break
                        
                
                if desenhar_botao(330, 372, 249, 56):
                    estado = LOGIN

            # Como será escolhido sua classe
            elif estado == COMO_SERA_ESCOLHIDO_A_CLASSE:
                screen.blit(imagem_fundo, (0, 0))
                screen.blit(rect_fundo, (0, 0))
                screen.blit(telas[20], (0,0))

                if desenhar_botao(7, 580, 154, 61):
                    estado = LOGIN


                if desenhar_botao(534, 237, 254, 309):
                    estado = ESCOLHA_DE_CLASSES
                if desenhar_botao(193, 235, 254, 308):
                    if botao_de_confirmação([" Você realmente quer escolher sua classe", "aleaóriamente"], "Confirmação"):
                        estado = ALEATÓRIO
                if desenhar_botao(874, 235, 254, 310):
                    estado = PERSONALIDADE

            elif estado == ALEATÓRIO:
                classe = choice(classes)
                estado = DADOS_CLASSE


            # Escoler manualmente
            elif estado == ESCOLHA_DE_CLASSES:
                screen.blit(imagem_fundo, (0, 0))
                screen.blit(rect_fundo, (0, 0))
                screen.blit(telas[16], (0,0))

                if desenhar_botao(7, 580, 154, 61):
                    estado = COMO_SERA_ESCOLHIDO_A_CLASSE

                if desenhar_botao(314, 256, 291, 328):
                    if botao_de_confirmação(["Você realmente deseja uma classe de suporte?"], "Comfirmação"):
                        estado = CLASSE_DE_SUPORTE

                if desenhar_botao(704, 254, 291, 338):
                    if botao_de_confirmação(["Você realmente deseja uma classe de combate?"], "Confirmação"):
                        estado = CLASSE_DE_COMBATE

            elif estado == CLASSE_DE_COMBATE:
                screen.blit(imagem_fundo, (0, 0))
                screen.blit(rect_fundo, (0, 0))
                screen.blit(telas[15], (0,0))

                if desenhar_botao(209, 172, 254, 220):
                    if botao_de_confirmação(["Você realmete quer a classe Assassino?"], "Confirmar Classe"):
                        estado = DADOS_CLASSE
                        classe = "Assassino"

                if desenhar_botao(518, 172, 254, 220):
                    if botao_de_confirmação(["Você realmete quer a classe Lanceiro?"], "Confirmar Classe"):
                        estado = DADOS_CLASSE
                        classe = "Lanceiro"

                if desenhar_botao(823, 175, 254, 214):
                    if botao_de_confirmação(["Você realmete quer a classe Espadachin?"], "Confirmar Classe"):
                        estado = DADOS_CLASSE
                        classe = "Espadachin"

                if desenhar_botao(209, 410, 254, 221):
                    if botao_de_confirmação(["Você realmete quer a classe Artilheiro?"], "Confirmar Classe"):
                        estado = DADOS_CLASSE
                        classe = "Artilheiro"

                if desenhar_botao(518, 412, 254, 219):
                    if botao_de_confirmação(["Você realmete quer a classe Arqueiro?"], "Confirmar Classe"):
                        estado = DADOS_CLASSE
                        classe = "Arqueiro"

                if desenhar_botao(827, 410, 254, 221):
                    if botao_de_confirmação(["Você realmete quer a classe Artista Marcial?"], "Confirmar Classe"):
                        estado = DADOS_CLASSE
                        classe = "Artista Marcial"

            elif estado == CLASSE_DE_SUPORTE:
                screen.blit(imagem_fundo, (0, 0))
                screen.blit(rect_fundo, (0, 0))
                screen.blit(telas[14], (0,0))

                if desenhar_botao(350, 166, 255, 221):
                    if botao_de_confirmação(["Você realmete quer a classe Curandeiro?"], "Confirmar Classe"):
                        estado = DADOS_CLASSE
                        classe = "Curandeiro"

                if desenhar_botao(727, 168, 255, 220):
                    if botao_de_confirmação(["Você realmete quer a classe Escudeiro?"], "Confirmar Classe"):
                        estado = DADOS_CLASSE
                        classe = "Escudeiro"

                if desenhar_botao(352, 404, 253, 221):
                    if botao_de_confirmação(["Você realmete quer a classe Bardo?"], "Confirmar Classe"):
                        estado = DADOS_CLASSE
                        classe = "Bardo"

                if desenhar_botao(728, 407, 253, 218):
                    if botao_de_confirmação(["Você realmete quer a classe Ilusionista?"], "Confirmar Classe"):
                        estado = DADOS_CLASSE
                        classe = "Ilusionista"


            elif estado == DADOS_CLASSE:
                screen.blit(imagem_fundo, (0, 0))
                screen.blit(rect_fundo, (0, 0))
                if classe == "Assassino":
                    screen.blit(telas[4], (0, 0))
                elif classe == "Lanceiro":
                    screen.blit(telas[10], (0, 0))
                elif classe == "Espadachin":
                    screen.blit(telas[9], (0, 0))
                elif classe == "Artilheiro":
                    screen.blit(telas[0], (0, 0))
                elif classe == "Arqueiro":
                    screen.blit(telas[1], (0, 0))
                elif classe == "Artista Marcial":
                    screen.blit(telas[2], (0, 0))
                elif classe == "Curandeiro":
                    screen.blit(telas[6], (0, 0))
                elif classe == "Escudeiro":
                    screen.blit(telas[7], (0, 0))
                elif classe == "Bardo":
                    screen.blit(telas[3], (0, 0))
                elif classe == "Ilusionista":
                    screen.blit(telas[8], (0, 0))

                if desenhar_botao(1085, 596, 203, 45):
                    estado = DADOS_PESSOAIS

                
            # Area para setar os dados do usuario
            elif estado == DADOS_PESSOAIS:
                screen.blit(imagem_fundo, (0, 0))
                screen.blit(rect_fundo, (0, 0))
                screen.blit(telas[12], (0, 0))

                if input_usuario["active"]:
                    if timer >= 0 and timer <= 32:
                        ponteiro = "|"
                        timer += 2
                        if timer >= 31:
                            timer = 64
                    elif timer <= 64 and timer >= 32:
                        ponteiro = " "
                        timer -= 2
                        if timer <= 33:
                            timer = 0
                
                else:
                    ponteiro = ""
                    timer = 0

                # Texto
                if input_usuario["text"] != "":
                    pygame.draw.rect(screen, (5, 5, 5), (460, 225, 425, 42))
                texto_surface = fonte_box.render(input_usuario["text"].title() + ponteiro, True, (220, 220, 220))
                screen.blit(texto_surface, (input_usuario["rect"].x + 5, input_usuario["rect"].y + 30))
                usuario = input_usuario["text"]

                if desenhar_botao(330, 372, 249, 56):
                    estado = DADOS_CLASSE

                if desenhar_botao(720, 372, 249, 56) or key[pygame.K_KP_ENTER]: 
                    erros = []

                    dados_pessoais = {}



                    dados_pessoais[input_boxes["label"]] = input_boxes["text"]
                    
                    if ver_se_o_usuario_ja_existe(dados_pessoais["Nome"]):
                        estado = DADOS_PESSOAIS
                        Mensagem_de_aviso(["Esse nome já existe, tente outro."], "Nome invalido")

                    elif dados_pessoais["Nome"] == "":
                        estado = DADOS_PESSOAIS
                        Mensagem_de_aviso(["Coloque algum nome no campo."], "Nome invalido")

                    else:
                        estado = CRIAR_E_IR


            # Escolher a sua classe com base na personalidade
            elif estado == PERSONALIDADE:
                screen.blit(imagem_fundo, (0, 0))
                screen.blit(rect_fundo, (0, 0))
                screen.blit(telas[19], (0, 0))
                if desenhar_botao(16, 600, 203, 44):
                    estado = COMO_SERA_ESCOLHIDO_A_CLASSE
                
                # Questões
                questao_1 = alternativas(136, 162, "Planejar", "Agir no momento", questao_1)

                questao_2 = alternativas(134, 255, "Calmo", "Estressado", questao_2)

                questao_3 = alternativas(134, 346, "Sozinho", "Pedir ajuda", questao_3)

                questao_4 = alternativas(134, 440, "Sim", "Não", questao_4)

                questao_5 = alternativas(702, 162, "Lógico", "Criativo", questao_5)

                questao_6 = alternativas(702, 255, "Força", "Agilidade", questao_6)

                questao_7 = alternativas(702, 346, "Resistência", "Explosões", questao_7)

                questao_8 = alternativas(702, 440, "Rápido", "Poderoso", questao_8)

                # Ir para a próxima tela
                if desenhar_botao(1085, 596, 203, 45):
                    if questao_1 != None and questao_2 != None and questao_3 != None and questao_4 != None and questao_5 != None and questao_6 != None and questao_7 != None and questao_8 != None:
                        estado = PERSONALIDADE_tela_2
                    else:
                        Mensagem_de_aviso(["Preencha todas as questões!"], "Questão vazia")
            
            # 2 Tela de escolher a sua classe com base na personalidade
            elif estado == PERSONALIDADE_tela_2:
                screen.blit(imagem_fundo, (0, 0))
                screen.blit(rect_fundo, (0, 0))
                screen.blit(telas[18], (0, 0))
                if desenhar_botao(16, 600, 203, 44):
                    estado = PERSONALIDADE

                questao_9 = alternativas(136, 162, "Esquivar", "Bloquear", questao_9)

                questao_10 = alternativas(134, 255, "Dor", "Cansaço", questao_10)

                questao_11 = alternativas(134, 346, "Liderar", "Seguir", questao_11)

                questao_12 = alternativas(134, 440, "Amigável", "Reservado", questao_12)

                questao_13 = alternativas(702, 162, "Sim", "Não", questao_13)

                questao_14 = alternativas(702, 255, "Sim", "Não", questao_14)

                questao_15 = alternativas(702, 346, "Conversa", "Ação", questao_15)

                questao_16 = alternativas(702, 440, "Furtivos", "Fortes", questao_16)

                # Ir para a próxima tela
                if desenhar_botao(1085, 596, 203, 45):
                    if questao_9 != None and questao_10 != None and questao_11 != None and questao_12 != None and questao_13 != None and questao_14 != None and questao_15 != None and questao_16 != None:
                        estado = PERSONALIDADE_tela_3
                    else:
                        Mensagem_de_aviso(["Preencha todas as questões!"], "Questão vazia")
            
            # 3 Tela de escolher a sua classe com base na personalidade
            elif estado == PERSONALIDADE_tela_3:
                screen.blit(imagem_fundo, (0, 0))
                screen.blit(rect_fundo, (0, 0))
                screen.blit(telas[17], (0, 0))
                if desenhar_botao(16, 600, 203, 44):
                    estado = PERSONALIDADE_tela_2

                questao_17 = alternativas(150, 165, "Defesa", "Ataque", questao_17)

                questao_18 = alternativas(150, 262, "Sozinho", "Em time", questao_18)

                questao_19 = alternativas(150, 380, "Corpo a corpo", "À distância", questao_19)


                # Ir pora a próxima tela
                if desenhar_botao(1085, 596, 203, 45):
                    if questao_16 != None and questao_17 != None and questao_18 != None and questao_19 != None:
                        respostas = {1: questao_1,
                                    2: questao_2,
                                    3: questao_3,
                                    4: questao_4,
                                    5: questao_5,
                                    6: questao_6,
                                    7: questao_7,
                                    8: questao_8,
                                    9: questao_9,
                                    10: questao_10,
                                    11: questao_11,
                                    12: questao_12,
                                    13: questao_13,
                                    14: questao_14,
                                    15: questao_15,
                                    16: questao_16,
                                    17: questao_17,
                                    18: questao_18,
                                    19: questao_19
                                    }
                        estado = DEFINIR_CLASSE
                    else:
                        Mensagem_de_aviso(["Preencha todas as questões!"], "Questão vazia")
            
            # Ver qua classe se adequa a sua personalidade
            elif estado == DEFINIR_CLASSE:
                classe = definir_classe(respostas)
                estado = DADOS_CLASSE


            # Cria a conta e entra no lobby do jogo
            elif estado == CRIAR_E_IR:
                screen.blit(imagem_fundo_secundario, (0, 0))
                dados_pessoais["Classe"] = classe

                if dados_pessoais["Classe"] == "Assassino":
                    criar_personagem(dados_pessoais["Nome"],
                                    "Assassino",
                                    3, 5, 2, 10, ["Punho", "comum"])
                    
                    status = [3, 5, 2, 10]
                    
                elif dados_pessoais["Classe"] == "Espadachin":
                    criar_personagem(dados_pessoais["Nome"],
                                    "Espadachin",
                                    4, 4, 3, 12, ["Punho", "comum"])
                    
                    status = [4, 4, 3, 12]
                    
                elif dados_pessoais["Classe"] == "Lanceiro":
                    criar_personagem(dados_pessoais["Nome"],
                                    "Lanceiro",
                                    3, 4, 4, 13, ["Punho", "comum"])
                    
                    status = [3, 4, 4, 13]
                
                elif dados_pessoais["Classe"] == "Arqueiro":
                    criar_personagem(dados_pessoais["Nome"],
                                    "Arqueiro",
                                    2, 6, 2, 11, ["Punho", "comum"])
                    
                    status = [2, 6, 2, 11]
                    
                elif dados_pessoais["Classe"] == "Artista Marcial":
                    criar_personagem(dados_pessoais["Nome"],
                                    "Artista Marcial",
                                    4, 6, 4, 18, ["Punho", "comum"])
                    
                    status = [4, 6, 4, 18]
                    
                elif dados_pessoais["Classe"] == "Escudeiro":
                    criar_personagem(dados_pessoais["Nome"],
                                    "Escudeiro",
                                    2, 3, 5, 15, ["Punho", "comum"])
                    
                    status = [2, 3, 5, 15]

                elif dados_pessoais["Classe"] == "Curandeiro":
                    criar_personagem(dados_pessoais["Nome"],
                                    "Escudeiro",
                                    1, 3, 6, 13, ["Punho", "comum"])
                    
                    status = [1, 3, 6, 13]

                elif dados_pessoais["Classe"] == "Artilheiro":
                    criar_personagem(dados_pessoais["Nome"],
                                    "Escudeiro",
                                    5, 3, 2, 9, ["Punho", "comum"])
                    
                    status = [5, 3, 2, 9]

                elif dados_pessoais["Classe"] == "Bardo":
                    criar_personagem(dados_pessoais["Nome"],
                                    "Escudeiro",
                                    2, 4, 3, 12, ["Punho", "comum"])
                    
                    status = [2, 4, 3, 12]

                elif dados_pessoais["Classe"] == "Ilusionista":
                    criar_personagem(dados_pessoais["Nome"],
                                    "Escudeiro",
                                    3, 5, 2, 10, ["Punho", "comum"])
                    
                    status = [3, 5, 2, 10]
                
                
                
                usuario = dados_pessoais["Nome"]
                
                with open(rf"{endereco_frontend}\ui\usuario.json", "w") as arquivo:
                    json.dump({"usuario": usuario,
                               
                               "dados_pessoais": dados_pessoais,
                               
                               "inventario": obter_inventario_do_usuario(obter_id_usuario_por_nome(usuario)),
                               
                               "status":   {"nivel": 1,
                                            "dano": status[0],
                                            "velocidade": status[1],
                                            "defesa": status[2],
                                            "vida": status[3],
                                            "experiencia": 0},
                                            
                                "progresso": {"capitulo": 0,
                                              "missao": 1},
                                
                                "keys": {"inventario": "E",
                                         "correr": "Lctrl",
                                         "habilidade": "R",
                                         "habilidade_1": "Z",
                                         "habilidade_2": "X",
                                         "mapa": "M"
                                         }}, arquivo, indent=4)
                    

                pygame.mixer.music.play(0)
                break



            pygame.display.flip()
            clock.tick(16)

        
        Popen([sys.executable, rf'{endereco_frontend}\ui\lobby.py'])

    else:
        Popen([sys.executable, rf'{endereco_frontend}\ui\lobby.py'])
