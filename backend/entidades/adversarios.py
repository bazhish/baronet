import sys, os; project_root = os.path.abspath(os.path.dirname(__file__)); 
while not os.path.isdir(os.path.join(project_root, ".git")) and os.path.dirname(project_root) != project_root: project_root = os.path.dirname(project_root); 
sys.path.append(project_root)
from backend.sistemas.modelos.modelo_adversarios import AdversarioMonstro, AdversarioDemiHumano
from backend.sistemas.modelos.modelos_armas import criar_arma
from backend.sistemas.classes.classes_combatentes import arqueiro, guerreiro, meedusa, batedor, assassino

# ----------------------------------------------------- MONSTROS ---------------------------------------------------------------------------------

slime_azul = AdversarioMonstro("slime azul", 2, 50, 4, 3, 12, 10, 1, "gosma azul", 90)
slime_azul.posição_x = 1200
slime_azul.post_init()

zumbi = AdversarioMonstro("zumbi", 5, 100, 6, 1, 14, 12, 2, None, None)
zumbi.posição_x = 1200
zumbi.post_init()

gárgula = AdversarioMonstro("gárgula", 10, 200, 9, 5, 34, 30, 3, "pedra", 100)
gárgula.posição_x = 1200
zumbi.post_init()

lobisomem = AdversarioMonstro("lobisomem", 9, 120, 30, 12, 100, 10, 13, "Garras", 80)
lobisomem.posição_x = 1200
lobisomem.post_init()

quimera = AdversarioMonstro("quimera", 12, 150, 50, 25, 120, 11, 8, None, None)
quimera.posição_x = 1200
quimera.post_init()

banshee = AdversarioMonstro("banshee", 12, 200, 60, 20, 145, 16, 13, None, None)
banshee.posição_x = 1200
banshee.post_init()

fenrir = AdversarioMonstro("fenrir", 12, 220, 70, 35, 150, 18, 18, "Pelo", 80)
fenrir.posição_x = 1200
fenrir.post_init()

ghoul = AdversarioMonstro("ghoul", 15, 310, 100, 50, 190, 23, 20, "Língua", 80)
ghoul.posição_x = 1200
ghoul.post_init()

# ----------------------------------------------------- DEMI | HUMANOS --------------------------------------------------------------------------------

goblin = AdversarioDemiHumano("goblin assassino", 5, 100, None, None)
goblin.posição_x = 1200
goblin.definir_classe(assassino)
goblin.definir_habilidades()
adaga_afiada = criar_arma("adaga", "adaga afiada", "comum", goblin, 15, 100, 1.5, 0.7, 0.1)
goblin.equipar_arma(adaga_afiada)
goblin.post_init()


ogro = AdversarioDemiHumano("ogro batedor", 9, 200, "dente", 50)
ogro.posição_x = 1200
ogro.definir_classe(batedor)
ogro.definir_habilidades()
machado_da_floresta = criar_arma("machado", "machado da floresta", "comum", ogro, 15, 100, 1.5, 0.7, 0.1)
ogro.equipar_arma(machado_da_floresta)
ogro.post_init()

esqueleto = AdversarioDemiHumano("esqueleto", 4, 120, "osso", 80)
esqueleto.posição_x = 1200
esqueleto.definir_classe(arqueiro)
esqueleto.definir_habilidades()
arco_de_ossos = criar_arma("arco", "arco de ossos", "comum", esqueleto, 15, 100, 1.5, 0.7, 0.1)
esqueleto.equipar_arma(arco_de_ossos)
esqueleto.post_init()

oni = AdversarioDemiHumano("oni", 17, 350, "chifres", 80)
oni.posição_x = 1200
oni.definir_classe(guerreiro)
oni.definir_habilidades()
clava_de_madeira = criar_arma("clava", "clava de madeira", "comum", oni, 15, 100, 1.5, 0.7, 0.1)
oni.equipar_arma(clava_de_madeira)
oni.post_init()

medusa = AdversarioDemiHumano("medusa", 18, 400, "cabeça de medusa", 90)
medusa.posição_x = 1200
medusa.definir_classe(meedusa)
medusa.definir_habilidades()
medusa.post_init()

# ---------------------------------------------------------------- CHEFÃO -----------------------------------------------------------------------------------------------------------

troll = AdversarioDemiHumano("troll", 25, 500, "olhos de toll", 100)
troll.posição_x = 1200
troll.definir_classe(guerreiro)
troll.definir_habilidades()
clava_de_pedra = criar_arma("clava", "clava de pedra", "comum", troll, 15, 100, 1.5, 0.7, 0.1)
troll.equipar_arma(clava_de_pedra)
troll.post_init()