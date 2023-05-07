import pytest

from src.data_operations.data_operations import DataOperations
from src.data_operations.data_generator import OnlineGenerator
from src.algorithms.next_fit_algorithm import NextFitAlgorithm


def test_if_create_3_bins():
    gen = OnlineGenerator(DataOperations().load_from_file('../data/test1.in'))
    alg = NextFitAlgorithm(gen.bin_width, gen.bin_height, gen)

    assert alg.run() == 3
    assert alg.is_valid()
