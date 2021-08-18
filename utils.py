from PIL import Image, ImageDraw, ImageFont
import os
import logging


def generate_certificate(font, font_size, offset, color, image, name, output_folder):
    font = ImageFont.truetype(font, font_size)
    image = Image.open(image)
    drawer = ImageDraw.Draw(image)
    text_width, text_height = drawer.textsize(name, font)
    img_width, img_height = image.size

    # draw text to image
    drawer.text(
        ((img_width - text_width) / 2, ((img_height - text_height) / 2) - offset),
        name,
        fill=color,
        font=font,
    )

    output = f"{output_folder}/{name}.png"

    if os.path.exists(output):
        logging.info(f"{name}'s certifcate already exist. Replacing ...")

    image.save(output, "PNG")


def get_name_list(filename):
    with open(filename, mode="r") as file:
        names = file.read().splitlines()
        names_count = len(names)
        return names, names_count
