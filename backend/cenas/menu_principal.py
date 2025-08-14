import os
import sys
import json
import sqlite3
from subprocess import Popen
from tela_criacao_personagem import obter_id_usuario_por_nome  # só função lógica

endereco = os.path.dirname(os.path.abspath(__file__))
endereco_banco_de_dados = rf"{endereco}\banco_de_dados.db"

# Inicialização do usuário
if not os.path.exists(rf"{endereco}\usuario.json"):
    Popen([sys.executable, rf'{endereco}\tela_criacao_personagem.py'])
    sys.exit()

with open(rf"{endereco}\usuario.json", "r") as arquivo:
    dados = json.load(arquivo)

nome_separado = dados["dados_pessoais"]["Nome"].split()
primeiro_nome = nome_separado[0].title()
classe = dados["dados_pessoais"]["Classe"].title()
teclas = dados["keys"]

# Função para salvar dados no JSON e banco de dados
def salvar(teclas):
    id_usuario = obter_id_usuario_por_nome(dados["usuario"])
    dados["keys"] = teclas
    with open(rf"{endereco}\usuario.json", "w") as arquivo:
        json.dump(dados, arquivo, indent=4)

    conexao = sqlite3.connect(endereco_banco_de_dados)
    cursor = conexao.cursor()

    cursor.execute("UPDATE usuarios SET nome=?, classe=? WHERE id=?",
                   (dados["usuario"], dados["dados_pessoais"]["Classe"], id_usuario))

    cursor.execute("UPDATE status SET nivel=?, dano=?, velocidade=?, defesa=?, vida=?, experiencia=? WHERE usuario_id=?",
                   (dados["status"]["nivel"], dados["status"]["dano"], dados["status"]["velocidade"],
                    dados["status"]["defesa"], dados["status"]["vida"], dados["status"]["experiencia"], id_usuario))

    cursor.execute("UPDATE progresso SET capitulo=?, missao=? WHERE usuario_id=?",
                   (dados["progresso"]["capitulo"], dados["progresso"]["missao"], id_usuario))

    cursor.execute("UPDATE inventario SET item=?, quantidade=? WHERE usuario_id=?",
                   (dados["inventario"][0][0], dados["inventario"][0][1], id_usuario))

    cursor.execute("""UPDATE keys
                      SET inventario=?, correr=?, habilidades=?, habilidade_1=?, habilidade_2=?, mapa=?
                      WHERE usuario_id=?""",
                   (teclas["inventario"], teclas["correr"], teclas["habilidade"],
                    teclas["habilidade_1"], teclas["habilidade_2"], teclas["mapa"], id_usuario))

    conexao.commit()
    conexao.close()

# Estado da tela
MENU = "menu"
OPCOES = "opcoes"
estado = MENU
