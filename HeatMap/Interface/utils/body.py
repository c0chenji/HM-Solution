class Body:
    def __init__(self, x0, y0, w, h, topColor,bottomColor, probability, check, frame):
        self.x0=x0
        self.y0=y0
        self.w= w
        self.h=h
        self.topColor=topColor
        self.bottomColor= bottomColor
        self.probability = probability
        self.check = check
        self.frame = frame