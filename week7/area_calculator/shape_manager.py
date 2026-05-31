from calculator import Shape
from triangle import Triangle
from hexagon import Hexagon
from square import Square
from rectangle import Rectangle
from circle import Circle
from shape_manager import ShapeManager


class ShapeManager:
    def __init__(self):
        self.shapes = []
        self.load_from_json()

def create_shape(self, shape):
    self.shape.append(shape)


def get_all_shapes(self):
    pass


def update_shape(self, shape_id, new_data):
    pass


def delete_shape(self, shape_id):
    pass


def save_to_json(self):
    pass


def load_from_json(self):
    pass


class Validitor:
    def __init__(self):
        
        self.valid = False

    def is_valid(self, *attr ):

        for a in attr:
            if isinstance(a,(int, float)):
                self.valid = True
            else:
                self.valid = False

        return self.valid

v = Validitor()
print(v.is_valid(12, 12, 12))