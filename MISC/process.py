from PIL import Image

# Load the image
image = Image.open("./brz.png")

# Get original dimensions
width, height = image.size

# Target size
target_width, target_height = 1360, 768

# Calculate cropping box
left = (width - target_width) // 2
top = (height - target_height) // 2
right = left + target_width
bottom = top + target_height

# Crop the center
cropped_image = image.crop((left, top, right, bottom))

# Save the cropped image
cropped_image.save("brz_cropped.png")