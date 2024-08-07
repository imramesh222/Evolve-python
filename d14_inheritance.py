class Animal: 
    def __init__(self):
        print("I am a Tiger")  # This message is printed when an Animal instance is created.

    def eat(self):
        print("I can eat anything")  # This method prints a message when called.

class Dog(Animal):  # Dog class inherits from Animal
    def __init__(self):
        super().eat()  # Calls the constructor of the parent class (Animal)
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


# # Comments on the Code
# Animal Class:

# The __init__ method prints "I am a Tiger" when an Animal instance is created.
# The eat method prints "I can eat anything" when called.
# Dog Class:

# Inherits from Animal.
# The __init__ method of Dog calls the __init__ method of Animal using super().__init__(), ensuring the base class is properly initialized.
# It prints "I can eat dog food" when a Dog instance is created.
# The speak method prints "I can Bark" when called.
# Bird Class:

# Inherits from Animal.
# The __init__ method of Bird calls the __init__ method of Animal using super().__init__(), ensuring the base class is properly initialized.
# It prints "I am a Bird" when a Bird instance is created.
# Creating Instances and Calling Methods:

# When a1 = Animal() is executed, it creates an instance of Animal and prints "I am a Tiger".
# When a1.eat() is called, it prints "I can eat anything".
# When a2 = Dog() is executed, it creates an instance of Dog, first prints "I am a Tiger" from the Animal constructor, then prints "I can eat dog food" from the Dog constructor.
# When a2.speak() is called, it prints "I can Bark".
# Overall Structure
# The structure demonstrates single inheritance correctly, where Dog and Bird are subclasses of Animal, inheriting its properties and methods. The use of super().__init__() ensures that the parent class's constructor is called, maintaining proper initialization.