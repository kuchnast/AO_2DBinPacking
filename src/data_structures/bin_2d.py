from src.data_structures.package_2d import Package2D, PlacedPackage2D
from src.data_structures.point_2d import Point2D
import itertools


class Bin2D:
    def __init__(self, width, height):
        self.packages = []
        self.width = width
        self.height = height
        pass

    def is_empty(self) -> bool:
        return False if len(self.packages) else True

    def insert(self, point: Point2D, package: Package2D) -> None:
        self.packages.append(PlacedPackage2D.from_package(package, point))

    @staticmethod
    def _is_overlap(first_l: Point2D, first_r: Point2D, second_l: Point2D, second_r: Point2D):

        # if rectangle has area 0, no overlap
        if first_l.x == first_r.x or first_l.y == first_r.y or second_r.x == second_l.x or second_l.y == second_r.y:
            return False

        # If one rectangle is on left side of other
        if first_l.x > second_r.x or second_l.x > first_r.x:
            return False

        # If one rectangle is above other
        if first_r.y > second_l.y or second_r.y > first_l.y:
            return False

        return True

    def is_valid(self) -> bool:
        for el1, el2 in itertools.combinations(self.packages, 2):
            if self._is_overlap(el1.location, Point2D(el1.location.x + el1.width, el1.location.y + el1.height),
                                el2.location, Point2D(el2.location.x + el2.width, el2.location.y + el2.height)):
                return False
        return True
