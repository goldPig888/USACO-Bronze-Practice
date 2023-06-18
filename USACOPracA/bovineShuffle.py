fin = open('shuffle.in', 'r')
nline = list(map(int, fin.readline().strip().split()))
order = list(map(int, fin.readline().strip().split()))
cows = list(map(int, fin.readline().strip().split()))
num = nline[0]
sort = []
for i in order:
    sort.append(cows[i-1])
for i in order:
    sort.append(sort[i-1])
for i in range(0,num):
    sort.pop(0)
for i in order:
    sort.append(sort[i-1])
for i in range(0,num):
    sort.pop(0)
with open('shuffle.out', 'w') as fin:
    for i in range(0,num):
        fin.write(str(sort[i]) + '\n')
        