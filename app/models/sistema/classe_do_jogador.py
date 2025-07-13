from random import choice
from classe_atributos import assassino, escudeiro, espadachim, lanceiro, batedor, arqueiro
from os import system

dados_pessoais = {}
classe_final = None

def classe_com_escolha_do_sistema(dados_pessoais, classe_final):
    nome = input("qual será seu nome? ").upper()
    while True:
        try:
            idade = int(input("\nidade: "))
            peso = float(input("\npeso: ").replace(",", "."))
            altura = float(input("\naltura: ").replace(",", "."))
            break
        except ValueError:
            print("\npor favor digite apenas números!")

    sexo = input("\nsexo: ").lower()
    while sexo not in ["homem", "menino", "rapaz", "masculino", "masc", "h", "mulher", "menina", "moça", "feminino", "fem", "f"]:
        system("cls")
        sexo = input("\nsexo inválido. digite novamente: ").lower()

    dados_pessoais = {
        "nome": nome,
        "idade": idade,
        "peso": peso,
        "altura": altura,
        "genero": sexo
        }

    system("cls")

    classes = [assassino, escudeiro, espadachim, lanceiro, batedor, arqueiro]
    classe_final = choice(classes)

    return dados_pessoais, classe_final

def classe_com_escolha_manual(dados_pessoais, classe_final):
    system("cls")

    nome = input("qual será seu nome? ").upper()
    while True:
        try:
            idade = int(input("\nidade: "))
            peso = float(input("\npeso: ").replace(",", "."))
            altura = float(input("\naltura: ").replace(",", "."))
            break
        except ValueError:
            print("\npor favor digite apenas números!")

    sexo = input("\nsexo: ").lower()
    while sexo not in ["homem", "menino", "rapaz", "masculino", "masc", "h", "mulher", "menina", "moça", "feminino", "fem", "f"]:
        system("cls")
        sexo = input("\nsexo inválido. digite novamente: ").lower()

    dados_pessoais = {
        "nome": nome,
        "idade": idade,
        "peso": peso,
        "altura": altura,
        "genero": sexo
        }

    system("cls")

    classes = [assassino, escudeiro, espadachim, lanceiro, batedor, arqueiro]
    
    print("\nclasses disponíveis:\n")
    for numero, nome in enumerate(["assassino", "escudeiro", "espadachim", "lanceiro", "batedor", "arqueiro"], 1):
        print(f"{numero} - {nome}")

    while True:
        resposta = input("\ndigite o número da classe: ")
        if resposta.isdigit() and 1 <= int(resposta) <= 6:
            return classes[int(resposta) - 1]
        print("\nresposta inválida, por favor digite um número de 1 a 6.\n")

    return dados_pessoais, classe_final

