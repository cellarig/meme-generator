"""Handling image manipulation and drawing text on the image.

Consuming Pillow module to handle image resizing, loading font and
drawing text on the image
"""
import random
import os
from typing import Tuple
from PIL import Image, ImageDraw, ImageFont

text_font_path = './fonts/RobotoMono-Regular.ttf'
author_font_path = './fonts/RobotoMono-Italic.ttf'


def draw_word_wrap(draw, text, position, max_width,
                   font=ImageFont.truetype(text_font_path, 22),
                   fill='black') -> int:
    """Draw the given ``text`` to the x and y position of the image.

    Use the minimum length word-wrapping algorithm to restrict the text to
    a pixel width of ``max_width.``
    """
    x_pos, y_pos = position
    text_size_x, text_size_y = draw.textsize(text, font=font)
    remaining = max_width
    space_width, space_height = draw.textsize(' ', font=font)
    # use this list as a stack, push/popping each line
    output_text = []
    # split on whitespace...
    for word in text.split():
        word_width, word_height = draw.textsize(word, font=font)
        if word_width + space_width > remaining:
            output_text.append(word)
            remaining = max_width - word_width
        else:
            if not output_text:
                output_text.append(word)
            else:
                output = output_text.pop()
                output += ' %s' % word
                output_text.append(output)
            remaining = remaining - (word_width + space_width)
    for txt in output_text:
        draw.text((x_pos, y_pos), txt, font=font, fill=fill,
                  stroke_width=2, stroke_fill='white')
        y_pos += text_size_y
    return y_pos


class MemeGenerator:
    """A class that responsible for image manipulation.

    Handles loading, resizing image and drawing text on the image.
    """

    def __init__(self, output_dir):
        """Construct a meme generator with given path for output image."""
        self.output_dir = output_dir

    def make_meme(self, img_path, text, author, width=500) -> str:
        """Create a meme, a loaded picture with a specify quote.

        Arguments:
            img_path {str} -- the file location for the input image.
            text {str} -- the desired text which will be drawn
                          on the input image.
            author {str} -- author of the drawn text
            width {int} -- The pixel width value. Default=500.
        Returns:
            str -- the file path to the output meme.
        """
        with Image.open(img_path) as im:
            im = self.resize_image(im, width)
            draw = ImageDraw.Draw(im)
            self.add_text(draw, im, text, author)
            output_path = self.make_output_path(img_path)
            im.save(output_path)
        return output_path

    def make_output_path(self, img_path) -> str:
        """Create the output path for the generated image."""
        basename = os.path.basename(img_path)
        split_basename = os.path.splitext(basename)
        meme_filename = f'meme_{split_basename[0]}{split_basename[1]}'
        output_path = os.path.join(self.output_dir, meme_filename)
        return output_path

    @staticmethod
    def resize_image(img, width=500) -> object:
        """Resize the image by given pixel width."""
        ratio = width / float(img.size[0])
        height = int(ratio * float(img.size[1]))
        img = img.resize((width, height), Image.NEAREST)
        return img

    @staticmethod
    def add_text(draw, img, text, author) -> None:
        """Put quote on the image with loaded fonts."""
        position = (random.randint(4, int(img.size[0] * 0.2)),
                    random.randint(4, int(img.size[1] * 0.8)))

        text_author = f'- {author}'
        max_width = int(0.75 * img.size[0])
        last_y_pos = draw_word_wrap(draw, text, position, max_width)
        draw.text((position[0], last_y_pos),
                  text_author,
                  font=ImageFont.truetype(author_font_path, 18),
                  fill='black')
