def JanelaDeBatalha(jogador):
    nome = jogador.get("nome", "Desconhecido")
    nivel = jogador.get("nível", 0)
    dano = jogador.get("dano", 0)
    velocidade = jogador.get("velocidade", 0)
    defesa = jogador.get("defesa", 0)
    
    vida_atual = jogador.get("vida", 0)
    vida_maxima = jogador.get("vida máxima", 0)
    vida_formatada = f"{vida_atual}/{vida_maxima}"
    
    arma = jogador.get("arma", "Nenhuma")
    
    experiencia_atual = jogador.get("experiencia", 0)
    experiencia_maxima = jogador.get("experiencia máxima", 0)
    experiencia_formatada = f"{experiencia_atual}/{experiencia_maxima}"
    
    classe = jogador.get("classe", "Indefinida")

    janela = {
        "jogador": nome,
        "nível": nivel,
        "dano": dano,
        "velocidade": velocidade,
        "defesa": defesa,
        "vida": vida_formatada,
        "arma": arma,
        "experiencia": experiencia_formatada,
        "classe": classe
    }

    return janela