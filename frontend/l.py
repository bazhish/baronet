from random import randint

i = [(500, 529), (500, 527), (500, 523)]
l = [(566, 624), (558, 615), (563, 618)]
y = [(896, 978), (901, 973), (899, 966)]
t = [(1347, 1380), (1351, 1380), (1361, 1380)]
d = [(0, 0), (0, 0), (0, 0)]
t = [(0, 0), (0, 0), (0, 0)]
o = [488, 498, 507]
k = []

for e, r in enumerate(o):
    for p in range(i[e][0], i[e][1], 9):
        k.append((p - randint(0, 4), r - randint(4, 7), "arvore_pequena"))

    for p in range(l[e][0], l[e][1], 9):
        k.append((p - randint(0, 4), r - randint(4, 7), "arvore_pequena"))

    for p in range(y[e][0], y[e][1], 9):
        k.append((p - randint(0, 4), r - randint(4, 7), "arvore_pequena"))

    for p in range(t[e][0], t[e][1], 9):
        k.append((p - randint(0, 4), r - randint(4, 7), "arvore_pequena"))
    
    for p in range(d[e][0], d[e][1], 9):
        k.append((p - randint(0, 4), r - randint(4, 7), "arvore_pequena"))

    for p in range(t[e][0], t[e][1], 9):
        k.append((p - randint(0, 4), r - randint(4, 7), "arvore_pequena"))
    
print(k)

