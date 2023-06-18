og, calf = list(map(int, input().strip().split()))
move = 1
dist = 0
pos = og
while True:
    pos += move
    if pos > calf and move > 0 and  og < calf < pos:
        dist += abs(calf-og)
        print(dist)
        exit()
    elif pos == calf:
        dist += abs(move)
        print(dist)
        exit()
    elif pos < calf and move < 0 and og > calf > pos:
        dist += abs(og-calf)
        print(dist)
        exit()
    dist += (max(pos,og) - min(pos,og)) * 2
    move *= -2
    pos = og

