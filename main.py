from PIL import Image


image = "Merlyn_Monroe.png"

pixel_size_for_cutting = 96

half_cutting_size = 96//2


def image_canals_split() -> object:
    with Image.open(image) as img:
        red, green, blue = img.split()
    return red, green, blue


def layers_displacement(*args) -> tuple:
    red, green, blue = args[0]
    
    red_layer = channel_cutting(red, 1)
    blue_layer = channel_cutting(blue, 0)
    
    coordinates = (half_cutting_size, 0, 696-half_cutting_size, 522)
    green_layer = green.crop(coordinates)
   
    return red_layer, blue_layer, green_layer


def channel_cutting(canal, key):
    cut_size = canal.size[0] - half_cutting_size
    cutted_left_right = canal.crop((half_cutting_size, 0, cut_size, 522))
    
    if key:
        coordinates = (pixel_size_for_cutting, 0, 696, 522)
        cutted_left_red_canal = canal.crop(coordinates)

        return Image.blend(cutted_left_red_canal, cutted_left_right, 0.3)
    else:
        cutting_blue_canal = 696-pixel_size_for_cutting
        coordinates = (0, 0, cutting_blue_canal, 522)
        cutted_rigth_blue_canal = canal.crop(coordinates)

        return Image.blend(cutted_rigth_blue_canal, cutted_left_right, 0.3)




def merge_all_layers(*args):
    red_layer, blue_layer, green_layer = args[0]
    super_image = Image.merge('RGB', (red_layer, green_layer, blue_layer))
    super_image.save(f"Style_{image.replace(".png", "_new")}.jpg")
    
    super_image.thumbnail((80, 80))
    super_image.save(f"thumbnail_{image.replace(".png", "_new")}.jpg")


if __name__ == "__main__":
    rgb = image_canals_split()
    layers = layers_displacement(rgb)
    merge_all_layers(layers)
