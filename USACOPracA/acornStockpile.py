import sys
line = list(map(int, input().strip().split()))
num,dist = line[0],line[1]
acorn = []
ans = []
temp = []
for i in range(num):
    acorn.append(int(sys.stdin.readline().strip()))

acorn = sorted(acorn)

for i in range(num):
    target = acorn[i]
    max = acorn[i] + dist
    temp=[]
    for i in acorn:
        if i <= max and i >= target:
            temp.append(i)
    if len(temp) > len(ans):
        ans = temp
print(len(ans))