def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    result = -1

    if target < arr[0]:
        result = -1
    elif target == arr[0]:
        result = 0
    else:
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                result = mid
                break
            elif arr[mid] < target < arr[mid + 1]:
                result = mid
                break
            elif target < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1

    return result


fin = open("alphastar.in", "r")
nTask, nQuoi = list(map(int, fin.readline().strip().split()))
taskTime = []
quoi = []
time = []
ans = []

for i in range(nTask):
    taskTime.append(int(fin.readline().strip()))

for i in range(nQuoi):
    quoi.append(int(fin.readline().strip()))

for i in range(1, nTask + 1):
    time.append(sum(taskTime[0:i]))

for q in range(nQuoi):
    print(binary_search(time, quoi[q]) + 2)
