class Point2D:
    def __init__(self, x: int | float, y: int | float):
        self.x = x
        self.y = y

    def add(self, x, y):
        self.x += x
        self.y += y
