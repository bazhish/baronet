import sys, os; project_root = os.path.abspath(os.path.dirname(__file__));
while not os.path.isdir(os.path.join(project_root, ".git")) and os.path.dirname(project_root) != project_root: project_root = os.path.dirname(project_root);
sys.path.append(project_root)

from backend.sistemas.modelos.modelos_armaduras import gerar_peça_do_conjunto, ConjuntoArmadura

# Comum
conjunto_comum = ConjuntoArmadura("Armadura de malha", "ataque")
gerar_peça_do_conjunto(conjunto_comum, "Elmo de malha", 5, "escamas de malha", "comum", None, 50)
gerar_peça_do_conjunto(conjunto_comum, "Peitoral de malha", 8, "escamas de malha", "comum", None, 125)
gerar_peça_do_conjunto(conjunto_comum, "Calça de malha", 4, "escamas de malha", "comum", None, 100)
gerar_peça_do_conjunto(conjunto_comum, "Botas de malha", 3, "escamas de malha", "comum", None, 35)
conjunto_comum.verificar_se_o_conjunto_esta_completo()
conjunto_comum.aplicar_bonus_do_conjunto(None)

# Raro
conjunto_raro = ConjuntoArmadura("Armadura de aço", "ataque")
gerar_peça_do_conjunto(conjunto_raro, "Elmo de aço", 15, "aço", "raro", None, 200)
gerar_peça_do_conjunto(conjunto_raro, "Peitoral de aço", 22, "aço", "raro", None, 400)
gerar_peça_do_conjunto(conjunto_raro, "Calça de aço", 12, "aço", "raro", None, 300)
gerar_peça_do_conjunto(conjunto_raro, "Botas de aço", 8, "aço", "raro", None, 120)
conjunto_raro.verificar_se_o_conjunto_esta_completo()
conjunto_raro.aplicar_bonus_do_conjunto(None)

# Épico
conjunto_epico = ConjuntoArmadura("Armadura de mithril", "defesa")
gerar_peça_do_conjunto(conjunto_epico, "Elmo de mithril", 25, "mithril", "épico", None, 500)
gerar_peça_do_conjunto(conjunto_epico, "Peitoral de mithril", 35, "mithril", "épico", None, 1000)
gerar_peça_do_conjunto(conjunto_epico, "Calça de mithril", 20, "mithril", "épico", None, 800)
gerar_peça_do_conjunto(conjunto_epico, "Botas de mithril", 15, "mithril", "épico", None, 350)
conjunto_epico.verificar_se_o_conjunto_esta_completo()
conjunto_epico.aplicar_bonus_do_conjunto(None)

# Lendário
conjunto_lendario = ConjuntoArmadura("Armadura do Dragão", "ataque")
gerar_peça_do_conjunto(conjunto_lendario, "Elmo do Dragão", 40, "escamas de dragão", "lendário", None, 2000)
gerar_peça_do_conjunto(conjunto_lendario, "Peitoral do Dragão", 60, "escamas de dragão", "lendário", None, 4000)
gerar_peça_do_conjunto(conjunto_lendario, "Calça do Dragão", 35, "escamas de dragão", "lendário", None, 3000)
gerar_peça_do_conjunto(conjunto_lendario, "Botas do Dragão", 25, "escamas de dragão", "lendário", None, 1500)
conjunto_lendario.verificar_se_o_conjunto_esta_completo()
conjunto_lendario.aplicar_bonus_do_conjunto(None)

# comum
conjunto_incomum = ConjuntoArmadura("Armadura de couro reforçado", "defesa")
gerar_peça_do_conjunto(conjunto_incomum, "Elmo de couro reforçado", 8, "couro reforçado", "comum", None, 80)
gerar_peça_do_conjunto(conjunto_incomum, "Peitoral de couro reforçado", 12, "couro reforçado", "comum", None, 180)
gerar_peça_do_conjunto(conjunto_incomum, "Calça de couro reforçado", 6, "couro reforçado", "comum", None, 120)
gerar_peça_do_conjunto(conjunto_incomum, "Botas de couro reforçado", 4, "couro reforçado", "comum", None, 60)
conjunto_incomum.verificar_se_o_conjunto_esta_completo()
conjunto_incomum.aplicar_bonus_do_conjunto(None)

# raro
conjunto_raro = ConjuntoArmadura("Armadura de bronze", "ataque")
gerar_peça_do_conjunto(conjunto_raro, "Elmo de bronze", 12, "bronze", "raro", None, 120)
gerar_peça_do_conjunto(conjunto_raro, "Peitoral de bronze", 16, "bronze", "raro", None, 220)
gerar_peça_do_conjunto(conjunto_raro, "Calça de bronze", 8, "bronze", "raro", None, 160)
gerar_peça_do_conjunto(conjunto_raro, "Botas de bronze", 6, "bronze", "raro", None, 90)
conjunto_raro.verificar_se_o_conjunto_esta_completo()
conjunto_raro.aplicar_bonus_do_conjunto(None)

# épico
conjunto_épico = ConjuntoArmadura("Armadura de adamantium", "defesa")
gerar_peça_do_conjunto(conjunto_épico, "Elmo de adamantium", 20, "adamantium", "épico", None, 350)
gerar_peça_do_conjunto(conjunto_épico, "Peitoral de adamantium", 28, "adamantium", "épico", None, 700)
gerar_peça_do_conjunto(conjunto_épico, "Calça de adamantium", 15, "adamantium", "épico", None, 500)
gerar_peça_do_conjunto(conjunto_épico, "Botas de adamantium", 10, "adamantium", "épico", None, 250)
conjunto_épico.verificar_se_o_conjunto_esta_completo()
conjunto_épico.aplicar_bonus_do_conjunto(None)

# lendario
conjunto_lendario = ConjuntoArmadura("Armadura lendario", "ataque")
gerar_peça_do_conjunto(conjunto_lendario, "Elmo lendario", 30, "fibra celestial", "lendario", None, 1000)
gerar_peça_do_conjunto(conjunto_lendario, "Peitoral lendario", 45, "fibra celestial", "lendario", None, 2000)
gerar_peça_do_conjunto(conjunto_lendario, "Calça lendario", 25, "fibra ceestial", "lendario", None, 1500)
gerar_peça_do_conjunto(conjunto_lendario, "Botas celestiais", 18, "fibra celestial", "lendario", None, 800)
conjunto_lendario.verificar_se_o_conjunto_esta_completo()
conjunto_lendario.aplicar_bonus_do_conjunto(None)