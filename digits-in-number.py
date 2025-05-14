num = int(input("Enter a number: "))
digits = 0

if num < 0:
    num = -num

while num != 0:
    num = num // 10
    digits += 1

print("Number of digits is " + str(digits))
