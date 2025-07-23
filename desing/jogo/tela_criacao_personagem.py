import pygame
import sys
import os
from random import choice
import sqlite3
from subprocess import Popen
import json

endereço = os.path.dirname(os.path.abspath(__file__))

endereco_banco_de_dados = rf"{endereço}\banco_de_dados.db"

pygame.init()
pygame.mixer.init()



pygame.mixer.music.load(rf"{endereço}\efeito_sonoro\Menu.mp3")
pygame.mixer.music.set_volume(0.15)
pygame.mixer.music.play(-1)

botao = pygame.mixer.Sound(rf"{endereço}\efeito_sonoro\botao.ogg")
erro = pygame.mixer.Sound(rf"{endereço}\efeito_sonoro\error.ogg")


# Tela
WIDTH, HEIGHT = 1300, 650

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Meu RPG")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)
GREEN = (0, 255, 0)

# Fonte
font_title = pygame.font.Font(rf"{endereço}\fonte\Minha fonte.ttf", 30)

font_button = pygame.font.Font(rf"{endereço}\fonte\Minha fonte.ttf", 18)

font_sub = pygame.font.Font(rf"{endereço}\fonte\Minha fonte.ttf", 20)

fonte_input = pygame.font.Font(rf"{endereço}\fonte\Minha fonte.ttf", 17)

fonte = pygame.font.Font(rf"{endereço}\fonte\Minha fonte.ttf", 9)

fonte_alternativa = pygame.font.Font(rf"{endereço}\fonte\Minha fonte.ttf", 12)


# Estados do jogo
MENU = "menu"
LOGIN = "login"
COMO_SERA_ESCOLHIDO_A_CLASSE = "como sera escolhido a classe"
ESCOLHA_DE_CLASSES = "escolha de classe"
ESCOLHA_DE_CLASSES_JANELA_2 = "escolha de classe janela 2"
ARQUEIRO = "arqueiro"
ARQUEIRO2 = "arqueiro2"
ESPADACHIN = "espadachin"
ESPADACHIN2 = "espadachin2"
ASSASSINO = "assassino"
ASSASSINO2 = "assassino2"
ESCUDEIRO = "escudeiro"
ESCUDEIRO2 = "escudeiro2"
LANCEIRO = "lanceiro"
LANCEIRO2 = "lanceiro2"
BATEDOR = "batedor"
BATEDOR2 = "batedor2"
DADOS_PESSOAIS = "dados pessoais"
VERIFICAR_DADOS = "verificar dados"
ENTRAR = "entrar"
ALEATÓRIO = "aleatorio"
PERSONALIDADE = "personalidade"
PERSONALIDADE_tela_2 = "personalidade tela 2"
PERSONALIDADE_tela_3 = "personalidade tela 3"
PERSONALIDADE_tela_4 = "personalidade tela 4"
CRIAR_E_IR = "criar e ir"
DEFINIR_CLASSE = "definir classe"
estado = MENU


clicou = False

TEXTO = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "ç", "á", "é", "ó", "í", "ú", "ã", "õ", "â", "ê", "ô", "û", "î", " "]
INTEIRO = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
DECIMAIS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ","]


# Cores
COR_ATIVA = (0, 120, 215)
COR_INATIVA = (150, 150, 150)
COR_TEXTO = (0, 0, 0)
COR_BG = (255, 255, 255)

clock = pygame.time.Clock()

# Local do arquivo
  # personagem de exemplo


imagem_fundo = pygame.image.load(rf"{endereço}\Imagens\classes\fundo.png")
imagem_fundo = pygame.transform.scale(imagem_fundo, (1300, 650))
fundo_x = 0
fundo_y = 0

imagem_fundo_secundario = pygame.image.load(rf"{endereço}\Imagens\classes\fundo_secundario.png")
imagem_fundo_secundario = pygame.transform.scale(imagem_fundo_secundario, (1300, 650))


