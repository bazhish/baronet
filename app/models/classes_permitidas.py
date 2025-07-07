from classe_atributos import (
    assassino, lanceiro, arqueiro, batedor, espadachim
)

def definir_classes_permitidas(tipo):
        if "arco" in tipo or "besta" in tipo or "zarabatana" in tipo:
            return [arqueiro, assassino]
        elif "espada" in tipo or "katana" in tipo or "sabre" in tipo:
            return [espadachim, assassino]
        elif "adaga" in tipo:
            return [assassino]
        elif "manopla" in tipo:
            return [batedor, assassino]
        elif "lança" in tipo:
            return [lanceiro]
        elif "machado" in tipo or "cutelo" in tipo:
            return [batedor, assassino]
