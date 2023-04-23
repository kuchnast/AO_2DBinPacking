
class Package2D:
    def __init__(self, w, h, with_rotation=False):
        self.with_rotation = with_rotation
        self.w = w
        self.h = h

    def rotate(self) -> None:
        self.w, self.h = self.h, self.w
