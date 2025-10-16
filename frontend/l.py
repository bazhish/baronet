import random
cord = []
for i in range(500, 1380, 25):
    for j in range(100, 980, 25):
        cord.append((i - random.randint(0, 13), j - random.randint(0, 13), random.randint(1, 15)))

print(cord)