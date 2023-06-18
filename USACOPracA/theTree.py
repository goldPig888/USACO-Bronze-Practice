def selectionSort(array, size):
    
    for i in range(size):
        min_index = i
 
        for j in range(i + 1, size):
            if array[j] < array[min_index]:
                min_index = j
        (array[i], array[min_index]) = (array[min_index], array[i])
 
import sys
line = list(map(int, input().strip().split()))
num,dist = line[0],line[1]
acorn = []
ans = []
ansNum = 0

for i in range(num):
    acorn.append(int(sys.stdin.readline().strip()))

selectionSort(acorn, num)

for i in range(num):
    if acorn[num-i-1] + ansNum < dist:
        ans.append(num-i-1)
        ansNum += acorn[num-i-1]
    elif acorn[num-i-1] + ansNum == dist:
            ans.append(num-i-1)
            print(len(ans))
            exit()

for i in range(num-len(ans)):
    if acorn[len(ans) - i] + ansNum >= dist:
        ans.append(len(ans) - i)
        ansNum += acorn[len(ans) - i]
        break
print(len(ans))

