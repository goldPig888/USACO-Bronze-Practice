n,m = map(int, input().split())

prices = []
maxL = 0
lim = 0
for i in range(m):
    price = int(input())
    prices.append(price)

prices = sorted(prices,reverse=True)

for ma in range(m):
    count = 0
    ans = 0
    for i in prices:

        if i >= prices[ma]:
            count +=1
    ans = prices[ma]*count
    if ans > maxL and ma<n:
        maxL = ans
        lim = prices[ma]

print(lim,maxL)