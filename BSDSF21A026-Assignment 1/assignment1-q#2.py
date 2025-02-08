from PIL import Image, ImageDraw

def create_colored_corner_boxes(image_size):
    # Create a white image
    image = Image.new('RGB', (image_size, image_size), 'white')
    draw = ImageDraw.Draw(image)

    # Box size is 1/10th of the image size
    box_size = image_size // 10

    # Coordinates for the four boxes
    boxes = [
        ((0, 0), 'black'),  # Top-left corner
        ((image_size - box_size, 0), 'blue'),  # Top-right corner
        ((0, image_size - box_size), 'green'),  # Bottom-left corner
        ((image_size - box_size, image_size - box_size), 'red')  # Bottom-right corner
    ]

    # Draw each box on the image
    for (x, y), color in boxes:
        draw.rectangle([x, y, x + box_size, y + box_size], fill=color)

    # Display the image
    image.show()

# Example usage
image_size = int(input("Enter the image size (e.g., 400): "))
create_colored_corner_boxes(image_size)
