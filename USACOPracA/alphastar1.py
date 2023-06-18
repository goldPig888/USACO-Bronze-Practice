import math,sys
all = []
fin = list(map(int, input().strip().split()))
nums = fin[0]
first = True

for i in range(nums):
    coords = list(map(int, sys.stdin.readline().strip().split()))
    all.append(coords)

for coord in all:
    for coord2 in all:
        if first == True:
            maxD = math.dist(coord, coord2)
            first = False

        dist = math.dist(coord, coord2)
        if dist > maxD:
            maxD = dist
            winners = [coord,coord2]
sorted(winners)
print(all.index(winners[0])+1,all.index(winners[1])+1)