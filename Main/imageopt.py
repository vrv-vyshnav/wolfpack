from pillow import *

class image_opt:
    
    def thumbnail(self):
        with image
        img = Image.open(self.path)
        img.thumbnail((100, 100))
        img.save(self.path, "JPEG")