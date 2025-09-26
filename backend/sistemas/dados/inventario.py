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
        tipo = item.tipo if hasattr(item, 'tipo') else None
        if tipo in self.equipados:
            self.equipados[tipo] = item


    def desequipar(self, tipo):
        if tipo in self.equipados and self.equipados[tipo]:
            self.equipados[tipo] = None

    def usar_item(self, item):
        if hasattr(item, "usar"):
            item.usar()
            self.remover_item(item)
