def minSwap(cows):
    swaps = 0
    n = len(cows)
    sorted_cows = sorted(cows)

    cow_pos = {cows[i]: i for i in range(n)}

    for i in range(n):
        current = cows[i]
        sorted_cow = sorted_cows[i]

        if current != sorted_cow:
            correct_index = cow_pos[sorted_cow]
            cows[i], cows[correct_index] = cows[correct_index], cows[i]
            cow_pos[current] = correct_index
            cow_pos[sorted_cow] = i
            swaps += 1
    return swaps

num = int(input().strip())
lineup = []
for i in range(num):
    line = list(map(int, input().strip().split()))
    lineup.extend(line)
min_swaps = minSwap(lineup)
print(min_swaps)
