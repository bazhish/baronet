from _jogador._classe import check_classe_do_jogador
classe = check_classe_do_jogador.classe_final
dados_pessoais = check_classe_do_jogador.dados_pessoais

def status_jogador(dados_pessoais):
    arma_inicial = "AdagaComum"
    atributos_base = 5
    
    descricao = {
        "nome": dados_pessoais.get("nome", "Desconhecido"),
        "idade": dados_pessoais.get("idade", 0),
        "peso": dados_pessoais.get("peso", 0),
        "sexo": dados_pessoais.get("sexo", "Indefinido"),
        "altura": dados_pessoais.get("altura", 0),
        
        "nível": atributos_base,
        "dano": 10 * atributos_base,
        "velocidade": 7 * atributos_base,
        "defesa": 8 * atributos_base,
        "vida": 120 * atributos_base,
        "vida máxima": 1000,
        
        "arma": arma_inicial,
        "escudo": "",
        
        "experiencia": 0,
        "experiencia máxima": 300,
        
        "classe": classe,
        
        "estamina": 100,
        "estamina máxima": 100,
        
        "habilidade passiva 1": classe.habilidade_passiva1,
        "habilidade passiva 2": classe.habilidade_passiva2,
        "habilidade passiva 3": classe.habilidade_passiva3,
        "habilidade ativa 1": classe.habilidade_ativa1,
        "habilidade ativa 2": classe.habilidade_ativa2,
    }
    
    return descricao

jogador = status_jogador()
