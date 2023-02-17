"""
Virtual proxy appears to be the fully initialized underlying object but in facts in masquerades underlying
functionality.
"Virtual" means that it appears like the object it's supposed to represent but behind the scenes it can offer
additional functionality and behaves differently.
"""


class Bitmap:
    def __init__(self, filename):
        self.filename = filename
        print(f"Loading image from {filename}")

    def draw(self):
        print(f"Drawing image {self.filename}")


class LazyBitmap:
    def __init__(self, filename):
        self.filename = filename
        self._bitmap = None  # instead of loading it when instantiating as above

    def draw(self):
        if not self._bitmap:  # loading happens only once (on first invocation)
            self._bitmap = Bitmap(self.filename)  # loads only when "draw" method is called
        self._bitmap.draw()


def draw_image(image):
    print("About to draw image")
    image.draw()
    print("Done drawing the image")


if __name__ == "__main__":
    # bmp = Bitmap("facepalm.jpg")
    # draw_image(bmp)

    bmp = LazyBitmap("facepalm.jpg")
    draw_image(bmp)
