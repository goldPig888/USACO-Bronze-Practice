num = int(input().strip())
result = []
countSee = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]


for i in range(num):
    first,second = map(str, input().split())
    result.append([first,second])

for i in range(num):
    temp=[]
    temp.extend(list(result[i][0]))
    temp.extend(list(result[i][1]))
    letters = set(temp)
    for letter in letters:
        count = max(result[i][0].count(letter), result[i][1].count(letter))
        countSee[ord(letter.upper())-65] += count
for i in countSee:
    print(i)
    