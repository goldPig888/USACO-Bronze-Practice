def xComp(lines):
    return lines[0]

def yComp(lines):
    return lines[1]

def area(px, py):
    x1, x2 = px
    y1, y2 = py
    return abs(x2 - x1) * abs(y2 - y1)

n = int(input().strip())

all_coordinates = []
for i in range(n):
    pair = tuple(map(int, input().strip().split()))
    all_coordinates.append(pair)

all_coordinates.sort(key=xComp)

maxY = float('-inf')
minY = float('inf')

for i in all_coordinates[:-1]:
    if i[1] > maxY:
        maxY = i[1]
    elif i[1] < minY:
        minY = i[1]

x1 = area((all_coordinates[0][0], all_coordinates[-2][0]), (minY, maxY))

maxY = float('-inf')
minY = float('inf')

for i in all_coordinates[1:]:
    if i[1] > maxY:
        maxY = i[1]
    elif i[1] < minY:
        minY = i[1]

x2 = area((all_coordinates[1][0], all_coordinates[-1][0]), (minY, maxY))

all_coordinates.sort(key=yComp)

maxX = float('-inf')
minX = float('inf')

for i in all_coordinates[:-1]:
    if i[0] > maxX:
        maxX = i[0]
    elif i[0] < minX:
        minX = i[0]

y1 = area((minX, maxX), (all_coordinates[0][1], all_coordinates[-2][1]))

maxX = float('-inf')
minX = float('inf')

for i in all_coordinates[1:]:
    if i[0] > maxX:
        maxX = i[0]
    elif i[0] < minX:
        minX = i[0]

y2 = area((minX, maxX), (all_coordinates[1][1], all_coordinates[-1][1]))

print(min(x1, x2, y1, y2))

