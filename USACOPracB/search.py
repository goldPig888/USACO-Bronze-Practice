def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    result = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            result = mid
            high = mid - 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return result


N, Q = map(int, input().split())
array = list(map(int, input().split()))

for i in range(Q):
    query = int(input())
    index = binary_search(array, query)
    print(index)
