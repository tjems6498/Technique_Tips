import cv2
import albumentations as A
import numpy as np
from albumentations_tutorial.utils import plot_examples
from PIL import Image

image = Image.open('images/elon.jpeg')

transform = A.Compose(
    [
        A.Resize(width=1920, height=1080),
        A.ChannelShuffle(p=0.7),
        # A.CLAHE(p=1)
        # A.RandomCrop(width=1280, height=720),
        # A.Rotate(limit=40, p=0.9, border_mode=cv2.BORDER_CONSTANT),  # BORDER_CONSTANT : 회전했을때 남은부분 검은색으로
        # A.HorizontalFlip(p=0.5),
        # A.VerticalFlip(p=0.1),
        # A.RGBShift(r_shift_limit=25, g_shift_limit=25, b_shift_limit=25, p=0.9),
        # A.OneOf([
        #     A.Blur(blur_limit=3, p=0.5),
        #     A.ColorJitter(p=0.5),
        # ], p=1.0),
    ]
)

images_list = [image]
image = np.array(image)
for i in range(5):
    augmentations = transform(image=image)
    augmented_img = augmentations['image']
    images_list.append(augmented_img)
plot_examples(images_list)