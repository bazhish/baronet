import sys, os
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = current_dir
while not os.path.isdir(os.path.join(project_root, ".git")) and os.path.dirname(project_root) != project_root:
    project_root = os.path.dirname(project_root)
sys.path.append(project_root)


from backend.sistemas.modelos.adversarios import AdversarioMonstro, AdversarioDemiHumano



#MONSTROS COMUNS MAPA 1
slime = AdversarioMonstro("slime", 1, 20, 8, 6, 50, 8, 2, "Gosma Azul", 80)
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

#MONSTROS RAROS MAPA 1
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

vampiro = AdversarioDemiHumano("vampiro", 250, 60.0, "masculino", 2.10, 9, 135, 45, 20, 18, 110, 20, "Sangue", 80)
vampiro.posição_x = 1200
vampiro.atualizar_atributos()
vampiro.atualizar_descrição()

#MONSTRO EPÍCOS MAPA 1
quimera = AdversarioMonstro("quimera", 12, 150, 50, 25, 120, 11, 8, None, None)
quimera.posição_x = 1200
quimera.atualizar_atributos()
quimera.atualizar_descrição()

banshee = AdversarioMonstro("banshee", 12, 200, 60, 20, 145, 16, 13, None, None)
banshee.posição_x = 1200
banshee.atualizar_atributos()
banshee.atualizar_descrição()
#MONSTROS#
# nome, nível, experiência, dano_base, defesa_base, vida_base, estamina_base, velocidade_base, queda, taxa_de_queda
#DEMIHUMANOS#
# nome, idade, peso, gênero, altura, nível, experiência, dano_base, velocidade_base, defesa_base, vida_base, estamina_base, queda, taxa_de_queda
fenrir = AdversarioMonstro("fenrir", 12, 220, 70, 35, 150, 18, 18, "Pelo", 80)
fenrir.posição_x = 1200
fenrir.atualizar_atributos()
fenrir.atualizar_descrição()

ghoul = AdversarioMonstro("ghoul", 15, 310, 100, 50, 190, 23, 20, "Língua", 80)
ghoul.posição_x = 1200
ghoul.atualizar_atributos()
ghoul.atualizar_descrição()

oni = AdversarioDemiHumano("oni", 450, 100.0, None, 2.30, 15, 350, 125, 35, 75, 210, 30, "Chifres", 80)
oni.posição_x = 1200
oni.atualizar_atributos()
oni.atualizar_descrição()

medusa = AdversarioDemiHumano("medusa", None, 145.0, "Feminino", 2.20, 15, 390, 135, 40, 80, 230, 45, "Cabeça", 80)
medusa.posição_x = 1200
medusa.atualizar_atributos()
medusa.atualizar_descrição()

#CHEFÃO MAPA 1
troll = AdversarioMonstro("troll", 20, 500, 260, 110, 320, 50, 30, "Olhos", 100)
troll.posição_x = 1200
troll.atualizar_atributos()
troll.atualizar_descrição()


###MONSTROS MAPA 2###

#MONSTROS COMUNS MAPA 2
zumbi_elite = AdversarioMonstro("zumbi elite", 20, 360, 110, 50, 220, 35, 25, "Carne Morta", 60)
zumbi_elite.posição_x = 1200
zumbi_elite.atualizar_atributos()
zumbi_elite.atualizar_descrição()

kappa = AdversarioDemiHumano("kappa", 158, 340.0, None, 3.40, 20, 410, 135, 40, 80, 240, 65, "bico", 60)
kappa.posição_x = 1200
kappa.atualizar_atributos()
kappa.atualizar_descrição()

fomori = AdversarioMonstro("fomori", 22, 420, 135, 75, 280, 45, 35, None, None)
fomori.posição_x = 1200
fomori.atualizar_atributos()
fomori.atualizar_descrição()

minotauro = AdversarioDemiHumano("minotauro", 500, 450.0, "Masculino", 3.50, 23, 460, 160, 38, 100, 310, 80, "Chifre", 60)
minotauro.posição_x = 1200
minotauro.atualizar_atributos()
minotauro.atualizar_descrição()

#MONSTROS RAROS MAPA 2
equidna = AdversarioDemiHumano("equidna", 456, 230.0, "Feminino", 3.79, 26,  ("Couro", "Espinhos"), 60)
equidna.posição_x = 1200
equidna.atualizar_atributos()
equidna.atualizar_descrição()

marid = AdversarioMonstro("marid", 2, 80, 18, 12, 90, 14, 4, "Pedaço de Tridente", 60)
marid.posição_x = 1200
marid.atualizar_atributos()
marid.atualizar_descrição()

kodama = AdversarioMonstro("kodama", 2, 60, 14, 9, 70, 11, 3, "Essência", 60)
kodama.posição_x = 1200
kodama.atualizar_atributos()
kodama.atualizar_descrição()

jubokko = AdversarioMonstro("jubokko", 2, 65, 16, 11, 75, 13, 3, "Pedaço de Jubo", 60)
jubokko.posição_x = 1200
jubokko.atualizar_atributos()
jubokko.atualizar_descrição()

#MONSTROS ÉPICOS MAPA 2
yukki_Onna = AdversarioDemiHumano("yukki Onna", 2, 90, 20, 15, 100, 16, 5, ("Roupa", "Cabelo"), 60)
yukki_Onna.posição_x = 1200
yukki_Onna.atualizar_atributos()
yukki_Onna.atualizar_descrição()