# Função para desenhar botão
def desenhar_botao(texto, posicao_x, posicao_y, largura, altura, posicao_da_letra, cor, cor_ativado, arredondamento_da_borda,
                   imagem_path=None, largura_da_imagem = None, altura_da_imagem = None, Distancia_de_cima = 40, fonte = 18):
    global clicou
    font_button = pygame.font.Font(rf"{endereço}\fonte\Minha fonte.ttf", fonte)
    
    mouse = pygame.mouse.get_pos()
    clique = pygame.mouse.get_pressed()
    
    
    # Checa se o mouse está em cima
    if posicao_x < mouse[0] < posicao_x + largura and posicao_y < mouse[1] < posicao_y + altura:
        largura += 10
        posicao_x -= 5
        altura += 10
        posicao_y -= 5
        font_button = pygame.font.Font(rf"{endereço}\fonte\Minha fonte.ttf", fonte + 2)
        pygame.time.delay(10)
        pygame.draw.rect(screen, cor_ativado, (posicao_x, posicao_y, largura, altura), border_radius=arredondamento_da_borda)
        texto_surface = font_button.render(texto, True, BLACK)
        texto_rect = texto_surface.get_rect(center=(posicao_x + largura // 2, posicao_y + altura - posicao_da_letra - 10))
        screen.blit(texto_surface, texto_rect)


        if clique[0] and not clicou:  # Clique com o botão esquerdo
            largura -= 20
            altura -= 20
            posicao_x += 10
            posicao_y += 10
            font_button = pygame.font.Font(rf"{endereço}\fonte\Minha fonte.ttf", fonte - 2)
            pygame.draw.rect(screen, cor, (posicao_x, posicao_y, largura, altura), border_radius=arredondamento_da_borda)
            texto_surface = font_button.render(texto, True, BLACK)
            texto_rect = texto_surface.get_rect(center=(posicao_x + largura // 2, posicao_y + altura - posicao_da_letra - 10))
            screen.blit(texto_surface, texto_rect)
            pygame.time.delay(50)
            botao.set_volume(0.2)
            botao.play()
            clicou = True
            return True
    else:
        largura -= 10
        altura -= 10
        posicao_x += 5
        posicao_y += 5
        pygame.draw.rect(screen, cor, (posicao_x, posicao_y, largura, altura), border_radius=arredondamento_da_borda)
        texto_surface = font_button.render(texto, True, BLACK)
        texto_rect = texto_surface.get_rect(center=(posicao_x + largura // 2, posicao_y + altura - posicao_da_letra))
        screen.blit(texto_surface, texto_rect)

        

    if imagem_path:
        imagem = pygame.image.load(imagem_path)
        imagem = pygame.transform.scale(imagem, (largura_da_imagem, altura_da_imagem))
        screen.blit(imagem, (posicao_x + (largura - largura_da_imagem)//2, posicao_y + Distancia_de_cima))
    

    if not clique[0]:
        clicou = False

    return False

        

tempo_por_letra = 100  # milissegundos
inicio_texto = pygame.time.get_ticks()
quantidade_letras = 0

input_boxes = [
    {"label": "Nome", "rect": pygame.Rect(450, 150, 400, 50), "text": "", "active": False, "peritido": TEXTO},
    {"label": "Idade", "rect": pygame.Rect(450, 220, 400, 50), "text": "", "active": False, "peritido": INTEIRO},
    {"label": "Altura", "rect": pygame.Rect(450, 290, 400, 50), "text": "", "active": False, "peritido": DECIMAIS},
    {"label": "Peso", "rect": pygame.Rect(450, 360, 400, 50), "text": "", "active": False, "peritido": DECIMAIS}
]


input_usuario = {"label": "Usuario", "rect": pygame.Rect(450, 150, 400, 50), "text": "", "active": False, "peritido": TEXTO}

def botao_de_confirmação(texto):
    fonte = pygame.font.SysFont("Arial", 23)
    
    
    while True:
        screen.blit(imagem_fundo_secundario, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        
        texto_renderizado = fonte_alternativa.render(texto, True, BLACK)
        pygame.draw.rect(screen, (170, 170, 170), (350, 150, 550, 300), border_radius=10)
        screen.blit(texto_renderizado, (360, 180))

        if desenhar_botao("Sim", 400, 380, 70, 50, 24, (100, 100, 160), (70, 70, 130), 4):
            pygame.event.clear()
            return True

        if desenhar_botao("Não", 750, 380, 70, 50, 24, (100, 100, 160), (70, 70, 130), 4):
            pygame.event.clear()
            return False
        
        pygame.display.update()

def Mensagem_de_aviso(texto):
    pygame.time.delay(20)
    erro.set_volume(1)
    erro.play()
    while True:
        screen.blit(imagem_fundo_secundario, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        
        texto_renderizado = fonte_alternativa.render(texto, True, BLACK)
        pygame.draw.rect(screen, (150, 150, 150), (350, 150, 550, 300), border_radius=10)
        screen.blit(texto_renderizado, (360, 180))

        if desenhar_botao("Ok", 750, 380, 70, 50, 24, (100, 100, 160), (70, 70, 130), 4):
            pygame.event.clear()
            return False
        
        pygame.display.update()

clicou = False  # variável global ou externa ao loop principal

def desenhar_texto(dados: list, cor, x, y):
    for status in dados:
        texto = font_sub.render(status, True, cor)
        screen.blit(texto, (x, y))
        y += 40

def desenhar_sub_texto(dados: list, cor, x, y):
    for status in dados:
        texto = font_button.render(status, True, cor)
        screen.blit(texto, (x, y))
        y += 36


def alternativas(posicao_x, posicao_y, questao, alternativa_1, alternativa_2, selecionada, largura = 700):
    global clicou  # precisa ser global ou controlada pelo escopo externo

    mouse = pygame.mouse.get_pos()
    clique = pygame.mouse.get_pressed()

    pygame.draw.rect(screen, (170, 170, 170), (posicao_x, posicao_y, largura, 100), border_radius=10)

    # Exibir a questão
    texto_questao = fonte.render(questao, True, (0, 0, 0))
    screen.blit(texto_questao, (posicao_x + 10, posicao_y + 5))

    # Coordenadas das bolinhas
    raio = 10
    bolinha1 = (posicao_x + 20, posicao_y + 40)
    bolinha2 = (posicao_x + 20, posicao_y + 80)

    # Exibir texto das alternativas
    texto1 = fonte_alternativa.render(alternativa_1, True, (0, 0, 0))
    texto2 = fonte_alternativa.render(alternativa_2, True, (0, 0, 0))
    screen.blit(texto1, (bolinha1[0] + 20, bolinha1[1] - 10))
    screen.blit(texto2, (bolinha2[0] + 20, bolinha2[1] - 10))

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

# 📌 Conexão inicial e criação das tabelas
def inicializar_banco():
    conexao = sqlite3.connect(endereco_banco_de_dados)
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        idade INTEGER,         
        altura INTEGER,
        peso INTEGER,
        genero TEXT,
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
        arma INTEGER,
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
        item LIST,
        quantidade INTEGER,
        FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
    )""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS skin (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario_id INTEGER,
        rosto INTEGER,
        camisa INTEGER,
        mao INTEGER,
        braço INTEGER,
        calça INTEGER,
        sapatos INTEGER,
        FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
    )""")

    conexao.commit()
    conexao.close()

nivel = 1
experiencia = 0

# 🧠 Função para criar personagem completo
def criar_personagem(nome, idade, altura, peso, genero, classe, dano, velocidade, defesa, vida, arma):
    global nivel, experiencia
    conexao = sqlite3.connect(endereco_banco_de_dados)
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")


    # Inserir usuário
    cursor.execute("""
        INSERT INTO usuarios (nome, idade, altura, peso, genero, classe) VALUES (?, ?, ?, ?, ?, ?)
    """, (nome, idade, altura, peso, genero, classe))
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
    INSERT INTO inventario (usuario_id, item, quantidade)
    VALUES (?, ?, ?)
""", (usuario_id, arma, 1))

    cursor.execute("""
        INSERT INTO skin (usuario_id, rosto, camisa, mao, braço, calça, sapatos)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (usuario_id, 0, 0, 0, 0, 0, 0))

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
        SELECT item, quantidade
        FROM inventario
        WHERE usuario_id = ?
    """, (usuario_id,))

    inventario = cursor.fetchall()
    conexao.close()
    return inventario

def ver_se_o_usuario_ja_existe(nome):
    conexao = sqlite3.connect(endereco_banco_de_dados)
    cursor = conexao.cursor()

    cursor.execute("PRAGMA foreign_keys = ON")

    cursor.execute("SELECT id, idade, altura, peso, classe FROM usuarios WHERE nome = ?", (nome,))
    usuario = cursor.fetchone()

    if usuario:
        Mensagem_de_aviso("Nome já existente")
        conexao.close()
        return True
    else:
        conexao.close()
        return False
    

def ver_se_o_usuario_nao_existe(nome):
    conexao = sqlite3.connect(endereco_banco_de_dados)
    cursor = conexao.cursor()

    cursor.execute("PRAGMA foreign_keys = ON")

    cursor.execute("SELECT id, idade, altura, peso, classe FROM usuarios WHERE nome = ?", (nome,))
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
        SELECT nome, idade, altura, genero, peso, classe
        FROM usuarios
        WHERE nome = ?
    """, (nome,))

    dados = cursor.fetchone()
    conexao.close()
    return dados

contador = 1


# Loop principal
if __name__ == "__main__":
    if not os.path.exists(rf"{endereço}\usuario.json"):
        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if evento.type == pygame.QUIT:
                    rodando = False

                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    for box in input_boxes:
                        box["active"] = box["rect"].collidepoint(evento.pos)
                    input_usuario["active"] = input_usuario["rect"].collidepoint(evento.pos)

                elif evento.type == pygame.KEYDOWN:
                    for box in input_boxes:
                        if box["active"]:
                            if evento.key == pygame.K_BACKSPACE:
                                box["text"] = box["text"][:-1]
                            elif evento.key == pygame.K_RETURN:
                                box["active"] = False
                            else:
                                if evento.unicode in box["peritido"]:
                                    box["text"] += evento.unicode
                    if input_usuario["active"]:
                        if evento.key == pygame.K_BACKSPACE:
                            input_usuario["text"] = input_usuario["text"][:-1]
                        elif evento.key == pygame.K_RETURN:
                            input_usuario["active"] = False
                        else:
                            if evento.unicode in input_usuario["peritido"]:
                                input_usuario["text"] += evento.unicode


            screen.fill(WHITE)

            if estado == MENU:

                inicializar_banco()

                # Botão iniciar
                screen.blit(imagem_fundo, (0, 0))

            
                
                mensagens = [
                            {"texto": "Olá, seja bem-vindo", "inicio": 0},
                            {"texto": "aqui cada escolha", "inicio": 2300},
                            {"texto": "importa, então", "inicio": 4160},
                            {"texto": "cuidado!!!", "inicio": 6050},
                            {"texto": "Pressione G para iniciar", "inicio": 7850},
                            ]
                mensagens_renderizadas = ["" for _ in mensagens]

                tempo_atual = pygame.time.get_ticks()
                

                for i, msg in enumerate(mensagens):

                    
                    teclado = pygame.mixer.Sound(rf"{endereço}\efeito_sonoro\teclado\keypress-{contador}.wav")
                    teclado.set_volume(0.5)

                    

                    tempo_relativo = tempo_atual - inicio_texto
                    letras_para_mostrar = (tempo_relativo - msg["inicio"]) // tempo_por_letra

                    if letras_para_mostrar < len(msg["texto"]) and tempo_relativo >= msg["inicio"]:
                        contador += 1
                        if contador > 32:
                            contador = 1
                        mensagens_renderizadas[i] = msg["texto"][:max(0, letras_para_mostrar)]
                        teclado.play()
                        pygame.time.delay(70)
                        

                    elif letras_para_mostrar >= len(msg["texto"]):
                        
                        mensagens_renderizadas[i] = msg["texto"]
                        

                    # Renderiza sempre a quantidade certa de texto
                    imagem = font_title.render(mensagens_renderizadas[i], True, (240, 220, 255))
                    screen.blit(imagem, (50, 300 + i * 50))
                    
                    
                    
                    

                        

                    

                key = pygame.key.get_pressed()
                if key[pygame.K_g]:
                    estado =  LOGIN



            elif estado == LOGIN:
                screen.blit(imagem_fundo_secundario, (0, 0))
                if desenhar_botao("LOGIN", 200, 100, 350, 500, 30, (90, 150, 90), (60, 120, 60), 20, rf"{endereço}\Imagens\classes\entrar.png", 290, 290, fonte=27):
                    estado = ENTRAR
                if desenhar_botao("Registrar-se", 750, 100, 350, 500, 30, (150, 90, 90), (110, 50, 50), 20, rf"{endereço}\Imagens\classes\registrar-se.png", 290, 290, fonte=27):
                    estado = COMO_SERA_ESCOLHIDO_A_CLASSE
            
                
            elif estado == ENTRAR:
                screen.blit(imagem_fundo_secundario, (0, 0))
                pygame.draw.rect(screen, (170, 170, 170), (300, 120, 620, 130), border_radius=27)

                cor_borda = COR_ATIVA if input_usuario["active"] else COR_INATIVA
                pygame.draw.rect(screen, cor_borda, input_usuario["rect"], 2, border_radius=15)
                
                # Label
                label_surface = fonte_input.render(input_usuario["label"] + ":", True, COR_TEXTO)
                screen.blit(label_surface, (input_usuario["rect"].x - 130, input_usuario["rect"].y + 15))

                # Texto
                texto_surface = fonte_input.render(input_usuario["text"], True, COR_TEXTO)
                screen.blit(texto_surface, (input_usuario["rect"].x + 10, input_usuario["rect"].y + 10))
                usuario = input_usuario["text"]

                if desenhar_botao("Entrar", 1070, 550, 180, 40, 17, (160, 210, 190), (100, 100, 100), 25):
                    if ver_se_o_usuario_nao_existe(usuario):
                        Mensagem_de_aviso("Nome não encontrado")
                    else:
                        with open(rf"{endereço}\usuario.json", "w") as arquivo:
                            json.dump({"usuario": usuario,
                                       "dados_pessoais": obter_dados_usuario_por_nome(usuario),
                                       "inventario": obter_inventario_do_usuario(obter_id_usuario_por_nome(usuario))}, arquivo)
                        break
                
                if desenhar_botao("<- Voltar", 50, 550, 185, 40, 17, (140, 140, 250), (100, 100, 210), 10):
                    estado = LOGIN

            elif estado == COMO_SERA_ESCOLHIDO_A_CLASSE:
                screen.blit(imagem_fundo_secundario, (0, 0))
                if desenhar_botao("<- Voltar", 50, 550, 185, 50, 17, (140, 140, 250), (100, 100, 210), 10):
                    estado = LOGIN
                texto = font_title.render("Como deseja escolher sua classe", True, WHITE)
                screen.blit(texto, (200, 40))
                if desenhar_botao("Escolher Classe", 100, 125, 300, 400, 30, (130, 90, 180), (100, 60, 150), 20, rf"{endereço}\Imagens\classes\escolha.png", 260, 260):
                    estado = ESCOLHA_DE_CLASSES
                if desenhar_botao("Classe aleatória", 500, 125, 300, 400, 30, (140, 110, 110), (110, 80, 80), 20, rf"{endereço}\Imagens\classes\aleatorio.png", 260, 260):
                    if botao_de_confirmação("Você quer escolher sua classe aleaóriamente"):
                        estado = ALEATÓRIO
                if desenhar_botao("personalidade", 900, 125, 300, 400, 30, (120, 180, 120), (50, 150, 50), 20, rf"{endereço}\Imagens\classes\personalidade.png", 260, 260):
                    estado = PERSONALIDADE



            elif estado == ESCOLHA_DE_CLASSES:
                screen.blit(imagem_fundo_secundario, (0, 0))
                texto = font_title.render("Escolha sua classe", True, WHITE)
                screen.blit(texto, (420, 40))

                if desenhar_botao("<- Voltar", 50, 580, 185, 40, 13, (160, 160, 160), (100, 100, 100), 25):
                    estado = COMO_SERA_ESCOLHIDO_A_CLASSE

                if desenhar_botao("Próximo ->", 1050, 580, 200, 40, 13, (160, 160, 160), (100, 100, 100), 25):
                    estado = ESCOLHA_DE_CLASSES_JANELA_2

                if desenhar_botao("Arqueiro", 60, 140, 270, 400, 20, (93, 166, 170), (63, 136, 140), 25, rf"{endereço}\Imagens\classes\arco e flecha.png", 250, 250):
                    if botao_de_confirmação("Você realmente deseja a classe Arqueiro?"):
                        estado = ARQUEIRO

                if desenhar_botao("Espadachin", 370, 140, 270, 400, 20, (168, 168, 168), (138, 138, 138), 25, rf"{endereço}\Imagens\classes\espada.png", 250, 250):
                    if botao_de_confirmação("Você realmente deseja a classe Espadachin?"):
                        estado = ESPADACHIN

                if desenhar_botao("Assassino", 680, 140, 270, 400, 20, (170, 93, 94), (140, 63, 64), 25, rf"{endereço}\Imagens\classes\faca.png", 250, 250):
                    if botao_de_confirmação("Você realmente deseja a classe Assassino?"):
                        estado = ASSASSINO

                if desenhar_botao("Escudeiro", 990, 140, 270, 400, 20, (170, 149, 93), (140, 119, 63), 25, rf"{endereço}\Imagens\classes\escudo.png", 250, 250):
                    if botao_de_confirmação("Você realmente deseja a classe Escudeiro?"):
                        estado = ESCUDEIRO



            elif estado == ESCOLHA_DE_CLASSES_JANELA_2:
                screen.blit(imagem_fundo_secundario, (0, 0))
                texto = font_title.render("Escolha sua classe", True, WHITE)
                screen.blit(texto, (450, 40))

                if desenhar_botao("<- Voltar", 50, 580, 185, 40, 13, (160, 160, 160), (100, 100, 100), 25):
                    estado = ESCOLHA_DE_CLASSES

                desenhar_botao("Próximo ->", 1050, 580, 200, 40, 13, (120, 120, 120), (120, 120, 120), 25)

                if desenhar_botao("Lanceiro", 60, 140, 270, 400, 20, (136, 93, 170), (106, 63, 140), 25, rf"{endereço}\Imagens\classes\lanca.png", 250, 250):
                    if botao_de_confirmação("Você realmente que a classe Lanceiro?"):
                        estado = LANCEIRO

                if desenhar_botao("Batedor", 370, 140, 270, 400, 20, (99, 170, 93), (69, 140, 63), 25, rf"{endereço}\Imagens\classes\besta.png", 250, 250):
                    if botao_de_confirmação("Você realmente que a classe Batedor?"):
                        estado = BATEDOR
                


            elif estado == ARQUEIRO:
                classe = ARQUEIRO
                screen.blit(imagem_fundo_secundario, (0, 0))
                pygame.draw.rect(screen, (93, 166, 170), (70, 70, 1160, 510), border_radius=27)
                texto = font_title.render("Arqueiro", True, (0, 0, 80))
                screen.blit(texto, (texto.get_rect(center=(650, 110))))
                if desenhar_botao("Próximo ->", 970, 500, 200, 40, 13, (143, 216, 220), (73, 146, 150), 25):
                    estado = ARQUEIRO2
                pygame.draw.aaline(screen, (0, 0, 80), (650, 140), (650, 580), 2)
                desenhar_texto(["Dano: 9", "Velocidade: 6", "Defesa: 2", "Vida: 11", "Arma: Arco E Flexa Velho", "Buff: x1.4 XP"], (0, 0, 90), 80, 170)

                desenhar_sub_texto(["HABILIDADE: Disparo preciso", "PASSIVA", "Nivel: 20+         custo: 0", "Coodowncooldown: 0.0",
                                    "_______________________________",
                                    "HABILIDADE: Tiro rápido", "PASSIVA", "Nivel: 15+         custo: 0", "Coodowncooldown: 0.0"], (0, 0, 90), 660, 170)

            elif estado == ARQUEIRO2:
                screen.blit(imagem_fundo_secundario, (0, 0))
                pygame.draw.rect(screen, (93, 166, 170), (70, 70, 1160, 510), border_radius=27)
                texto = font_title.render("Batedor", True, (0, 0, 80))
                screen.blit(texto, (texto.get_rect(center=(650, 110))))
                if desenhar_botao("Próximo ->", 970, 500, 200, 40, 13, (143, 216, 220), (73, 146, 150), 25):
                    estado = DADOS_PESSOAIS
                pygame.draw.aaline(screen, (0, 0, 80), (650, 140), (650, 580), 2)
                desenhar_sub_texto(["HABILIDADE: Chuva de flechas", "PASSIVA", "Nivel: 30+   custo: 0", "Coodowncooldown: 0.0",
                                    "_______________________________",
                                    "HABILIDADE: Disparo explosivo", "ATIVA", "Nivel: 40+   custo: 25", "Coodowncooldown: 20.0"], (0, 0, 90), 80, 170)
                
                desenhar_sub_texto(["HABILIDADE: Camuflagem", "ATIVA", "Nivel: 35+   custo: 20", "Coodowncooldown: 15.0",
                                    "_______________________________",
                                    ], (0, 0, 90), 660, 170)






            elif estado == ESPADACHIN:
                classe = ESPADACHIN
                screen.blit(imagem_fundo_secundario, (0, 0))
                pygame.draw.rect(screen, (168, 168, 168), (70, 70, 1160, 510), border_radius=27)
                texto = font_title.render("Espadachin", True, (50, 50, 50))
                screen.blit(texto, (texto.get_rect(center=(650, 110))))
                if desenhar_botao("Próximo ->", 970, 500, 200, 40, 13, (218, 218, 218), (148, 148, 148), 25):
                    estado = ESPADACHIN2
                pygame.draw.aaline(screen, (50, 50, 50), (650, 140), (650, 580), 2)
                desenhar_texto(["Dano: 12", "Velocidade: 4", "Defesa: 3", "Vida: 12", "Arma: Espada Cega", "Buff: x1.2 XP"], (60, 60, 60), 80, 170)

                desenhar_sub_texto(["HABILIDADE: Golpe de espada", "PASSIVA", "Nivel: 20+         custo: 0", "Coodowncooldown: 0.0",
                                    "_______________________________",
                                    "HABILIDADE: Defesa de espada", "PASSIVA", "Nivel: 15+         custo: 0", "Coodowncooldown: 0.0"], (60, 60, 60), 660, 170)

            elif estado == ESPADACHIN2:
                screen.blit(imagem_fundo_secundario, (0, 0))
                pygame.draw.rect(screen, (168, 168, 168), (70, 70, 1160, 510), border_radius=27)
                texto = font_title.render("Assassino", True, (50, 50, 50))
                screen.blit(texto, (texto.get_rect(center=(650, 110))))
                if desenhar_botao("Próximo ->", 970, 500, 200, 40, 13, (218, 218, 218), (148, 148, 148), 25):
                    estado = DADOS_PESSOAIS

                pygame.draw.aaline(screen, (50, 50, 50), (650, 140), (650, 580), 2)

                desenhar_sub_texto(["HABILIDADE: Ataque rápido", "PASSIVA", "Nivel: 15+   custo: 0", "Coodowncooldown: 0.0",
                                    "_______________________________",
                                    "HABILIDADE: Corte preciso", "ATIVA", "Nivel: 30+   custo: 20", "Coodowncooldown: 15.0"], (60, 60, 60), 80, 170)
                
                desenhar_sub_texto(["HABILIDADE: Bloqueio de espada", "ATIVA", "Nivel: 25+   custo: 15", "Coodowncooldown: 10.0",
                                    "_______________________________",
                                    ], (60, 60, 60), 660, 170)


            elif estado == ASSASSINO:
                classe = ASSASSINO
                screen.blit(imagem_fundo_secundario, (0, 0))
                pygame.draw.rect(screen, (170, 93, 94), (70, 70, 1160, 510), border_radius=27)
                texto = font_title.render("Assassino", True, (80, 0, 0))
                screen.blit(texto, (texto.get_rect(center=(650, 110))))
                if desenhar_botao("Próximo ->", 970, 500, 200, 40, 13, (220, 143, 144), (150, 73, 74), 25):
                    estado = ASSASSINO2
                pygame.draw.aaline(screen, (80, 0, 0), (650, 140), (650, 580), 2)

                desenhar_texto(["Dano: 10", "Velocidade: 5", "Defesa: 2", "Vida: 10", "Arma: Adaga Sem Ponta", "Buff: x1.5 XP"], (90, 0, 0), 80, 170)

                desenhar_sub_texto(["HABILIDADE: Furtividade", "PASSIVA", "Nivel: 20+         custo: 0", "Coodowncooldown: 0.0",
                                    "_______________________________",
                                    "HABILIDADE: Evasão", "PASSIVA", "Nivel: 30+         custo: 0", "Coodowncooldown: 0.0"], (90, 0, 0), 660, 170)

            elif estado == ASSASSINO2:
                screen.blit(imagem_fundo_secundario, (0, 0))
                pygame.draw.rect(screen, (170, 93, 94), (70, 70, 1160, 510), border_radius=27)
                texto = font_title.render("Assassino", True, (80, 0, 0))
                screen.blit(texto, (texto.get_rect(center=(650, 110))))
                if desenhar_botao("Próximo ->", 970, 500, 200, 40, 13, (220, 143, 144), (150, 73, 74), 25):
                    estado = DADOS_PESSOAIS

                pygame.draw.aaline(screen, (80, 0, 0), (650, 140), (650, 580), 2)

                desenhar_sub_texto(["HABILIDADE: Sangramento", "PASSIVA", "Nivel: 40+   custo: 0", "Coodowncooldown: 0.0",
                                    "_______________________________",
                                    "HABILIDADE: Golpe mortal", "ATIVA", "Nivel: 60+   custo: 30", "Coodowncooldown: 15.0"], (90, 0, 0), 80, 170)
                
                desenhar_sub_texto(["HABILIDADE: Invisibilidade", "ATIVA", "Nivel: 50+   custo: 20", "Coodowncooldown: 10.0",
                                    "_______________________________",
                                    ], (90, 0, 0), 660, 170)
                



            elif estado == ESCUDEIRO:
                classe = ESCUDEIRO
                screen.blit(imagem_fundo_secundario, (0, 0))
                pygame.draw.rect(screen, (170, 149, 93), (70, 70, 1160, 510), border_radius=27)
                texto = font_title.render("Escudeiro", True, (90, 60, 30))
                screen.blit(texto, (texto.get_rect(center=(650, 110))))
                if desenhar_botao("Próximo ->", 970, 500, 200, 40, 13, (220, 199, 143), (150, 129, 73), 25):
                    estado = ESCUDEIRO2
                pygame.draw.aaline(screen, (90, 60, 30), (650, 140), (650, 580), 2)

                desenhar_texto(["Dano: 8", "Velocidade: 3", "Defesa: 5", "Vida: 15", "Arma: Escudo De Mão", "Buff: x1.0 XP"], (100, 70, 40), 80, 170)

                desenhar_sub_texto(["HABILIDADE: Bloqueio de ataque", "PASSIVA", "Nivel: 20+         custo: 0", "Coodowncooldown: 0.0",
                                    "_______________________________",
                                    "HABILIDADE: Contra-ataque", "PASSIVA", "Nivel: 25+         custo: 0", "Coodowncooldown: 0.0"], (100, 70, 40), 660, 170)

            elif estado == ESCUDEIRO2:
                screen.blit(imagem_fundo_secundario, (0, 0))
                pygame.draw.rect(screen, (170, 149, 93), (70, 70, 1160, 510), border_radius=27)
                texto = font_title.render("Escudeiro", True, (90, 60, 30))
                screen.blit(texto, (texto.get_rect(center=(650, 110))))
                if desenhar_botao("Próximo ->", 970, 500, 200, 40, 13, (220, 199, 143), (150, 129, 73), 25):
                    estado = DADOS_PESSOAIS

                pygame.draw.aaline(screen, (90, 60, 30), (650, 140), (650, 580), 2)

                desenhar_sub_texto(["HABILIDADE: Proteção de aliados", "PASSIVA", "Nivel: 30+   custo: 20", "Coodowncooldown: 15.0",
                                    "_______________________________",
                                    "HABILIDADE: Ataque com escudo", "ATIVA", "Nivel: 20+   custo: 15", "Coodowncooldown: 10.0"], (100, 70, 40), 80, 170)
                
                desenhar_sub_texto(["HABILIDADE: Defesa reforçada", "ATIVA", "Nivel: 35+   custo: 20", "Coodowncooldown: 15.0",
                                    "_______________________________",
                                    ], (100, 70, 40), 660, 170)
            


            elif estado == LANCEIRO:
                classe = LANCEIRO
                screen.blit(imagem_fundo_secundario, (0, 0))
                pygame.draw.rect(screen, (136, 93, 170), (70, 70, 1160, 510), border_radius=27)
                texto = font_title.render("Lanceiro", True, (60, 0, 80))
                screen.blit(texto, (texto.get_rect(center=(650, 110))))
                if desenhar_botao("Próximo ->", 970, 500, 200, 40, 13, (186, 143, 220), (116, 73, 150), 25):
                    estado = LANCEIRO2
                pygame.draw.aaline(screen, (60, 0, 80), (650, 140), (650, 580), 2)
                desenhar_texto(["Dano: 11", "Velocidade: 4", "Defesa: 4", "Vida: 13", "Arma: Lança Com Cabo Quebrado", "Buff: x1.3 XP"], (80, 0, 100), 80, 170)
                desenhar_sub_texto(["HABILIDADE: Ataque de lança", "PASSIVA", "Nivel: 20+         custo: 0", "Coodowncooldown: 0.0",
                                    "_______________________________",
                                    "HABILIDADE: Empurrão", "PASSIVA", "Nivel: 15+         custo: 0", "Coodowncooldown: 0.0"], (70, 0, 90), 660, 170)

            elif estado == LANCEIRO2:
                screen.blit(imagem_fundo_secundario, (0, 0))
                pygame.draw.rect(screen, (136, 93, 170), (70, 70, 1160, 510), border_radius=27)
                texto = font_title.render("Lanceiro", True, (60, 0, 80))
                screen.blit(texto, (texto.get_rect(center=(650, 110))))
                if desenhar_botao("Próximo ->", 970, 500, 200, 40, 13, (186, 143, 220), (116, 73, 150), 25):
                    estado = DADOS_PESSOAIS

                pygame.draw.aaline(screen, (60, 0, 80), (650, 140), (650, 580), 2)

                desenhar_sub_texto(["HABILIDADE: Ataque em área", "PASSIVA", "Nivel: 30+   custo: 0", "Coodowncooldown: 0.0",
                                    "_______________________________",
                                    "HABILIDADE: Golpe de lança", "ATIVA", "Nivel: 40+   custo: 25", "Coodowncooldown: 20.0"], (70, 0, 90), 80, 170)
                
                desenhar_sub_texto(["HABILIDADE: Defesa com lança", "ATIVA", "Nivel: 35+   custo: 20", "Coodowncooldown: 15.0",
                                    "_______________________________",
                                    ], (70, 0, 90), 660, 170)



            elif estado == BATEDOR:
                classe = BATEDOR
                screen.blit(imagem_fundo_secundario, (0, 0))
                pygame.draw.rect(screen, (99, 170, 93), (70, 70, 1160, 510), border_radius=27)
                texto = font_title.render("Batedor", True, (0, 80, 0))
                screen.blit(texto, (texto.get_rect(center=(650, 110))))
                if desenhar_botao("Próximo ->", 970, 500, 200, 40, 13, (149, 220, 143), (79, 150, 73), 25):
                    estado = BATEDOR2
                pygame.draw.aaline(screen, (0, 80, 0), (650, 140), (650, 580), 2)
                desenhar_texto(["Dano: 7", "Velocidade: 5", "Defesa: 3", "Vida: 14", "Arma: Soco Espinhado", "Buff: x1.1 XP"], (0, 100, 0), 80, 170)
                desenhar_sub_texto(["HABILIDADE: Ataque silencioso", "PASSIVA", "Nivel: 15+         custo: 0", "Coodowncooldown: 0.0",
                                    "_______________________________",
                                    "HABILIDADE: Evasão rápida", "PASSIVA", "Nivel: 20+         custo: 0", "Coodowncooldown: 0.0"], (0, 90, 0), 660, 170)

            elif estado == BATEDOR2:
                screen.blit(imagem_fundo_secundario, (0, 0))
                pygame.draw.rect(screen, (99, 170, 93), (70, 70, 1160, 510), border_radius=27)
                texto = font_title.render("Batedor", True, (0, 80, 0))
                screen.blit(texto, (texto.get_rect(center=(650, 110))))
                if desenhar_botao("Próximo ->", 970, 500, 200, 40, 13, (149, 220, 143), (79, 150, 73), 25):
                    estado = DADOS_PESSOAIS
                pygame.draw.aaline(screen, (0, 80, 0), (650, 140), (650, 580), 2)
                desenhar_sub_texto(["HABILIDADE: Exploração furtiva", "PASSIVA", "Nivel: 15+   custo: 0", "Coodowncooldown: 0.0",
                                    "_______________________________",
                                    "HABILIDADE: Ataque surpresa", "ATIVA", "Nivel: 3040+   custo: 2025", "Coodowncooldown: 15.0"], (0, 90, 0), 80, 170)
                desenhar_sub_texto(["HABILIDADE: Fuga rápida", "ATIVA", "Nivel: 35+   custo: 25", "Coodowncooldown: 20.0",
                                    "_______________________________",
                                    ], (0, 90, 0), 660, 170)

            elif estado == DADOS_PESSOAIS:
                fonte_input = pygame.font.SysFont("arial", 28)
                screen.blit(imagem_fundo_secundario, (0, 0))
                pygame.draw.rect(screen, (175, 175, 175), (200, 100, 900, 400), border_radius=20)

                genero = alternativas(875, 200, "Qual sera seu genero", "Masculino", "Feminino", genero, 200)

                for box in input_boxes:
                    cor_borda = COR_ATIVA if box["active"] else COR_INATIVA
                    pygame.draw.rect(screen, cor_borda, box["rect"], 2, border_radius=15)
                    
                    # Label
                    label_surface = fonte_input.render(box["label"] + ":", True, COR_TEXTO)
                    screen.blit(label_surface, (box["rect"].x - 120, box["rect"].y + 10))

                    # Texto
                    texto_surface = fonte_input.render(box["text"], True, COR_TEXTO)
                    screen.blit(texto_surface, (box["rect"].x + 10, box["rect"].y + 10))

                    if "," in box["text"]:
                        box["text"] = box["text"].replace(",", ".")

                    if desenhar_botao("Próximo ->", 870, 410, 200, 40, 13, (160, 160, 160), (100, 100, 100), 25):  
                        erros = []

                        for box in input_boxes:
                            label = box["label"]
                            texto = box["text"]

                            # Validação para idade (inteiro)
                            if label == "Idade":
                                if not texto.isdigit():
                                    erros.append("Idade deve conter apenas números.")

                            # Validação para altura e peso (números decimais ou inteiros)
                            elif label in ["Altura", "Peso"]:
                                try:
                                    float(texto.replace(",", "."))  # Aceita ponto ou vírgula
                                except ValueError:
                                    erros.append(f"{label} deve conter um número válido.")
                        
                        

                        dados_pessoais = {}

                        for box in input_boxes:
                            dados_pessoais[box["label"]] = box["text"]

                        dados_pessoais["Genero"] = genero

                        if dados_pessoais["Genero"] == None:
                            Mensagem_de_aviso("Genero Invalido: Selecione um genero")
                                            
                        elif len(erros) != 0:
                            estado = DADOS_PESSOAIS
                            Mensagem_de_aviso(erros[0])

                        elif not (16 <= int(dados_pessoais["Idade"]) <= 100):
                            Mensagem_de_aviso("Idade Invalida: Tente de 16 a 100")
                        
                        elif not (1.0 <= float(dados_pessoais["Altura"]) <= 3.0):
                            Mensagem_de_aviso("Altura Invalida: Tente entre 1.0 a 3.0")

                        elif not (40.0 <= float(dados_pessoais["Peso"]) <= 130.0):
                            Mensagem_de_aviso("Peso Invalido: Tente de 40.0 a 130")

                        elif ver_se_o_usuario_ja_existe(dados_pessoais["Nome"]):
                            estado = DADOS_PESSOAIS
                            Mensagem_de_aviso("Nome já existente")

                        else:
                            estado = CRIAR_E_IR



                        
            elif estado == ALEATÓRIO:
                pygame.draw.rect(screen, (0, 0, 0), (0, 0, 1300, 650))
                classes = [ARQUEIRO, ESPADACHIN, ASSASSINO, ESCUDEIRO, LANCEIRO, BATEDOR]
                estado = choice(classes)
                
            elif estado == PERSONALIDADE:
                screen.blit(imagem_fundo_secundario, (0, 0))
                if desenhar_botao("<- Voltar", 30, 580, 185, 40, 13, (160, 160, 160), (100, 100, 100), 25):
                    estado = COMO_SERA_ESCOLHIDO_A_CLASSE
                
                questao_1 = alternativas(300, 35, "Você prefere planejar tudo antes de agir ou agi no momento:", "Planejar", "Agir No Momento", questao_1)

                questao_2 = alternativas(300, 155, "Quando está sob pressão, você mantém a calma ou se estressa facilmente:", "Calma", "Estressado", questao_2)

                questao_3 = alternativas(300, 275, "Você prefere resolver problemas sozinho ou pedir ajuda:", "Sozinho", "Pedir Ajuda", questao_3)

                questao_4 = alternativas(300, 395, "Você tem facilidade para se concentrar por longos períodos:", "Sim", "Não", questao_4)

                questao_5 = alternativas(300, 515, "Você costuma ser mais lógico ou mais criativo:", "Lógico", "Criativo", questao_5)

                if desenhar_botao("Avançar ->", 1070, 580, 200, 40, 15, (160, 160, 160), (100, 100, 100), 25):
                    if questao_1 != None and questao_2 != None and questao_3 != None and questao_4 != None and questao_5 != None:
                        estado = PERSONALIDADE_tela_2
                    else:
                        Mensagem_de_aviso("Preencha todas as questões!")
                
            elif estado == PERSONALIDADE_tela_2:
                screen.blit(imagem_fundo_secundario, (0, 0))
                if desenhar_botao("<- Voltar", 30, 580, 185, 40, 13, (160, 160, 160), (100, 100, 100), 25):
                    estado = PERSONALIDADE
                
                questao_6 = alternativas(300, 35, "Você prefere força bruta ou agilidade para lutar:", "Força", "Agilidade", questao_6)

                questao_7 = alternativas(300, 155, "Você aguenta mais tempo lutando ou tem explosões curtas de energia:", "Resistente", "Explosoes", questao_7)

                questao_8 = alternativas(300, 275, "Você prefere ataques rápidos ou golpes poderosos:", "Rápido", "Poderoso", questao_8)

                questao_9 = alternativas(300, 395, "Você é bom em esquivar ou em bloquear ataques:", "Esquiva", "Bloquear", questao_9)

                questao_10 = alternativas(300, 515, "Você se considera mais resistente a dores ou mais resistente ao cansaço:", "Dor", "Cansaço", questao_10)

                if desenhar_botao("Avançar ->", 1070, 580, 200, 40, 15, (160, 160, 160), (100, 100, 100), 25):
                    if questao_6 != None and questao_7 != None and questao_8 != None and questao_9 != None and questao_10 != None:
                        estado = PERSONALIDADE_tela_3
                    else:
                        Mensagem_de_aviso("Preencha todas as questões!")
            
            elif estado == PERSONALIDADE_tela_3:
                screen.blit(imagem_fundo_secundario, (0, 0))
                if desenhar_botao("<- Voltar", 30, 580, 185, 40, 13, (160, 160, 160), (100, 100, 100), 25):
                    estado = PERSONALIDADE_tela_2
                
                questao_11 = alternativas(300, 35, "Você prefere liderar ou seguir ordens:", "Liderar", "Seguir", questao_11)

                questao_12 = alternativas(300, 155, "Você costuma ser mais amigável ou reservado com os outros:", "Amigável", "Reservado", questao_12)

                questao_13 = alternativas(300, 275, "Você confia facilmente nas pessoas:", "Sim", "Não", questao_13)

                questao_14 = alternativas(300, 395, "Você é bom em convencer e influenciar os outros:", "Sim", "Não", questao_14)

                questao_15 = alternativas(300, 515, "Você prefere resolver conflitos com conversa ou com ação:", "Conversa", "Ação", questao_15)

                if desenhar_botao("Avançar ->", 1070, 580, 200, 40, 15, (160, 160, 160), (100, 100, 100), 25):
                    if questao_11 != None and questao_12 != None and questao_13 != None and questao_14 != None and questao_15 != None:
                        estado = PERSONALIDADE_tela_4
                    else:
                        Mensagem_de_aviso("Preencha todas as questões!")

            elif estado == PERSONALIDADE_tela_4:
                screen.blit(imagem_fundo_secundario, (0, 0))
                if desenhar_botao("<- Voltar", 30, 580, 185, 40, 13, (160, 160, 160), (100, 100, 100), 25):
                    estado = PERSONALIDADE_tela_3
                
                questao_16 = alternativas(300, 35, "Você prefere ataques rápidos e furtivos ou ataques lentos e fortes:", "Furtivo", "Forte", questao_16)

                questao_17 = alternativas(300, 155, "Você é melhor em defesa ou em ataque:", "Defesa", "Ataque", questao_17)

                questao_18 = alternativas(300, 275, "Você prefere lutar sozinho ou com um parceiro:", "Individual", "Em Time", questao_18)

                questao_19 = alternativas(300, 395, "Você tem mais experiência em combate corpo a corpo ou à distância:", "Corpo A Corpo", "Distânte", questao_19)

                if desenhar_botao("Avançar ->", 1070, 580, 200, 40, 15, (160, 160, 160), (100, 100, 100), 25):
                    if questao_16 != None and questao_17 != None and questao_18 != None and questao_19 != None:
                        estado = DEFINIR_CLASSE
                    else:
                        Mensagem_de_aviso("Preencha todas as questões!")

            elif estado == DEFINIR_CLASSE:
                classes = {ARQUEIRO: 0,
                        ESPADACHIN: 0,
                        ASSASSINO: 0,
                        ESCUDEIRO: 0,
                        LANCEIRO: 0,
                        BATEDOR: 0}
                
                # PERGUNTA 1

                if questao_1 == 'Planejar':
                    classes["espadachin"] += 1
                    classes["arqueiro"] += 2
                    classes["assassino"] += 3

                elif questao_1 == 'Agir No Momento':
                    classes["batedor"] += 3
                    classes["lanceiro"] += 1
                    classes["escudeiro"] += 2

                # PERGUNTA 2

                if questao_2 == 'Calma':
                    classes["espadachin"] += 2
                    classes["arqueiro"] += 2
                    classes["assassino"] += 1
                    classes["escudeiro"] += 3

                elif questao_2 == 'Estressado':
                    classes["lanceiro"] += 2
                    classes["batedor"] += 2

                # PERGUNTA 3

                if questao_3 == 'Sozinho':
                    classes["assassino"] += 2
                    classes["batedor"] += 1
                    classes["espadachin"] += 3

                elif questao_3 == 'Pedir Ajuda':
                    classes["arqueiro"] += 2
                    classes["batedor"] += 3
                    classes["espadachin"] += 3
                    classes["escudeiro"] += 1

                # PERGUNTA 4

                if questao_4 == 'Sim':
                    classes["arqueiro"] += 3
                    classes["batedor"] += 1
                    classes["lanceiro"] += 3
                    classes["assassino"] += 2
                    classes["escudeiro"] += 2

                elif questao_4 == 'Não':
                    classes["espadachin"] += 3

                # PERGUNTA 5

                if questao_5 == 'Lógico':
                    classes["espadachin"] += 2
                    classes["escudeiro"] += 2
                    classes["batedor"] += 3

                elif questao_5 == 'Criativo':
                    classes["assassino"] += 3
                    classes["arqueiro"] += 2
                    classes["lanceiro"] += 2


                # Com base nos dados fisicos

                # Pergunta 1
                
                if questao_6 == 'Força':
                    classes["escudeiro"] += 3
                    classes["espadachin"] += 1
                    classes["batedor"] += 1

                elif questao_6 == 'Agilidade':
                    classes["batedor"] += 1
                    classes["lanceiro"] += 2
                    classes["assassino"] += 2
                    classes["espadachin"] += 1
                    classes["arqueiro"] += 3

                # PERGUNTA 2

                if questao_7 == 'Resistente':
                    classes["escudeiro"] += 2
                    classes["espadachin"] += 2
                    classes["assassino"] += 4
                    classes["batedor"] += 1

                elif questao_7 == 'Explosoes':
                    classes["batedor"] += 3
                    classes["lanceiro"] += 2
                    classes["arqueiro"] += 1

                # PERGUNTA 3

                if questao_8 == 'Rápido':
                    classes["arqueiro"] += 3
                    classes["assassino"] += 2
                    classes["lanceiro"] += 1
                    classes["batedor"] += 3

                elif questao_8  == 'Poderoso':
                    classes["espadachin"] += 1
                    classes["batedor"] += 2

                # PERGUNTA 4

                if questao_9 == 'Esquiva':
                    classes["arqueiro"] += 3
                    classes["batedor"] += 2
                    classes["lanceiro"] += 1
                    classes["assassino"] += 3
                    classes["espadachin"] += 2

                elif questao_9 == 'Bloquear':
                    classes["escudeiro"] += 1

                # PERGUNTA 5

                if questao_10 == 'Dor':
                    classes["escudeiro"] += 1
                    classes["lanceiro"] += 2
                    classes["espadachin"] += 3
                    classes["batedor"] += 1
                    classes["assassino"] += 2

                elif questao_10 == 'Cansaço':
                    classes["escudeiro"] += 3
                    classes["assassino"] += 2
                    classes["espadachin"] += 1
                    classes["arqueiro"] += 3

                # Com base nos dados sociais

                # PERGUNTA 1

                if questao_11 == 'Liderar':
                    classes["arqueiro"] += 3
                    classes["assassino"] += 2
                    classes["lanceiro"] += 1

                elif questao_11 == 'Seguir':
                    classes["escudeiro"] += 1
                    classes["espadachin"] += 2
                    classes["batedor"] += 3

                # PERGUNTA 2

                if questao_12 == 'Amigável':
                    classes["escudeiro"] += 3
                    classes["arqueiro"] += 2
                    classes["espadachin"] += 1

                elif questao_12 == 'Reservado':
                    classes["batedor"] += 1
                    classes["assassino"] += 2
                    classes["lanceiro"] += 3

                # PERGUNTA 3

                if questao_13 == 'Sim':
                    classes["escudeiro"] += 2
                    classes["espadachin"] += 3
                    classes["arqueiro"] += 2

                elif questao_13 == 'Não':
                    classes["assassino"] += 2
                    classes["lanceiro"] += 2
                    classes["batedor"] += 2

                # PERGUNTA 4

                if questao_14 == 'Sim':
                    classes["escudeiro"] += 3
                    classes["arqueiro"] += 3
                    classes["espadachin"] += 3

                elif questao_14 == 'Não':
                    classes["assassino"] += 1
                    classes["batedor"] += 1
                    classes["lanceiro"] += 1

                # PERGUNTA 5

                if questao_15 == 'Conversa':
                    classes["espadachin"] += 1
                    classes["arqueiro"] += 2
                    classes["assassino"] += 2
                    classes["escudeiro"] += 1

                elif questao_15 == 'Ação':
                    classes["batedor"] += 2
                    classes["lanceiro"] += 1

                # Com base nos dados sociais

                # PERGUNTA 1

                if questao_16 == 'Furtivo':
                    classes["arqueiro"] += 2
                    classes["lanceiro"] += 1
                    classes["assassino"] += 3

                elif questao_16 == 'Forte':
                    classes["batedor"] += 2
                    classes["espadachin"] += 3
                    classes["escudeiro"] += 3

                # PERGUNTA 2

                if questao_17 == 'Defesa':
                    classes["escudeiro"] += 3

                elif questao_17 == 'Ataque':
                    classes["lanceiro"] += 1
                    classes["espadachin"] += 1
                    classes["assassino"] += 1
                    classes["arqueiro"] += 1
                    classes["batedor"] += 1

                # PERGUNTA 3

                if questao_18 == 'Individual':
                    classes["assassino"] += 4
                    classes["batedor"] += 1
                    classes["lanceiro"] += 3

                elif questao_18 == 'Em Time':
                    classes["arqueiro"] += 2
                    classes["espadachin"] += 1
                    classes["escudeiro"] += 1

                # PERGUNTA 4

                if questao_19 == 'Corpo A Corpo':
                    classes["escudeiro"] += 2
                    classes["batedor"] += 1
                    classes["espadachin"] += 2
                    classes["assassino"] += 3

                elif questao_19 == 'Distânte':
                    classes["lanceiro"] += 2
                    classes["arqueiro"] += 1

                estado = max(classes, key=classes.get)

            elif estado == CRIAR_E_IR:
                screen.blit(imagem_fundo_secundario, (0, 0))
                dados_pessoais["Classe"] = classe

                if dados_pessoais["Classe"] == ASSASSINO:
                    criar_personagem(dados_pessoais["Nome"],
                                    dados_pessoais["Idade"],
                                    dados_pessoais["Altura"],
                                    dados_pessoais["Peso"],
                                    dados_pessoais["Genero"],
                                    ASSASSINO,
                                    10, 5, 2, 10, "Adaga Sem Ponta")
                    
                elif dados_pessoais["Classe"] == ESPADACHIN:
                    criar_personagem(dados_pessoais["Nome"],
                                    dados_pessoais["Idade"],
                                    dados_pessoais["Altura"],
                                    dados_pessoais["Peso"],
                                    dados_pessoais["Genero"],
                                    ESPADACHIN,
                                    12, 4, 3, 12, "Espada Cega")
                    
                elif dados_pessoais["Classe"] == LANCEIRO:
                    criar_personagem(dados_pessoais["Nome"],
                                    dados_pessoais["Idade"],
                                    dados_pessoais["Altura"],
                                    dados_pessoais["Peso"],
                                    dados_pessoais["Genero"],
                                    LANCEIRO,
                                    11, 4, 4, 13, "Lança Com Cabo Quebrado")
                
                elif dados_pessoais["Classe"] == ARQUEIRO:
                    criar_personagem(dados_pessoais["Nome"],
                                    dados_pessoais["Idade"],
                                    dados_pessoais["Altura"],
                                    dados_pessoais["Peso"],
                                    dados_pessoais["Genero"],
                                    ARQUEIRO,
                                    9, 6, 2, 11, "Arco E Flexa Velho")
                    
                elif dados_pessoais["Classe"] == BATEDOR:
                    criar_personagem(dados_pessoais["Nome"],
                                    dados_pessoais["Idade"],
                                    dados_pessoais["Altura"],
                                    dados_pessoais["Peso"],
                                    dados_pessoais["Genero"],
                                    BATEDOR,
                                    7, 5, 3, 14, "Soco Espinhado")
                    
                elif dados_pessoais["Classe"] == ESCUDEIRO:
                    criar_personagem(dados_pessoais["Nome"],
                                    dados_pessoais["Idade"],
                                    dados_pessoais["Altura"],
                                    dados_pessoais["Peso"],
                                    dados_pessoais["Genero"],
                                    ESCUDEIRO,
                                    8, 3, 5, 15, "Escudo De Mão")
                

                
                usuario = dados_pessoais["Nome"]
                
                with open(rf"{endereço}\usuario.json", "w") as arquivo:
                    json.dump({"usuario": usuario,
                               "dados_pessoais": dados_pessoais,
                               "inventario": obter_inventario_do_usuario(obter_id_usuario_por_nome(usuario))}, arquivo)
                
                break



            pygame.display.flip()
            clock.tick(16)

        
        Popen([sys.executable, rf'{endereço}\lobby.py'])

    else:
        Popen([sys.executable, rf'{endereço}\lobby.py'])