def Atacarjogador(jogador, monstro):
    if jogador["defesa"] > 0:
        jogador["defesa"] -= monstro["dano"]
        if jogador["defesa"] < 0:
            jogador["vida"] += jogador["defesa"]
            jogador["defesa"] = 0
    else:
        jogador["vida"] -= monstro["dano"]

    if jogador["vida"] <= 0:
        print("jogador morreu")

def AtacarMontro(monstro, jogador):
    if monstro["defesa"] > 0:
        monstro["defesa"] -= jogador["dano"]
        if monstro["defesa"] < 0:
            monstro["vida"] += monstro["defesa"]
            monstro["defesa"] = 0
    else:
        monstro["vida"] -= jogador["dano"]

    if monstro["vida"] <= 0:
        print("monstro morreu")
