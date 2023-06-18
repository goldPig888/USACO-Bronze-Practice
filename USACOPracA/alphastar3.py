import sys
fin = list(map(int, input().strip().split()))
total, num = fin[0], fin[1]

for i in range(num):
    line = list(map(int, sys.stdin.readline().strip().split()))
    s, m, r = line[0], line[1], line[2]
    dist = 0
    min = 0
    alarm = 0
    while not dist >= total:
        alarm += 1
        min += 1
        dist += s
        if dist >= total:
            print(min)
        if alarm == m:
            min += r
            alarm = 0