# ARMAS


def possiveis_armas():
    raridade_arma = {
        'adaga': {
            'comum':    {'dano': 8,  'alcance': 1, 'velocidade': 10},
            'raro':     {'dano': 12, 'alcance': 1, 'velocidade': 10},
            'épico':    {'dano': 16, 'alcance': 1, 'velocidade': 10},
            'lendário': {'dano': 20, 'alcance': 1, 'velocidade': 10},
        },
        'espada': {
            'comum':    {'dano': 12, 'alcance': 1, 'velocidade': 7},
            'raro':     {'dano': 18, 'alcance': 1, 'velocidade': 7},
            'épico':    {'dano': 24, 'alcance': 1, 'velocidade': 7},
            'lendário': {'dano': 30, 'alcance': 1, 'velocidade': 7},
        },
        'cutelo': {
            'comum':    {'dano': 16, 'alcance': 1, 'velocidade': 5},
            'raro':     {'dano': 24, 'alcance': 1, 'velocidade': 5},
            'épico':    {'dano': 32, 'alcance': 1, 'velocidade': 5},
            'lendário': {'dano': 40, 'alcance': 1, 'velocidade': 5},
        },
        'machado': {
            'comum':    {'dano': 16, 'alcance': 1, 'velocidade': 5},
            'raro':     {'dano': 24, 'alcance': 1, 'velocidade': 5},
            'épico':    {'dano': 32, 'alcance': 1, 'velocidade': 5},
            'lendário': {'dano': 40, 'alcance': 1, 'velocidade': 5},
        },
        'espada curta': {
            'comum':    {'dano': 10, 'alcance': 1, 'velocidade': 9},
            'raro':     {'dano': 15, 'alcance': 1, 'velocidade': 9},
            'épico':    {'dano': 20, 'alcance': 1, 'velocidade': 9},
            'lendário': {'dano': 25, 'alcance': 1, 'velocidade': 9},
        },
        'espada longa': {
            'comum':    {'dano': 14, 'alcance': 2, 'velocidade': 6},
            'raro':     {'dano': 21, 'alcance': 2, 'velocidade': 6},
            'épico':    {'dano': 28, 'alcance': 2, 'velocidade': 6},
            'lendário': {'dano': 35, 'alcance': 2, 'velocidade': 6},
        },
        'lança': {
            'comum':    {'dano': 12, 'alcance': 3, 'velocidade': 6},
            'raro':     {'dano': 18, 'alcance': 3, 'velocidade': 6},
            'épico':    {'dano': 24, 'alcance': 3, 'velocidade': 6},
            'lendário': {'dano': 30, 'alcance': 3, 'velocidade': 6},
        },
        'arco': {
            'comum':    {'dano': 10, 'alcance': 4, 'velocidade': 6},
            'raro':     {'dano': 15, 'alcance': 4, 'velocidade': 6},
            'épico':    {'dano': 20, 'alcance': 4, 'velocidade': 6},
            'lendário': {'dano': 25, 'alcance': 4, 'velocidade': 6},
        },
        'monopola': {
            'comum':    {'dano': 6,  'alcance': 1, 'velocidade': 8},
            'raro':     {'dano': 9,  'alcance': 1, 'velocidade': 8},
            'épico':    {'dano': 12, 'alcance': 1, 'velocidade': 8},
            'lendário': {'dano': 15, 'alcance': 1, 'velocidade': 8},
        },
        'zarabatana': {
            'comum':    {'dano': 8,  'alcance': 4, 'velocidade': 7},
            'raro':     {'dano': 12, 'alcance': 4, 'velocidade': 7},
            'épico':    {'dano': 16, 'alcance': 4, 'velocidade': 7},
            'lendário': {'dano': 20, 'alcance': 4, 'velocidade': 7},
        },
        'adaga dupla': {
            'comum':    {'dano': 16,  'alcance': 5, 'velocidade': 5},
            'raro':     {'dano': 24, 'alcance': 5, 'velocidade': 5},
            'épico':    {'dano': 30, 'alcance': 5, 'velocidade': 5},
            'lendário': {'dano': 40, 'alcance': 5, 'velocidade': 5},
        },
        'espada dupla': {
            'comum':    {'dano': 24, 'alcance': 1, 'velocidade': 4},
            'raro':     {'dano': 36, 'alcance': 1, 'velocidade': 4},
            'épico':    {'dano': 48, 'alcance': 1, 'velocidade': 4},
            'lendário': {'dano': 60, 'alcance': 1, 'velocidade': 4},
        },
        'cutelo duplo': {
            'comum':    {'dano': 32, 'alcance': 1, 'velocidade': 5},
            'raro':     {'dano': 48, 'alcance': 1, 'velocidade': 5},
            'épico':    {'dano': 64, 'alcance': 1, 'velocidade': 5},
            'lendário': {'dano': 80, 'alcance': 1, 'velocidade': 5},
        },
    }
    return raridade_arma

armas = possiveis_armas()
arma_inicial = armas["adaga"]["comum"]

# CLASSES

classe = {
    "arqueiro": 0,
    "espadachin": 0,
    "assassino": 0,
    "escudeiro": 0,
    "lanceiro": 0,
    "batedor": 0,
    "MODERADOR": 0
}

