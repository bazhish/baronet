import sys, os; project_root = os.path.abspath(os.path.dirname(__file__)); 
while not os.path.isdir(os.path.join(project_root, ".git")) and os.path.dirname(project_root) != project_root: project_root = os.path.dirname(project_root); 
sys.path.append(project_root)

from backend.sistemas.modelos.modelos_armas import criar_arma, Arma

lamina_amanhecer = criar_arma("espada", "Lâmina do Amanhecer", "comum", None, 140, 167, 1.35, 1.75, 1.5)
ventos_rapidos = criar_arma("espada", "Espada dos Ventos Rápidos", "rara", None, 250, 252, 0.89, 1.25, 1.0)

fio_viajante = criar_arma("espada Curta", "Fio do Viajante", "comum", None, 137, 139, 1.65, 1.87, 1.7)
corte_destino = criar_arma("espada Curta", "Corte do Destino", "rara", None, 265, 268, 1.15, 1.12, 1.2)

guardiao = criar_arma("espada Longa", "Espada do Guardião", "comum", None, 143, 163, 1.28, 1.4, 1.4)
aurora = criar_arma("espada Longa", "Lâmina da Aurora", "rara", None, 273, 279, 1.2, 0.78, 0.8)

gemeas_crepusculo = criar_arma("espada Dupla", "Gêmeas do Crepúsculo", "comum", None, 116, 163, 1.98, 1.35, 1.45)
dancarinas_tempestade = criar_arma("espada Dupla", "Dançarinas da Tempestade", "rara", None, 244, 267, 1.17, 0.9, 0.8)

agulha_sombria = criar_arma("adaga", "Agulha Sombria", "comum", None, 187, 143, 1.73, 1.4, 1.75)
lamina_sussurro = criar_arma("adaga", "Lâmina do Sussurro", "rara", None, 249, 100, 1.11, 1.05, 1.25)

garras_lince = criar_arma("adaga dupla", "Garras do Lince", "comum", None, 123, 138, 1.76, 1.2, 1.5)
furiosas_meia_noite = criar_arma("adaga dupla", "Furiosas da Meia-Noite", "rara", None, 257, 269, 1.3, 0.75, 0.9)

sopro_selva = criar_arma("zarabatana", "Sopro da Selva", "comum", None, 129, 126, 1.89, 1.3, 1.7)
flecha_silencio = criar_arma("zarabatana", "Flecha do Silêncio", "rara", None, 243, 246, 1.27, 0.95, 1.15)

besta_cacador = criar_arma("besta", "Besta do Caçador", "comum", None, 138, 173, 1.89, 1.25, 1.5)
besta_relampago = criar_arma("besta", "Besta Relâmpago", "rara", None, 251, 279, 1.23, 0.5, 0.76)

arco_bosque = criar_arma("arco", "Arco do Bosque", "comum", None, 123, 156, 1.79, 1.46, 1.63)
arco_lua_crescente = criar_arma("arco", "Arco da Lua Crescente", "rara", None, 287, 283, 1.27, 0.7, 0.95)

lanca_pioneiro = criar_arma("lança", "Lança do Pioneiro", "comum", None, 135, 163, 1.98, 1.2, 1.47)
lanca_trovao = criar_arma("lança", "Lança do Trovão", "rara", None, 243, 267, 1.2, 0.5, 0.75)

machado_lenhador = criar_arma("machado", "Machado do Lenhador", "comum", None, 123, 158, 1.78, 1.4, 1.6)
machado_furia = criar_arma("machado", "Machado da Fúria", "rara", None, 235, 276, 1.25, 0.56, 0.68)

machados_gemeos = criar_arma("machado duplo", "Machados Gêmeos", "comum", None, 132, 166, 1.67, 1.35, 1.5)
machados_berserker = criar_arma("machado duplo", "Machados do Berserker", "rara", None, 257, 277, 0.97, 0.57, 0.77)

cutelo_mercador = criar_arma("cutelo", "Cutelo do Mercador", "comum", None, 157, 126, 1.69, 1.46, 1.56)
cutelo_acougueiro = criar_arma("cutelo", "Cutelo do Açougueiro", "rara", None, 264, 283, 1.13, 0.58, 0.7)

corte_duplo = criar_arma("cutelo duplo", "Corte Duplo", "comum", None, 146, 167, 1.87, 1.4, 1.6)
cortadores_eclipse = criar_arma("cutelo duplo", "Cortadores do Eclipse", "rara", None, 257, 265, 1.43, 0.6, 0.83)

manopla_ferro = criar_arma("manopla", "Manopla de Ferro", "comum", None, 173, 134, 1.67, 1.58, 1.8)
manopla_colosso = criar_arma("manopla", "Manopla do Colosso", "rara", None, 267, 276, 0.89, 0.56, 0.9)

katana_vento = criar_arma("katana", "Katana do Vento", "comum", None, 117, 143, 1.65, 1.45, 1.65)
katana_dragao = criar_arma("katana", "Katana do Dragão", "rara", None, 229, 258, 0.78, 0.8, 1.0)

sabre_marinheiro = criar_arma("sabre", "Sabre do Marinheiro", "comum", None, 137, 164, 1.87, 1.45, 1.6)
sabre_mares = criar_arma("sabre", "Sabre das Marés", "rara", None, 243, 227, 1.13, 0.7, 0.8)

punho_aprendiz = criar_arma("punho", "Punho do Aprendiz", "comum", None, 169, 183, 1.87, 1.4, 1.58)
punho_mestre = criar_arma("punho", "Punho do Mestre", "rara", None, 273, 276, 1.16, 0.8, 0.95)

clava_errante = criar_arma("clava", "Clava do Errante", "comum", None, 169, 151, 1.79, 1.6, 1.65)
clava_tita = criar_arma("clava", "Clava do Titã", "rara", None, 273, 287, 0.91, 0.68, 0.96)

lâmina_do_amanheçer = Arma("espada", "Lâmina do Amanhecer", 6, 3, 140, 167, 1.35, 1.75, 1.5)
lâmina_do_amanheçer.escolha_de_raridade("comum")
lâmina_do_amanheçer.nivel_com_parametro_manual(5)
lâmina_do_amanheçer.dano_da_arma()
lâmina_do_amanheçer.atributo_adicional_aleatorio()
lâmina_do_amanheçer.velocidade_que_o_usuario_ira_perder()
lâmina_do_amanheçer.atualizar_atributos_jogador()
lâmina_do_amanheçer.descrição = lâmina_do_amanheçer.descrição_da_arma()

