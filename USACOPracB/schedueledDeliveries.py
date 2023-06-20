def gcf(a, b):
    while b != 0:
        a, b = b, a % b
    return a

n = int(input())
days = [int(input()) for _ in range(n)]
intervals = [days[i] - 1 for i in range(1, n)]
print(intervals)
for i in range(0, n-1):
    print("checking", intervals[i])
    for sec in range(i+1,n-1):
        x = gcf(intervals[i], intervals[sec])
        if intervals[i] != 0 and intervals[sec] != 0 and intervals[sec] % intervals[i] == 0:
            
            intervals[sec] = 0
    print(intervals)
while 0 in intervals: intervals.remove(0)
print(len(intervals))

