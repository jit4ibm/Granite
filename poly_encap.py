class Animal:
    def __init__(self, name):
        self.__name = name  # Private variable

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    def speak(self):
        return f"{self._Animal__name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self._Animal__name} says Meow!"

# Using both concepts
dog = Dog("Buddy")
cat = Cat("Whiskers")
print(dog.speak())
print(cat.speak())
