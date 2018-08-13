# drawing.py

# To try this example out, first install the Pillow image library by executing
# the following at a terminal prompt:
#    pip install pillow
#
# Documentation for the ImageDraw class is here:
#    https://pillow.readthedocs.io/en/3.3.x/reference/ImageDraw.html

from PIL import Image
from PIL import ImageDraw

WIDTH = 500
HEIGHT = 500

# Create a WIDTHxHEIGHT RGB (red-green-blue) image, initially all black, on which to draw
img = Image.new("RGB", (WIDTH, HEIGHT))

# Create a "drawing" object to draw on <img>
d = ImageDraw.Draw(img)

# Draw a network/mesh of thin gray lines in the upper-left corner
for i in range(0, HEIGHT, 10):
    d.line([(0, i), (WIDTH - i, 0)], fill="darkslategray")

# Draw a 3-pixel thick GREEN line from (0, 0) to (WIDTH, HEIGHT)
d.line([(0, 0), (WIDTH, HEIGHT)], fill="green", width=3)

# Draw a 2-pixel thick RED line from (WIDTH, 0) to (0, HEIGHT)
d.line([(WIDTH, 0), (0, HEIGHT)], fill="red", width=2)

# Draw a solid BLUE circle (radius 10 pixels) centered in the image
# Then draw a hollow ORANGE circle (radius 20 pixels) centered on that
cx = WIDTH // 2
cy = HEIGHT // 2
d.ellipse([(cx - 10, cy - 10), (cx + 10, cy + 10)], fill="blue")
d.ellipse([(cx - 20, cy - 20), (cx + 20, cy + 20)], outline="orange")

# Load an external image ("duck.png") into an Image object
# Then paste it into the main image 200 pixels to the left and 100 pixels above the center
# (When pasting, use the transparency information in the duck.png file as a "mask")
bird = Image.open("duck.png")
img.paste(bird, (cx - 200, cy - 100), mask=bird)

# Draw some bright text above the duck's head at coordinates (cx - 200, cy - 110)
d.text((cx - 200, cy - 110), "Quack!", fill="white")

# Save the image to disk as "demo.png"
img.save("demo.png")