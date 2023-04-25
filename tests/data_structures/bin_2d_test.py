import pytest

from src.data_structures.bin_2d import *
from src.data_structures.package_2d import *
from src.data_structures.point_2d import *


def test_bin_2d():
    bin = Bin2D(10, 5)
    assert bin.is_empty() == True
    assert bin.is_valid() == True

    bin.insert(Point2D(0, 0), Package2D(5, 5))
    assert bin.is_empty() == False
    assert bin.is_valid() == True

    bin.insert(Point2D(5, 0), Package2D(5, 5))
    assert bin.is_valid() == True

    bin.insert(Point2D(5, 0), Package2D(5, 5))
    assert bin.is_valid() == False
