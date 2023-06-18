def is_radar(brand):
    return str(brand) == str(brand)[::-1]

def find_radar(brand):
    steps = 0
    current = brand
    while not is_radar(current):
        current += int(str(current)[::-1])
        steps += 1
    return steps, current

brand = int(input())
steps, radar_brand = find_radar(brand)
print(steps, radar_brand)
