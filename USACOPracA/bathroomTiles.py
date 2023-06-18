import math

num = int(input())
max = math.sqrt(num)
possible = []
ans = 0

t1,t2,t3,t4 = 0,0,0,0

for i in range(0,math.ceil(math.sqrt(num))+1):
    possible.append(i)

for t2 in possible:
    for t3 in possible:
        for t4 in possible:
            a = num - t2**2 - t3**2 - t4**2
            if a >= 0 and math.isqrt(a) ** 2 == a:
                ans += 1
print(ans)