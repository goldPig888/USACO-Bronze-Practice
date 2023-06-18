import sys
nline = list(map(int, input().strip().split()))
rooms = nline[0]
people = []
doors = []
min = 0
distance = 0

for i in range(rooms):
    nline = list(map(int, sys.stdin.readline().strip().split()))
    people.append(nline[0])
    doors.append(i)

for i in range(len(doors)+2):
    if i == 1:
        min = distance
    else:
        distance = 0
    for i2 in range(len(people)):
        distance += people[i2]*doors[i2]
    if distance < min:
        min = distance
    doors.append(doors[0])
    doors.pop(0)
print(min)
