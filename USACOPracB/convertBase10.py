num, base = list(map(int,input().strip().split()))
pos = 0
ans = 0

for p in reversed(str(num)):
    i = int(p)
    ans += (i * pow(base,pos))
    pos += 1
print(ans)