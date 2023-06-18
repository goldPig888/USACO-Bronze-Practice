import sys
nline = list(map(int, input().strip().split()))
rnd = nline[0]
first = []
sec = []
ans = 0
ans2 = 0
for i in range(rnd):
    line = list(map(int, sys.stdin.readline().strip().split()))
    first.append(line[0])
    sec.append(line[1])

cc = [
    [0,1,0],
    [0,0,1],
    [1,0,0]
]
ccw = [
    [0,0,1],
    [1,0,0],
    [0,1,0]
]

for i in range(rnd):
    ans += cc[sec[i]-1][first[i]-1]

for i in range(rnd):
    ans2 += ccw[sec[i]-1][first[i]-1]

print(max(ans,ans2))
