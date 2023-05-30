import argparse
from algorithms_launcher import run_algorithm, print_result
from algorithms.next_fit_algorithm import NextFitAlgorithm
from algorithms.best_fit_algorithm import BestFitAlgorithm
from algorithms.first_fit_algorithm import FirstFitAlgorithm
from algorithms.worst_fit_algorithm import WorstFitAlgorithm
from algorithms.longer_side_first_algorithm import LongerSideFirstAlgorithm
from ploting import plot_bins2d
from typing import Optional, Sequence
import matplotlib.pyplot as plt
from os.path import isfile, isdir
from packing_stats import PackingResult, PackingStats

__version__ = "1.0.0"

alg_collection = {
    "next_fit": NextFitAlgorithm,
    "first_fit": FirstFitAlgorithm,
    "best_fit": BestFitAlgorithm,
    "worst_fit": WorstFitAlgorithm,
    "longer_side_first": LongerSideFirstAlgorithm,
}


def main(parameters: Optional[Sequence[str]] = None):
    parser = argparse.ArgumentParser()
    parser.set_defaults(action=run)
    parser.add_argument("-v", "--version", action="version", version=f"bin_packing_2d {__version__}")
    parser.add_argument(
        "-i", "--input", type=str, nargs="?", dest="input", default=None, required=True, help="Input file or directory"
    )
    parser.add_argument("-p", "--plot", dest="plot", action="store_true", help="Plot results")

    alg_keys = list(alg_collection.keys())
    alg_keys.append("all")
    parser.add_argument(
        "-a",
        "--algorithm",
        type=str,
        nargs="?",
        dest="algorithm",
        default="all",
        choices=alg_keys,
        help="Algorithm that will be executed or all if not set",
    )
    args = parser.parse_args(parameters)
    args.action(args)


def run(args):
    print(f"Running algorithm {args.algorithm} for {args.input}")
    is_plottable = isfile(args.input) and args.plot
    is_directory = isdir(args.input)

    if args.algorithm == "all":
        stats = PackingStats()
        for _, alg in alg_collection.items():
            result, bins = run_algorithm(args.input, alg)
            print_result(args.input, alg, result)

            if isinstance(result, PackingStats):
                stats.add_result_list(alg.get_name(), list(result.results.values())[0])
            elif isinstance(result, PackingResult):
                stats.add_result(alg.get_name(), result)
            elif isinstance(result, int):
                packages = 0
                for i in bins:
                    packages += len(i.packages)
                stats.add_result(alg.get_name(), PackingResult(bins_num=result, packages_num=packages))
            if is_plottable:
                plot_bins2d(bins, plot_title=alg.get_name())

        summary = stats.generate_summary()
        stats.print_summary_report(summary)
    else:
        result, bins = run_algorithm(args.input, alg_collection[args.algorithm])
        print_result(args.input, alg_collection[args.algorithm], result)
        if is_plottable:
            plot_bins2d(bins, plot_title=args.algorithm.get_name())

    if is_plottable:
        plt.show(block=True)


if __name__ == "__main__":
    main()
