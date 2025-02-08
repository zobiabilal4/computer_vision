from PIL import Image, ImageDraw

def create_image_1(image_size, outer_box_size, inner_box_size):
    image = Image.new('RGB', (image_size, image_size), 'black')
    draw = ImageDraw.Draw(image)

    # Center the inner box
    outer_offset = (image_size - outer_box_size) // 2
    inner_offset = (image_size - inner_box_size) // 2

    # Draw the outer black box (though the background is black, it's already filled)
    draw.rectangle([outer_offset, outer_offset, outer_offset + outer_box_size, outer_offset + outer_box_size], fill='black')

    # Draw the inner white box
    draw.rectangle([inner_offset, inner_offset, inner_offset + inner_box_size, inner_offset + inner_box_size], fill='white')

    image.show()

# Example Usage
#create_image_1(400, 300, 150)  # Example parameters

def create_image_2(image_size, box_size, line_width):
    image = Image.new('RGB', (image_size, image_size), 'white')
    draw = ImageDraw.Draw(image)

    # Top-left box
    draw.rectangle([0, 0, box_size, box_size], fill='black')

    # Bottom-right box
    draw.rectangle([image_size - box_size, image_size - box_size, image_size, image_size], fill='black')

    # Draw lines between the two boxes
    draw.line([(box_size // 2, box_size // 2), (image_size - box_size // 2, image_size - box_size // 2)], fill='black', width=line_width)

    image.show()

# Example Usage
#create_image_2(400, 50, 5)  # Example parameters

def create_image_3(image_size, num_lines, line_width):
    image = Image.new('RGB', (image_size, image_size), 'white')
    draw = ImageDraw.Draw(image)

    # Calculate spacing between lines
    spacing = image_size // (num_lines + 1)

    # Draw vertical lines
    for i in range(1, num_lines + 1):
        x = i * spacing
        draw.line([(x, 0), (x, image_size)], fill='black', width=line_width)

    # Draw horizontal lines
    for i in range(1, num_lines + 1):
        y = i * spacing
        draw.line([(0, y), (image_size, y)], fill='black', width=line_width)

    image.show()

# Example Usage
#create_image_3(400, 5, 5)  # Example parameters

image_size = int(input("Enter the image size: "))
box_size = int(input("Enter the box size: "))
line_width = int(input("Enter the line width: "))
num_lines = int(input("Enter the number of lines: "))

create_image_1(image_size, box_size, box_size // 2)
create_image_2(image_size, box_size, line_width)
create_image_3(image_size, num_lines, line_width)