# INCERTEZA

incertezas = ["talvez", "não sei", "tanto faz", "nenhum", "qualquer"]

# PERGUNTAS DADOS PESSOAIS
def função_para_dados_pessoais():
    nome = str(input("\rQual será seu nome?\n")).upper()
    
    # CONDIÇÕES DE VALIDAÇÃO DE TIPO
    while True:
        try:
            idade = int(input("Qual será sua idade? (Digite apenas números)\n"))
            break
        except ValueError:
            print("Por favor, digite um número inteiro para a idade.")
    
    while True:
        try:
            peso = float(input("Qual será o peso? (Digite apenas números)\n").replace(",", "."))
            break
        except ValueError:
            print("Por favor, digite um número válido para o peso.")
    
    while True:
        try:
            altura = float(input("Qual será sua altura? (Digite apenas números)\n").replace(",", "."))
            break
        except ValueError:
            print("Por favor, digite um número válido para a altura.")

    # POSSIVEIS RESPOSTAS PARA O SEXO DO PERSONAGEM

    homem = ["homem", "menino", "rapaz", "masculino", "masc", "h"]
    mulher = ["mulher", "menina", "moça", "feminino", "fem", "f"]

    sexo = input("Qual será o sexo do seu personagem?\n").lower()

    # LOOP DE CONDIÇÃO PARA O SEXO DO PERSONAGEM

    while sexo not in homem + mulher:
        print("\nDesculpe, mas aceitamos apenas gênero masculino e feminino")
        sexo = str(input("\nDigite o sexo novamente:\n"))
        
    return {
        "nome": nome,
        "idade": idade,
        "peso": peso,
        "altura": altura,
        "sexo": sexo,
    }

# DEFININDO AS VARIAVEIS FORA DA FUNÇÃO

dados_pessoais = função_para_dados_pessoais()

# CONDIÇÕES PARA DADOS PESSOAIS

if 22 >= dados_pessoais["idade"] <= 32 and 70 >= dados_pessoais["peso"] <= 90 and 1.70 >= dados_pessoais["altura"] <= 1.90 :
    classe["arqueiro"] += 1
    classe["espadachin"] += 1

elif 22 >= dados_pessoais["idade"] <= 32 and 70 >= dados_pessoais["peso"] <= 90 and 1.90 >= dados_pessoais["altura"] <= 2.10:
    classe["lanceiro"] += 1

elif 22 >= dados_pessoais["idade"] <= 28 and 60 >= dados_pessoais["peso"] <= 75 and 1.70 >= dados_pessoais["altura"] <= 1.90:
    classe["asssassino"] += 1

elif 30 >= dados_pessoais["idade"] <= 38 and dados_pessoais["peso"] >= 90:
    classe["escudeiro"] += 1

# PERGUNTAS PARA DADOS MENTAIS

dados_mentais = {
    "planejamento": str(input("Você prefere planejar tudo antes de agir ou agir no momento?\n").lower()),
    "calma_pressao": str(input("Quando está sob pressão, você mantém a calma ou se estressa facilmente?\n").lower()),
    "resolver_problema": str(input("Você prefere resolver problemas sozinho ou pedir ajuda?\n").lower()),
    "concentracao": str(input("Você tem facilidade para se concentrar por longos períodos?\n").lower()),
    "logica_criatividade": str(input("Você costuma ser mais lógico ou mais criativo?\n").lower())
}

# POSSIVEIS RESPOSTAS PARA DADOS MENTAIS

planejar = ["planejar", "planejo"]
agir_no_momento = ["momento", "na hora", "improviso"]

calma = ["calmo", "calma", "tranquilo", "tranquila"]
estresse = ["estressado", "estressada", "estresso", "nervoso", "nervosa", "ansioso", "ansiosa"]

sozinho = ["sozinho", "sozinha", "sozin", "só"]
ajuda = ["ajuda", "pedir ajuda"]

sim_concentra = ["sim", "s"]
nao_concentra = ["não", "n", "nao"]

logico = ["lógico", "logico", "lógica", "logica", ]
criativo = ["criativo", "criativa"]

# CONDIÇÕES PARA DADOS MENTAIS

# PERGUNTA 1

if any(palavra in dados_mentais["planejamento"] for palavra in planejar):
    classe["espadachin"] += 1
    classe["arqueiro"] += 2
    classe["assassino"] += 3

elif any(palavra in dados_mentais["planejamento"] for palavra in agir_no_momento):
    classe["batedor"] += 3
    classe["lanceiro"] += 1
    classe["escudeiro"] += 2

elif any(palavra in dados_mentais["planejamento"] for palavra in planejar + agir_no_momento):
    classe["batedor"] += 1
    classe["lanceiro"] += 1
    classe["escudeiro"] += 1
    classe["espadachin"] += 1
    classe["arqueiro"] += 1
    classe["assassino"] += 1

elif any(palavra in dados_mentais["planejamento"] for palavra in incertezas):
    print("você não terá pontos atribuidos")

# PERGUNTA 2

