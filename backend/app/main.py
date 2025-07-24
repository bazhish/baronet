import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from backend.app.models.personagens.adversarios import AdversarioDemiHumano, AdversarioMontro
from backend.app.models.personagens.personagem_principal import Usuario

goblin = AdversarioDemiHumano("goblin", 30, 50, "masculino", 1.5, 8, 5, 1, 2, 3, 10, 10, None, None, None, None, None, None, None, None)

slime = AdversarioMontro("slime", 30, 1.0, 9, 0, 3, 8, 2, 15, None, None)

jogador = Usuario(20, 90, "pedro", "maculino", 1.80, None, None, None, None, None, None, None, None)
jogador.receber_experiência(5000)

while jogador.vida_atual > 0 and goblin.vida_atual > 0:
    print(f"{jogador.nome} ataca {goblin.nome}!")
    jogador.atacar(goblin)
    print(f"{goblin.nome} agora tem {goblin.vida_atual} de vida.")

    if goblin.vida_atual <= 0:
        print(f"{goblin.nome} foi derrotado!")
        jogador.receber_experiência(goblin.experiência)
        print(f"{jogador.nome} recebeu {goblin.experiência} de experiência")
        break

    print(f"{goblin.nome} ataca {jogador.nome}!")
    goblin.atacar(jogador)
    print(f"{jogador.nome} agora tem {jogador.vida_atual} de vida.")

    if jogador.vida_atual <= 0:
        print(f"{jogador.nome} foi derrotado!")
        break

print ("\n",jogador.descrição)
print (goblin.descrição)