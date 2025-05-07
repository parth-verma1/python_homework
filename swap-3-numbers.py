num = int(input("Enter a 3-digit number: "))
a = num // 100    
b = (num // 10) % 10
c = num % 10
print("Original number:", num)
print("Digits are:")
print("a =", a)
print("b =", b)
print("c =", c)
temp = a
a = b
b = c
c = temp
new_num = a * 100 + b * 10 + c

print("Number after swapping digits:", new_num)
