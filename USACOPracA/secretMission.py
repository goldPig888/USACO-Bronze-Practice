cow_name = input().strip()
code = input().strip()

prod1 = 1
prod2 = 1

for ch in cow_name:
    prod1 *= (ord(ch) - 64)
prod1 %= 47

for ch in code:
    prod2 *= (ord(ch) - 64)
prod2 %= 47

if prod1 == prod2:
    print("GO")
else:
    print("STAY")