ciclopes = AdversarioDemiHumano("ciclopes", 2, 85, 19, 14, 95, 15, 5, "Olho", 60)
ciclopes.posição_x = 1200
ciclopes.atualizar_atributos()
ciclopes.atualizar_descrição()

dullahan = AdversarioMonstro("dullahan", 2, 95, 22, 16, 110, 17, 6, "Pedaço de Espada", 60)
dullahan.posição_x = 1200
dullahan.atualizar_atributos()
dullahan.atualizar_descrição()

tifão = AdversarioMonstro("tifão", 2, 100, 25, 18, 120, 18, 7, "Assas", 60)
tifão.posição_x = 1200
tifão.atualizar_atributos()
tifão.atualizar_descrição()

balor = AdversarioDemiHumano("balor", 2, 110, 28, 20, 130, 20, 8, "Chifre", 60)
balor.posição_x = 1200
balor.atualizar_atributos()
balor.atualizar_descrição()

kobolds = AdversarioDemiHumano("kobolds", 2, 70, 15, 10, 80, 12, 3, "Calda", 60)
kobolds.posição_x = 1200
kobolds.atualizar_atributos()
kobolds.atualizar_descrição()

#CHEFÃO MAPA 2
rei_fantasma = AdversarioMonstro("rei fantasma", 2, 120, 30, 22, 140, 22, 9, "Benção Fantasma", 100)
rei_fantasma.posição_x = 1200
rei_fantasma.atualizar_atributos()
rei_fantasma.atualizar_descrição()


###MONSTROS MAPA 3###

#MONSTROS COMUNS MAPA 3
goblin_arqueiro = AdversarioMonstro("goblin arqueiro", 3, 40, 10, 8, 50, 8, 2, None, None)
goblin_arqueiro.posição_x = 1200
goblin_arqueiro.atualizar_atributos()
goblin_arqueiro.atualizar_descrição()

zombi_venenoso = AdversarioMonstro("zombi venenoso", 3, 45, 12, 9, 55, 9, 3, "Carne Podre", 60)
zombi_venenoso.posição_x = 1200
zombi_venenoso.atualizar_atributos()
zombi_venenoso.atualizar_descrição()

golem_de_pedra = AdversarioMonstro("golem de pedra", 3, 50, 14, 10, 60, 10, 4, "Pedra", 60)
golem_de_pedra.posição_x = 1200
golem_de_pedra.atualizar_atributos()
golem_de_pedra.atualizar_descrição()

zumbi_bombadeiro = AdversarioMonstro("zumbi bombadeiro", 3, 55, 16, 12, 65, 12, 5, "Bomba", 60)
zumbi_bombadeiro.posição_x = 1200
zumbi_bombadeiro.atualizar_atributos()
zumbi_bombadeiro.atualizar_descrição()

#MONSTROS RAROS MAPA 3
orc_vermelho = AdversarioDemiHumano("orc vermelho", 3, 60, 14, 10, 70, 12, 3, None, None)
orc_vermelho.posição_x = 1200
orc_vermelho.atualizar_atributos()
orc_vermelho.atualizar_descrição()

slime_acido = AdversarioMonstro("slime ácido", 3, 50, 12, 10, 60, 10, 4, None, None)
slime_acido.posição_x = 1200
slime_acido.atualizar_atributos()
slime_acido.atualizar_descrição()

esqueleto_anão = AdversarioMonstro("esqueleto anão", 3, 55, 13, 11, 65, 11, 4, "Osso", 60)
esqueleto_anão.posição_x = 1200
esqueleto_anão.atualizar_atributos()
esqueleto_anão.atualizar_descrição()

demonio_de_sangue = AdversarioDemiHumano("demônio de sangue", 3, 65, 18, 14, 75, 14, 5, None, None)
demonio_de_sangue.posição_x = 1200
demonio_de_sangue.atualizar_atributos()
demonio_de_sangue.atualizar_descrição()

#MONSTROS ÉPICOS MAPA 3
zumbi_samurai = AdversarioMonstro("zumbi samurai", 3, 70, 20, 16, 80, 16, 6, None, None)
zumbi_samurai.posição_x = 1200
zumbi_samurai.atualizar_atributos()
zumbi_samurai.atualizar_descrição()

grifo = AdversarioMonstro("grifo", 3, 75, 22, 18, 85, 18, 7, None, None)
grifo.posição_x = 1200
grifo.atualizar_atributos()
grifo.atualizar_descrição()

kritan = AdversarioMonstro("kritan", 3, 80, 25, 20, 90, 20, 8, None, None)
kritan.posição_x = 1200
kritan.atualizar_atributos()
kritan.atualizar_descrição()

fantasma_insano = AdversarioMonstro("fantasma insano", 3, 85, 28, 22, 95, 22, 9, None, None)
fantasma_insano.posição_x = 1200
fantasma_insano.atualizar_atributos()
fantasma_insano.atualizar_descrição()

kelpie = AdversarioMonstro("kelpie", 3, 90, 30, 24, 100, 24, 10, None, None)
kelpie.posição_x = 1200
kelpie.atualizar_atributos()
kelpie.atualizar_descrição()

hipogrifo = AdversarioMonstro("hipogrifo", 3, 95, 32, 26, 105, 26, 11, None, None)
hipogrifo.posição_x = 1200
hipogrifo.atualizar_atributos()
hipogrifo.atualizar_descrição()

#CHEFÃO MAPA 3
rei_tirano = AdversarioDemiHumano("rei tirano", 3, 120, 40, 30, 150, 30, 12, None, None)
rei_tirano.posição_x = 1200
rei_tirano.atualizar_atributos()
rei_tirano.atualizar_descrição()

