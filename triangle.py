class Triangle(object):
    def __init__(self, a, b, c, color):
        self.a = a  # point
        self.b = b  # point
        self.c = c  # point
        self.u = self.b - self.a  # direction vektor
        self.v = self.c - self.a  # direction vektor
        self.color = color #rgb

    def __repr__(self):
        return 'Triangle(%s, %s,%s)' % ((self.a), (self.b), (self.c))

    def intersectionParameter(self, ray):
        w = ray.origin - self.a
        dv = ray.direction.cross(self.v)
        dvu = dv.dot(self.u)
        if dvu == 0.0:
            return None
        wu = w.cross(self.u)
        r = dv.dot(w) / dvu
        s = wu.dot(ray.direction) / dvu
        if 0 <= r and r <= 1 and 0 <= s and s <= 1 and r + s <= 1:
            return wu.dot(self.v) / dvu
        else:
            return None

    def normalAt(self, p):
        return (self.u.cross(self.v)).normalized()

    def colorAt(self,ray):
        return self.color