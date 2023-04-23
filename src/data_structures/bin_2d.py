import itertools

from src.data_structures.package_2d import Package2D
from itertools import combinations

class Bin2D:
    def __init__(self, width, height):
        self.packages = list
        self.width = width
        self.height = height
        pass

    def is_empty(self) -> bool:
        return True if len(self.packages) else False

    def insert(self, x, y, package: Package2D):
        self.packages.append([x, y, package])

    def is_valid(self) -> bool:
        for el in itertools.combinations(self.packages, 2):
            pass



