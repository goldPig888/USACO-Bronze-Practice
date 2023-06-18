def calculate_overlap(rect1, rect2):
    
    x1, y1, x2, y2 = rect1
    x3, y3, x4, y4 = rect2
    
    overlap_width = min(x2, x4) - max(x1, x3)
    overlap_height = min(y2, y4) - max(y1, y3)
    
    if overlap_width > 0 and overlap_height > 0:
        return overlap_width * overlap_height
    else:
        return 0
def calculateCovered(rect1, rect2):
    x1, y1, x2, y2 = rect1
    x3, y3, x4, y4 = rect2
    corners = [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]
    count = 0
    for corner in corners:
        x, y = corner
        
        if x >= x3 and x <= x4 and y >= y3 and y <= y4:
            count += 1
    
    return count
def area(rect1):
    x1, y1, x2, y2 = rect1
    return (x2 - x1)*(y2 - y1)

x1, y1, x2, y2 = tuple(map(int, input().split()))
x3, y3, x4, y4 = tuple(map(int, input().split()))
count = calculateCovered((x1, y1, x2, y2),(x3, y3, x4, y4))


if count == 2:
    all = area((x1, y1, x2, y2))
    overlap = calculate_overlap((x1, y1, x2, y2),(x3, y3, x4, y4))
    ans = all - overlap
elif count == 4:
    ans = 0
else:
    ans = area((x1, y1, x2, y2))

print(ans)