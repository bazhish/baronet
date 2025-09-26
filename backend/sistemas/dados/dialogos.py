import json

class DialogoManager:
    def __init__(self, arquivo_json):
        with open(arquivo_json, "r", encoding="utf-8") as f:
            self.dialogos = json.load(f)

    def iniciar_dialogo(self, npc_id, quest_manager):
        if npc_id not in self.dialogos:
            print("Este NPC não possui diálogo.")
            return

        for parte in self.dialogos[npc_id]:
            print(f"{npc_id}: {parte['fala']}")

            # Se houver escolhas, exibe opções
            if "escolhas" in parte:
                for i, escolha in enumerate(parte["escolhas"], start=1):
                    print(f"{i} - {escolha['resposta']}")

                opcao = int(input("Escolha uma opção: "))
                escolha = parte["escolhas"][opcao - 1]

                if escolha["acao"] == "aceitar_missao":
                    quest_manager.aceitar_missao(escolha["missao_id"])
                elif escolha["acao"] == "recusar_missao":
                    print("Você recusou a missão.")

                # Após a escolha, encerra este diálogo
                break
qm = QuestManager("missoes.json")
dm = DialogoManager("dialogos.json")

# Jogador conversa com o fazendeiro
dm.iniciar_dialogo("fazendeiro", qm)
