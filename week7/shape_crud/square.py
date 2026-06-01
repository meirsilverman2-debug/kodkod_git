from rectangle import Rectangle
# Level-3_Square:

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(width =side,  height=side)
        self.side = side

    def get_area(self):
        return super().get_area()
    
    def get_perimeter(self):
        return self.side * 4
    
    def to_dict(self):
        return {"area": self.get_area(),"perimeter": self.get_perimeter()}


    def __str__(self):
        return f"The formula for getting a square area is: {self.width} * {self.heigth} = {self.width * self.heigth} \n The formula for getting a square perimeter is: {self.side} * 4 = {self.side * 4} "
    

# s = Square(3)

# print(s.get_area())
# print(s.get_perimter())
# print(s)
# print(s.to_dict())