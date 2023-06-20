def leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def findNext(pos, month, year):
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 1 and leap(year):
        days[1] = 29
    return (pos + days[month]) % 7

N = int(input())

counter = [0] * 7
pos = 0
for year in range(1900, 1900 + N):
    for month in range(12):
        counter[pos] += 1  
        pos = findNext(pos, month, year)

print(' '.join(map(str, counter)))
