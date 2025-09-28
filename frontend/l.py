from random import randint

i = [(542, 571), (541, 581), (537, 583)]
l = [(626, 647), (623, 672), (618, 679)]
y = [(704, 892), (709, 877), (723, 860)]
t = [(1053, 1120), (1056, 1128), (1053, 1380)]
d = [(1255, 1380), (1249, 1380), (0, 0)]
t = [(0, 0), (0, 0), (0, 0)]
o = (321, 329, 339)
k = []

#(0, 0), (0, 0), (0, 0)

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

