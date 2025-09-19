import sys, os; project_root = os.path.abspath(os.path.dirname(__file__)); 
while not os.path.isdir(os.path.join(project_root, ".git")) and os.path.dirname(project_root) != project_root: project_root = os.path.dirname(project_root); 
sys.path.append(project_root)
from backend.sistemas.modelos.modelo_artefatos import (criar_escudo, criar_varinha_de_ilusoes, criar_lira, criar_cajado)
from tests.personagem_ficticio import ayala

# Escudos
escudo_velho = criar_escudo("Escudo Velho","comum", ayala)
escudo_do_amanhecer = criar_escudo("Escudo do Amanhecer","raro", ayala)

# Varinhas Ilusorias
espirito_raposa = criar_varinha_de_ilusoes("Espirito da Raposa", "comum", ayala)
varinha_dos_sussurros = criar_varinha_de_ilusoes("Varinha dos Sussurros", "raro", ayala)

# Liras
lira_das_estrelas = criar_lira("Lira das Estrelas", "comum", ayala)
lira_dos_sonhos = criar_lira("Lira dos Sonhos", "raro", ayala)

# Cajados
cajado_da_floresta = criar_cajado("Cajado da Floresta", "comum", ayala)
cajado_do_arcano = criar_cajado("Cajado do Arcano", "raro", ayala)