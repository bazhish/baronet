from random import randint

i = [(500, 553), (500, 552), (500, 533)]
l = [(594, 626), (595, 655), (580, 628)]
y = [(865, 1000), (851, 993), (824, 984)]
t = [(1327, 1380), (1335, 1380), (1345, 1380)]
d = [(0, 0), (0, 0), (0, 0)]
t = [(0, 0), (0, 0), (0, 0)]
o = [465, 474, 483]
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

