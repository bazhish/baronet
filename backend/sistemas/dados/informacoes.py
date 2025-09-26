import json, sys, os; project_root = os.path.abspath(os.path.dirname(__file__)); 
while not os.path.isdir(os.path.join(project_root, ".git")) and os.path.dirname(project_root) != project_root: project_root = os.path.dirname(project_root); 
sys.path.append(project_root)
from os import path
from backend.entidades.jogador import agnes

def salvar_usuario(usuario, caminho_json):
    dados = {
        "usuario": "admimin",
        "dados_pessoais": {
            "Nome": usuario.nome,
            "Classe": usuario.nome_da_classe_do_usuário,
            "Tentativas": usuario.tentativas_restantes,
            "1° passiva": usuario.nome_da_primeira_habilidade_passiva,
            "2° passiva": usuario.nome_da_segunda_habilidade_passiva,
            "3° passiva": usuario.nome_da_terceira_habilidade_passiva,
            "Habilidade ativa": usuario.nome_da_habilidade_ativa,
            "Habilidade especial": usuario.nome_da_habilidade_especial
        },
        "inventario": {
            "itens": [getattr(item, 'nome', 'Sem nome') for item in usuario.inventario.itens],
            "equipado": {
                k: getattr(v, 'nome', 'nenhum') if v else 'nenhum'
                for k, v in usuario.inventario.equipados.items()
            },
            "dinheiro": 4000
        },
        "atributos": {
            "nivel": usuario.nível_atual,
            "experiencia": usuario.experiência_atual,
            "dano": usuario.dano_final,
            "velocidade": usuario.velocidade_final,
            "defesa": usuario.defesa_final,
            "vida": usuario.vida_final,
            "estamina": usuario.estamina_final,
            "multiplicador_de_experiencia": usuario.multiplicador_de_experiência
        },
        "armadura": {
            "elmo": usuario.nome_do_elmo,
            "peitoral": usuario.nome_do_peitoral,
            "calça": usuario.nome_da_calça,
            "botas": usuario.nome_das_botas,
        },
        "status": {
            "estado": usuario.estado,
            "pode se mover": usuario.pode_mover,
            "pode atacar": usuario.pode_atacar,
            "bloqueio ativo": usuario.bloqueio_ativo,
        },
        "progresso": {
            "capitulo": 0,
            "missao": 1
        },
        "keys": {
            "inventario": "E",
            "correr": "Lctrl",
            "habilidade": "R",
            "habilidade_1": "Z",
            "habilidade_2": "X",
            "mapa": "M"
        }
    }

    with open(caminho_json, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)

caminho_arquivo = path.join(path.dirname(__file__), "usuario.json")
salvar_usuario(agnes, caminho_arquivo)
