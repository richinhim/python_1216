class Circle:

    def calcCir(self):
        print("원")
class  Rectangle:

    def calcRec(self):
        print("사각형")
class Sam:
    def calcSam(self):
        print("삼각형")
    
class Shape(Circle, Rectangle, Sam):
    def calcAres(self):
        Circle.calcCir()
        Rectangle.calcRec()
        Sam.calcSam()


objectSam = Shape()

objectSam.calcAres()