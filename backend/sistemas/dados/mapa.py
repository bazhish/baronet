import json

class Mapa:
    def __init__(self, arquivo_json):
        with open(arquivo_json, "r", encoding="utf-8") as f:
            self.locais = json.load(f)

    def mostrar_locais(self, missoes_concluidas):
        print("\nLocais disponíveis:")
        for local in self.locais:
            if (local["requisito_missao"] is None 
                or local["requisito_missao"] in missoes_concluidas):
                print(f"- {local['nome']}: {local['descricao']}")

    def desbloquear_local(self, local_id, missoes_concluidas):
        for local in self.locais:
            if local["id"] == local_id:
                if (local["requisito_missao"] is None 
                    or local["requisito_missao"] in missoes_concluidas):
                    print(f"Você pode acessar {local['nome']}.")
                    return local
                else:
                    print(f"{local['nome']} ainda não está disponível.")
                    return None

# Supondo que já temos QuestManager
qm = QuestManager("missoes.json")
mapa = Mapa("mapa.json")

# Jogador conclui a missão 1
qm.aceitar_missao("missao_1")
qm.atualizar_progresso("missao_1", 10)

# Mostrar locais liberados
mapa.mostrar_locais(qm.missoes_concluidas)

# Tentar acessar floresta
mapa.desbloquear_local("floresta", qm.missoes_concluidas)
