string = input().strip()
result = ""
collide = []
for lead in range(len(string)):
    end = len(string) - string[::-1].index(string[lead]) - 1

    for others in range(lead+1,end):
        if string[lead+1:end].count(string[others]) != 2:
            collide.append(string[others])
            print(string[others])
print(len(set(collide)))