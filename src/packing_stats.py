from collections import defaultdict
from dataclasses import dataclass
from tabulate import tabulate
from typing import List, Dict
import pandas as pd


@dataclass
class PackingResult:
    bins_num: int = 0
    packages_num: int = 0
    package_max_width: int = 0
    package_max_height: int = 0
    bin_max_width: int = 0
    bin_max_height: int = 0


@dataclass
class SingleAlgorithmSummary:
    num_meas = 0
    min_val = float('inf')
    max_val = 0
    sum_val = 0

    def get_avg(self):
        return round(self.sum_val / self.num_meas, 1)

    def add_measurement(self, bins: int):
        self.num_meas += 1
        self.sum_val += bins

        if bins > self.max_val:
            self.max_val = bins
        if bins < self.min_val:
            self.min_val = bins


class PackingStats:
    def __init__(self):
        self.results = defaultdict(list[PackingResult])

    def add_result(self, algorithm_name: str, res: PackingResult):
        self.results[algorithm_name].append(res)
        self.results[algorithm_name].sort(key=lambda x: x.packages_num)

    def add_result_list(self, algorithm_name: str, res: List[PackingResult]):
        self.results[algorithm_name] += res
        self.results[algorithm_name].sort(key=lambda x: x.packages_num)

    def print_results_for_algorithm(self, algorithm_name: str):
        names = ["Packages num", "Package max size", "Bin size", "Bins num"]
        report: List[List] = []

        for el in self.results[algorithm_name]:
            report.append(
                [
                    el.packages_num,
                    f"{el.package_max_width}x{el.package_max_height}",
                    f"{el.bin_max_width}x{el.bin_max_height}",
                    el.bins_num,
                ]
            )

        print("Results for algorithm " + algorithm_name)
        print(tabulate(report, names, numalign="center", tablefmt="pretty"))

    def generate_summary(self):
        report = defaultdict(Dict[str, SingleAlgorithmSummary])

        for algorithm_name, results in self.results.items():
            summary = defaultdict(SingleAlgorithmSummary)
            for el in results:
                summary[el.packages_num].add_measurement(el.bins_num)

            report[algorithm_name] = summary

        return report

    @staticmethod
    def print_summary_report(summary: Dict[str, Dict[str, SingleAlgorithmSummary]]):
        column_names = list(summary.keys())
        column_names.insert(0, "Packages/Algorithm")
        index = []
        report: List[List] = []

        for i in list(summary.values())[0].keys():
            index.append(i)

        for i in range(len(list(summary.values())[0])):
            report.append([index[i]])

        for alg_name, alg_summary in summary.items():
            val = list(alg_summary.values())
            for i in range(len(val)):
                report[i].append(f"({val[i].min_val}, {val[i].get_avg()}, {val[i].max_val})")

        print(tabulate(report, column_names, numalign="center", tablefmt="pretty"))

