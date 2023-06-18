import sys

fin = list(map(int, sys.stdin.readline().strip().split()))
row, col, num = fin[0], fin[1], fin[2]

def dilate_shape(shape, factor):
    dilated_shape = []
    for row in shape:
        dilated_row = ''
        for char in row:
            dilated_row += char * factor
        dilated_shape.extend([dilated_row] * factor)
    return dilated_shape

symbol = []

for i in range(row):
    symbol.append(sys.stdin.readline().strip())

ans = dilate_shape(symbol, num)
for row in ans:
    print(row)