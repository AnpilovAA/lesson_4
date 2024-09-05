from PIL import Image


image = "Merlyn_Monroe.png"


def extract_canals_from_img() -> object:
    with Image.open(image) as img:
        red, green, blue = img.split()
    return red, green, blue


def layers_displacement(*args) -> tuple:
    red, green, blue = args[0]

    coordinates = (25, 0, 696, 522)
    croped_blue_canal = blue.crop(coordinates)

    coordinates_red = (0, 0, 671, 522)
    croped_red_canal = red.crop(coordinates_red)

    red_layer = Image.blend(croped_blue_canal, croped_red_canal, 0.3)
    
    coordinates = (0, 0, 671, 522)
    croped_blue_canal = blue.crop(coordinates)

    coordinates_red = (25, 0, 696, 522)
    croped_red_canal = red.crop(coordinates_red)

    blue_layer = Image.blend(croped_blue_canal, croped_red_canal, 0.3)
   
    coordinates = (25, 0, 696, 522)
    croped_green_canal = green.crop(coordinates)
    coordinates_red = (0, 0, 671, 522)
    croped_red_canal = red.crop(coordinates_red)

    green_layer = Image.blend(croped_red_canal, croped_green_canal, 0.3)
    return red_layer, blue_layer, green_layer


def merge_all_layers(*args):
    red_layer, blue_layer, green_layer = args[0]
    super_image = Image.merge('RGB', (green_layer, blue_layer, red_layer))
    super_image.save(f"Style_{image.replace(".png", "_new")}.jpg")
    
    super_image.thumbnail((80, 80))
    super_image.save(f"thumbnail_{image.replace(".png", "_new")}.jpg")


if __name__ == "__main__":
    rgb = extract_canals_from_img()
    layers = layers_displacement(rgb)
    merge_all_layers(layers)
