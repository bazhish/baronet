import json

class NPC:
    def __init__(self, dados):
        self.id = dados["id"]
        self.nome = dados["nome"]
        self.mapa = dados["mapa"]
        self.missao_id = dados.get("missao_id")
        self.dialogo = dados["dialogo"]

    def falar(self):
        print(f"{self.nome}: {self.dialogo}")
class GerenciadorNPCs:
    def __init__(self, arquivo_json):
        with open(arquivo_json, "r", encoding="utf-8") as f:
            self.npcs = {npc["id"]: NPC(npc) for npc in json.load(f)}

    def get_npc(self, npc_id):
        return self.npcs.get(npc_id)

    def interagir(self, npc_id, quest_manager):
        npc = self.get_npc(npc_id)
        if not npc:
            print("NPC não encontrado.")
            return

        npc.falar()
        if npc.missao_id:
            quest_manager.aceitar_missao(npc.missao_id)

# Supondo que já temos QuestManager carregado
qm = QuestManager("missoes.json")
npcs = GerenciadorNPCs("personagens.json")

# Jogador encontra o fazendeiro
npcs.interagir("fazendeiro", qm)

# Avança progresso da missão
qm.atualizar_progresso("missao_1", 10)
