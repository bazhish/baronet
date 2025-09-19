import sys, os; project_root = os.path.abspath(os.path.dirname(__file__));
while not os.path.isdir(os.path.join(project_root, ".git")) and os.path.dirname(project_root) != project_root: project_root = os.path.dirname(project_root);
sys.path.append(project_root)

from backend.sistemas.modelos.modelos_armaduras import gerar_peça_do_conjunto, ConjuntoArmadura
from tests.personagem_ficticio import ayala

# Comum
conjunto_de_malha = ConjuntoArmadura("Armadura de malha", "ataque")
gerar_peça_do_conjunto(conjunto_de_malha, "Elmo de malha", 5, "escamas de malha", "comum", ayala, 50)
gerar_peça_do_conjunto(conjunto_de_malha, "Peitoral de malha", 8, "escamas de malha", "comum", ayala, 125)
gerar_peça_do_conjunto(conjunto_de_malha, "Calça de malha", 4, "escamas de malha", "comum", ayala, 100)
gerar_peça_do_conjunto(conjunto_de_malha, "Botas de malha", 3, "escamas de malha", "comum", ayala, 35)
conjunto_de_malha.verificar_se_o_conjunto_esta_completo()
conjunto_de_malha.aplicar_bonus_do_conjunto(ayala)

# Raro
conjunto_de_aço = ConjuntoArmadura("Armadura de aço", "ataque")
gerar_peça_do_conjunto(conjunto_de_aço, "Elmo de aço", 15, "aço", "raro", ayala, 200)
gerar_peça_do_conjunto(conjunto_de_aço, "Peitoral de aço", 22, "aço", "raro", ayala, 400)
gerar_peça_do_conjunto(conjunto_de_aço, "Calça de aço", 12, "aço", "raro", ayala, 300)
gerar_peça_do_conjunto(conjunto_de_aço, "Botas de aço", 8, "aço", "raro", ayala, 120)
conjunto_de_aço.verificar_se_o_conjunto_esta_completo()
conjunto_de_aço.aplicar_bonus_do_conjunto(ayala)

# Épico
conjunto_de_mithril = ConjuntoArmadura("Armadura de mithril", "defesa")
gerar_peça_do_conjunto(conjunto_de_mithril, "Elmo de mithril", 25, "mithril", "épico", ayala, 500)
gerar_peça_do_conjunto(conjunto_de_mithril, "Peitoral de mithril", 35, "mithril", "épico", ayala, 1000)
gerar_peça_do_conjunto(conjunto_de_mithril, "Calça de mithril", 20, "mithril", "épico", ayala, 800)
gerar_peça_do_conjunto(conjunto_de_mithril, "Botas de mithril", 15, "mithril", "épico", ayala, 350)
conjunto_de_mithril.verificar_se_o_conjunto_esta_completo()
conjunto_de_mithril.aplicar_bonus_do_conjunto(ayala)

# Lendário
conjunto_de_escamas = ConjuntoArmadura("Armadura do Dragão", "ataque")
gerar_peça_do_conjunto(conjunto_de_escamas, "Elmo do Dragão", 40, "escamas de dragão", "lendário", ayala, 2000)
gerar_peça_do_conjunto(conjunto_de_escamas, "Peitoral do Dragão", 60, "escamas de dragão", "lendário", ayala, 4000)
gerar_peça_do_conjunto(conjunto_de_escamas, "Calça do Dragão", 35, "escamas de dragão", "lendário", ayala, 3000)
gerar_peça_do_conjunto(conjunto_de_escamas, "Botas do Dragão", 25, "escamas de dragão", "lendário", ayala, 1500)
conjunto_de_escamas.verificar_se_o_conjunto_esta_completo()
conjunto_de_escamas.aplicar_bonus_do_conjunto(ayala)

# comum
conjunto_de_couroreforçado = ConjuntoArmadura("Armadura de couro reforçado", "defesa")
gerar_peça_do_conjunto(conjunto_de_couroreforçado, "Elmo de couro reforçado", 8, "couro reforçado", "comum", ayala, 80)
gerar_peça_do_conjunto(conjunto_de_couroreforçado, "Peitoral de couro reforçado", 12, "couro reforçado", "comum", ayala, 180)
gerar_peça_do_conjunto(conjunto_de_couroreforçado, "Calça de couro reforçado", 6, "couro reforçado", "comum", ayala, 120)
gerar_peça_do_conjunto(conjunto_de_couroreforçado, "Botas de couro reforçado", 4, "couro reforçado", "comum", ayala, 60)
conjunto_de_couroreforçado.verificar_se_o_conjunto_esta_completo()
conjunto_de_couroreforçado.aplicar_bonus_do_conjunto(ayala)

# raro
conjunto_de_bronze = ConjuntoArmadura("Armadura de bronze", "ataque")
gerar_peça_do_conjunto(conjunto_de_bronze, "Elmo de bronze", 12, "bronze", "raro", ayala, 120)
gerar_peça_do_conjunto(conjunto_de_bronze, "Peitoral de bronze", 16, "bronze", "raro", ayala, 220)
gerar_peça_do_conjunto(conjunto_de_bronze, "Calça de bronze", 8, "bronze", "raro", ayala, 160)
gerar_peça_do_conjunto(conjunto_de_bronze, "Botas de bronze", 6, "bronze", "raro", ayala, 90)
conjunto_de_bronze.verificar_se_o_conjunto_esta_completo()
conjunto_de_bronze.aplicar_bonus_do_conjunto(ayala)

# épico
conjunto_de_adamantium = ConjuntoArmadura("Armadura de adamantium", "defesa")
gerar_peça_do_conjunto(conjunto_de_adamantium, "Elmo de adamantium", 20, "adamantium", "épico", ayala, 350)
gerar_peça_do_conjunto(conjunto_de_adamantium, "Peitoral de adamantium", 28, "adamantium", "épico", ayala, 700)
gerar_peça_do_conjunto(conjunto_de_adamantium, "Calça de adamantium", 15, "adamantium", "épico", ayala, 500)
gerar_peça_do_conjunto(conjunto_de_adamantium, "Botas de adamantium", 10, "adamantium", "épico", ayala, 250)
conjunto_de_adamantium.verificar_se_o_conjunto_esta_completo()
conjunto_de_adamantium.aplicar_bonus_do_conjunto(ayala)

# lendario
conjunto_lendario = ConjuntoArmadura("Armadura lendario", "ataque")
gerar_peça_do_conjunto(conjunto_lendario, "Elmo lendario", 30, "fibra celestial", "lendario", ayala, 1000)
gerar_peça_do_conjunto(conjunto_lendario, "Peitoral lendario", 45, "fibra celestial", "lendario", ayala, 2000)
gerar_peça_do_conjunto(conjunto_lendario, "Calça lendario", 25, "fibra ceestial", "lendario", ayala, 1500)
gerar_peça_do_conjunto(conjunto_lendario, "Botas celestiais", 18, "fibra celestial", "lendario", ayala, 800)
conjunto_lendario.verificar_se_o_conjunto_esta_completo()
conjunto_lendario.aplicar_bonus_do_conjunto(ayala)