if any(palavra in dados_mentais["calma_pressao"] for palavra in calma):
    classe["espadachin"] += 2
    classe["arqueiro"] += 2
    classe["assassino"] += 1
    classe["escudeiro"] += 3

elif any(palavra in dados_mentais["calma_pressao"] for palavra in estresse):
    classe["lanceiro"] += 2
    classe["batedor"] += 2

elif any(palavra in dados_mentais["calma_pressao"] for palavra in calma + estresse):
    classe["batedor"] += 1
    classe["lanceiro"] += 1
    classe["escudeiro"] += 1
    classe["espadachin"] += 1
    classe["arqueiro"] += 1
    classe["assassino"] += 1

elif any(palavra in dados_mentais["calma_pressao"] for palavra in incertezas):
    print("você não terá pontos atribuidos")

# PERGUNTA 3

if any(palavra in dados_mentais["resolver_problema"] for palavra in sozinho):
    classe["assassino"] += 2
    classe["batedor"] += 1
    classe["espadachin"] += 3

elif any(palavra in dados_mentais["resolver_problema"] for palavra in ajuda):
    classe["arqueiro"] += 2
    classe["batedor"] += 3
    classe["espadachin"] += 3
    classe["escudeiro"] += 1

elif any(palavra in dados_mentais["resolver_problema"] for palavra in sozinho + ajuda):
    classe["batedor"] += 1
    classe["lanceiro"] += 1
    classe["escudeiro"] += 1
    classe["espadachin"] += 1
    classe["arqueiro"] += 1
    classe["assassino"] += 1

elif any(palavra in dados_mentais["resolver_problema"] for palavra in incertezas):
    print("você não terá pontos atribuidos")

# PERGUNTA 4

if any(palavra in dados_mentais["concentracao"] for palavra in sim_concentra):
    classe["arqueiro"] += 3
    classe["batedor"] += 1
    classe["lanceiro"] += 3
    classe["assassino"] += 2
    classe["escudeiro"] += 2

elif any(palavra in dados_mentais["concentracao"] for palavra in nao_concentra):
    classe["espadachin"] += 3

elif any(palavra in dados_mentais["concentracao"] for palavra in sim_concentra + nao_concentra):
    classe["batedor"] += 1
    classe["lanceiro"] += 1
    classe["escudeiro"] += 1
    classe["espadachin"] += 1
    classe["arqueiro"] += 1
    classe["assassino"] += 1

elif any(palavra in dados_mentais["concentracao"] for palavra in incertezas):
    print("você não terá pontos atribuidos")

# PERGUNTA 5

if any(palavra in dados_mentais["logica_criatividade"] for palavra in logico):
    classe["espadachin"] += 2
    classe["escudeiro"] += 2
    classe["batedor"] += 3

elif any(palavra in dados_mentais["logica_criatividade"] for palavra in criativo):
    classe["assassino"] += 3
    classe["arqueiro"] += 2
    classe["lanceiro"] += 2

elif any(palavra in dados_mentais["logica_criatividade"] for palavra in logico + criativo):
    classe["batedor"] += 1
    classe["lanceiro"] += 1
    classe["escudeiro"] += 1
    classe["espadachin"] += 1
    classe["arqueiro"] += 1
    classe["assassino"] += 1

elif any(palavra in dados_mentais["logica_criatividade"] for palavra in incertezas):
    print("você não terá pontos atribuidos")

# PERGUNTAS DADOS FISICOS

dados_fisicos = {
    "forca_ou_agilidade": str(input("Você prefere força bruta ou agilidade para lutar?\n").lower()),
    "aguenta_tempo": str(input("Você aguenta mais tempo lutando ou tem explosões curtas de energia?\n").lower()),
    "ataques_rapidos_ou_poderosos": str(input("Você prefere ataques rápidos ou ataques poderosos?\n").lower()),
    "esquiva_ou_bloqueio": str(input("Você é melhor em esquivar ou em bloquear ataques?\n").lower()),
    "resistencia_dor_ou_cansaco": str(input("Você se considera mais resistente a dores ou mais resistente ao cansaço?\n").lower())
}

# POSSIVEIS RESPOSTAS PARA DADOS FISICOS

forca = ["força", "forca"]
agilidade = ["agilidade"]

resistente_tempo = ["tempo", "aguento",]
explosivo = ["explosivo", "explosão", "explosões", "curta", "curto"]

ataque_rapido = ["rápido", "rapido", "rápidos", "rapidos"]
ataque_poderoso = ["poderoso", "poderosos"]

esquivar = ["esquiva", "esquivar", "desviar", "fugir", "evitar"]
bloquear = ["bloquear", "bloqueio", "defender", "parar", "segurar"]

resistente_dor = ["dor", "resistente a dor"]
resistente_cansaço = ["cansaço", "resistente a cansaço"]

# CONDIÇÕES PARA DADOS FISICOS

# PERGUNTA 1

if any(palavra in dados_fisicos["forca_ou_agilidade"] for palavra in forca):
    classe["escudeiro"] += 3
    classe["espadachin"] += 1
    classe["batedor"] += 1

elif any(palavra in dados_fisicos["forca_ou_agilidade"] for palavra in agilidade):
    classe["batedor"] += 1
    classe["lanceiro"] += 2
    classe["assassino"] += 2
    classe["espadachin"] += 1
    classe["arqueiro"] += 3

