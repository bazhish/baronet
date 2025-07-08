from abc import ABC, abstractmethod

class EfeitoMunição:
    def __init__(self, nome, alcance, duração, dano , velocidade, defesa):
        self.nome = nome
        self.alcance = alcance
        self.duração = duração
        self.dano = dano
        self.velocidade = velocidade
        self.defesa = defesa
        self.descrição = {
            "nome do efeito": self.nome,
            "Alcance do efeito": self.alcance,
            "Duração do efeito": self.duração,
            "Dano do efeito por turno": self.dano,
            "Velocidade que será reduzida do alvo": self.velocidade,
            "Defesa que será reduzida do alvo": self.defesa
        }

    @abstractmethod
    def aplicar_efeito(ABC):
        pass

class Veneno(EfeitoMunição):
    def __init__(self):
        super().__init__("Veneno", 3, 3, 5, 1, 2)
        
    def aplicar_efeito(self, alvo: dict):
        for turno in range(self.duração):
            alvo["vida"] -= self.dano
            alvo["velocidade"] = max(0, alvo["velocidade"] - self.velocidade)
            alvo["defesa"] = max(0, alvo["defesa"] - self.defesa)

class Flamejante(EfeitoMunição):
    def __init__(self):
        super().__init__("Flamejante", 1, 2, 5, 2, 3)

    def aplicar_efeito(self, alvo: dict):
        for turno in range(self.duração):
            alvo["vida"] -= self.dano
            alvo["velocidade"] = max(0, alvo["velocidade"] - self.velocidade)
            alvo["defesa"] = max(0, alvo["defesa"] - self.defesa)

class Paralisante(EfeitoMunição):
    def __init__(self):
        super().__init__("Paralisante", 1, 4, 0, 0, 0)

    def aplicar_efeito(self, alvo: dict):
        for turno in range(self.duração):
            alvo["velocidade"] = 0
            alvo["defesa"] = 0 

class Tranquilizante(EfeitoMunição):
    def __init__(self):
        super().__init__("Tranquilizante", 5, 5, 0, 3, 2)

    def aplicar_efeito(self, alvo: dict):
        for turno in range(self.duração):
            alvo["velocidade"] = max(0, alvo["velocidade"] - self.velocidade)
            alvo["defesa"] = max(0, alvo["defesa"] - self.defesa)

class Assoviante(EfeitoMunição):
    def __init__(self):
        super().__init__("Assoviante", 10, 1, 0, 0, 10)
        
    def aplicar_efeito(self, alvo: dict):
        for turno in range(self.duração):
            alvo["defesa"] = max(0, alvo["defesa"] - self.defesa)

class Explosiva(EfeitoMunição):
    def __init__(self):
        super().__init__("Explosiva", 5, 1, 30, 10, 9)

    def aplicar_efeito(self, alvo: dict):
        for turno in range(self.duração):
            alvo["vida"] -= self.dano
            alvo["velocidade"] = max(0, alvo["velocidade"] - self.velocidade)
            alvo["defesa"] = max(0, alvo["defesa"] - self.defesa)

class Eletrocutante(EfeitoMunição):
    def __init__(self):
        super().__init__("Eletrocutante", 3, 2, 10, 5, 4)

    def aplicar_efeito(self, alvo: dict):
        for turno in range(self.duração):
            alvo["vida"] -= self.dano
            alvo["velocidade"] = max(0, alvo["velocidade"] - self.velocidade)
            alvo["defesa"] = max(0, alvo["defesa"] - self.defesa)

class Desintegrador(EfeitoMunição):
    def __init__(self):
        super().__init__("Desintegrador", 1, 1, 50, 0, 0)

    def aplicar_efeito(self, alvo: dict):
        for turno in range(self.duração):
            alvo["vida"] -= self.dano
            alvo["velocidade"] = max(0, alvo["velocidade"] - self.velocidade)
            alvo["defesa"] = max(0, alvo["defesa"] - self.defesa)

class Congelante(EfeitoMunição):
    def __init__(self):
        super().__init__("Congelante", 2, 3, 15, 3, 5)

    def aplicar_efeito(self, alvo: dict):
        for turno in range(self.duração):
            alvo["vida"] -= self.dano
            alvo["velocidade"] = max(0, alvo["velocidade"] - self.velocidade)
            alvo["defesa"] = max(0, alvo["defesa"] - self.defesa)   

efeito_assoviante = Assoviante()
efeito_congelante = Congelante()
efeito_desintegrador = Desintegrador()
efeito_eletrocutante = Eletrocutante()
efeito_explosivo = Explosiva()
efeito_flamengante = Flamejante()
efeito_paralisante = Paralisante()
efeito_tranquilizante = Tranquilizante()
efeito_venenoso = Veneno()