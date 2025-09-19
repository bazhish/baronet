import sys, os; project_root = os.path.abspath(os.path.dirname(__file__)); 
while not os.path.isdir(os.path.join(project_root, ".git")) and os.path.dirname(project_root) != project_root: project_root = os.path.dirname(project_root); 
sys.path.append(project_root)
from backend.sistemas.modelos.modelo_artefatos import (criar_escudo, criar_varinha_de_ilusoes, criar_lira, criar_cajado)
from tests.personagem_ficticio import ayala

# Escudos

escudo_velho = criar_escudo("Escudo Velho","comum", ayala)

print(escudo_velho.descrição)