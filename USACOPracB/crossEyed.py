A, B = map(str, input().split())

min_sum = int(A.replace('6', '5')) + int(B.replace('6', '5'))
max_sum = int(A.replace('5', '6')) + int(B.replace('5', '6'))

print(min_sum, max_sum)