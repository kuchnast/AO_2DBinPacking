from data_structures.point_2d import Point2D
from typing import TypeVar


class Package2D:
    T = TypeVar("T", bound="Package2D")

    def __init__(self, width: int, height: int, with_rotation=False):
        self.with_rotation = with_rotation
        self.width = width
        self.height = height

    def rotate(self) -> None:
        self.width, self.height = self.height, self.width


class PlacedPackage2D(Package2D):
    def __init__(self, width: int, height: int, location: Point2D, with_rotation=False):
        super().__init__(width, height, with_rotation)
        self.location = location

    def __str__(self):
        return f"size: {self.width}x{self.height} loc: {self.location}"

    @classmethod
    def from_package(cls, package: Package2D, location: Point2D):
        return cls(package.width, package.height, location, package.with_rotation)
