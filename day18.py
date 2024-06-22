class Shape:
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius
    
my_rectangle = Rectangle(5,6)
result1 = my_rectangle.area()
print(result1)
my_circle = Circle(7)
result2 = my_circle.area()
print(result2)

    