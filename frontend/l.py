from random import randint

i = [(0, 0), (0, 0), (0, 0)]
l = [(621, 1017), (683, 1004), (697, 985)]
y = [(0, 0), (0, 0), (0, 0)]
t = [(1277, 1380), (1267, 1380), (1255, 1380)]
o = [285, 304, 314]
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
    
print(k)

