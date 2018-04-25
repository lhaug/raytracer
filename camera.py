class Camera(object):

    def __init__(self, e, c, up):
        self.e = e  # punkt
        self.c = c  # punkt
        self.up = up  # vektor
        self.f = (c - e).normalized()  # vektor