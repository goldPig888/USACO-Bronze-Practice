nTask, nQuoi = list(map(int, input().strip().split()))
taskTime = []
quoi = []
time = []
ans = []

for i in range(nTask):
    taskTime.append(int(input().strip()))

for i in range(nQuoi):
    quoi.append(int(input().strip()))

for i in range(1,nTask+1):
    time.append(sum(taskTime[0:i]))
for q in range(nQuoi):
    for t in range(nTask):
        if quoi[q] < time[t]:
            print(t+1)
            break
