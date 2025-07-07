from random import *

classes = ["Arqueiro", "Espadachin", "Assassino", "Escudeiro", "Lanceiro", "Batedor"]

class Adviversarios:
    def __init__ (self, nome, classe):
        self.nome = nome
        self.classe = classe.choice(classes)
        self.nível = 1
        self.vida = 1
        self.dano = Dano
        self.velocidade = velocidade

    def NívelDoAdversario(self):

        if jogador["nível"] <= 10:
            self.nível = random.randint(0, 10)

        elif 10 <= jogador["nível"] <= 20:
            self.nível = random.randint(10, 20)

        elif 20 <= jogador["nível"] <= 30:
            self.nível = random.randint(20, 30)

        elif 30 <= jogador["nível"] <= 40:
            self.nível = random.randint(30, 40)
        
        elif 40 <= jogador["nível"] <= 50:
            self.nível = random.randint(40, 50)

        elif 50 <= jogador["nível"] <= 60:
            self.nível = random.randint(50, 60)
        
        elif 60 <= jogador["nível"] <= 70:
            self.nível = random.randint(60, 70)
        
        elif 70 <= jogador["nível"] <= 80:
            self.nível = random.randint(70, 80)
        
        elif 80 <= jogador["nível"] <= 90:
            self.nível = random.randint(80, 90)

        elif 90 <= jogador["nível"] <= 100:
            self.nível = random.randint(90, 100)

        else: pass
