try:
    age = int(input("enter ur age: "))
    if age % 2 == 0:
        print("age is even")
    else:
        print("age is odd")
except:
    print("value error")
