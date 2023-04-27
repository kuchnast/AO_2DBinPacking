from data_operations.data_generator import *
import os

if __name__ == "__main__":
    dg = DataGenerator()
    packages_size = [10, 100, 1000]
    packages_max_size = [5, 10, 25]
    box_dim = [5, 10, 25]
    path = "./data/in"

    if not os.path.exists(path):
        os.makedirs(path)

    for size in packages_size:
        for box_width in box_dim:
            for box_height in box_dim:
                for max_width in packages_max_size:
                    for max_height in packages_max_size:
                        if max_width > box_width or max_height > box_height:
                            continue
                        df = dg.generate_input_data(box_width, box_height, max_width, max_height, size)
                        file_name = f's{size}_b{box_width}_{box_height}_p{max_width}_{max_height}.in'
                        dg.save_to_file(path + '/' + file_name, df)
