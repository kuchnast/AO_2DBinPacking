from abc import ABC, abstractmethod
from src.data_structures.bin_2d import Bin2D
from src.data_operations.data_generator import OnlineGenerator, OfflineGenerator, GeneratorBaseType, GeneratorBase
from typing import List

"""
Base class for algorithms
"""


class AlgorithmBase(ABC):
    generator_class = None

    def __init__(self, bin_width: int, bin_height: int, generator: GeneratorBaseType):
        self.data_generator = generator
        self.bin_width = bin_width
        self.bin_height = bin_height
        self.opened_bins: List[Bin2D] = []
        self.closed_bins: List[Bin2D] = []
        super().__init__()

    @abstractmethod
    def run(self):
        RuntimeError("Not implemented")

    def is_valid(self) -> bool:
        for bin in self.opened_bins:
            if not bin.is_valid():
                return False
        for bin in self.closed_bins:
            if not bin.is_valid():
                return False
        return True

    def _close_all(self) -> None:
        for i in self.opened_bins:
            self.closed_bins.append(i)
        self.opened_bins.clear()


class OnlineAlgorithm(AlgorithmBase):
    generator_class = OnlineGenerator

    def __init__(self, bin_width: int, bin_height: int, generator: GeneratorBaseType):
        super().__init__(bin_width, bin_height, generator)
        if not isinstance(self.data_generator, OnlineGenerator):
            RuntimeError(f"Wrong generator type. Expected {OnlineGenerator}, get {generator}")

    @abstractmethod
    def run(self):
        RuntimeError("Not implemented")


class OfflineAlgorithm(AlgorithmBase):
    generator_class = OnlineGenerator

    def __init__(self, bin_width: int, bin_height: int, generator: GeneratorBaseType):
        super().__init__(bin_width, bin_height, generator)
        if not isinstance(self.data_generator, OfflineGenerator):
            RuntimeError(f"Wrong generator type. Expected {OfflineGenerator}, get {generator}")

    @abstractmethod
    def run(self):
        RuntimeError("Not implemented")