elif any(palavra in dados_fisicos["forca_ou_agilidade"] for palavra in forca + agilidade):
    classe["batedor"] += 1
    classe["lanceiro"] += 1
    classe["escudeiro"] += 1
    classe["espadachin"] += 1
    classe["arqueiro"] += 1
    classe["assassino"] += 1

elif any(palavra in dados_fisicos["forca_ou_agilidade"] for palavra in incertezas):
    print("você não terá pontos atribuidos")

# PERGUNTA 2

if any(palavra in dados_fisicos["aguenta_tempo"] for palavra in resistente_tempo):
    classe["escudeiro"] += 2
    classe["espadachin"] += 2
    classe["assassino"] += 13
    classe["batedor"] += 1

elif any(palavra in dados_fisicos["aguenta_tempo"] for palavra in explosivo):
    classe["batedor"] += 3
    classe["lanceiro"] += 2
    classe["arqueiro"] += 1

elif any(palavra in dados_fisicos["aguenta_tempo"] for palavra in resistente_tempo + explosivo):
    classe["batedor"] += 1
    classe["lanceiro"] += 1
    classe["escudeiro"] += 1
    classe["espadachin"] += 1
    classe["arqueiro"] += 1
    classe["assassino"] += 1

elif any(palavra in dados_fisicos["aguenta_tempo"] for palavra in incertezas):
    print("você não terá pontos atribuidos")

# PERGUNTA 3

if any(palavra in dados_fisicos["ataques_rapidos_ou_poderosos"] for palavra in ataque_rapido):
    classe["arqueiro"] += 3
    classe["assassino"] += 2
    classe["lanceiro"] += 1
    classe["batedor"] += 3

elif any(palavra in dados_fisicos["ataques_rapidos_ou_poderosos"] for palavra in ataque_poderoso):
    classe["espadachin"] += 1
    classe["batedor"] += 2

elif any(palavra in dados_fisicos["ataques_rapidos_ou_poderosos"] for palavra in ataque_rapido + ataque_poderoso):
    classe["batedor"] += 1
    classe["lanceiro"] += 1
    classe["escudeiro"] += 1
    classe["espadachin"] += 1
    classe["arqueiro"] += 1
    classe["assassino"] += 1

elif any(palavra in dados_fisicos["ataques_rapidos_ou_poderosos"] for palavra in incertezas):
    print("você não terá pontos atribuidos")

# PERGUNTA 4

if any(palavra in dados_fisicos["esquiva_ou_bloqueio"] for palavra in esquivar):
    classe["arqueiro"] += 3
    classe["batedor"] += 2
    classe["lanceiro"] += 1
    classe["assassino"] += 3
    classe["espadachin"] += 2

elif any(palavra in dados_fisicos["esquiva_ou_bloqueio"] for palavra in bloquear):
    classe["escudeiro"] += 1

elif any(palavra in dados_fisicos["esquiva_ou_bloqueio"] for palavra in esquivar + bloquear):
    classe["batedor"] += 1
    classe["lanceiro"] += 1
    classe["escudeiro"] += 1
    classe["espadachin"] += 1
    classe["arqueiro"] += 1
    classe["assassino"] += 1

elif any(palavra in dados_fisicos["esquiva_ou_bloqueio"] for palavra in incertezas):
    print("você não terá pontos atribuidos")

# PERGUNTA 5

if any(palavra in dados_fisicos["resistencia_dor_ou_cansaco"] for palavra in resistente_dor):
    classe["escudeiro"] += 1
    classe["lanceiro"] += 2
    classe["espadachin"] += 3
    classe["batedor"] += 1
    classe["assassino"] += 2

elif any(palavra in dados_fisicos["resistencia_dor_ou_cansaco"] for palavra in resistente_cansaço):
    classe["escudeiro"] += 3
    classe["assassino"] += 2
    classe["espadachin"] += 1
    classe["arqueiro"] += 3

elif any(palavra in dados_fisicos["resistencia_dor_ou_cansaco"] for palavra in resistente_dor + resistente_cansaço):
    classe["batedor"] += 1
    classe["lanceiro"] += 1
    classe["escudeiro"] += 1
    classe["espadachin"] += 1
    classe["arqueiro"] += 1
    classe["assassino"] += 1

elif any(palavra in dados_fisicos["resistencia_dor_ou_cansaco"] for palavra in incertezas):
    print("você não terá pontos atribuidos")

# PERGUNTAS PARA DADOS SOCIAIS

dados_sociais = {
    "liderar_ou_seguir": str(input("Você prefere liderar ou seguir ordens?\n").lower()),
    "amigavel_ou_reservado": str(input("Você costuma ser mais amigável ou reservado com os outros?\n").lower()),
    "confia_facilmente": str(input("Você confia facilmente nas pessoas?\n").lower()),
    "resolver_conflitos": str(input("Você prefere resolver conflitos com conversa ou com luta?\n").lower()),
    "convencer_os_outros": str(input("Você é bom em convencer e influenciar os outros?\n").lower())
}

