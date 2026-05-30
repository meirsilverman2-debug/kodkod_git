from rectangle import Rectangle
from shape_manager import Validitor

# Level-4_Triangle:

class Triangle(Rectangle):
    def __init__(self, base, height, side_a, side_b, side_c):
        super().__init__(width= base, height= height)
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.valid = Validitor()
    
    def get_area(self):
        if self.valid.is_valid(self.width, self.heigth):
            return super().get_area(self.width, self.heigth) / 2
        
        return("All attr most be an int or flout not str and bigger than zero")
       

    def get_perimeter(self):
        if self.valid.is_valid(self.side_a, self.side_b, self.side_c):
            return self.side_a + self.side_b + self.side_c
        
        return("All attr most be an int or flout not str and bigger than zero")
        
    
    def __str__(self):
        if self.valid.is_valid(self.side_a, self.side_b, self.side_c):
            return f"The formula for getting a triangle area is: {self.width} * {self.heigth} = {self.width * self.heigth} \n ,and the formula for getting the perimeter is: {self.side_a} + {self.side_b} + {self.side_c} = {self.side_a + self.side_b + self.side_c}"
        
        return("All attr most be an int or flout not str and bigger than zero")
        
    

# t = triangle(2, 4, 2, 2, 2)

# print(t.get_area())
# print(t.get_perimter())
# print(t)