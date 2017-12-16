class HuMan:

    eyes  = 2
    nose = 1
    mouth = 1
    ears  = 2

    def eat(self):
        print("먹고 있다.")

    def sleep(self):
        print("자고 있다.")

    def hear(self):
        print("듣고 있다.")

class Man(HuMan):

    def walk(self):
        print("걷고 있다.")

kkw = Man()

kkw.hear()
kkw.walk()

print(kkw.nose)
print("")

www = HuMan()

www.eat()
#www.walk()