# POSSIVEIS RESPOSTAS PARA DADOS SOCIAIS

liderar = ["liderar", "líder", "comando", "chefe", "mandar"]
seguir = ["seguir", "obedecer", "subordinado", "respeitar", "atender"]

amigavel = ["amigável", "amigo", "amigavel"]
reservado = ["reservado", "quieto", "tímido", "introvertido", "calado"]

confia_sim = ["sim", "s"]
confia_nao = ["não", "n", "nao"]

conflito_conversa = ["conversa", "dialogo", "falar", "discutir", "argumentar"]
conflito_acao = ["luta", "lutar", "brigar", "briga"]

convencer_sim = ["sim", "s"]
convencer_nao = ["não", "n", "nao"]

# CONDIÇÕES PARA DADOS SOCIAIS

# PERGUNTA 1

if any(palavra in dados_sociais["liderar_ou_seguir"] for palavra in liderar):
    classe["arqueiro"] += 3
    classe["assassino"] += 2
    classe["lanceiro"] += 1

elif any(palavra in dados_sociais["liderar_ou_seguir"] for palavra in seguir):
    classe["escudeiro"] += 1
    classe["espadachin"] += 2
    classe["batedor"] += 3

elif any(palavra in dados_sociais["liderar_ou_seguir"] for palavra in liderar + seguir):
    classe["batedor"] += 1
    classe["lanceiro"] += 1
    classe["escudeiro"] += 1
    classe["espadachin"] += 1
    classe["arqueiro"] += 1
    classe["assassino"] += 1

elif any(palavra in dados_sociais["liderar_ou_seguir"] for palavra in incertezas):
    print("você não terá pontos atribuidos")

# PERGUNTA 2

if any(palavra in dados_sociais["amigavel_ou_reservado"] for palavra in amigavel):
    classe["escudeiro"] += 3
    classe["arqueiro"] += 2
    classe["espadachin"] += 1

elif any(palavra in dados_sociais["amigavel_ou_reservado"] for palavra in reservado):
    classe["batedor"] += 1
    classe["assassino"] += 2
    classe["lanceiro"] += 3

elif any(palavra in dados_sociais["amigavel_ou_reservado"] for palavra in amigavel + reservado):
    classe["batedor"] += 1
    classe["lanceiro"] += 1
    classe["escudeiro"] += 1
    classe["espadachin"] += 1
    classe["arqueiro"] += 1
    classe["assassino"] += 1

elif any(palavra in dados_sociais["amigavel_ou_reservado"] for palavra in incertezas):
    print("você não terá pontos atribuidos")

# PERGUNTA 3

if any(palavra in dados_sociais["confia_facilmente"] for palavra in confia_sim):
    classe["escudeiro"] += 2
    classe["espadachin"] += 3
    classe["arqueiro"] += 2

elif any(palavra in dados_sociais["confia_facilmente"] for palavra in confia_nao):
    classe["assassino"] += 2
    classe["lanceiro"] += 2
    classe["batedor"] += 2

elif any(palavra in dados_sociais["confia_facilmente"] for palavra in confia_sim + confia_nao):
    classe["batedor"] += 1
    classe["lanceiro"] += 1
    classe["escudeiro"] += 1
    classe["espadachin"] += 1
    classe["arqueiro"] += 1
    classe["assassino"] += 1

elif any(palavra in dados_sociais["confia_facilmente"] for palavra in incertezas):
    print("você não terá pontos atribuidos")

# PERGUNTA 4

if any(palavra in dados_sociais["resolver_conflitos"] for palavra in conflito_conversa):
    classe["escudeiro"] += 3
    classe["arqueiro"] += 3
    classe["espadachin"] += 3

elif any(palavra in dados_sociais["resolver_conflitos"] for palavra in conflito_acao):
    classe["assassino"] += 1
    classe["batedor"] += 1
    classe["lanceiro"] += 1

elif any(palavra in dados_sociais["resolver_conflitos"] for palavra in conflito_conversa + conflito_acao):
    classe["batedor"] += 1
    classe["lanceiro"] += 1
    classe["escudeiro"] += 1
    classe["espadachin"] += 1
    classe["arqueiro"] += 1
    classe["assassino"] += 1

elif any(palavra in dados_sociais["resolver_conflitos"] for palavra in incertezas):
    print("você não terá pontos atribuidos")

# PERGUNTA 5

if any(palavra in dados_sociais["convencer_os_outros"] for palavra in convencer_sim):
    classe["espadachin"] += 1
    classe["arqueiro"] += 2
    classe["assassino"] += 2
    classe["escudeiro"] += 1

elif any(palavra in dados_sociais["convencer_os_outros"] for palavra in convencer_nao):
    classe["batedor"] += 2
    classe["lanceiro"] += 1

elif any(palavra in dados_sociais["convencer_os_outros"] for palavra in convencer_sim + convencer_nao):
    classe["batedor"] += 1
    classe["lanceiro"] += 1
    classe["escudeiro"] += 1
    classe["espadachin"] += 1
    classe["arqueiro"] += 1
    classe["assassino"] += 1

elif any(palavra in dados_sociais["convencer_os_outros"] for palavra in incertezas):
    print("você não terá pontos atribuidos")

