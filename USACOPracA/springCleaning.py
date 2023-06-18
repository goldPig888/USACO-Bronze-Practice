fin = open("USACOPrac/alphastar.in", "r")
sq,num = map(int, fin.readline().split())
sorting = []
ans = []
for i in range(sq):
    ans.append(0)

for i in range(num):
    line = list(map(str, fin.readline().strip().split()))
    sorting.append([int(line[0]), line[1], int(line[2]),int(line[3])])

def comp(lines):
    return lines[0]
sorting.sort(key=comp)

for i in range(num):
    sorting[i][2] *= 60
    sorting[i][2] += sorting[i][3]
for i in range(0,num,2):
    ans[sorting[i][0]-1] += sorting[i+1][2]-sorting[i][2]

for a in ans:
    print(a//60, a%60)