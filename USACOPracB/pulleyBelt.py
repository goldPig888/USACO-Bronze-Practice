n =int(input().strip())
cows = []
sumOne = 0
for i in range(n-1):
    line = list(map(int , input().strip().split()))
    cows.append(line)
    sumOne += line[2]
if sumOne % 2 == 0:
    print(0)
else:
    print(1)