#coding: euc-kr

class Car:
    def drive(self):
        self.speed = 60

    def __init__(self, speed, color, model):
         self.speed = speed
         self.color = color
         self.model = model


myCar = Car(0, "blue", "E-Class")
#
# myCar.speed = 0
#
# myCar.color = "blue"
# myCar.model = "E-Class"
# myCar.year = "2017"


print("�ڵ��� ��ü�� �����Ͽ����ϴ�.")

print("�ڵ����� �ӵ���", myCar.speed)

print("�ڵ����� ������ ", myCar.color)
print("�ڵ����� ���� ", myCar.model)

print("�ڵ����� �����մϴ�.")

myCar.drive()

print("�ڵ����� �ӵ��� ", myCar.speed)