# PERGUNTAS PARA DADOS DE COMBATE

dados_combate = {
    "ataque_rapido_ou_lento": str(input("Você prefere ataques rápidos e furtivos ou ataques lentos e fortes?\n").lower()),
    "defesa_ou_ataque": str(input("Você é melhor em defesa ou em ataque?\n").lower()),
    "lutar_sozinho_ou_parceiro": str(input("Você prefere lutar sozinho ou com um parceiro?\n").lower()),
    "experiencia_corpo_a_corpo_ou_distancia": str(input("Você tem mais experiência em combate corpo a corpo ou à distância?\n").lower())
}

# POSSIVEIS RESPOSTAS PARA DADOS DE COMBATE

ataque_rapido = ["rápido", "furtivo", "rapido"]
ataque_lento = ["lento", "forte"]

defesa = ["defesa", "proteger", "bloquear", "escudo", "resistir"]
ataque = ["ataque", "atacar", "agressivo", "golpear", "ferir"]

sozinho = ["sozinho", "solo", "individual", "só"]
parceiro = ["parceiro", "dupla", "time", "grupo", "amigo"]

corpo_a_corpo = ["corpo a corpo", "perto", "curta distância", "combate próximo"]
distancia = ["distante", "longa distância", "longa distancia", "arco", "tiro", "distância", "distancia"]

# CONDIÇÕES PARA DADOS DE COMBATE

# PERGUNTA 1

if any(palavra in dados_combate["ataque_rapido_ou_lento"] for palavra in ataque_rapido):
    classe["arqueiro"] += 2
    classe["lanceiro"] += 1
    classe["assassino"] += 3

elif any(palavra in dados_combate["ataque_rapido_ou_lento"] for palavra in ataque_lento):
    classe["batedor"] += 2
    classe["espadachin"] += 3
    classe["escudeiro"] += 3

elif any(palavra in dados_combate["ataque_rapido_ou_lento"] for palavra in ataque_rapido + ataque_lento):
    classe["batedor"] += 1
    classe["lanceiro"] += 1
    classe["escudeiro"] += 1
    classe["espadachin"] += 1
    classe["arqueiro"] += 1
    classe["assassino"] += 1

elif any(palavra in dados_combate["ataque_rapido_ou_lento"] for palavra in incertezas):
    print("você não terá pontos atribuidos")

# PERGUNTA 2

if any(palavra in dados_combate["defesa_ou_ataque"] for palavra in defesa):
    classe["escudeiro"] += 3

elif any(palavra in dados_combate["defesa_ou_ataque"] for palavra in ataque):
    classe["lanceiro"] += 1
    classe["espadachin"] += 1
    classe["assassino"] += 1
    classe["arqueiro"] += 1
    classe["batedor"] += 1

elif any(palavra in dados_combate["defesa_ou_ataque"] for palavra in defesa + ataque):
    classe["batedor"] += 1
    classe["lanceiro"] += 1
    classe["escudeiro"] += 1
    classe["espadachin"] += 1
    classe["arqueiro"] += 1
    classe["assassino"] += 1

elif any(palavra in dados_combate["defesa_ou_ataque"] for palavra in incertezas):
    print("você não terá pontos atribuidos")

# PERGUNTA 3

if any(palavra in dados_combate["lutar_sozinho_ou_parceiro"] for palavra in sozinho):
    classe["assassino"] += 31
    classe["batedor"] += 1
    classe["lanceiro"] += 3

elif any(palavra in dados_combate["lutar_sozinho_ou_parceiro"] for palavra in parceiro):
    classe["arqueiro"] += 2
    classe["espadachin"] += 1
    classe["escudeiro"] += 1

elif any(palavra in dados_combate["lutar_sozinho_ou_parceiro"] for palavra in sozinho + parceiro):
    classe["batedor"] += 1
    classe["lanceiro"] += 1
    classe["escudeiro"] += 1
    classe["espadachin"] += 1
    classe["arqueiro"] += 1
    classe["assassino"] += 1

elif any(palavra in dados_combate["lutar_sozinho_ou_parceiro"] for palavra in incertezas):
    print("você não terá pontos atribuidos")

# PERGUNTA 4

if any(palavra in dados_combate["experiencia_corpo_a_corpo_ou_distancia"] for palavra in corpo_a_corpo):
    classe["escudeiro"] += 2
    classe["batedor"] += 1
    classe["espadachin"] += 2
    classe["assassino"] += 3

elif any(palavra in dados_combate["experiencia_corpo_a_corpo_ou_distancia"] for palavra in distancia):
    classe["lanceiro"] += 2
    classe["arqueiro"] += 1

elif any(palavra in dados_combate["experiencia_corpo_a_corpo_ou_distancia"] for palavra in corpo_a_corpo + distancia):
    classe["batedor"] += 1
    classe["lanceiro"] += 1
    classe["escudeiro"] += 1
    classe["espadachin"] += 1
    classe["arqueiro"] += 1
    classe["assassino"] += 1

elif any(palavra in dados_combate["experiencia_corpo_a_corpo_ou_distancia"] for palavra in incertezas):
    print("você não terá pontos atribuidos")

