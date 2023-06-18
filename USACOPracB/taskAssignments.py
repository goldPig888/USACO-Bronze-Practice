n,nTask = list(map(int, input().strip().split()))
counter = []
for i in range(n):
    counter.append(0)
for i in range(nTask):
    start, increm = list(map(int, input().strip().split()))
    for i in range(start-1,n,increm):
        counter[i] = 1
print(counter.count(0))