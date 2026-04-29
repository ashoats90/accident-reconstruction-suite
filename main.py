from reconstruction.image_measurement import load_image, display_image
from reconstruction.braking import speed_from_skid

def main():
    file_path = input("Enter image path: ")

    img = load_image(file_path)

    if img is None:
        return

    result = display_image(img)

    if result is None:
        return

    print(result)

    skid_distance = result["skid_length_ft"]
    drag_factor = float(input("Enter estimate of drag factor: "))
    braking_efficiency = float(input("Enter estimate of braking efficiency: "))
    road_grade = float(input("Enter estimate of road grade: "))

    speed = speed_from_skid(skid_distance, drag_factor, braking_efficiency, road_grade)

    print(f"Estimated speed: {speed:.2f} mph")

if __name__ == "__main__":
    main()