from PIL import Image
import numpy as np

# Fixed XOR value for encryption and decryption
FIXED_XOR_VALUE = 128

def validate_output_path(output_path):
    # Ensure the output path has a valid image extension
    valid_extensions = ['.png', '.jpg', '.jpeg', '.bmp', '.tiff']
    if not any(output_path.lower().endswith(ext) for ext in valid_extensions):
        # Default to .png if no valid extension is provided
        output_path += '.png'
    return output_path

def encrypt_image(image_path, output_path):
    image = Image.open(image_path)
    image_array = np.array(image)

    # Encrypt by applying a fixed XOR value
    encrypted_array = np.bitwise_xor(image_array, FIXED_XOR_VALUE)

    encrypted_image = Image.fromarray(encrypted_array.astype('uint8'))
    output_path = validate_output_path(output_path)
    encrypted_image.save(output_path)
    print(f"Encrypted image saved to {output_path}")

def decrypt_image(encrypted_path, output_path):
    encrypted_image = Image.open(encrypted_path)
    encrypted_array = np.array(encrypted_image)

    # Decrypt by applying the same fixed XOR value
    decrypted_array = np.bitwise_xor(encrypted_array, FIXED_XOR_VALUE)

    decrypted_image = Image.fromarray(decrypted_array.astype('uint8'))
    output_path = validate_output_path(output_path)
    decrypted_image.save(output_path)
    print(f"Decrypted image saved to {output_path}")

def swap_pixels(image_path, output_path):
    image = Image.open(image_path)
    image_array = np.array(image)

    # Get image dimensions
    height, width, _ = image_array.shape

    # Swap pixels horizontally
    for i in range(height):
        for j in range(0, width - 1, 2):
            # Swap pairs of pixels
            image_array[i, j], image_array[i, j + 1] = image_array[i, j + 1], image_array[i, j]

    swapped_image = Image.fromarray(image_array.astype('uint8'))
    output_path = validate_output_path(output_path)
    swapped_image.save(output_path)
    print(f"Image with swapped pixels saved to {output_path}")

def restore_swapped_pixels(swapped_path, output_path):
    swapped_image = Image.open(swapped_path)
    swapped_array = np.array(swapped_image)

    # Get image dimensions
    height, width, _ = swapped_array.shape

    # Swap pixels back
    for i in range(height):
        for j in range(0, width - 1, 2):
            # Swap pairs of pixels back to original
            swapped_array[i, j], swapped_array[i, j + 1] = swapped_array[i, j + 1], swapped_array[i, j]

    restored_image = Image.fromarray(swapped_array.astype('uint8'))
    output_path = validate_output_path(output_path)
    restored_image.save(output_path)
    print(f"Restored image saved to {output_path}")

def main():
    print("Image Encryption Tool")
    print("1. Encrypt Image")
    print("2. Decrypt Image")
    print("3. Swap Pixels")
    print("4. Restore Swapped Pixels")
    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        image_path = input("Enter the path of the image to encrypt: ")
        output_path = input("Enter the path to save the encrypted image: ")
        encrypt_image(image_path, output_path)

    elif choice == '2':
        encrypted_path = input("Enter the path of the encrypted image: ")
        output_path = input("Enter the path to save the decrypted image: ")
        decrypt_image(encrypted_path, output_path)

    elif choice == '3':
        image_path = input("Enter the path of the image to swap pixels: ")
        output_path = input("Enter the path to save the image with swapped pixels: ")
        swap_pixels(image_path, output_path)

    elif choice == '4':
        swapped_path = input("Enter the path of the image with swapped pixels: ")
        output_path = input("Enter the path to save the restored image: ")
        restore_swapped_pixels(swapped_path, output_path)

    else:
        print("Invalid choice! Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()