# Resultado classe

classe_jogador = max(classe , key=classe.get)

print(f"\n{dados_pessoais['nome']}, sua classe é: {classe_jogador}")

# CRIANDO O JOGADOR

def status_jogador():
    if classe_jogador == classe['escudeiro']:
        descrição_jogador["escudo"] = "sim"
    
    atributos_jogador = 5
    
    descrição_jogador = {
        "nome": dados_pessoais["nome"],
        "idade": dados_pessoais["idade"],
        "peso": dados_pessoais["peso"],
        "sexo": dados_pessoais["sexo"],
        "altura": dados_pessoais["altura"],
        "nível": atributos_jogador,
        "dano": 10 * atributos_jogador,
        "velocidade": 7 * atributos_jogador,
        "defesa": 8 * atributos_jogador,
        "vida": 120 * atributos_jogador,
        "vida máxima": 1.000,
        "arma": arma_inicial,
        "experiencia": 0,
        "experiencia máxima": 300,
        "classe": classe_jogador,
        "escudo": ""
    }
    
    return descrição_jogador

jogador = status_jogador()

# JANELA DE STATUS

def janela_de_status():

    atributos_jogador = 5

    return {
        "nome": dados_pessoais["nome"],
        "nível": atributos_jogador,
        "dano": 10 * atributos_jogador,
        "velocidade":  7 * atributos_jogador,
        "defesa":  8 * atributos_jogador,
        "vida":  120 * atributos_jogador,
        "arma": jogador["arma"],
        "experiencia": 0,
        "classe": classe_jogador
    }

from random import randint, choice

def monstros_comum():
    lista_de_monstros = []

    def goblin():
        atributos = randint(0, 0)
        return {
            "nome": "goblin",
            "nível": atributos,
            "ataque": 0 * atributos,
            "velocidade": 0 * atributos,
            "defesa": 0 * atributos,
            "vida": 0 * atributos,
            "arma": "adaga"
        }

    def esqueleto():
        atributos = randint(0, 80)
        return {
            "nome": "esqueleto",
            "nível": atributos,
            "ataque": 0 * atributos,
            "velocidade": 0 * atributos,
            "defesa": 0 * atributos,
            "vida": 0 * atributos,
            "arma": "espada básica"
        }

    def lobo():
        atributos = randint(0, 0)
        return {
            "nome": "lobo",
            "nível": atributos,
            "ataque": 0 * atributos,
            "velocidade": 0 * atributos,
            "defesa": 0 * atributos,
            "vida": 0 * atributos,
            "arma": "nenhuma"
        }

    def zumbi():
        atributos = randint(0, 0)
        return {
            "nome": "zumbi",
            "nível": atributos,
            "ataque": 0 * atributos,
            "velocidade": 0 * atributos,
            "defesa": 0 * atributos,
            "vida": 0 * atributos,
            "arma": "espada básica"
        }
    
    def cão_selvagem():
        atributos = randint(0, 80)
        return {
            "nome": "cão selvagem",
            "nível": atributos,
            "ataque": 0 * atributos,
            "velocidade": 0 * atributos,
            "defesa": 0 * atributos,
            "vida": 0 * atributos,
            "arma": "nenhuma"
        }
    
    def rato_saqueador():
        atributos = randint(0, 0)
        return {
            "nome": "rato_saqueador",
            "nível": atributos,
            "ataque": 0 * atributos,
            "velocidade": 0 * atributos,
            "defesa": 0 * atributos,
            "vida": 0 * atributos,
            "arma": "nenhuma"
        }

    def gorila_raivoso():
        atributos = randint(0, 0)
        return {
            "nome": "gorila_raivoso",
            "nível": atributos,
            "ataque": 0 * atributos,
            "velocidade": 0 * atributos,
            "defesa": 0 * atributos,
            "vida": 0 * atributos,
            "arma": "nenhuma"
        }

def monstros_icomum():
    lista_de_monstros = []

    def orc():
        atributos = randint(0, 0)
        return {
            "nome": "orc",
            "nível": atributos,
            "ataque": 0 * atributos,
            "velocidade": 0 * atributos,
            "defesa": 0 * atributos,
            "vida": 0 * atributos,
            "arma": "lábris"
        }

    def troll():
        atributos = randint(0, 0)
        return {
            "nome": "troll",
            "nível": atributos,
            "ataque": 0 * atributos,
            "velocidade": 0 * atributos,
            "defesa": 0 * atributos,
            "vida": 0 * atributos,
            "arma": "cutelo"
        }

    def goblin_sombrio():
        atributos = randint(0, 0)
        return {
            "nome": "goblin sombrio",
            "nível": atributos,
            "ataque": 0 * atributos,
            "velocidade": 0 * atributos,
            "defesa": 0 * atributos,
            "vida": 0 * atributos,
            "arma": "adagas duplas"
        }

    def javali_mutante():
        atributos = randint(0, 0)
        return {
            "nome": "javali mutante",
            "nível": atributos,
            "ataque": 0 * atributos,
            "velocidade": 0 * atributos,
            "defesa": 0 * atributos,
            "vida": 0 * atributos,
            "arma": "nenhuma"
        }

    def goblin_arqueiro():
        atributos = randint(0, 0)
        return {
            "nome": "goblin arqueiro",
            "nível": atributos,
            "ataque": 0 * atributos,
            "velocidade": 0 * atributos,
            "defesa": 0 * atributos,
            "vida": 0 * atributos,
            "arma": "arco"
        }
    
