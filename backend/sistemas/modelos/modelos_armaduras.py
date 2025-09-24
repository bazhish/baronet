from random import choice


class PecaArmadura:
    def __init__(self, nome_da_peca, tipo, defesa, material, durabilidade):
        self.nome_da_peca = nome_da_peca
        self.tipo = tipo
        self.defesa = defesa
        self.material = material
        self.efeitos = ["dano", "velocidade", "vida", "defesa", "bonus_de_experiencia"]
        self.equipada = False
        self.raridade = "comum"
        self.durabilidade = durabilidade
        self.efeito_aplicado = None
        self.descricao = self._gerar_descricao()

    def _gerar_descricao(self):
        return (
            f"nome da peça: {self.nome_da_peca}\n"
            f"tipo da peça: {self.tipo}\n"
            f"defesa da peça: {self.defesa}\n"
            f"material da peça: {self.material}\n"
            f"raridade da peça: {self.raridade}\n"
            f"durabilidade da peça: {self.durabilidade}"
        )

    def equipar(self, usuario):
        usuario.defesa_bonus += self.defesa
        self.equipada = True

    def escolher_raridade(self, raridade: str):
        self.raridade = raridade
        self.descricao = self._gerar_descricao()

    def aplicar_efeito_aleatorio(self, usuario):
        efeito = choice(self.efeitos)
        self.aplicar_efeito(usuario, efeito)
        self.efeito_aplicado = efeito

    def remover_beneficios(self, usuario):
        usuario.defesa_bonus = max(0, usuario.defesa_bonus - self.defesa)

        base = {
            "dano": 4,
            "velocidade": 2,
            "vida": 10,
            "defesa": 3,
            "bonus_de_experiencia": 5,
        }

        fatores = {
            "comum": 1,
            "rara": 1.5,
            "epica": 2,
            "lendario": 2.5,
        }

        fator = fatores.get(self.raridade, 1)

        if self.efeito_aplicado:
            efeito = self.efeito_aplicado
            valor = int(base.get(efeito, 0) * fator)
            if hasattr(usuario, efeito + "_bonus"):
                setattr(
                    usuario, efeito + "_bonus", getattr(usuario, efeito + "_bonus") - valor
                )

        self.equipada = False
        self.efeito_aplicado = None

    def diminuir_durabilidade(self, adversario, usuario):
        if self.durabilidade > 0:
            self.durabilidade -= adversario.dano_final // 3

        if self.durabilidade <= 0:
            self.remover_beneficios(usuario)

    def aplicar_efeito(self, usuario, efeito: str):
        base = {
            "dano": 4,
            "velocidade": 2,
            "vida": 10,
            "defesa": 3,
            "bonus_de_experiencia": 5,
        }

        fatores = {
            "comum": 1,
            "rara": 1.5,
            "epica": 2,
            "lendario": 2.5,
        }

        fator = fatores.get(self.raridade, 1)
        valor = int(base.get(efeito, 0) * fator)

        if not self.equipada and hasattr(usuario, efeito + "_bonus"):
            atual = getattr(usuario, efeito + "_bonus")
            setattr(usuario, efeito + "_bonus", atual + valor)
            self.efeito_aplicado = efeito


class ConjuntoArmadura:
    def __init__(self, nome_do_conjunto, tipo_de_conjunto):
        self.nome_do_conjunto = nome_do_conjunto
        self.tipo_de_conjunto = tipo_de_conjunto
        self.armaduras: list[PecaArmadura] = []
        self.conjunto_completo = "incompleto"
        self.status_do_conjunto = False
        self.bonus = "nenhum"
        self.status_do_bonus = False
        self.pecas_obrigatorias = ["elmo", "peitoral", "calca", "bota"]
        self.descricao = ""
        self.atualizar_descricao()

    def adicionar_peca(self, peca: PecaArmadura):
        if len(self.armaduras) < 4:
            self.armaduras.append(peca)
        self.verificar_se_o_conjunto_esta_completo()
        self.atualizar_descricao()

    def verificar_se_o_conjunto_esta_completo(self):
        if len(self.armaduras) == 4:
            self.status_do_conjunto = True
            self.conjunto_completo = "completo"
            self.status_do_bonus = True

    def aplicar_bonus_do_conjunto(self, usuario):
        if not self.status_do_bonus:
            return

        if self.tipo_de_conjunto == "ataque":
            usuario.dano_bonus *= 1.8
            usuario.defesa_bonus *= 1.6
            usuario.velocidade_bonus *= 1.4
            usuario.vida_bonus *= 1.2
        elif self.tipo_de_conjunto == "defesa":
            usuario.dano_bonus *= 1.3
            usuario.defesa_bonus *= 1.8
            usuario.velocidade_bonus *= 1.2
            usuario.vida_bonus *= 1.6
        self.exibir_bonus()

    def exibir_bonus(self):
        if self.tipo_de_conjunto == "ataque":
            self.bonus = (
                "mais 80% de dano\nmais 60% de defesa\nmais 40% de velocidade\nmais 20% de vida"
            )
        elif self.tipo_de_conjunto == "defesa":
            self.bonus = (
                "mais 30% de dano\nmais 80% de defesa\nmais 20% de velocidade\nmais 60% de vida"
            )

    def atualizar_descricao(self):
        self.descricao = (
            f"nome do conjunto: {self.nome_do_conjunto}\n"
            f"tipo do conjunto: {self.tipo_de_conjunto}\n"
            f"status do conjunto: {self.conjunto_completo}\n"
            f"peças do conjunto: {', '.join([peca.nome_da_peca for peca in self.armaduras])}\n"
            f"status do bônus: {self.bonus}\n"
        )


def gerar_peça_do_conjunto(
    conjunto: ConjuntoArmadura,
    nome_da_peca: str,
    defesa: int,
    material: str,
    raridade: str,
    usuario,
    durabilidade: int,
):
    tipo = conjunto.tipo_de_conjunto
    peca = PecaArmadura(nome_da_peca, tipo, defesa, material, durabilidade)
    peca.escolher_raridade(raridade)
    peca.aplicar_efeito_aleatorio(usuario)
    peca.equipar(usuario)
    conjunto.adicionar_peca(peca)
    return peca
