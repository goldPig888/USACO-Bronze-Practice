line = input().strip()
line0 = line + "0000"
line = line.zfill(len(line0))
ans = ""
carry = 0
for i in range(len(line)):
    num1, num2 = int(line0[len(line) - i - 1]), int(line[len(line) - i - 1])
    sumBinary = num1 + num2 + carry
    carry = sumBinary // 2
    ans += str(sumBinary % 2)

while carry > 0:
    ans += str(carry % 2)
    carry //= 2

print(ans[::-1])
