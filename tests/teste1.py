import sys, os
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = current_dir
while not os.path.isdir(os.path.join(project_root, ".git")) and os.path.dirname(project_root) != project_root:
    project_root = os.path.dirname(project_root)
sys.path.append(project_root)


from backend.sistemas.modelos.adversarios import AdversarioMonstro

slime = AdversarioMonstro("slime", 2, 30, 4, 3, 12, 8, 1, "Gosma Azul", 80)
<<<<<<< HEAD
=======
slime.posição_x = 1200
>>>>>>> 62bcdd9a599cd57efdea37a723fa1e2eb8c5c87a
slime.atualizar_atributos()
slime.atualizar_descrição()

slime_especiais = AdversarioMonstro("Slime Especial", 3, 46, 13, 6, 17, 10, 2, "Gosma Verde", 80)
slime.posição_x = 1200
slime_especiais.atualizar_atributos()
slime_especiais.atualizar_descrição()


