from PIL import Image, ImageDraw, ImageFont

# Load a font file
font_path = "c:/Users/alvin/code/python/code-camp/font.tff"
font = ImageFont.truetype(font_path, size=24)

# Create an image
image = Image.new("RGB", (200, 100), "white")
draw = ImageDraw.Draw(image)

# Draw text with the specified font
draw.text((10, 10), "Hello, world!", fill="black", font=font)

# Save or display the image
image.show()
