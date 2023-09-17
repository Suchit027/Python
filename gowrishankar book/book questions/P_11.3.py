import math


class ArcLength:
    def __init__(self, r, angle):
        self.radius = r
        self.angle = angle

    def cal(self):
        result = 2 * math.pi * self.radius * self.angle / 360
        print(result)


test = ArcLength(9, 75)
test.cal()