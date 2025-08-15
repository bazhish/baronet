import sys, os
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = current_dir
while not os.path.isdir(os.path.join(project_root, ".git")) and os.path.dirname(project_root) != project_root:
    project_root = os.path.dirname(project_root)
sys.path.append(project_root)

from backend.sistemas.modelos.personagem_principal import Usuario
from backend.sistemas.modelos.adversarios import AdversarioDemiHumano, AdversarioMonstro
from backend.sistemas.modelos.classes_combatentes import artista_marcial

agnes = Usuario("agnes")
agnes.definir_classe(artista_marcial)
agnes.definir_habilidades()
agnes.atualizar_descrição()
print(agnes.descrição)
slime = AdversarioMonstro("slime", 50, 1.5, 2, 30, 4, 3, 12, 8, 1, "gosma", 80)
slime.atualizar_atributos()
slime.atualizar_descrição()
print()
print(slime.descrição)