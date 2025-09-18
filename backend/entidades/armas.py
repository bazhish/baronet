import sys, os; project_root = os.path.abspath(os.path.dirname(__file__)); 
while not os.path.isdir(os.path.join(project_root, ".git")) and os.path.dirname(project_root) != project_root: project_root = os.path.dirname(project_root); 
sys.path.append(project_root)

from backend.sistemas.modelos.modelos_armas import criar_arma, Arma
from tests.personagem_ficticio import ayala

lamina_amanhecer = criar_arma("espada", "Lâmina do Amanhecer", "comum", ayala, 140, 167, 1.35, 1.75, 1.5)
ventos_rapidos = criar_arma("espada", "Espada dos Ventos Rápidos", "rara", ayala, 250, 252, 0.89, 1.25, 1.0)

fio_viajante = criar_arma("espada Curta", "Fio do Viajante", "comum", ayala, 137, 139, 1.65, 1.87, 1.7)
corte_destino = criar_arma("espada Curta", "Corte do Destino", "rara", ayala, 265, 268, 1.15, 1.12, 1.2)

guardiao = criar_arma("espada Longa", "Espada do Guardião", "comum", ayala, 143, 163, 1.28, 1.4, 1.4)
aurora = criar_arma("espada Longa", "Lâmina da Aurora", "rara", ayala, 273, 279, 1.2, 0.78, 0.8)

gemeas_crepusculo = criar_arma("espada Dupla", "Gêmeas do Crepúsculo", "comum", ayala, 116, 163, 1.98, 1.35, 1.45)
dancarinas_tempestade = criar_arma("espada Dupla", "Dançarinas da Tempestade", "rara", ayala, 244, 267, 1.17, 0.9, 0.8)

agulha_sombria = criar_arma("adaga", "Agulha Sombria", "comum", ayala, 187, 143, 1.73, 1.4, 1.75)
lamina_sussurro = criar_arma("adaga", "Lâmina do Sussurro", "rara", ayala, 249, 100, 1.11, 1.05, 1.25)

garras_lince = criar_arma("adaga dupla", "Garras do Lince", "comum", ayala, 123, 138, 1.76, 1.2, 1.5)
furiosas_meia_noite = criar_arma("adaga dupla", "Furiosas da Meia-Noite", "rara", ayala, 257, 269, 1.3, 0.75, 0.9)

sopro_selva = criar_arma("zarabatana", "Sopro da Selva", "comum", ayala, 129, 126, 1.89, 1.3, 1.7)
flecha_silencio = criar_arma("zarabatana", "Flecha do Silêncio", "rara", ayala, 243, 246, 1.27, 0.95, 1.15)

besta_cacador = criar_arma("besta", "Besta do Caçador", "comum", ayala, 138, 173, 1.89, 1.25, 1.5)
besta_relampago = criar_arma("besta", "Besta Relâmpago", "rara", ayala, 251, 279, 1.23, 0.5, 0.76)

arco_bosque = criar_arma("arco", "Arco do Bosque", "comum", ayala, 123, 156, 1.79, 1.46, 1.63)
arco_lua_crescente = criar_arma("arco", "Arco da Lua Crescente", "rara", ayala, 287, 283, 1.27, 0.7, 0.95)

lanca_pioneiro = criar_arma("lança", "Lança do Pioneiro", "comum", ayala, 135, 163, 1.98, 1.2, 1.47)
lanca_trovao = criar_arma("lança", "Lança do Trovão", "rara", ayala, 243, 267, 1.2, 0.5, 0.75)

machado_lenhador = criar_arma("machado", "Machado do Lenhador", "comum", ayala, 123, 158, 1.78, 1.4, 1.6)
machado_furia = criar_arma("machado", "Machado da Fúria", "rara", ayala, 235, 276, 1.25, 0.56, 0.68)

machados_gemeos = criar_arma("machado duplo", "Machados Gêmeos", "comum", ayala, 132, 166, 1.67, 1.35, 1.5)
machados_berserker = criar_arma("machado duplo", "Machados do Berserker", "rara", ayala, 257, 277, 0.97, 0.57, 0.77)

cutelo_mercador = criar_arma("cutelo", "Cutelo do Mercador", "comum", ayala, 157, 126, 1.69, 1.46, 1.56)
cutelo_acougueiro = criar_arma("cutelo", "Cutelo do Açougueiro", "rara", ayala, 264, 283, 1.13, 0.58, 0.7)

corte_duplo = criar_arma("cutelo duplo", "Corte Duplo", "comum", ayala, 146, 167, 1.87, 1.4, 1.6)
cortadores_eclipse = criar_arma("cutelo duplo", "Cortadores do Eclipse", "rara", ayala, 257, 265, 1.43, 0.6, 0.83)

manopla_ferro = criar_arma("manopla", "Manopla de Ferro", "comum", ayala, 173, 134, 1.67, 1.58, 1.8)
manopla_colosso = criar_arma("manopla", "Manopla do Colosso", "rara", ayala, 267, 276, 0.89, 0.56, 0.9)

katana_vento = criar_arma("katana", "Katana do Vento", "comum", ayala, 117, 143, 1.65, 1.45, 1.65)
katana_dragao = criar_arma("katana", "Katana do Dragão", "rara", ayala, 229, 258, 0.78, 0.8, 1.0)

sabre_marinheiro = criar_arma("sabre", "Sabre do Marinheiro", "comum", ayala, 137, 164, 1.87, 1.45, 1.6)
sabre_mares = criar_arma("sabre", "Sabre das Marés", "rara", ayala, 243, 227, 1.13, 0.7, 0.8)

punho_aprendiz = criar_arma("punho", "Punho do Aprendiz", "comum", ayala, 169, 183, 1.87, 1.4, 1.58)
punho_mestre = criar_arma("punho", "Punho do Mestre", "rara", ayala, 273, 276, 1.16, 0.8, 0.95)

clava_errante = criar_arma("clava", "Clava do Errante", "comum", ayala, 169, 151, 1.79, 1.6, 1.65)
clava_tita = criar_arma("clava", "Clava do Titã", "rara", ayala, 273, 287, 0.91, 0.68, 0.96)