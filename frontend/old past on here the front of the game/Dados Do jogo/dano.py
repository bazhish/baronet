jogador = None

def atacar_jogador(monstro):
    jogador["vida"] -= monstro["dano"]

def atacar_monstro(monstro):
    monstro["vida"] -= jogador["dano"]
    atacar_jogador(monstro)
