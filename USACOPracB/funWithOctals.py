hexadecimal = input().strip()  
binary = bin(int(hexadecimal, 16))[2:]
binary = binary.zfill(4)

octal = oct(int(binary, 2))[2:] 

print(octal) 
