import sys, os
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = current_dir
while not os.path.isdir(os.path.join(project_root, ".git")) and os.path.dirname(project_root) != project_root:
    project_root = os.path.dirname(project_root)
sys.path.append(project_root)


from backend.sistemas.modelos.adversarios import AdversarioMonstro

<<<<<<< HEAD
# nome, nível, experiência, dano_base, defesa_base, vida_base, estamina_base, velocidade_base, queda, taxa_de_queda

slime = AdversarioMonstro("slime", 1, 25, 8, 5, 50, 8, 1, "Gosma Azul", 80)
=======
slime = AdversarioMonstro("slime", 2, 30, 4, 3, 12, 8, 1, "Gosma Azul", 80)
>>>>>>> 62bcdd9a599cd57efdea37a723fa1e2eb8c5c87a
slime.posição_x = 1200
slime.atualizar_atributos()
slime.atualizar_descrição()

slime_especiais = AdversarioMonstro("Slime Especial", 3, 46, 13, 6, 17, 10, 2, "Gosma Verde", 80)
slime.posição_x = 1200
slime_especiais.atualizar_atributos()
slime_especiais.atualizar_descrição()

esqueleto = AdversarioMonstro("esqueleto", 1, 1, 1, 1, 1, 1, 1, "Osso", 80)
esqueleto.posição_x = 1200
esqueleto.atualizar_atributos()
esqueleto.atualizar_descrição()

goblin = AdversarioMonstro("goblin", 1, 1, 1, 1, 1, 1, 1, 80)
goblin.posição_x = 1200
goblin.atualizar_atributos()
goblin.atualizar_descrição()


