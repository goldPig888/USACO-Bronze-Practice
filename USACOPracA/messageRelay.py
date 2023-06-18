num = int(input().strip())
line = list(map(int,input().strip().split()))
line = sorted(line)
msg = []
right = []

for pos in range(num):
    if pos == 0:
        right.append(1)
    elif pos == num-1:
        right.append(0)
    elif line[pos+1]-line[pos] < line[pos]-line[pos-1]:
        right.append(1)
    elif line[pos]-line[pos-1] < line[pos+1]-line[pos]:
        right.append(0)
    elif line[pos]-line[pos-1] == line[pos+1]-line[pos]:
        right.append(0)
    msg.append(0)

for pos in range(num):
    if right[pos] == 1:
        msg[pos+1] += 1
    else:
        msg[pos-1] += 1
ans = msg.count(0)
for pos in range(0,num-1):
    if right[pos] == 1 and right[pos+1] == 0 and msg[pos] == 1 and msg[pos+1] == 1:
        ans += 1
print(ans)