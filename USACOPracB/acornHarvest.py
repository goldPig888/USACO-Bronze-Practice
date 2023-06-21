import math

def touching(x1, x2, y1, y2, r1, r2):
    distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    if distance == (r1 + r2):
        return True
    else:
        return False

n = int(input().strip())
xLs = []
yLs = []
rLs = []
count = []
for _ in range(n):
    x, y, r = map(int, input().strip().split())
    if x == 0 and y == 0:
        xLs.insert(0, x)
        yLs.insert(0, y)
        rLs.insert(0, r)
        count.append(0)
    else:
        xLs.append(x)
        yLs.append(y)
        rLs.append(r)
        count.append(0)

for i in range(0, n):
    for next in range(0, n):
        if i != next:
            if touching(xLs[i], xLs[next], yLs[i], yLs[next], rLs[i], rLs[next]):
                count[next] += 1

for i in range(n):
    if count[i] == 1 and i != 0:
        print(xLs[i], yLs[i])
