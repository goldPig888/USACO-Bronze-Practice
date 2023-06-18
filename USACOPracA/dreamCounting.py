
first = list(map(int, input().strip().split()))
start,end = first[0],first[1]
counter = [0,0,0,0,0,0,0,0,0,0]
dreams = []
for i in range(start,end+1):
    for digit in str(i):
        dreams.append(int(digit))

for digit in dreams:
    counter[digit] += 1
print(*counter)
