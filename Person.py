from typing_extensions import Self


class Person:
    def __init__(self, name) -> None:
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}")


person1 = Person("John Smith")
print(person1.name)
person1.talk()
