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

    print("Please click on two points in the image where a reference length is known.")
    points_ref = plt.ginput(2, timeout=0)

    if len(points_ref) < 2:
        print("Error: Two points were not selected.")
        return None

    p1, p2 = points_ref

    ax.plot(
        [p1[0], p2[0]],
        [p1[1], p2[1]],
        marker="o"
    )

    px_d = pixel_distance(p1, p2)

    print(f"Point 1: {p1}")
    print(f"Point 2: {p2}")
    print(f"Pixel distance: {px_d:.2f} px")

    ref_length = float(input("Enter length of measured object in feet: "))

    if ref_length <= 0:
        print("Error: Reference length must be positive.")
        return None

    length_per_pixel = ref_length/px_d

    print("Please click on two points marking beginning and end of skid marks:")

    points_skid = plt.ginput(2, timeout=0)

    if len(points_skid) < 2:
        print("Error: Two points were not selected.")
        return None

    p3, p4 = points_skid

    ax.plot(
        [p3[0], p4[0]],
        [p3[1], p4[1]],
        marker="x"
    )

    px_d2 = pixel_distance(p3, p4)

    print(f"Point 1: {p3}")
    print(f"Point 2: {p4}")
    skid_length = length_per_pixel * px_d2
    print(f"Reference pixel distance: {px_d:.2f} px")
    print(f"Scale: {length_per_pixel:.4f} ft/px")
    print(f"Skid distance: {px_d2:.2f} px -> {skid_length:.2f} ft")

    plt.show()

    return {
        "reference_points": (p1, p2),
        "reference_pixel_distance": px_d,
        "reference_length_ft": ref_length,
        "scale_ft_per_px": length_per_pixel,
        "skid_points": (p3, p4),
        "skid_pixel_distance": px_d2,
        "skid_length_ft": skid_length,
    }

def pixel_distance(p1, p2):
    return np.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)