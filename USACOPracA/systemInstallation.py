nr,nc = map(int, input().split())
matrix = []
maxSum = 0
for row in range(nr):
    line = list(map(int, input().strip().split()))
    matrix.append(line)

for row in range(0,nr-2):
    for i in range(0,nc-2):
        sum = matrix[row][i] + matrix[row][i+1] + matrix[row][i+2] + matrix[row+1][i] + matrix[row+1][i+1] + matrix[row+1][i+2] + matrix[row+2][i] + matrix[row+2][i+1] + matrix[row+2][i+2]
        if sum > maxSum:
            maxSum = sum
        #print(matrix[row][i],matrix[row][i+1],matrix[row][i+2])
        #print(matrix[row+1][i],matrix[row+1][i+1],matrix[row+1][i+2])
        #print(matrix[row+2][i],matrix[row+2][i+1],matrix[row+2][i+2])
print(maxSum)
        