def monstros_raros():

    def esqueleto_negro():
        atributos = randint(0, 0)
        return {
            "nome": "esqueleto negro",
            "nível": atributos,
            "ataque": 0 * atributos,
            "velocidade": 0 * atributos,
            "defesa": 0 * atributos,
            "vida": 0 * atributos,
            "arma": "espaga longa"
        }
    
    def demonio():
        atributos = randint(0, 0)
        return {
            "nome": "demonio",
            "nível": atributos,
            "ataque": 0 * atributos,
            "velocidade": 0 * atributos,
            "defesa": 0 * atributos,
            "vida": 0 * atributos,
            "arma": "manopola"
        }
    
    def besta_de_gelo():
        atributos = randint(0, 0)
        return {
            "nome": "besta de gelo",
            "nível": atributos,
            "ataque": 0 * atributos,
            "velocidade": 0 * atributos,
            "defesa": 0 * atributos,
            "vida": 0 * atributos,
            "arma": "nehuma"
        }

    def aranha_rainha():
        atributos = randint(0, 0)
        return {
            "nome": "aranha rainha",
            "nível": atributos,
            "ataque": 0 * atributos,
            "velocidade": 0 * atributos,
            "defesa": 0 * atributos,
            "vida": 0 * atributos,
            "arma": "nenhuma"
        }

    def lobo_alfa():
        atributos = randint(0, 0)
        return {
            "nome": "lobo alfa",
            "nível": atributos,
            "ataque": 0 * atributos,
            "velocidade": 0 * atributos,
            "defesa": 0 * atributos,
            "vida": 0 * atributos,
            "arma": "nenhuma"
        }

    def goblin_assassino():
        atributos = randint(0, 0)
        return {
            "nome": "goblin assassino",
            "nível": atributos,
            "ataque": 0 * atributos,
            "velocidade": 0 * atributos,
            "defesa": 0 * atributos,
            "vida": 0 * atributos,
            "arma": "cutelo duplo"
        }

    def esqueleto_cavalero():
        atributos = randint(0, 0)
        return {
            "nome": "esqueleto cavaleiro",
            "nível": atributos,
            "ataque": 0 * atributos,
            "velocidade": 0 * atributos,
            "defesa": 0 * atributos,
            "vida": 0 * atributos,
            "arma": "espaga longa"
        }

    def gigante_da_montanha():
        atributos = randint(0, 0)
        return {
            "nome": "gigante da montanha",
            "nível": atributos,
            "ataque": 0 * atributos,
            "velocidade": 0 * atributos,
            "defesa": 0 * atributos,
            "vida": 0 * atributos,
            "arma": "lança"
        }

    def esqueleto_negro():
        atributos = randint(0, 0)
        return {
            "nome": "esqueleto negro",
            "nível": atributos,
            "ataque": 0 * atributos,
            "velocidade": 0 * atributos,
            "defesa": 0 * atributos,
            "vida": 0 * atributos,
            "arma": "espaga longa"
        }

    def serpente_gigante():
        atributos = randint(0, 0)
        return {
            "nome": "serpente gigante",
            "nível": atributos,
            "ataque": 0 * atributos,
            "velocidade": 0 * atributos,
            "defesa": 0 * atributos,
            "vida": 0 * atributos,
            "arma": "nenhuma"
        }

def montros_lendario():

    def colosso_cego():
        atributos = randint(0, 0)
        return {
            "nome": "colosso cego",
            "nível": atributos,
            "ataque": 0 * atributos,
            "velocidade": 0 * atributos,
            "defesa": 0 * atributos,
            "vida": 0 * atributos,
            "arma": "manopola   "
        }
    
    def rei_carniceiro():
        atributos = randint(0, 0)
        return {
            "nome": "rei carniceiro",
            "nível": atributos,
            "ataque": 0 * atributos,
            "velocidade": 0 * atributos,
            "defesa": 0 * atributos,
            "vida": 0 * atributos,
            "arma": "espada dupla"
        }

    def maquina_de_guerra():
        atributos = randint(0, 0)
        return {
            "nome": "maquina de guerra",
            "nível": atributos,
            "ataque": 0 * atributos,
            "velocidade": 0 * atributos,
            "defesa": 0 * atributos,
            "vida": 0 * atributos,
            "arma": "nenhuma"
        }

def chefe_final():

    def rei_tirano():
        atributos = 0
        return {
            "nome": "rei tirano",
            "nível": atributos,
            "ataque": 0 * atributos,
            "velocidade": 0 * atributos,
            "defesa": 0 * atributos,
            "vida": 0 * atributos,
            "arma": "todas"
        }

def atacar_jogador(monstro):
    jogador["vida"] -= monstro["dano"]

def atacar_monstro(monstro):
    monstro["vida"] -= jogador["dano"]
    atacar_jogador(monstro)
