from PIL import Image
from pathlib import Path, PurePath, PosixPath
import math

image_folder = Path.cwd() / 'output'
all_folder = image_folder / 'all'

def get_image_list():

    return sorted(all_folder.glob('*.png'))


def cropper(cats):

    for i, file in enumerate(cats):
        file = PurePath(file)
        path = Path(file)

        cat_stem = file.stem

        for j in range(1,25):

            image = Image.open(path)

            cat_position = j

            out_folder = image_folder / str(cat_position)

            Path(out_folder).mkdir(exist_ok=True)

            output = str(out_folder) + '/' + str(cat_stem) + '_' + str(cat_position) + '.png'

            # Infer row and column
            # Using 8.5 for rows, since if divided by 8, the 8th and 16th cats are given one row too high
            row = math.floor(cat_position / 8.5) + 1
            column = cat_position % 8 or 8

            right = (2 + 128) * column # 130, 260, 390, 520
            left = right - 128 # 2, 132, 262, 392
            lower = (2 + 128) * row
            upper = lower - 128

            image = image.crop((left, upper, right, lower))

            image.save(output)


def main():

    cats = get_image_list()
    cropper(cats)

    # Gif command in terminal
    # convert -loop 0 -delay 1x3 *.png out.gif


if __name__ == "__main__":
    main()
