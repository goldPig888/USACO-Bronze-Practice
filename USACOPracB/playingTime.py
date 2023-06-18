n =  int(input().strip())
log = list(map(int, input().strip().split()))
log = list(reversed(log))
log[-1] = 0

for i in range(n):
    if log[i] > 0 and log[i+1]==-1:
        log[i+1] = log[i]-1
        if log[i] == log[i-1] and log[i+1] != 0:
            print(-1)
            exit()
print(log.count(0) , log.count(0) + log.count(-1))