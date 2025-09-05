import sys, os; project_root = os.path.abspath(os.path.dirname(__file__)); 
while not os.path.isdir(os.path.join(project_root, ".git")) and os.path.dirname(project_root) != project_root: project_root = os.path.dirname(project_root); 
sys.path.append(project_root)
from backend.sistemas.modelos.adversarios import AdversarioMonstro, AdversarioDemiHumano

# ----------------------------------------------------- MONSTROS ---------------------------------------------------------------------------------

slime = AdversarioMonstro("slime", 1, 20, 8, 5, 50, 8, 2, "gosma", 80)
slime.posição_x = 1200
slime.atualizar_atributos()
slime.atualizar_descrição()

slime_especiais = AdversarioMonstro("Slime Especial", 5, 40, 16, 10, 100, 10, 4, "Gosma Verde", 80)
slime.posição_x = 1200
slime_especiais.atualizar_atributos()
slime_especiais.atualizar_descrição()

esqueleto = AdversarioMonstro("esqueleto", 2, 30, 12, 4, 40, 10, 5, "Osso", 80)
esqueleto.posição_x = 1200
esqueleto.atualizar_atributos()
esqueleto.atualizar_descrição()

goblin = AdversarioMonstro("goblin", 3, 30, 15, 12, 80, 9, 3, None, None)
goblin.posição_x = 1200
goblin.atualizar_atributos()
goblin.atualizar_descrição()

zumbi = AdversarioMonstro("zumbi", 4, 25, 18, 8, 60, 6, 2, None, None)
zumbi.posição_x = 1200
zumbi.atualizar_atributos()
zumbi.atualizar_descrição()

ogro = AdversarioMonstro("ogro", 8, 120, 35, 20, 110, 9, 5, "Dente", 80)
ogro.posição_x = 1200
ogro.atualizar_atributos()
ogro.atualizar_descrição()

gárgula = AdversarioMonstro("gárgula", 8, 100, 25, 10, 80, 8, 12, "pedra", 80)
gárgula.posição_x = 1200
gárgula.atualizar_atributos()
gárgula.atualizar_descrição()

lobisomem = AdversarioMonstro("lobisomem", 9, 120, 30, 12, 100, 10, 13, "Garras", 80)
lobisomem.posição_x = 1200
lobisomem.atualizar_atributos()
lobisomem.atualizar_descrição()

quimera = AdversarioMonstro("quimera", 12, 150, 50, 25, 120, 11, 8, None, None)
quimera.posição_x = 1200
quimera.atualizar_atributos()
quimera.atualizar_descrição()

banshee = AdversarioMonstro("banshee", 12, 200, 60, 20, 145, 16, 13, None, None)
banshee.posição_x = 1200
banshee.atualizar_atributos()
banshee.atualizar_descrição()

fenrir = AdversarioMonstro("fenrir", 12, 220, 70, 35, 150, 18, 18, "Pelo", 80)
fenrir.posição_x = 1200
fenrir.atualizar_atributos()
fenrir.atualizar_descrição()

ghoul = AdversarioMonstro("ghoul", 15, 310, 100, 50, 190, 23, 20, "Língua", 80)
ghoul.posição_x = 1200
ghoul.atualizar_atributos()
ghoul.atualizar_descrição()

troll = AdversarioMonstro("troll", 20, 500, 260, 110, 320, 50, 30, "Olhos", 100)
troll.posição_x = 1200
troll.atualizar_atributos()
troll.atualizar_descrição()

# ----------------------------------------------------- DEMI | HUMANOS --------------------------------------------------------------------------------

oni = AdversarioDemiHumano("oni", 450, 100.0, None, 2.30, 15, 350, 125, 35, 75, 210, 30, "Chifres", 80)
oni.posição_x = 1200
oni.atualizar_atributos()
oni.atualizar_descrição()

medusa = AdversarioDemiHumano("medusa", None, 145.0, "Feminino", 2.20, 15, 390, 135, 40, 80, 230, 45, "Cabeça", 80)
medusa.posição_x = 1200
medusa.atualizar_atributos()
medusa.atualizar_descrição()

vampiro = AdversarioDemiHumano("vampiro", 250, 60.0, "masculino", 2.10, 9, 135, 45, 20, 18, 110, 20, "Sangue", 80)
vampiro.posição_x = 1200
vampiro.atualizar_atributos()
vampiro.atualizar_descrição()