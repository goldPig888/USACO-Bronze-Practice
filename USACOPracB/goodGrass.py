def area(rect1):
    x1, y1, x2, y2 = rect1
    return (x2 - x1)*(y2 - y1)

def calculate_overlap(rect1, rect2):
    
    x1, y1, x2, y2 = rect1
    x3, y3, x4, y4 = rect2
    
    overlap_width = min(x2, x4) - max(x1, x3)
    overlap_height = min(y2, y4) - max(y1, y3)
    
    if overlap_width > 0 and overlap_height > 0:
        return overlap_width * overlap_height
    else:
        return 0

x1, y1, x2, y2 = tuple(map(int, input().split()))
x3, y3, x4, y4 = tuple(map(int, input().split()))
x5, y5, x6, y6 = tuple(map(int, input().split()))

rect1 = area((x1, y1, x2, y2))
rect2 = area((x3, y3, x4, y4))
rect1_overlap = calculate_overlap((x1, y1, x2, y2), (x5, y5, x6, y6))
rect2_overlap = calculate_overlap((x3, y3, x4, y4), (x5, y5, x6, y6))
print(rect1 + rect2 - rect1_overlap - rect2_overlap)


