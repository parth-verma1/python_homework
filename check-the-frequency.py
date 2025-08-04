test = {'Codingal':3, 'is':2, 'best':2, 'for':2, 'Coding':1}

val = int(input("enter value to check freq: "))

count = list(test.values()).count(val)

print("frequency is", count)
