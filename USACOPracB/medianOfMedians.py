N = int(input())

painting = []
for _ in range(N):
    row = list(map(int, input().split()))
    painting.append(row)

medians = []
for row in painting:
    row.sort()
    median = row[N // 2]
    medians.append(median)

medians.sort()
median_of_medians = medians[N // 2]

print(median_of_medians)
