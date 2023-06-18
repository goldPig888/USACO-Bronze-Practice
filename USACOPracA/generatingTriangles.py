from itertools import islice
nr,num = map(int, input().split())
seq = []
total = 0
lengthSplit = []
output = []

for i in range(1,nr+1):
    total += i
    lengthSplit.append(i)

for i in range(total):
    if num < 9:
        seq.append(num)
    elif num == 9:
        seq.append(num)
        num = 0
    num += 1

Inputt = iter(seq)
spliced = [list(islice(Inputt, elem))
        for elem in lengthSplit]

pos=0
for i in range(nr):
    line = []
    for ls in spliced:
        try:
            line.append(ls[i])
        except IndexError:
            line.append(" ")
    print(*line)
