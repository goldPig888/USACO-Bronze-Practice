N, S = map(int, input().split())
fox_lengths = [int(input()) for i in range(N)]
fox_lengths.sort()

left = 0
right = N - 1
count = 0

while left < right:
    if fox_lengths[left] + fox_lengths[right] <= S:
        count += (right - left)
        left += 1
    else:
        right -= 1

print(count)
