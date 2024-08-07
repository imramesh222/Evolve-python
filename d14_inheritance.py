class Animal: 
    def __init__(self):
        print("I am a Tiger")  # This message is printed when an Animal instance is created.

    def eat(self):
        print("I can eat anything")  # This method prints a message when called.

class Dog(Animal):  # Dog class inherits from Animal
    def __init__(self):
        super().__init__()  # Calls the constructor of the parent class (Animal)
        print("I can eat dog food")  # This message is printed when a Dog instance is created.

    def speak(self):
        print("I can Bark")  # This method prints a message when called.

class Bird(Animal):  # Bird class inherits from Animal
    def __init__(self):
        super().__init__()  # Calls the constructor of the parent class (Animal)
        print("I am a Bird")  # This message is printed when a Bird instance is created.

# Creating instances and calling methods
a1 = Animal()
a1.eat()

a2 = Dog()
a2.speak()
