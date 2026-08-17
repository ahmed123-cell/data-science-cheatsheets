#-----------------------------------------------------------------------------------------------------------
# OOP (Object Oriented Programming) Class syntax
class user:
    def __init__(self):
        print("Hello from class syntax.")

person1= user() # --> Hello from class syntax.
print(person1.__class__)  # --> <class '__main__.user'>
#-----------------------------------------------------------------------------------------------------------
# OOP Instance Attributes
class Person:
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute

# Creating instances
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

print(person1.name, person1.age)  # --> Alice 30
print(person2.name, person2.age)  # --> Bob 25
#-----------------------------------------------------------------------------------------------------------
# OOP Instance Methods
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

# Creating instances
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

print(person1.greet())  # --> Hello, my name is Alice and I am 30 years old.
print(person2.greet())  # --> Hello, my name is Bob and I am 25 years old.
#-----------------------------------------------------------------------------------------------------------
# Class attribute
class Animal:

    species = "Mammal" # <-- class attribute

    def __init__(self, name, age):
        # Instance attributes
        self.name = name
        self.age = age

# Creating instances
dog = Animal("Buddy", 5)
cat = Animal("Whiskers", 3)

print(dog.species)  # --> Mammal
print(cat.species)  # --> Mammal
print(Animal.species)  # --> Mammal
#-----------------------------------------------------------------------------------------------------------
# Class and Static Method
# Class Method: Class Methods: Use @classmethod and cls to modify the class state.
class MyClass:
    class_variable = 0

    def __init__(self, value):
        self.instance_variable = value
        MyClass.class_variable += 1

    @classmethod
    def get_class_variable(cls):
        return cls.class_variable
    
    @classmethod
    def class_type(cls, genre):
        if genre == 'simple':
            return cls(0)
        else:
            return cls(100)

# Creating instances
obj1 = MyClass(1)
obj2 = MyClass(2)

print(MyClass.get_class_variable())  # --> 2
print(MyClass.class_type('simple'))  # --> object
print(obj1.get_class_variable())     # --> 3
print(obj2.get_class_variable())     # --> 3
#-----------------------------------------------------
# Static Methods: Use @staticmethod for utility functions that do not modify class or instance state.
class MathOperations:
    
    @staticmethod
    def add(x, y):
        return x + y
    
    @staticmethod
    def multiply(x, y):
        return x * y

# Calling static methods
print(MathOperations.add(5, 3))      # --> 8
print(MathOperations.multiply(5, 3)) # --> 15
#-----------------------------------------------------------------------------------------------------------
# Magic Methods (Dunder)

# __init__: Initializes a new instance of the class.
# __str__: Gives a human-readable output of the object.
# __repr__: Gives a detailed and unambiguous output of the object
# __len__: Returns the length of the container.

class skills:
    def __init__(self):
        self.skills= ["python", "php", "javascript"]

    def __str__(self):
        return f"this is my skills now: {self.skills}"
    
    def __len__(self):
        return len(self.skills)
    
    def __repr__(self):
        return f"skills({self.skills})"
    
profile= skills()
print(str(profile)) # --> this is my skills now: ["python", "php", "javascript"]
print(len(profile)) # --> 3
print(repr(profile)) # --> skills(["python", "php", "javascript"])

# Adding new skills
profile.skills.append("html") 
print(len(profile)) # --> 4
#-----------------------------------------------------------------------------------------------------------
# Inheritance
# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

# Child class
class Dog(Animal):
    def speak(self):
        return f"{self.name} barks."

# Creating instances
animal = Animal("Generic Animal")
dog = Dog("Buddy")

print(animal.speak())  # --> Generic Animal makes a sound.
print(dog.speak())     # --> Buddy barks.
#----------------------------------------------------------
# Multiple Inheritance
class Flyable:
    def fly(self):
        return "Flying"

class Swimmable:
    def swim(self):
        return "Swimming"

class Duck(Flyable, Swimmable):
    pass

duck = Duck()
print(duck.fly())   # --> Flying
print(duck.swim())  # --> Swimming
#----------------------------------------------------------
# Multilevel Inheritance: A child class inherits from another child class.
class Grandparent:
    def __init__(self, name):
        self.name = name

class Parent(Grandparent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

class Child(Parent):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

child = Child("Alice", 12, "7th Grade")
print(child.name)   # --> Alice
print(child.age)    # --> 12
print(child.grade)  # --> 7th Grade
#----------------------------------------------------------
# Hierarchical Inheritance: Multiple child classes inherit from the same parent class.
class Parent:
    def __init__(self, name):
        self.name = name

class Child1(Parent):
    pass

class Child2(Parent):
    pass

child1 = Child1("Child 1")
child2 = Child2("Child 2")
print(child1.name)  # Output: Child 1
print(child2.name)  # Output: Child 2
#----------------------------------------------------------
# Method Overriding by using super()
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed # --> method overriding

    def speak(self):
        return f"{self.name} barks. Breed: {self.breed}"

dog = Dog("Buddy", "Golden Retriever")
print(dog.speak())  # Output: Buddy barks. Breed: Golden Retriever
#-----------------------------------------------------------------------------------------------------------
# Polymorphism
class Animal:
    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# List of animals
animals = [Dog(), Cat()]

for animal in animals:
    print(animal.speak()) # Woof! \n Meow!
#-----------------------------------------------------------------------------------------------------------
# Getters & Setters (Encapsulation)
class Student:
    def __init__(self, name, marks):
        self.name = name  # public attribute
        self.__marks = marks  # private attribute
    
    def show_the_marks(self):  # <-- Getter 
        return self.__marks
    
    def change_the_marks(self, new_marks):  # <-- Setter
        if 0 <= new_marks <= 100:
            self.__marks = new_marks
            return f"The marks has been changed to: {new_marks}"
        
        else:
            return "The marks should be between 0 and 100"

student = Student("Ahmed", 85)

print(student.name) # --> Ahmed
print(student.__marks) # --> # Error (private attribute)
print(student.show_the_marks()) # --> 85

print(student.change_the_marks(90))
print(student.show_the_marks()) # --> 90
#-----------------------------------------------------------------------------------------------------------
# Property Decorator: It treats the method as an attribute
class member:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        return f"Hello {self.name}"
    
    @property
    def age_in_days(self):
        return self.age * 365
    
man= member("ahmed", 40)
print(man.age_in_days) # --> 14600
# print(man.age_in_days()) # Error TypeError
#-----------------------------------------------------------------------------------------------------------
# Using Property in Encapsulation
class BankAccount:
    def __init__(self):
        self.__balance = 0

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value >= 0:
            self.__balance = value
acc = BankAccount()

acc.balance = 1000
print(acc.balance)
#-----------------------------------------------------------------------------------------------------------
# Abstraction
from abc import ABC, abstractmethod

# Abstract base class
class Animal(ABC):
    @abstractmethod
    def make_sound(self):  # --> This method must be implemnted in all inheirted classed
        pass

    def sleep(self):
        print("This animal is sleeping.")

# Concrete class
class Dog(Animal):
    def make_sound(self):
        print("Woof! Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

# Using the classes
dog = Dog()
dog.make_sound()
dog.sleep()

cat = Cat()
cat.make_sound()
cat.sleep()