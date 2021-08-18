import os
from configparser import ConfigParser
import logging
from utils import generate_certificate, get_name_list


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
    log_output = "log.txt"

    logging.basicConfig(level=logging.INFO,
                        format="%(levelname)s - %(message)s",
                        handlers=[
                            logging.FileHandler(log_output, mode="w"),
                            logging.StreamHandler()
                        ])

    if not os.path.exists(output_folder):
        os.mkdir(output_folder)

    names, names_count = get_name_list(name_list)

    for line, name in enumerate(names):
        logging.info(
            f"({line + 1}/{names_count}) Generate {name}'s certificate")

        try:
            generate_certificate(
                font=font,
                font_size=int(font_size),
                offset=int(offset),
                color=font_color,
                image=template,
                name=name,
                output_folder=output_folder)
        except Exception as e:
            logging.error(f"Error while generate certificate: {e}")

    logging.info("Done")


if __name__ == "__main__":
    main()
