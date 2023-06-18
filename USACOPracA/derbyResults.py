N = int(input())

results = []

for _ in range(N):
    hours, minutes, seconds = map(int, input().split())
    results.append((hours, minutes, seconds))

results.sort()

for time in results:
    print(time[0], time[1], time[2])
