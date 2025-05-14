base = int(input("Enter the base number: "))
limit = int(input("Enter how many powers to calculate: "))

i = 1
while i <= limit:
    result = base ** i
    print(str(base) + " to the power " + str(i) + " is " + str(result))
    i += 1
