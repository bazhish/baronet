from random import randint

i = []
l = []
y = []
t = []
o = [148]
k = []

# for p in range(500, 618, 9):
#     i.append(p)

# for p in range(660, 1380, 9):
#     l.append(p)

# for p in range(1098, 1165, 9):
#     y.append(p)

# for p in range(1293, 1380, 9):
#     t.append(p)

l = i + l + y + t

for y, p in enumerate(o):
    for h in l:
        k.append((h - randint(0, 4), p - randint(4, 7), "arvore_pequena"))
print(l)

