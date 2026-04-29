from reconstruction.image_measurement import load_image, display_image

def main():
    file_path = input("Enter image path: ")

    img = load_image(file_path)

    if img is None:
        return

    result = display_image(img)

    if result:
        print(result)


if __name__ == "__main__":
    main()