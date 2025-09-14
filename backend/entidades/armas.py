import sys, os; project_root = os.path.abspath(os.path.dirname(__file__)); 
while not os.path.isdir(os.path.join(project_root, ".git")) and os.path.dirname(project_root) != project_root: project_root = os.path.dirname(project_root); 
sys.path.append(project_root)

from backend.sistemas.modelos.modelos_armas import criar_arma

lamina_amanhecer = criar_arma("espada", "Lâmina do Amanhecer", "comum", None, 100, 100, 1.0, 0.5, 0.3)
ventos_rapidos = criar_arma("espada", "Espada dos Ventos Rápidos", "rara", None, 100, 100, 1.0, 0.5, 0.3)

fio_viajante = criar_arma("espada Curta", "Fio do Viajante", "comum", None, 100, 100, 1.0, 0.5, 0.3)
corte_destino = criar_arma("espada Curta", "Corte do Destino", "rara", None, 100, 100, 1.0, 0.5, 0.3)

guardiao = criar_arma("espada Longa", "Espada do Guardião", "comum", None, 100, 100, 1.0, 0.5, 0.3)
aurora = criar_arma("espada Longa", "Lâmina da Aurora", "rara", None, 100, 100, 1.0, 0.5, 0.3)

gemeas_crepusculo = criar_arma("espada Dupla", "Gêmeas do Crepúsculo", "comum", None, 100, 100, 1.0, 0.5, 0.3)
dancarinas_tempestade = criar_arma("espada Dupla", "Dançarinas da Tempestade", "rara", None, 100, 100, 1.0, 0.5, 0.3)

agulha_sombria = criar_arma("adaga", "Agulha Sombria", "comum", None, 100, 100, 1.0, 0.5, 0.3)
lamina_sussurro = criar_arma("adaga", "Lâmina do Sussurro", "rara", None, 100, 100, 1.0, 0.5, 0.3)

garras_lince = criar_arma("adaga dupla", "Garras do Lince", "comum", None, 100, 100, 1.0, 0.5, 0.3)
furiosas_meia_noite = criar_arma("adaga dupla", "Furiosas da Meia-Noite", "rara", None, 100, 100, 1.0, 0.5, 0.3)

sopro_selva = criar_arma("zarabatana", "Sopro da Selva", "comum", None, 100, 100, 1.0, 0.5, 0.3)
flecha_silencio = criar_arma("zarabatana", "Flecha do Silêncio", "rara", None, 100, 100, 1.0, 0.5, 0.3)

besta_cacador = criar_arma("besta", "Besta do Caçador", "comum", None, 100, 100, 1.0, 0.5, 0.3)
besta_relampago = criar_arma("besta", "Besta Relâmpago", "rara", None, 100, 100, 1.0, 0.5, 0.3)

arco_bosque = criar_arma("arco", "Arco do Bosque", "comum", None, 100, 100, 1.0, 0.5, 0.3)
arco_lua_crescente = criar_arma("arco", "Arco da Lua Crescente", "rara", None, 100, 100, 1.0, 0.5, 0.3)

lanca_pioneiro = criar_arma("lança", "Lança do Pioneiro", "comum", None, 100, 100, 1.0, 0.5, 0.3)
lanca_trovao = criar_arma("lança", "Lança do Trovão", "rara", None, 100, 100, 1.0, 0.5, 0.3)

machado_lenhador = criar_arma("machado", "Machado do Lenhador", "comum", None, 100, 100, 1.0, 0.5, 0.3)
machado_furia = criar_arma("machado", "Machado da Fúria", "rara", None, 100, 100, 1.0, 0.5, 0.3)

machados_gemeos = criar_arma("machado duplo", "Machados Gêmeos", "comum", None, 100, 100, 1.0, 0.5, 0.3)
machados_berserker = criar_arma("machado duplo", "Machados do Berserker", "rara", None, 100, 100, 1.0, 0.5, 0.3)

cutelo_mercador = criar_arma("cutelo", "Cutelo do Mercador", "comum", None, 100, 100, 1.0, 0.5, 0.3)
cutelo_acougueiro = criar_arma("cutelo", "Cutelo do Açougueiro", "rara", None, 100, 100, 1.0, 0.5, 0.3)

corte_duplo = criar_arma("cutelo duplo", "Corte Duplo", "comum", None, 100, 100, 1.0, 0.5, 0.3)
cortadores_eclipse = criar_arma("cutelo duplo", "Cortadores do Eclipse", "rara", None, 100, 100, 1.0, 0.5, 0.3)

manopla_ferro = criar_arma("manopla", "Manopla de Ferro", "comum", None, 100, 100, 1.0, 0.5, 0.3)
manopla_colosso = criar_arma("manopla", "Manopla do Colosso", "rara", None, 100, 100, 1.0, 0.5, 0.3)

katana_vento = criar_arma("katana", "Katana do Vento", "comum", None, 100, 100, 1.0, 0.5, 0.3)
katana_dragao = criar_arma("katana", "Katana do Dragão", "rara", None, 100, 100, 1.0, 0.5, 0.3)

sabre_marinheiro = criar_arma("sabre", "Sabre do Marinheiro", "comum", None, 100, 100, 1.0, 0.5, 0.3)
sabre_mares = criar_arma("sabre", "Sabre das Marés", "rara", None, 100, 100, 1.0, 0.5, 0.3)

punho_aprendiz = criar_arma("punho", "Punho do Aprendiz", "comum", None, 100, 100, 1.0, 0.5, 0.3)
punho_mestre = criar_arma("punho", "Punho do Mestre", "rara", None, 100, 100, 1.0, 0.5, 0.3)

clava_errante = criar_arma("clava", "Clava do Errante", "comum", None, 100, 100, 1.0, 0.5, 0.3)
clava_tita = criar_arma("clava", "Clava do Titã", "rara", None, 100, 100, 1.0, 0.5, 0.3)