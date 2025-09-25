from random import randint

i = [(541, 573), (532, 582), (522, 582)]
l = [(626, 646), (619, 672), (619, 683)]
y = [(706, 887), (714, 877), (721, 860)]
t = [(1053, 1117), (1050, 1131), (1047, 1143)]
d = [(1254, 1380), (1231, 1380), (1212, 1380)]
o = [323, 333, 338]
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
    
print(k)

