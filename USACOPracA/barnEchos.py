string1 = input().strip()
string2 = input().strip()

max_overlap = 0
overlap = min(len(string1), len(string2))

while overlap > 0:
    if string1[:overlap] == string2[-overlap:]:
        max_overlap = overlap
        break
    elif string2[:overlap] == string1[-overlap:]:
        max_overlap = overlap
        break
    overlap -= 1

print(max_overlap)
