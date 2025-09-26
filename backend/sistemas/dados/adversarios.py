import sys, os; project_root = os.path.abspath(os.path.dirname(__file__));
while not os.path.isdir(os.path.join(project_root, ".git")) and os.path.dirname(project_root) != project_root: project_root = os.path.dirname(project_root);
sys.path.append(project_root)

import json
from backend.entidades.adversarios import (
    slime, zumbi, gárgula, lobisomem, quimera, banshee, fenrir, ghoul,
    goblin, ogro, esqueleto, oni, medusa, troll)

def salvar_adversarios_json(adversarios, arquivo="adversarioss.json"):
    """
    Recebe uma lista de adversários (monstros e demi-humanos)
    e salva os atributos principais em JSON.
    """
    dados = []

    for adv in adversarios:
        # Coleta atributos comuns
        registro = {
            "tipo": adv.__class__.__name__,  # AdversarioMonstro ou AdversarioDemiHumano
            "nome": adv.nome,
            "nível": getattr(adv, "nível", getattr(adv, "nível_atual", None)),
            "experiência": adv.experiência,
            "dano_base": getattr(adv, "dano_base", None),
            "defesa_base": getattr(adv, "defesa_base", None),
            "vida_base": getattr(adv, "vida_base", None),
            "estamina_base": getattr(adv, "estamina_base", None),
            "velocidade_base": getattr(adv, "velocidade_base", None),
            "queda": adv.queda,
            "taxa_de_queda": adv.taxa_de_queda,
            "posição_x": adv.posição_x,
            "posição_y": adv.posição_y,
            "estado": adv.estado
        }

        # Campos extras só de demi-humanos
        if hasattr(adv, "nome_da_classe"):
            registro.update({
                "classe": adv.nome_da_classe,
                "arma": adv.nome_da_arma,
                "escudo": adv.nome_do_escudo,
                "elmo": adv.nome_do_elmo,
                "peitoral": adv.nome_do_peitoral,
                "calça": adv.nome_da_calça,
                "botas": adv.nome_das_botas,
                "habilidades": {
                    "passiva_1": adv.nome_da_primeira_habilidade_passiva,
                    "passiva_2": adv.nome_da_segunda_habilidade_passiva,
                    "passiva_3": adv.nome_da_terceira_habilidade_passiva,
                    "ativa": adv.nome_da_habilidade_ativa,
                    "especial": adv.nome_da_habilidade_especial,
                }
            })

        dados.append(registro)

    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=2, ensure_ascii=False)

    print(f"Arquivo '{arquivo}' salvo com {len(dados)} adversários.")

# Lista com todos os adversários instanciados
todos_adversarios = [
    slime, zumbi, gárgula, lobisomem, quimera, banshee, fenrir, ghoul,
    goblin, ogro, esqueleto, oni, medusa, troll
]

# Exporta para JSON
salvar_adversarios_json(todos_adversarios, "adversarioss.json")
