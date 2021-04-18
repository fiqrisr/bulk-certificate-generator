from image_drawer import draw_image


class CertificateGenerator:
    def __init__(
        self,
        font,
        font_size,
        font_color,
        image,
        name_list,
        offset,
        output_folder,
    ):
        self.font = font
        self.font_size = font_size
        self.font_color = font_color
        self.image = image
        self.name_list = name_list
        self.offset = offset
        self.output_folder = output_folder

    def generate(self):
        name_list_length = len(self.name_list)

        for line, name in enumerate(self.name_list):
            print(
                "({}/{}) Generate {} certificate".format(
                    line + 1, name_list_length, name
                )
            )
            draw_image(
                font=self.font,
                font_size=self.font_size,
                offset=self.offset,
                color=self.font_color,
                image=self.image,
                text=name,
                output_folder=self.output_folder,
            )

        print("\nDone!")