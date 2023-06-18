fin = open("USACOPrac/alphastar.in", "r")
num, col = list(map(int, fin.readline().strip().split()))
first = []
second = []
final = 0

for i in range(num):
    line = fin.readline().strip()
    first.append([line[j:j+1] for j in range(0, len(line), 1)])

for i in range(num):
    line = fin.readline().strip()
    second.append([line[j:j+1] for j in range(0, len(line), 1)])

firstAll = []
secAll = []

for c in range(col):
    firstCol = []
    secCol = []
    ans = 0
    for i in range(num):
        firstCol.append(first[i][c])
        secCol.append(second[i][c])

    firstAll.append(firstCol)
    secAll.append(secCol)

for i in range(col):
    ans = 0
    for thing in set(firstAll[i]):
        ans += 1
        if thing not in set(secAll[i]):
            ans -= 1
    if ans == 0:
        final += 1
    
print(final)

