from PIL import Image
import os


def encrypt_decrypt_image(image_path, key):

    try:

        # Check if file exists
        if not os.path.exists(image_path):
            print("\nFile not found!")
            print("Make sure the image is in the same folder as the Python file.")
            return

        image = Image.open(image_path)

        # Convert image to RGB
        image = image.convert("RGB")

        pixels = image.load()

        width, height = image.size

        # XOR each pixel
        for x in range(width):
            for y in range(height):

                r, g, b = pixels[x, y]

                pixels[x, y] = (
                    r ^ key,
                    g ^ key,
                    b ^ key
                )

        # Create output filename
        filename, extension = os.path.splitext(image_path)

        output_path = f"{filename}_processed{extension}"

        image.save(output_path)

        print("\nImage processed successfully!")
        print(f"Saved as: {output_path}")

    except Exception as e:
        print("\nError:", e)


def get_key():

    while True:

        try:

            key = int(input("Enter key (0-255): "))

            if 0 <= key <= 255:
                return key

            print("Key must be between 0 and 255.")

        except ValueError:
            print("Please enter a valid number.")


def main():

    print("\n===== Image Encryption Tool =====")

    print("\nCurrent Working Directory:")
    print(os.getcwd())

    image_path = input("\nEnter image filename: ").strip()

    key = get_key()

    encrypt_decrypt_image(image_path, key)


if __name__ == "__main__":
    main()
