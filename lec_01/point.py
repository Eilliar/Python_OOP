import math


class Point:

    def __init__(self, x=0.0, y=0.0) -> None:
        self.move(x, y)

    def move(self, x: float, y: float):
        self.x = x
        self.y = y

    def reset(self):
        self.move(0, 0)

    def calculate_distance(self, other_point) -> float:
        return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)
