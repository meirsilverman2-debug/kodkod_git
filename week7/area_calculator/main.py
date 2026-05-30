from calculator import Shape
from triangle import Triangle
from hexagon import Hexagon
from square import Square
from rectangle import Rectangle
from circle import Circle
from shape_manager import ShapeManager

# Level-7_main.py:

instances = [Triangle(2, -12, 2, 2, 2 ), Hexagon(3), Square(4), Rectangle(5, 4), Circle(7)]

for instance in instances:
    print(f"Shape: {type(instance).__name__} \n Area: {instance.get_area()} \n Perimeter: {instance.get_perimeter()}  ")
    print()
    print("=========================================")



s = ShapeManager()
s.append()