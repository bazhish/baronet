from random import randint

i = []
l = []
o = [100, 106, 112, 118]
k = []

for p in range(500, 575, 7):
    i.append(p)

for p in range(620, 1380, 7):
    l.append(p)

l = i + l

for y, p in enumerate(o):
    for h in l:
        k.append((h - randint(0, 3), p - randint(2, 4), "arvore_pequena"))
print(k)