def classe_com_base_na_personalidade_do_usuario():
    classe = {c: 0 for c in ["arqueiro", "espadachim", "assassino", "escudeiro", "lanceiro", "batedor"]}
    incertezas = ["talvez", "não sei", "tanto faz", "nenhum", "qualquer"]

    def aplicar_pontos(resposta, grupos):
        for condicoes, pontos in grupos.items():
            if any(p in resposta for p in condicoes):
                for classe_nome, valor in pontos.items():
                    classe[classe_nome] += valor
                return
        if any(p in resposta for p in incertezas):
            print("você não terá pontos atribuídos.")

    def perguntar(perguntas):
        return {chave: input(texto).lower() for chave, texto in perguntas.items()}

    # Dados pessoais
    nome = input("Qual será seu nome?\n").upper()
    while True:
        try:
            idade = int(input("Idade:\n"))
            peso = float(input("Peso:\n").replace(",", "."))
            altura = float(input("Altura:\n").replace(",", "."))
            break
        except ValueError:
            print("Digite valores válidos.")

    sexo = input("Sexo:\n").lower()
    while sexo not in ["homem", "menino", "rapaz", "masculino", "masc", "h", "mulher", "menina", "moça", "feminino", "fem", "f"]:
        sexo = input("Sexo inválido. Digite novamente:\n").lower()

    # Exemplo de condição física
    if 22 <= idade <= 32 and 70 <= peso <= 90 and 1.70 <= altura <= 1.90:
        classe["arqueiro"] += 1
        classe["espadachin"] += 1

    # Dados mentais
    dados_mentais = perguntar({
        "planejamento": "Prefere planejar ou agir no momento?\n",
        "calma_pressao": "Calmo ou estressado sob pressão?\n",
        "resolver_problema": "Resolve problemas sozinho ou pede ajuda?\n",
        "concentracao": "Tem facilidade de concentração por longos períodos? (sim/não)\n",
        "logica_criatividade": "É mais lógico ou criativo?\n",
    })

    aplicar_pontos(dados_mentais["planejamento"], {
        ("planejar",): {"espadachin": 1, "arqueiro": 2, "assassino": 3},
        ("momento", "improviso"): {"batedor": 3, "lanceiro": 1, "escudeiro": 2}
    })

    aplicar_pontos(dados_mentais["calma_pressao"], {
        ("calmo", "tranquilo"): {"espadachin": 2, "arqueiro": 2, "assassino": 1, "escudeiro": 3},
        ("estressado", "ansioso"): {"lanceiro": 2, "batedor": 2}
    })

    aplicar_pontos(dados_mentais["resolver_problema"], {
        ("sozinho",): {"assassino": 2, "batedor": 1, "espadachin": 3},
        ("ajuda",): {"arqueiro": 2, "batedor": 3, "espadachin": 3, "escudeiro": 1}
    })

    aplicar_pontos(dados_mentais["concentracao"], {
        ("sim",): {"arqueiro": 3, "batedor": 1, "lanceiro": 3, "assassino": 2, "escudeiro": 2},
        ("não", "nao"): {"espadachin": 3}
    })

    aplicar_pontos(dados_mentais["logica_criatividade"], {
        ("lógico", "logico"): {"espadachin": 2, "escudeiro": 2, "batedor": 3},
        ("criativo",): {"assassino": 3, "arqueiro": 2, "lanceiro": 2}
    })

    # Dados físicos
    dados_fisicos = perguntar({
        "forca_ou_agilidade": "Prefere força bruta ou agilidade?\n",
        "aguenta_tempo": "Aguenta mais tempo lutando ou tem explosões curtas de energia?\n",
        "ataques": "Prefere ataques rápidos ou poderosos?\n",
        "esquiva_ou_bloqueio": "É melhor em esquivar ou bloquear?\n",
        "resistencia": "É mais resistente a dor ou ao cansaço?\n"
    })

    aplicar_pontos(dados_fisicos["forca_ou_agilidade"], {
        ("força", "forca"): {"escudeiro": 3, "espadachin": 1, "batedor": 1},
        ("agilidade",): {"batedor": 1, "lanceiro": 2, "assassino": 2, "espadachin": 1, "arqueiro": 3}
    })

    aplicar_pontos(dados_fisicos["aguenta_tempo"], {
        ("tempo", "aguento"): {"escudeiro": 2, "espadachin": 2, "assassino": 3, "batedor": 1},
        ("explosivo", "curta"): {"batedor": 3, "lanceiro": 2, "arqueiro": 1}
    })

    aplicar_pontos(dados_fisicos["ataques"], {
        ("rápido", "rapido"): {"arqueiro": 3, "assassino": 2, "lanceiro": 1, "batedor": 3},
        ("poderoso",): {"espadachin": 1, "batedor": 2}
    })

    aplicar_pontos(dados_fisicos["esquiva_ou_bloqueio"], {
        ("esquiva", "esquivar"): {"arqueiro": 3, "batedor": 2, "lanceiro": 1, "assassino": 3, "espadachin": 2},
        ("bloquear", "bloqueio"): {"escudeiro": 1}
    })

    aplicar_pontos(dados_fisicos["resistencia"], {
        ("dor",): {"escudeiro": 1, "lanceiro": 2, "espadachin": 3, "batedor": 1, "assassino": 2},
        ("cansaço",): {"escudeiro": 3, "assassino": 2, "espadachin": 1, "arqueiro": 3}
    })

    # Dados sociais
    dados_sociais = perguntar({
        "lideranca": "Prefere liderar ou seguir ordens?\n",
        "sociabilidade": "É mais amigável ou reservado?\n",
        "confianca": "Confia facilmente nas pessoas? (sim/não)\n",
        "conflitos": "Resolve conflitos com conversa ou luta?\n",
        "persuasao": "É bom em convencer os outros? (sim/não)\n"
    })

    aplicar_pontos(dados_sociais["lideranca"], {
        ("liderar",): {"arqueiro": 3, "assassino": 2, "lanceiro": 1},
        ("seguir",): {"escudeiro": 1, "espadachin": 2, "batedor": 3}
    })

    aplicar_pontos(dados_sociais["sociabilidade"], {
        ("amigável", "amigavel"): {"escudeiro": 3, "arqueiro": 2, "espadachin": 1},
        ("reservado", "quieto", "introvertido"): {"batedor": 1, "assassino": 2, "lanceiro": 3}
    })

    aplicar_pontos(dados_sociais["confianca"], {
        ("sim",): {"escudeiro": 2, "espadachin": 3, "arqueiro": 2},
        ("não", "nao"): {"assassino": 2, "lanceiro": 2, "batedor": 2}
    })

    aplicar_pontos(dados_sociais["conflitos"], {
        ("conversa",): {"escudeiro": 3, "arqueiro": 3, "espadachin": 3},
        ("luta",): {"assassino": 1, "batedor": 1, "lanceiro": 1}
    })

    aplicar_pontos(dados_sociais["persuasao"], {
        ("sim",): {"espadachin": 1, "arqueiro": 2, "assassino": 2, "escudeiro": 1},
        ("não", "nao"): {"batedor": 2, "lanceiro": 1}
    })

    # Dados de combate
    dados_combate = perguntar({
        "tipo_ataque": "Prefere ataques rápidos e furtivos ou lentos e fortes?\n",
        "estilo": "É melhor em defesa ou ataque?\n",
        "parceria": "Prefere lutar sozinho ou com parceiro?\n",
        "distancia": "Tem mais experiência corpo a corpo ou à distância?\n"
    })

    aplicar_pontos(dados_combate["tipo_ataque"], {
        ("rápido", "furtivo"): {"arqueiro": 2, "lanceiro": 1, "assassino": 3},
        ("lento", "forte"): {"batedor": 2, "espadachin": 3, "escudeiro": 3}
    })

    aplicar_pontos(dados_combate["estilo"], {
        ("defesa",): {"escudeiro": 3},
        ("ataque",): {"lanceiro": 1, "espadachin": 1, "assassino": 1, "arqueiro": 1, "batedor": 1}
    })

    aplicar_pontos(dados_combate["parceria"], {
        ("sozinho",): {"assassino": 3, "batedor": 1, "lanceiro": 3},
        ("parceiro",): {"arqueiro": 2, "espadachin": 1, "escudeiro": 1}
    })

    aplicar_pontos(dados_combate["distancia"], {
        ("corpo a corpo",): {"escudeiro": 2, "batedor": 1, "espadachin": 2, "assassino": 3},
        ("distância", "distancia"): {"lanceiro": 2, "arqueiro": 1}
    })

    # RESULTADO DA CLASSE

    if all(valor == 0 for valor in classe.values()):
        print("Nenhuma classe recebeu pontos! Escolhendo uma classe aleatória pra você...")
        classe_final = choice(list(classe.keys()))
    else:
        classe_final = max(classe, key=lambda k: classe[k])

    dados_pessoais = {
        "nome": nome,
        "idade": idade,
        "peso": peso,
        "altura": altura,
        "genero": sexo,
        }

    return dados_pessoais, classe_final

