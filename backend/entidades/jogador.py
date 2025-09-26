import sys, os; project_root = os.path.abspath(os.path.dirname(__file__)); 
while not os.path.isdir(os.path.join(project_root, ".git")) and os.path.dirname(project_root) != project_root: project_root = os.path.dirname(project_root); 
sys.path.append(project_root)

from backend.sistemas.modelos.modelo_personagem_principal import Usuario
from backend.sistemas.classes.classes_combatentes import artista_marcial
from backend.sistemas.modelos.modelos_armas import criar_arma
from backend.sistemas.dados.inventario import Inventario

agnes = Usuario()
agnes.inventario = Inventario()
agnes.definir_classe(artista_marcial)
agnes.definir_habilidades()
agnes.receber_experiencia(5000)
punho_aprendiz = criar_arma("punho", "Punho do Aprendiz", "comum", agnes, 169, 183, 1.87, 1.4, 1.58)
agnes.inventario.adicionar_item(punho_aprendiz)
agnes.inventario.equipar(punho_aprendiz)
agnes.equipar_arma(punho_aprendiz)
agnes.atualizar_atributos()
agnes.atualizar_descrição()
