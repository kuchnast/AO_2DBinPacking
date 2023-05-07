from os.path import join, isfile, isdir
from src.algorithms.algorithm_base import AlgorithmBase
from src.data_operations.data_operations import DataOperations
from src.packing_stats import PackingResult, PackingStats
from typing import Type


def run_algorithm(
    path: str, algorithm: Type[AlgorithmBase], with_validation=True
) -> PackingStats | PackingResult | int:
    if isfile(path):
        return run_for_file(path, algorithm, with_validation)
    elif isdir(path):
        return run_for_directory(path, algorithm, with_validation)
    else:
        raise RuntimeError(f"Not file or directory: {path}")


def print_result(path: str, algorithm: Type[AlgorithmBase], res: PackingStats | PackingResult | int):
    if isinstance(res, PackingStats):
        print(f"Result for {path}:")
        res.print_results_for_algorithm(algorithm.__name__)
    elif isinstance(res, PackingResult):
        print(f"Result for {path} and {algorithm.__name__}: {res}")
    elif isinstance(res, int):
        print(f"Result for {path} and {algorithm.__name__}: {res} bins")
    else:
        RuntimeError(f"Wrong type: {type(res)}")


def run_for_file(file: str, algorithm: Type[AlgorithmBase], with_validation=True) -> PackingResult | int:
    gen = algorithm.generator_class(DataOperations().load_from_file(file))
    alg = algorithm(gen.bin_width, gen.bin_height, gen)
    bins_num = alg.run()

    if with_validation and not alg.is_valid():
        RuntimeError(f"Invalid result for {algorithm.__name__} file {file}")

    parsed = DataOperations().parse_input_file_name(file)
    if parsed is None:
        return bins_num
    else:
        return PackingResult(
            bins_num,
            parsed["size"],
            parsed["max_width"],
            parsed["max_height"],
            parsed["box_width"],
            parsed["box_height"],
        )


def run_for_directory(directory: str, algorithm: Type[AlgorithmBase], with_validation=True) -> PackingStats:
    do = DataOperations()
    stats = PackingStats()
    files = do.get_all_input_files(directory)
    files.sort(key=str.upper)

    for f in files:
        gen = algorithm.generator_class(DataOperations().load_from_file(join(directory, f)))
        alg = algorithm(gen.bin_width, gen.bin_height, gen)
        bins_num = alg.run()

        if with_validation and not alg.is_valid():
            RuntimeError(f"Invalid result for {algorithm.__name__} file {f}")

        parsed = do.parse_input_file_name(f)
        if parsed is None:
            RuntimeError("Invalid input file name")
        res = PackingResult(
            bins_num,
            parsed["size"],
            parsed["max_width"],
            parsed["max_height"],
            parsed["box_width"],
            parsed["box_height"],
        )
        stats.add_result(algorithm.__name__, res)

    return stats
