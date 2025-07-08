
class Usuário:
    def __init__(self, nome: str, idade: int, peso: float, gênero: str, altura: float) -> None:
     
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.genero = gênero
        self.altura = altura

        self.nível_atual = 1
        self.nível_máximo = 100
        self.dano = 10
        self.velocidade = 7
        self.defesa = 8
        self.vida_atual = 100
        self.vida_máxima = 100

        self.arma = None
        self.escudo = None

        self.classe_do_usuário = None

        self.experiência_atual = 0
        self.experiência_máxima = 100

        self.estamina_atual = 100
        self.estamina_máxima = 100

        self.primeira_habilidade_passiva = None
        self.segunda_habilidade_passiva = None
        self.terceira_habilidade_passiva = None

        self.primeira_habilidade_ativa = None
        self.segunda_habilidade_ativa = None

        self.limite_de_altura()
        self.limite_de_idade()
        self.limite_de_peso()

    def limite_de_peso(self):
        if not (70 <= self.peso <= 110):
            raise ValueError
 
    def limite_de_altura(self):
        if not (1.5 <= self.altura <= 2.5):
            raise ValueError
        
    def limite_de_idade(self):
        if not (16 <= self.idade <= 25):
            raise ValueError

    def subir_de_nível(self):

        multiplicador = float(1.0)
        if 0 < self.nível_atual <= 25:
            multiplicador = 1.25
        if 25 < self.nível_atual <= 50:
            multiplicador = 1.5
        if 50 < self.nível_atual <= 75:
            multiplicador = 1.75
        if 75 < self.nível_atual == 100:
            multiplicador = 2.0

        self.experiência_máxima *= multiplicador
        self.nível_atual += 1
        self.dano *= 1.35
        self.velocidade *= 1.25
        self.defesa *= 1.25
        self.vida_máxima *= 1.75
        self.vida_atual = self.vida_máxima
        self.estamina_máxima *= 1.35
        self.estamina_atual = self.estamina_máxima

    def receber_experiência(self, experiência):
        self.experiência_atual += experiência

        while self.nível_atual < self.nível_máximo:
            if self.experiência_atual >= self.experiência_máxima:
                if self.experiência_atual == self.experiência_máxima:
                    self.experiência_atual = 0
                else:
                    self.experiência_atual -= self.experiência_máxima
                
                self.subir_de_nível()
    

    def

            
    



