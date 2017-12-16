#coding: euc-kr

#다중상속
class ParentOne:
    def func(self):
        print("ParentOne의 함수 호출!")

class ParentTwo:
    def func(self):
        print("ParentTwo의 함수 호출!")

class Child(ParentOne, ParentTwo):
    def childFunc(self):
        ParentOne.func(self)
        ParentTwo.func(self)

objectChild = Child()

objectChild.childFunc()

objectChild.func()