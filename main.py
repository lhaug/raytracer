import math


from camera import Camera
from raytracer import Raytracer
from triangle import Triangle
from vektor import Vektor
from plane import Plane
from sphere import Sphere
from ray import Ray

#t1 = Triangle(np.array([0, 0, -20]), np.array([5, 3, -20]), np.array([1, 3, -20]))
t1 = Triangle(Vektor(0, 0, -20), Vektor(5, 3, -20), Vektor(1, 3, -20), (0, 255, 0))
k1 = Sphere(Vektor(-100,1000,100),200000000000000, (0, 255, 0))
k2 = Sphere(Vektor(100,1000,100),200000000000000, (0, 0, 255))

objectlist = [k2] #dreiKugeln, eine Ebene, ein Dreieck

wRes = 100
hRes = 100
#Lichtquelle
light = Vektor(30, 30, 10)

fieldofview = math.radians(45)

#camera
e = Vektor(0, 1.8, 10)
c = Vektor(0, 3, 0)
up = Vektor(0, 1, 0)

cam = Camera(e, c, up)
raytray = Raytracer(objectlist, wRes, hRes, light, fieldofview, cam)
raytray.rayCastAlg()