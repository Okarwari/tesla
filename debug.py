

class Person:
    country = None

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self):
        print("hello world")


p = Person('stack', 12)
print(Person.__dict__)
print(p.__dict__)
print(hasattr(Person, 'say'))
print(hasattr(p, 'country'))

