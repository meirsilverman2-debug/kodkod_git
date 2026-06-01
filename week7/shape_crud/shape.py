# # Level-1_Shape:

class Shape:
    def __init__(self, shape_id, shape_type):
        self.id = shape_id
        self.shape_type = shape_type

    def get_area(self):
        pass

    def get_perimeter(self):
        pass

    def to_dict(self):
        return {"area": self.get_area(),"perimeter": self.get_perimeter()}

    def __str__(self):
        pass




