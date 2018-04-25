class Ray(object):
    def __init__(self, origin, direction):
        self.origin = origin  # point
        self.direction = direction.normalized()  # vektor

    def __repr__(self):
        return 'Ray(%s,%s)' % (self.origin, self.direction)

    def pointAtParameter(self, t):
        return self.origin + self.direction.scale(t)