import sys
line = list(map(int, input().strip().split()))
row,col = line[0],line[1]
arr=[]
ans = 0

for i in range(row):
    line = list(sys.stdin.readline().strip())
    arr.append(line)

for r in range(row):
    for c in range(col):
        if arr[r][c] == '.':
            arr[r][c] = 0
        else:
            arr[r][c] = 1

for r in range(row):
    for c in range(col):
        if arr[r][c] == 1:
            try:
                if arr[r][c+1] == 1:
                    arr[r][c+1] = 0
            except IndexError:
                pass
                
            try:
                if arr[r+1][c] == 1:
                    arr[r+1][c] = 0
            except IndexError:
                continue


for r in range(row):
    for c in range(col):
        ans += arr[r][c]
print(ans)
