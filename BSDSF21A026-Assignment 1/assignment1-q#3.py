from PIL import Image

def mirror_image(image_path, output_path):
    try:
        # Open the image and convert it to grayscale
        img = Image.open(image_path).convert('L')
    except FileNotFoundError:
        print(f"Error: The file {image_path} was not found.")
        return
    except UnidentifiedImageError:
        print(f"Error: The file {image_path} is not a valid image.")
        return

    # Save the grayscale image
    grayscale_path = output_path.replace(".jpg", "_grayscale.jpg")
    img.save(grayscale_path)
    
    # Get image dimensions
    width, height = img.size
    
    # Crop the lower half of the image
    lower_half = img.crop((0, height // 2, width, height))
    
    # Flip the lower half vertically to create a mirrored effect
    mirrored_upper_half = lower_half.transpose(Image.FLIP_TOP_BOTTOM)
    
    # Create a new image by pasting the mirrored upper half onto the original image
    img.paste(mirrored_upper_half, (0, 0))
    
    # Save the final mirrored image
    img.save(output_path)

# Example usage
image_path = input("Enter the path of the image: ")  # Provide a valid image path here
output_path = "mirrored_image.jpg"
mirror_image(image_path, output_path)

print(f"Mirrored image saved as {output_path}")
