import os
import Augmentor


TRAIN_PATH = "./processed_data/train/"


def generate_data(output_file, path):
    output_path = "output_data/" + output_file
    p = Augmentor.Pipeline(source_directory=path)
    # Point to a directory containing ground truth data.
    # Images with the same file names will be added as ground truth data
    # and augmented in parallel to the original data.
    # p.ground_truth("/path/to/ground_truth_images")
    # Add operations to the pipeline as normal:
    p.rotate(probability=1, max_left_rotation=14, max_right_rotation=14)
    # p.flip_left_right(probability=0.5)
    p.zoom_random(probability=0.5, percentage_area=0.8)
    # p.flip_top_bottom(probability=0.5)
    p.random_distortion(probability=0.7, grid_width=5, grid_height=5, magnitude=8)
    p.flip_left_right(probability=0.3)
    p.flip_top_bottom(probability=0.4)
    p.rotate_random_90(probability=0.3)
    p.skew(0.2, 0.7)
    p.skew_tilt(0.6, 0.7)
    p.sample(100)


if __name__ == '__main__':
    for dir in os.listdir(TRAIN_PATH):
        input_path = TRAIN_PATH + dir
        print(input_path)
        generate_data(dir, input_path)
