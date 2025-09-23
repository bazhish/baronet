from random import randint

i = []
l = []
o = [100, 109, 118]
k = []

for p in range(500, 575, 9):
    i.append(p)

for p in range(625, 1380, 9):
    l.append(p)

l = i + l

for y, p in enumerate(o):
    for h in l:
        k.append((h - randint(0, 4), p - randint(4, 7), "arvore_pequena"))
print(k)



