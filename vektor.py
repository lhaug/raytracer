import math

class Vektor(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return "(%s, %s, %s)"%(self.x, self.y, self.z)

    def __add__(self, other):
        a = self.x + other.x
        b = self.y + other.y
        c = self.z + other.z
        return Vektor(a,b,c)

    def __sub__(self, other):
        a = self.x - other.x
        b = self.y - other.y
        c = self.z - other.z
        return Vektor(a,b,c)

    def __mul__(self, other):
        a = self.x * other.x
        b = self.y * other.y
        c = self.z * other.z
        return Vektor(a,b,c)

    def __div__(self, other):
        a = self.x / other.x
        b = self.y / other.y
        c = self.z / other.z
        return Vektor(a, b, c)

    def div(self, p):
        a = self.x / p
        b = self.y / p
        c = self.z / p
        return Vektor(a, b, c)

    def normalized(self):
        length = math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)
        return self.div(length)

    def cross(self, other):
        a = (self.y * other.z) - (self.z * other.y)
        b = (self.z * other.x) - (self.x * other.z)
        c = (self.x * other.y) - (self.y * other.x)
        return Vektor(a, b, c)

    def scale(self,t):
        a = self.x * t
        b = self.y * t
        c = self.z * t
        return Vektor(a, b, c)

    def dot(self,other):
        a = self.x * other.x
        b = self.y * other.y
        c = self.z * other.z
        return a+b+c