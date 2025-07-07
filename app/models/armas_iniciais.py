from armas import Arma
from _munições import Munição
from escudo import Escudo


# FUNC ESPADA
def espada_inicial(usuario):
    espada = Arma("espada curta", "espada de ferro enferrujada", 6, 2, 50, 100, 0.1, 0.25, 0.2)
    espada.nivel_com_parametro_manual(1)
    espada.dano_da_arma()
    espada.velocidade_que_o_usuario_ira_perder(usuario)
    espada.escolha_de_raridade("comum")
    espada.atributo_adicional_aleatorio(usuario)

    return espada

# FUNC ADAGA
def adaga_inicial(usuario):
    adaga = Arma("adaga", "adaga sem ponta", 5, 3, 50, 100, 0.1, 0.25, 0.2)
    adaga.nivel_com_parametro_manual(1)
    adaga.dano_da_arma()
    adaga.velocidade_que_o_usuario_ira_perder(usuario)
    adaga.escolha_de_raridade("comum")
    adaga.atributo_adicional_aleatorio(usuario)
    return adaga

# FUNC LANÇA
def lanca_inicial(usuario):
    lanca = Arma("lança", "lança com o cabo quebrado", 6, 4, 50, 100, 0.1, 0.25, 0.2)
    lanca.nivel_com_parametro_manual(1)
    lanca.dano_da_arma()
    lanca.velocidade_que_o_usuario_ira_perder(usuario)
    lanca.escolha_de_raridade("comum")
    lanca.atributo_adicional_aleatorio(usuario)
    return lanca

# FUNC ARCO
def arco_inicial(usuario):
    arco = Arma("arco", "arco antigo", 5, 3, 50, 100, 0.1, 0.25, 0.2)
    arco.nivel_com_parametro_manual(1)
    arco.dano_da_arma()
    arco.velocidade_que_o_usuario_ira_perder(usuario)
    arco.escolha_de_raridade("comum")
    arco.atributo_adicional_aleatorio(usuario)
    return arco

# FUNC FLECHAS
def flechas_iniciais():
    flecha = Munição("flecha sem ponta", 5, 1)
    flecha.definir_nivel_manual(1)
    flecha.escolher_raridade("comum")
    flecha.escolher_efeito_aleatorio()
    flecha.calcular_dano()
    return flecha

# FUNC MANOPLA
def manopla_inicial(usuario):
    manopla = Arma("manopla", "soco espinhado", 8, 4, 50, 100, 0.1, 0.25, 0.2)
    manopla.nivel_com_parametro_manual(1)
    manopla.dano_da_arma()
    manopla.velocidade_que_o_usuario_ira_perder(usuario)
    manopla.escolha_de_raridade("comum")
    manopla.atributo_adicional_aleatorio(usuario)
    
    return manopla

# FUNC ESCUDO
def escudo_inicial(usuario):
    escudo = Escudo("escudo de mão", 5, 3)
    escudo.definir_nivel_manual(1)
    escudo.escolher_raridade("comum")
    escudo.calcular_defesa()
    escudo.escolher_atributo_adicional_aleatorio()
    escudo.aplicar_bonus_no_usuario(usuario)
    return escudo

# ARMAS:

espada = espada_inicial
adaga = adaga_inicial
lanca = lanca_inicial
arco = arco_inicial
flecha = flechas_iniciais
manopla = manopla_inicial
escudo = escudo_inicial