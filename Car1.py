#coding: euc-kr

class Car1:
    def __init__(self, speed, color, model):
        self.speed = speed
        self.color = color
        self.model = model

    def drive(self):
        self.speed = 60

dadCar = Car1(0, "silver", "A6")
momCar = Car1(1, 'white', '520d')
myCar = Car1(2, "blue", "E-Class")

dadCar.drive()

print(dadCar.speed)

print(momCar.speed)

print(myCar.speed)

print(myCar.color)

print(myCar.model)