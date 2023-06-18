import sys
rnds = int(sys.stdin.readline().strip())

bessie = 7
mildred = 7
elsie = 7
leaders = []
lines = []
counter = 0
prev_leaders = []
for i in range(rnds):
    line = sys.stdin.readline().strip().split()
    lines.append([int(line[0]), line[1], int(line[2])])

def comp(lines):
    return lines[0]
lines.sort(key=comp)

for i in lines:
    if i[1] == "Bessie":
        bessie += i[2]
    elif i[1] == "Mildred":
        mildred += i[2]
    elif i[1] == "Elsie":
        elsie += i[2]

    leaderNum = max(bessie, mildred, elsie)
    prev_leaders = leaders.copy()
    leaders = [index for index, score in enumerate([bessie, mildred, elsie]) if score == leaderNum]

    if set(prev_leaders) != set(leaders):
        counter += 1

print(counter)
