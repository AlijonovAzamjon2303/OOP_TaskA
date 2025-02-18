from abc import ABC, abstractmethod

class Person(ABC):
    @abstractmethod
    def speak(self):
        ...


class English(Person):
    def speak(self):
        print("I can speak in English")

class Uzbek(Person):
    ...

e = English()
e.speak()
u = Uzbek()