class circle:
    def __init__(self,r):
        self.r=r
    
    def area(self):
        return 3.14*self.r*self.r

    def peri(self):
        return 2*3.14*self.r

r=int(input("enter radius:"))
c=circle(r)
print("area is",c.area())
print("perimeter is",c.peri())
