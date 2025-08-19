import sys, os
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = current_dir
while not os.path.isdir(os.path.join(project_root, ".git")) and os.path.dirname(project_root) != project_root:
    project_root = os.path.dirname(project_root)
sys.path.append(project_root)

from backend.sistemas.modelos.personagem_principal import Usuario
from backend.sistemas.modelos.adversarios import AdversarioDemiHumano, AdversarioMonstro
from backend.sistemas.modelos.classes_combatentes import artista_marcial
from backend.sistemas.modelos.armas import criar_arma


agnes = Usuario("agnes")
agnes.definir_classe(artista_marcial)
agnes.definir_habilidades()
agnes.atualizar_descrição()
agnes.atualizar_status_com_bonus()
punho = criar_arma("punho", "punhos caleijados", "comum", agnes, 100, 50, 1.2, 0.5, 0.3)
agnes.equipar_arma(punho)  # Equipa a arma corretamente
agnes.atualizar_status_com_bonus()
agnes.atualizar_descrição()