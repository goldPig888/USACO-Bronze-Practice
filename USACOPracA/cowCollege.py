n = int(input().strip())
prices = list(map(int, input().strip().split()))

prices = sorted(prices, reverse=True)

max_revenue = 0
optimal_tuition = prices[0]

for i in range(n):
    revenue = prices[i] * (i + 1)
    if revenue >= max_revenue:
        max_revenue = revenue
        optimal_tuition = prices[i]

print(max_revenue, optimal_tuition)
