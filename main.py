from certificate_generator import CertificateGenerator
import os
from configparser import ConfigParser


def main():
    config = ConfigParser()
    config.read("config.cfg")

    template = config.get("config", "template")
    name_list = config.get("config", "name_list")
    output_folder = config.get("config", "output_folder")
    font = config.get("font", "font")
    font_size = config.get("font", "font_size")
    font_color = config.get("font", "font_color")
    offset = config.get("font", "offset")

    if not os.path.exists(output_folder):
        os.mkdir(output_folder)

    with open(name_list, mode="r") as file:
        name_list = file.read().splitlines()

    generator = CertificateGenerator(
        font=font,
        font_size=int(font_size),
        font_color=font_color,
        image=template,
        name_list=name_list,
        offset=int(offset),
        output_folder=output_folder,
    )

    generator.generate()


if __name__ == "__main__":
    main()
