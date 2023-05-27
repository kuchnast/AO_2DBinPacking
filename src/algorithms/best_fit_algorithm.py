from algorithms.algorithm_base import OnlineAlgorithm
from data_operations.data_generator import GeneratorBaseType
from data_structures.bin_2d import Bin2D
from data_structures.package_2d import Package2D
from data_structures.point_2d import Point2D

"""
Base class for algorithms
"""


class Row():  # klasa dodana przeze mnie
    def __init__(self, w, h1, h2):
        self.width = w
        self.bottomheight = h1
        self.upperheight = h2


class BestFitAlgorithm(OnlineAlgorithm):
    def __init__(self, bin_width: int, bin_height: int, generator: GeneratorBaseType):
        super().__init__(bin_width, bin_height, generator)
        self.row_list = []  # dodane przeze mnie
        self._open_bin()

    def _check_if_fit(self, loc: Point2D, package: Package2D):
        if loc.x + package.width > self.bin_width or loc.y + package.height > self.bin_height:
            return False
        return True

    def _insert_if_fit(self, loc: Point2D, package: Package2D):
        if self._check_if_fit(loc, package):
            self.opened_bins[0].insert(loc, package)
            return True
        return False

    def _open_bin(self):
        self.opened_bins.append(Bin2D(self.bin_width, self.bin_height))

    def _pack(self, package: Package2D) -> None:

        min_spaces = []  # lista ktora przechowuje wolne miejsca w rzedach

        for box in self.opened_bins:
            self.row_list.append([])
            if len(self.row_list) == 0:  # czy lista pusta

                if self._insert_if_fit(Point2D(0, 0), package):  # wkladam boxa w punkcie 0,0

                    print(self.opened_bins.index(box))
                    self.row_list[self.opened_bins.index(box)].append(Row(package.width, package.height,0))  # dodaje pierwszy rzad z aktualna zajeta szerokoscia i wysokosself._current_height = self._next_height
                    print(self.row_list[self.opened_bins.index(box)][0])

            for row in self.row_list[self.opened_bins.index(box)]:  # ide teraz po rzedach

                if row.width != self.bin_width:  # sprawdzam czy rzad ma jakies wolne miejsce na boxa

                    if package.width < box.width - row.width or package.height <= row.height:  # sprawdzam czy box sie miesci

                        free_space = row.width - package.width  # licze ile by zostalo miejsca
                        min_spaces.append(self.opened_bins.index(box, row.index, free_space))

                else:
                    continue
            # dalsze kroki -> wylonic min wolne miejsce aby wstawic boxa, jesli lista jest pusta to tworzy nowego boxa i dodaje rzad

        if len(min_spaces) != 0:  # jesli znalazlo jakakolwiek wolna przestrzen dla nowego pudelka

            var_min = [0, 0, 0]

            for i in min_spaces:  # szuka minimum z wolnych przestrzeni
                if var_min[2] < i[2]:
                    var_min = i

            if self._insert_if_fit(Point2D(self.row_list[var_min[0]][var_min[1]].width,self.row_list[var_min[0]][var_min[1]].bottomheight), package):
                self.row_list[var_min[0]][var_min[1]].width += package.width  # wpierdalam tutaj pudelko w wolna przestrzen i aktualizuje szerokosc w rzedzie, wysokosci nie musze bo jest taka sama

        elif self._insert_if_fit(Point2D(0, self.row_list[-1][-1].upperheight), package):  # insert package in new row
            self.row_list[-1].append(Row(package.width, package.height, 0))

        else:  # open new bin
            self._open_bin()
            if self._insert_if_fit(Point2D(0, 0), package):
                self.row_list[-1].append(Row(package.width, package.height, 0))
            else:
                RuntimeError("Package bigger than bin")

        min_spaces.clear()

    def run(self) -> int:
        while True:
            package = self.data_generator.get()
            if package is None:
                break
            self._pack(package)

        self._close_all()
        return len(self.closed_bins)