import random
import pandas


class DataGenerator:
    def __init__(self):
        random.seed()
        pass

    @staticmethod
    def generate_input_data(box_width: int, box_height: int, max_width: int, max_height: int, size: int) -> pandas.DataFrame:
        val_dict = {'width': [box_width], 'height': [box_height]}

        for i in range(size):
            val_dict['width'].append(random.randint(1, max_width))
            val_dict['height'].append(random.randint(1, max_height))

        return pandas.DataFrame(val_dict)

    @staticmethod
    def save_to_file(path: str, df: pandas.DataFrame) -> None:
        df.to_csv(path, header=True, index=False)

    @staticmethod
    def load_from_file(path) -> pandas.DataFrame:
        return pandas.read_csv(filepath_or_buffer=path)
