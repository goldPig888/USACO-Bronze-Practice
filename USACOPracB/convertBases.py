num, base = list(map(int,input().strip().split()))
ans = ""
while num != 0 and num != 1:
    print(num//base)
    ans += str(num%base)
    num = num//base
print(*list(reversed(ans)), sep='')