import sys
line = list(map(int, input().strip().split()))
ppl,qs,req = line[0],line[1],line[2]
arr=[]
counter = []
reqs = []
ans = 0
player = 0
for i in range(ppl):
    line = list(map(int,sys.stdin.readline().strip().split()))
    arr.append(line)
    counter.append(0)

for i in range(req):
    line = list(sys.stdin.readline().strip().split())
    reqs.append(line)

for q in range(req):
    player = 0
    for i in arr:
        val,val2 = reqs[q][0], reqs[q][1]
        if i[int(val)-1] == int(val2):
            counter[player] += 1
        player += 1
for i in counter:
    if i == len(reqs):
        ans += 1

print(ans)