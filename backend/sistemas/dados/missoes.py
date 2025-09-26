import json

class QuestManager:
    def __init__(self, arquivo_json):
        with open(arquivo_json, "r", encoding="utf-8") as f:
            self.missoes = {m["id"]: m for m in json.load(f)}
        self.missoes_ativas = {}
        self.missoes_concluidas = set()

    def aceitar_missao(self, missao_id):
        if missao_id in self.missoes_concluidas:
            print(f"Missão '{missao_id}' já foi concluída.")
            return
        missao = self.missoes.get(missao_id)
        if missao and (missao["requisito_previo"] is None or missao["requisito_previo"] in self.missoes_concluidas):
            self.missoes_ativas[missao_id] = {"progresso": 0, "objetivo": missao["objetivo"]}
            print(f"Missão aceita: {missao['titulo']}")
        else:
            print("Não é possível aceitar essa missão agora.")

    def atualizar_progresso(self, missao_id, quantidade=1):
        if missao_id not in self.missoes_ativas:
            return
        progresso = self.missoes_ativas[missao_id]
        objetivo = progresso["objetivo"]["quantidade"]

        progresso["progresso"] += quantidade
        print(f"Progresso da missão {missao_id}: {progresso['progresso']}/{objetivo}")

        if progresso["progresso"] >= objetivo:
            self.concluir_missao(missao_id)

    def concluir_missao(self, missao_id):
        if missao_id not in self.missoes_ativas:
            return
        missao = self.missoes[missao_id]
        self.missoes_concluidas.add(missao_id)
        del self.missoes_ativas[missao_id]
        print(f"Missão concluída: {missao['titulo']}")
        print(f"Recompensa: +{missao['recompensa']['xp']} XP, +{missao['recompensa']['moeda']} moedas")
        if missao["recompensa"]["item"]:
            print(f"Item recebido: {missao['recompensa']['item']}")

q = QuestManager("missoess.json")

q.aceitar_missao("missao_1")
q.atualizar_progresso("missao_1", 5)
q.atualizar_progresso("missao_1", 5)