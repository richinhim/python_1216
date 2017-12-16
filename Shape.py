class Circle:

    def calcCir(self):
        a = 1
        return a
class  Rectangle:

    def calcRec(self):
        b = 2
        return b
class Sam:
    def calcSam(self):
        c = 3
        return c

class Shape(Circle, Rectangle, Sam):
    def calcAres(self):
        print("원의 면적:" , Circle.calcCir())
        print("사각형의 면적:",  Rectangle.calcRec())
        print("삼각형의 면적:" ,  Sam.calcSam())


objectSam = Shape()

objectSam.calcAres()