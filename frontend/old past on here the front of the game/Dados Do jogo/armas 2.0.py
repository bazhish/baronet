# CLASSE PRINCIPAL: ARMA

class Arma:
    def __init__(self, nome, raridade):
        self.nome = nome
        self.raridade = raridade
        self.dano = 0
        self.bonus = 0
        self.velocidade = 0
        self.atributo = None
        self.nível = 1
        
    def NívelDaArma(self):

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

    def DanoDaArma(self):
        self.dano = self.dano * self.nível

    def VelocidadeQueOplayerIraPerder(self):
        if jogador["arma"] is not None:
            jogador["velocidade"] -= self.velocidade

    def BonusDeExperiência(self, bonus):
        self.bonus = bonus

    def AtributoAdicional(self, atributo):
        self.atributo = atributo

        if atributo == "dano":
            jogador["dano"] += 5
        elif atributo == "vida":
            jogador["vida"] += 100
        elif atributo == "velocidade":
            jogador["velocidade"] += 10
        elif atributo == "defesa":
            jogador["defesa"] += 10

# SUBCLASSES: RARIDADE

class ArmasComuns(Arma):
    def __init__(self, nome):
        super().__init__(nome, "comum")

class ArmasRaras(Arma):
    def __init__(self, nome):
        super().__init__(nome, "rara")

class ArmasÉpicas(Arma):
    def __init__(self, nome):
        super().__init__(nome, "épico")

class ArmasLendarias(Arma):
    def __init__(self, nome):
        super().__init__(nome, "lendário")

# CRIANDO ADAGAS

AdagaComum = ArmasComuns("Adaga cega")
AdagaComum.dano = 6
AdagaComum.DanoDaArma()
AdagaComum.NívelDaArma()
AdagaComum.velocidade = 2
AdagaComum.VelocidadeQueOplayerIraPerder()
AdagaComum.BonusDeExperiência(0.1)
AdagaComum.AtributoAdicional("vida")

AdagaRara = ArmasRaras("Adaga afiada")
AdagaRara.dano = 12
AdagaRara.DanoDaArma()
AdagaRara.NívelDaArma()
AdagaRara.velocidade = 16
AdagaRara.VelocidadeQueOplayerIraPerder()
AdagaRara.BonusDeExperiência(0.25)
AdagaRara.AtributoAdicional("velocidade")

AdagaÉpica = ArmasÉpicas("Adaga relâmpago")
AdagaÉpica.dano = 20
AdagaÉpica.DanoDaArma()
AdagaÉpica.NívelDaArma()
AdagaÉpica.velocidade = 20
AdagaÉpica.VelocidadeQueOplayerIraPerder()
AdagaÉpica.BonusDeExperiência(0.60)
AdagaÉpica.AtributoAdicional("velocidade")

AdagaLendaria = ArmasLendarias("Adaga caída dos céus")
AdagaLendaria.dano = 30
AdagaLendaria.DanoDaArma()
AdagaLendaria.NívelDaArma()
AdagaLendaria.velocidade = 30
AdagaLendaria.VelocidadeQueOplayerIraPerder()
AdagaLendaria.BonusDeExperiência(0.78)
AdagaLendaria.AtributoAdicional("velocidade")

# CRIANDO ESPADAS

EspadaComum = ArmasComuns("Espada cega")
EspadaComum.dano = 6
EspadaComum.DanoDaArma()
EspadaComum.NívelDaArma()
EspadaComum.velocidade = 2
EspadaComum.VelocidadeQueOplayerIraPerder()
EspadaComum.BonusDeExperiência(0.1)
EspadaComum.AtributoAdicional("vida")

EspadaRara = ArmasRaras("Espada afiada")
EspadaRara.dano = 12
EspadaRara.DanoDaArma()
EspadaRara.NívelDaArma()
EspadaRara.velocidade = 16
EspadaRara.VelocidadeQueOplayerIraPerder()
EspadaRara.BonusDeExperiência(0.25)
EspadaRara.AtributoAdicional("velocidade")

EspadaÉpica = ArmasÉpicas("Espada relâmpago")
EspadaÉpica.dano = 20
EspadaÉpica.DanoDaArma()
EspadaÉpica.NívelDaArma()
EspadaÉpica.velocidade = 20
EspadaÉpica.VelocidadeQueOplayerIraPerder()
EspadaÉpica.BonusDeExperiência(0.60)
EspadaÉpica.AtributoAdicional("velocidade")

EspadaLendaria = ArmasLendarias("Espada caída dos céus")
EspadaLendaria.dano = 30
EspadaLendaria.DanoDaArma()
EspadaLendaria.NívelDaArma()
EspadaLendaria.velocidade = 30
EspadaLendaria.VelocidadeQueOplayerIraPerder()
EspadaLendaria.BonusDeExperiência(0.78)
EspadaLendaria.AtributoAdicional("velocidade")

# CRIANDO CUTELOSS

CuteloComum = ArmasComuns("Cutelo cega")
CuteloComum.dano = 6
CuteloComum.DanoDaArma()
CuteloComum.NívelDaArma()
CuteloComum.velocidade = 2
CuteloComum.VelocidadeQueOplayerIraPerder()
CuteloComum.BonusDeExperiência(0.1)
CuteloComum.AtributoAdicional("vida")

