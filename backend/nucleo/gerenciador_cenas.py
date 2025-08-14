from frontend.cenas.arena_combate import executar_arena

def executar_cena(nome_cena):
    if nome_cena == "arena":
        executar_arena()
    elif nome_cena == "menu":
        print("Executando menu (placeholder)")
