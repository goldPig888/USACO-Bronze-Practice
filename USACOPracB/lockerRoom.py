N = int(input())
events = []
for _ in range(N):
    s, t, b = map(int, input().split())
    events.append((s, b))
    events.append((t, -b))
events.sort()
max_lockers = 0
curr_lockers = 0
for event in events:
    curr_lockers += event[1]

    if curr_lockers > max_lockers:
        max_lockers = curr_lockers
print(max_lockers)
