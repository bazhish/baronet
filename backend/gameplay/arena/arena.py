class Combatente:
    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque

    def atacar(self, outro):
        outro.vida -= self.ataque

    def esta_vivo(self):
        return self.vida > 0

class Arena:
    def __init__(self, combatente1, combatente2):
        self.combatente1 = combatente1
        self.combatente2 = combatente2

    def batalhar(self):
        rodada = 1
        while self.combatente1.esta_vivo() and self.combatente2.esta_vivo():
            print(f"Rodada {rodada}:")
            self.combatente1.atacar(self.combatente2)
            print(f"{self.combatente1.nome} ataca {self.combatente2.nome} ({self.combatente2.vida} vida restante)")
            if not self.combatente2.esta_vivo():
                print(f"{self.combatente1.nome} venceu!")
                break
            self.combatente2.atacar(self.combatente1)
            print(f"{self.combatente2.nome} ataca {self.combatente1.nome} ({self.combatente1.vida} vida restante)")
            if not self.combatente1.esta_vivo():
                print(f"{self.combatente2.nome} venceu!")
                break
            rodada += 1

# Exemplo de uso:
if __name__ == "__main__":
    c1 = Combatente("Herói", 30, 5)
    c2 = Combatente("Vilão", 25, 6)
    arena = Arena(c1, c2)
    arena.batalhar()