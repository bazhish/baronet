class Inventario:
    def __init__(self):
        self.itens = []
        self.equipados = {
            "arma": None,
            "armadura": None,
            "escudo": None
        }

    def adicionar_item(self, item):
        self.itens.append(item)

    def remover_item(self, item):
        if item in self.itens:
            self.itens.remove(item)

    def listar_itens(self):
        return [(type(item).__name__, getattr(item, 'nome', 'Sem nome')) for item in self.itens]

    def equipar(self, item):
        tipo = type(item).__name__.lower()
        if tipo in self.equipados:
            self.equipados[tipo] = item
            print(f"{tipo} equipado: {getattr(item, 'nome', 'sem nome')}")
        else:
            print("Este item não pode ser equipado.")

    def desequipar(self, tipo):
        if tipo in self.equipados and self.equipados[tipo]:
            print(f"{tipo} desequipado: {getattr(self.equipados[tipo], 'nome', 'sem nome')}")
            self.equipados[tipo] = None

    def usar_item(self, item):
        if hasattr(item, "usar"):
            item.usar()
            self.remover_item(item)

inventario = Inventario()
inventario.adicionar_item("Espada")
inventario.listar_itens()

