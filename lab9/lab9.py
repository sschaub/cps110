# drawing.py

# To try this example out, first install the Pillow image library by executing
# the following at a terminal prompt:
#    pip install pillow
#
# Documentation for the ImageDraw class is here:
#    https://pillow.readthedocs.io/en/3.3.x/reference/ImageDraw.html

from PIL import Image
from PIL import ImageDraw
from PIL import ImageSequence
import math

WIDTH = 1024
HEIGHT = 800

class FlyingObject:
    def __init__(self, image: Image, x: int, y: int, speed: int, heading: int):
        self.x = x
        self.y = y
        self.speed = speed
        self.heading = heading
        self.image = image

    def move(self):
        self.y -= self.speed * math.sin(self.heading * math.pi / 180)
        self.x += self.speed * math.cos(self.heading * math.pi / 180)

    def draw(self, surface: Image):
        surface.paste(self.image, (round(self.x), round(self.y)), mask=self.image)


class AnimatedFlyingObject:
    def __init__(self, frames: list, x: int, y: int, speed: int, heading: int):
        self.x = x
        self.y = y
        self.speed = speed
        self.heading = heading
        self.frames = frames
        self.curFrame = 0

    def move(self):
        self.y -= self.speed * math.sin(self.heading * math.pi / 180)
        self.x += self.speed * math.cos(self.heading * math.pi / 180)

    def draw(self, surface: Image):
        image = self.frames[self.curFrame]
        surface.paste(image, (round(self.x), round(self.y)), mask=image)
        self.curFrame = (self.curFrame + 1) % len(self.frames)

def loadAnimatedGif(filename: str)-> list:
    animGif = Image.open(filename)

    frames = []
    for frame in ImageSequence.Iterator(animGif):
        rgbFrame = Image.new("RGBA", frame.size)
        rgbFrame.paste(frame)
        frames.append(rgbFrame)

    return frames

def loadImage(filename: str) -> Image:
    img = Image.open(filename)
    rgbFrame = Image.new("RGBA", img.size)
    rgbFrame.paste(img)
    return rgbFrame

def generateMovie(objects: list, filename: str):

    frames = []
    for i in range(100):
        frame = Image.new("RGBA", (WIDTH, HEIGHT))
        for fo in objects:
            fo.draw(frame)
            fo.move()
        frames.append(frame)

    frames[0].save(filename, save_all=True, duration=33, append_images=frames[1:])

if __name__ == "__main__":
    print("Generating movie...")

    cloudImage = loadImage("fluffy-cloud.jpg")
    wolfFrames = loadAnimatedGif("wolf-animated-gif-20.gif")
    flamingoFrames = loadAnimatedGif("flamingo-flying-2.gif")

    objects = [
        FlyingObject(cloudImage, 0, 20, 2, 0),
        AnimatedFlyingObject(wolfFrames, 700, 150, 20, 180)
        ]

    for i in range(0, 360, 45):
        objects.append(AnimatedFlyingObject(flamingoFrames, WIDTH / 2, HEIGHT / 2, 6, i))

    generateMovie(objects, "demo.gif")

    # launch viewer
    import subprocess, sys
    imageViewerFromCommandLine = {'linux':'eog',
                                  'win32':'explorer',
                                  'darwin':'open'}[sys.platform]
    subprocess.run([imageViewerFromCommandLine, 'demo.gif'])
    
