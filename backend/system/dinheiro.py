class Dinheiro:
    def __init__(self, ouro=0):
        self.ouro = ouro

    def adicionar(self, quantidade):
        if quantidade < 0:
            print("Não é possível adicionar uma quantidade negativa.")
            return
        self.ouro += quantidade
        print(f"Adicionado {quantidade} ouro(s).")

    def gastar(self, quantidade):
        if quantidade < 0:
            print("Não é possível gastar uma quantidade negativa.")
            return False
        if quantidade > self.ouro:
            print("Saldo insuficiente!")
            return False
        self.ouro -= quantidade
        print(f"Gastou {quantidade} ouro(s).")
        return True

    def mostrar(self):
        print(f"Saldo atual: {self.ouro} ouro(s).")

# Exemplo de uso:
dinheiro_jogador = Dinheiro(ouro=50)
dinheiro_jogador.mostrar()

dinheiro_jogador.adicionar(25)
dinheiro_jogador.mostrar()

if dinheiro_jogador.gastar(60):
    print("Compra realizada com sucesso!")
else:
    print("Falha na compra.")

dinheiro_jogador.mostrar()
