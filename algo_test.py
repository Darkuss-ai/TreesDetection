#pip install tqdm~=4.62.3 Pillow~=8.4.0


from tqdm import tqdm
import os

from PIL import Image

data_root = "C:/Users/Sergey/Desktop/StudVesna/Neuro/"

train_dir = '3mTrain/'
val_dir = '3mVal/'

class_names = ['aspen/', 'birch/', 'pine/', 'spruce/']

for class_name in class_names:

    source_dir = os.path.join(data_root, train_dir, class_name)
    for filename in enumerate(tqdm(os.listdir(source_dir))):
        if filename[1] == 'Thumbs.db':
            continue
        if filename[1] == 'desktop.ini':
            continue
        im = Image.open(source_dir + filename[1])
        imHF = im.transpose(Image.FLIP_LEFT_RIGHT)

        widths, heights = zip(*(i.size for i in [im, imHF]))

        total_width = sum(widths)
        max_height = max(heights)

        new_imHF = Image.new('RGB', (total_width, max_height))

        x_offset = 0
        for images in [im, imHF]:
            new_imHF.paste(images, (x_offset, 0))
            x_offset += im.size[0]

        im = new_imHF
        finalim = new_imHF.transpose(Image.FLIP_TOP_BOTTOM)

        widths, heights = zip(*(i.size for i in [im, finalim]))
        total_width = max(widths)
        max_height = max(heights) * 2

        finalimage = Image.new('RGB', (total_width, max_height))

        x_offset = 0
        finalimage.paste(im, (x_offset, 0))
        finalimage.paste(finalim, (x_offset, int(max_height / 2)))

        # finalimage.show()

        finalimage.save(source_dir + filename[1])