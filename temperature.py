temp = float(input("enter temperature (celcius): "))
if temp > 30:
    print("it is hot outside, wear something light and soft.")
elif temp > 15:
    print("it is a really good weather outside. Wear something comfortable and enjoy!")
elif temp > 0:
    print("it is cold outside. Wear a jacket.")
else:
    print("It is freezing outside. Wear multiple layers of warm clothing.")