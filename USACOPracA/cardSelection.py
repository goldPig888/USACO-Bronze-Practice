import sys

cards, played = map(int, input().strip().split())

line = {}

for i in range(cards):
    line[i] = int(input().strip())

ans = []

for _ in range(played):
    highest_power = max(line.values())
    played_card = min([card for card, power in line.items() if power == highest_power])
    ans.append(played_card)
    
    power_to_distribute = highest_power // (cards - 1)
    remainder = highest_power % (cards - 1)
    
    for card in line.keys():
        if card != played_card:
            line[card] += power_to_distribute
            if remainder > 0:
                line[card] += 1
                remainder -= 1
    
    line[played_card] = 0

for card in ans:
    print(card + 1)
