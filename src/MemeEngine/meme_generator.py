import random
import os
from typing import Tuple

from PIL import Image, ImageDraw, ImageFont


class MemeGenerator:
    def __init__(self, output_dir):
        self.output_dir = output_dir

    def make_meme(self, img_path, text, author, width=500) -> str:
        """Create a meme, a loaded picture with a specify quote

        Arguments:
                img_path {str} -- the file location for the input image.
                text {str} -- the desired text which will be drawn on the input image.
                author {str} -- author of the drawn text
                width {int} -- The pixel width value. Default=500.
            Returns:
                str -- the file path to the output meme.
        """
        with Image.open(img_path) as im:
            ratio = width / float(im.size[0])
            height = int(ratio * float(im.size[1]))
            im = im.resize((width, height), Image.NEAREST)

            draw = ImageDraw.Draw(im)
            position = self.generate_text_position(width, height)
            text_author = f'\n\n- {author}'
            body_font = ImageFont.truetype('./fonts/RobotoMono-Regular.ttf', size=16)
            author_font = ImageFont.truetype('./fonts/RobotoMono-Italic.ttf', size=14)
            draw.text(position, text, font=body_font, fill='black', stroke_width=1, stroke_fill='white')
            draw.text(position, text_author, font=author_font, fill='black')

            output_path = self.make_output_path(img_path)
            im.save(output_path)

        return output_path

    def make_output_path(self, img_path) -> str:
        basename = os.path.basename(img_path)
        split_basename = os.path.splitext(basename)
        meme_filename = f'meme_{split_basename[0]}{split_basename[1]}'
        output_path = os.path.join(self.output_dir, meme_filename)
        return output_path

    @staticmethod
    def generate_text_position(width, height) -> tuple:
        position: Tuple[int, int] = (random.randint(4, int(width * 0.2)),
                                     random.randint(4, int(height * 0.8)))
        return position
