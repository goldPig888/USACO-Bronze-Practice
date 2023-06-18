line = list(map(int, input().strip().split()))
max,num = line[0],line[1]
line = []
line2 = []
ans = 0

for i in range(num):
    nums = int(input().strip())
    line.append(nums)

line = sorted(line,key=abs)

dist = abs(line[0])
for i in range(num-1):
    if dist < max:
        dist += abs(line[i] - line[i+1])
        if dist >= max:
            ans+=1
            print(ans)
            exit()
        ans += 1
    else:
        print(ans)