CuteloRaro = ArmasRaras("Cutelo afiada")
CuteloRaro.dano = 12
CuteloRaro.DanoDaArma()
CuteloRaro.NívelDaArma()
CuteloRaro.velocidade = 16
CuteloRaro.VelocidadeQueOplayerIraPerder()
CuteloRaro.BonusDeExperiência(0.25)
CuteloRaro.AtributoAdicional("velocidade")

CuteloÉpico = ArmasÉpicas("Cutelo relâmpago")
CuteloÉpico.dano = 20
CuteloÉpico.DanoDaArma()
CuteloÉpico.NívelDaArma()
CuteloÉpico.velocidade = 20
CuteloÉpico.VelocidadeQueOplayerIraPerder()
CuteloÉpico.BonusDeExperiência(0.60)
CuteloÉpico.AtributoAdicional("velocidade")

CuteloLendario = ArmasLendarias("Cutelo caída dos céus")
CuteloLendario.dano = 30
CuteloLendario.DanoDaArma()
CuteloLendario.NívelDaArma()
CuteloLendario.velocidade = 30
CuteloLendario.VelocidadeQueOplayerIraPerder()
CuteloLendario.BonusDeExperiência(0.78)
CuteloLendario.AtributoAdicional("velocidade")

# CRIANDO MACHADOS

MachadoComum = ArmasComuns("Machado cega")
MachadoComum.dano = 6
MachadoComum.DanoDaArma()
MachadoComum.NívelDaArma()
MachadoComum.velocidade = 2
MachadoComum.VelocidadeQueOplayerIraPerder()
MachadoComum.BonusDeExperiência(0.1)
MachadoComum.AtributoAdicional("vida")

MachadoRaro = ArmasRaras("Machado afiada")
MachadoRaro.dano = 12
MachadoRaro.DanoDaArma()
MachadoRaro.NívelDaArma()
MachadoRaro.velocidade = 16
MachadoRaro.VelocidadeQueOplayerIraPerder()
MachadoRaro.BonusDeExperiência(0.25)
MachadoRaro.AtributoAdicional("velocidade")

MachadoÉpico = ArmasÉpicas("Machado relâmpago")
MachadoÉpico.dano = 20
MachadoÉpico.DanoDaArma()
MachadoÉpico.NívelDaArma()
MachadoÉpico.velocidade = 20
MachadoÉpico.VelocidadeQueOplayerIraPerder()
MachadoÉpico.BonusDeExperiência(0.60)
MachadoÉpico.AtributoAdicional("velocidade")

MachadoLendario = ArmasLendarias("Machado caída dos céus")
MachadoLendario.dano = 30
MachadoLendario.DanoDaArma()
MachadoLendario.NívelDaArma()
MachadoLendario.velocidade = 30
MachadoLendario.VelocidadeQueOplayerIraPerder()
MachadoLendario.BonusDeExperiência(0.78)
MachadoLendario.AtributoAdicional("velocidade")

# CRIANDO ESPADA CURTA

EspadaCurtaComum = ArmasComuns("Espada cega")
EspadaCurtaComum.dano = 6
EspadaCurtaComum.DanoDaArma()
EspadaCurtaComum.NívelDaArma()
EspadaCurtaComum.velocidade = 2
EspadaCurtaComum.VelocidadeQueOplayerIraPerder()
EspadaCurtaComum.BonusDeExperiência(0.1)
EspadaCurtaComum.AtributoAdicional("vida")

EspadaCurtaRara = ArmasRaras("EspadaCurta afiada")
EspadaCurtaRara.dano = 12
EspadaCurtaRara.DanoDaArma()
EspadaCurtaRara.NívelDaArma()
EspadaCurtaRara.velocidade = 16
EspadaCurtaRara.VelocidadeQueOplayerIraPerder()
EspadaCurtaRara.BonusDeExperiência(0.25)
EspadaCurtaRara.AtributoAdicional("velocidade")

EspadaCurtaÉpica = ArmasÉpicas("EspadaCurta relâmpago")
EspadaCurtaÉpica.dano = 20
EspadaCurtaÉpica.DanoDaArma()
EspadaCurtaÉpica.NívelDaArma()
EspadaCurtaÉpica.velocidade = 20
EspadaCurtaÉpica.VelocidadeQueOplayerIraPerder()
EspadaCurtaÉpica.BonusDeExperiência(0.60)
EspadaCurtaÉpica.AtributoAdicional("velocidade")

EspadaCurtaLendaria = ArmasLendarias("EspadaCurta caída dos céus")
EspadaCurtaLendaria.dano = 30
EspadaCurtaLendaria.DanoDaArma()
EspadaCurtaLendaria.NívelDaArma()
EspadaCurtaLendaria.velocidade = 30
EspadaCurtaLendaria.VelocidadeQueOplayerIraPerder()
EspadaCurtaLendaria.BonusDeExperiência(0.78)
EspadaCurtaLendaria.AtributoAdicional("velocidade")




