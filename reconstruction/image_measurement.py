from PIL import Image
import os
import matplotlib.pyplot as plt
import numpy as np


def load_image(file_path):
    if not os.path.isfile(file_path):
        print(f"Error: File '{file_path}' does not exist.")
        return None

    try:
        img = Image.open(file_path)
        img.verify()

        img = Image.open(file_path)
        print(f"Image loaded successfully: {img.format}, {img.size}, {img.mode}")
        return img

    except (OSError, IOError) as e:
        print(f"Error: Unable to open image. {e}")
        return None


def display_image(img):
    fig, ax = plt.subplots()
    ax.imshow(img)
    ax.set_title("Click on two points")

    print("Please click on two points in the image.")
    points = plt.ginput(2, timeout=0)

    if len(points) < 2:
        print("Error: Two points were not selected.")
        return None

    p1, p2 = points

    ax.plot(
        [p1[0], p2[0]],
        [p1[1], p2[1]],
        marker="o"
    )

    px_d = pixel_distance(p1, p2)

    print(f"Point 1: {p1}")
    print(f"Point 2: {p2}")
    print(f"Pixel distance: {px_d:.2f} px")

    plt.show()

    return {
        "point_1": p1,
        "point_2": p2,
        "pixel_distance": px_d
    }


def pixel_distance(p1, p2):
    return np.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)