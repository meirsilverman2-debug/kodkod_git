from calculator import Shape
from triangle import Triangle
from hexagon import Hexagon
from square import Square
from rectangle import Rectangle
from circle import Circle
import json

class ShapeManager:
    def __init__(self):
        self.shapes = []
        self.load_from_json()

    def create_shape(self, shape):
            self.shapes.append(shape)
            self.save_to_json()


    def get_all_shapes(self):
        for shape in self.shapes:
            print(shape)


    def update_shape(self, shape_id, new_data):
        for shape in self.shapes:

            if shape.id == shape_id:

                if isinstance(shape, Square):
                    shape.side = new_data["side"]
                    shape.width = new_data["side"]
                    shape.height = new_data["side"]

                elif isinstance(shape, Rectangle):
                    shape.width = new_data["width"]
                    shape.height = new_data["height"]

                elif isinstance(shape, Circle):
                    shape.radius = new_data["radius"]
                
                elif isinstance(shape, Hexagon):
                    shape.side = new_data["side"]

                elif isinstance(shape, Triangle ):
                    shape.side_a = new_data["side_a"]
                    shape.side_b = new_data["side_b"]
                    shape.side_c = new_data["side_c"]


                self.save_to_json()
                
                

    def delete_shape(self, shape_id):
        for shape in self.shapes:

            if shape.id == shape_id:
                self.shapes.remove(shape)
                self.save_to_json()
                return

    def save_to_json(self):
        data = []

        for shape in self.shapes:
            data.append(shape.to_dict())

        with open(file="shapes.json", mode="w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    def load_from_json(self):
        try:
            with open(file="shapes.json", mode="r", encoding="utf-8") as r_file:
                data = json.load(r_file)
                    
            
                for item in data:

                    if item["type"] == "square":
                        shape = Square(
                            item["id"],
                            item["side"]
                        )

                    elif item["type"] == "rectangle":
                        shape = Rectangle(
                            item["id"],
                            item["width"],
                            item["height"]
                        )

                    elif item["type"] == "circle":
                        shape = Circle(
                            item["id"],
                            item["radius"]
                        )

                    elif item["type"] == "hexagon":
                        shape = Hexagon(
                            item["id"],
                            item["side"]
                        )

                    elif item["type"] == "triangle":
                        shape = Triangle(
                            item["id"],
                            item["side_a"],
                            item["side_b"],
                            item["side_c"]
                        )

                    self.shapes.append(shape)


        except Exception as e:
            print(f"ERROR: {e}")
            self.shapes = []

class Validator:
    def __init__(self):
        
        self.valid = False

    def is_valid(self, *attr ):

        for a in attr:
            if isinstance(a,(int, float)):
                self.valid = True
            else:
                self.valid = False

        return self.valid

