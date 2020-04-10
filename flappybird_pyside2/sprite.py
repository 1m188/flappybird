from PySide2.QtGui import QPixmap


# sprite basic class
class Sprite:
    def __init__(self, image: QPixmap):
        self.image = image
        self.x = 0
        self.y = 0

    @property
    def spriteImg(self):
        return self.image

    @spriteImg.setter
    def spriteImg(self, val: QPixmap):
        self.image = val

    @property
    def width(self) -> int:
        return self.image.width()

    @property
    def height(self) -> int:
        return self.image.height()

    @property
    def x(self):
        return self.x

    @x.setter
    def x(self, val):
        self.x = val

    @property
    def y(self):
        return self.y

    @y.setter
    def y(self, val):
        self.y = val

    # 每一帧的变化
    def update(self):
        pass
