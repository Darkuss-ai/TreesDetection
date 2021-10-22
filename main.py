import shutil
from tqdm import tqdm
import os

from PIL import Image

data_root = "C:/Users/Sergey/Desktop/StudVesna/Neuro/"

train_dir = '5mTrainMONO/'
val_dir = '5mValMONO/'

class_names = ['aspen/', 'birch/', 'pine/', 'spruce/']


#MIRRORING IMAGES
# for class_name in class_names:
#
#     source_dir = os.path.join(data_root, val_dir, class_name)
#     for filename in enumerate(tqdm(os.listdir(source_dir))):
#         if filename[1] == 'Thumbs.db':
#             continue
#         if filename[1] == 'desktop.ini':
#             continue
#         im = Image.open(source_dir + filename[1])
#         imHF = im.transpose(Image.FLIP_LEFT_RIGHT)
#
#         widths, heights = zip(*(i.size for i in [im, imHF]))
#
#         total_width = sum(widths)
#         max_height = max(heights)
#
#         new_imHF = Image.new('RGB', (total_width, max_height))
#
#         x_offset = 0
#         for images in [im, imHF]:
#             new_imHF.paste(images, (x_offset, 0))
#             x_offset += im.size[0]
#
#         im = new_imHF
#         finalim = new_imHF.transpose(Image.FLIP_TOP_BOTTOM)
#
#         widths, heights = zip(*(i.size for i in [im, finalim]))
#         total_width = max(widths)
#         max_height = max(heights)*2
#
#         finalimage = Image.new('RGB', (total_width, max_height))
#
#         x_offset = 0
#         finalimage.paste(im, (x_offset, 0))
#         finalimage.paste(finalim, (x_offset, int(max_height/2)))
#
#         #finalimage.show()
#
#         finalimage.save(source_dir + filename[1])


#COPY TO NEW FOLDERS FROM SOURCE
# for dir_name in [train_dir, val_dir]:
#     for class_name in class_names:
#         os.makedirs(os.path.join(dir_name, class_name), exist_ok=True)
#
# for class_name in class_names:
#     source_dir = os.path.join(data_root, '3m/', class_name)
#     for i, file_name in enumerate(tqdm(os.listdir(source_dir))):
#         if i % 6 == 0:
#             dest_dir = os.path.join(val_dir, class_name)
#             shutil.copy(os.path.join(source_dir, file_name), os.path.join(dest_dir, file_name))
#         else:
#             dest_dir = os.path.join(train_dir, class_name)
#             shutil.copy(os.path.join(source_dir, file_name), os.path.join(dest_dir, file_name))

#REVERSE TO BLACK&WHITE
# for class_name in class_names:
#     source_dir = os.path.join(data_root, train_dir, class_name)
#     for filename in enumerate(tqdm(os.listdir(source_dir))):
#         if filename[1] == 'Thumbs.db':
#             continue
#         if filename[1] == 'desktop.ini':
#             continue
#         image_file = Image.open(source_dir+filename[1])
#         image_file = image_file.convert('1')
#         image_file.save(source_dir+filename[1])

