
class Human:

    def create_Human(name, age):
        person = Human()
        person.name = name
        person.age = age

        return person

    def old(person):
        person.age += 1
        print("{}가 나이를 먹어서 {}살이 되었습니다.".
        format(person.name, person.age))

    def young(person):
        person.age -= 1
        print("{}가 과거로 돌아가 {}살이 되었습니다.".
              format(person.name, person.age))

person = Human.create_Human("짱구",10)

person.old()
person.young()
person.old()




