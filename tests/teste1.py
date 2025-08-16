import sys, os
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = current_dir
while not os.path.isdir(os.path.join(project_root, ".git")) and os.path.dirname(project_root) != project_root:
    project_root = os.path.dirname(project_root)
sys.path.append(project_root)

from backend.sistemas.modelos.adversarios import AdversarioMonstro

slime = AdversarioMonstro("slime", 2, 30, 8, 3, 12, 8, 1, "gosma", 80)
slime.posição_x = 1200
slime.atualizar_atributos()
slime.atualizar_descrição()