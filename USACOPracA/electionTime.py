num, adv = list(map(int,input().strip().split()))
all = []
og = []
for i in range(num):
    line = list(map(int, input().strip().split()))
    all.append(line)
    og.append(line)

def comp(lines):
    return lines[0]
all.sort(key=comp)
#print(all)
max = 0
cow = 0
for i in all[num-adv:num]:
    if i[1] > max:
        max = i[1]
        cow = og.index(i)
print(cow+1)
        