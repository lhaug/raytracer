from PIL import Image

import numpy as np

from ray import Ray
from vektor import Vektor


class Raytracer(object):

    def __init__(self, objectlist, wRes, hRes, l, fieldofview, cam):

        self.objectlist = objectlist
        self.wRes = wRes
        self.hRes = hRes
        self.light = l
        self.fieldofview = fieldofview
        self.cam = cam
        self.height = 2 * np.tan(fieldofview / 2)
        self.width = (wRes / hRes) * self.height
        self.image = Image.new('RGB', (2, 3), (255, 255, 255))
        global BACKGROUND_COLOR
        BACKGROUND_COLOR = (255, 255, 255)

    def rayCastAlg(self):
        imageHeight = self.image.height
        imageWidth = self.image.width
        print(imageHeight, imageWidth)
        print(self.hRes, self.wRes)
        for x in range(imageWidth):
            for y in range(imageHeight):
                ray = self.calcRay(x, y)
                maxdist = float('inf')
                color = BACKGROUND_COLOR
                for object in self.objectlist:
                    hitdist = object.intersectionParameter(ray)
                    if hitdist:
                        if hitdist < maxdist:
                            maxdist = hitdist
                            color = object.colorAt(ray)
                self.image.putpixel((x, y), color)
        self.image.save("bild.png")
        print("bild erstellt")



    def calcRay(self,width,height):
        pixelWidth = width / (self.wRes-1)
        pixelHeight = height / (self.hRes-1)
        f = self.cam.f
        up = self.cam.up
        e = self.cam.e
        s = f.cross(up).normalized()
        u = s.cross(f)
        for y in range(self.hRes):
            for x in range(self.wRes):
                xcomp = s.scale(x*pixelWidth-width/2)
                ycomp = u.scale(y*pixelHeight-height/2)
                ray = Ray(e, f+xcomp+ycomp) #evtl mehrere strahlen pro pixel
        return ray