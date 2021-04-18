from PIL import Image, ImageDraw, ImageFont
import os


def draw_image(font, font_size, offset, color, image, text, output_folder):
    font = ImageFont.truetype(font, font_size)
    image = Image.open(image)
    drawer = ImageDraw.Draw(image)
    text_width, text_height = drawer.textsize(text, font)
    img_width, img_height = image.size

    # draw text to image
    drawer.text(
        ((img_width - text_width) / 2, ((img_height - text_height) / 2) - offset),
        text,
        fill=color,
        font=font,
    )

    output = "{}/{}.png".format(output_folder, text)

    if os.path.exists(output):
        print("{}'s certifcate already exist. Replacing ...".format(text))

    image.save(output, "PNG")
