"""
Python OOP (Object-Oriented Programming) - Study Reference

Topics covered:
    1.  Class syntax and __init__
    2.  Instance attributes and instance methods
    3.  Class attributes
    4.  Class methods and static methods
    5.  Magic (dunder) methods
    6.  Inheritance (single, multiple, multilevel, hierarchical, overriding)
    7.  Polymorphism
    8.  Encapsulation (getters/setters, @property)
    9.  Abstraction (ABC)

Note: class names such as Person, Animal and Dog are reused across sections.
Each section is self-contained, so a later definition simply replaces the
earlier one.
"""

from abc import ABC, abstractmethod


#========================
# 1. Class Syntax
#========================
# __init__ runs automatically every time a new object is created.
class User:
    """Minimal class showing that __init__ runs on creation."""

    def __init__(self):
        print("Hello from class syntax.")


user1 = User()            # --> Hello from class syntax.
print(user1.__class__)    # --> <class '__main__.User'>


#========================
# 2. Instance Attributes
#========================
# Instance attributes belong to each object and are set through `self`.
class Person:
    """A person with a name and an age."""

    def __init__(self, name, age):
        self.name = name  # instance attribute
        self.age = age    # instance attribute


person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

print(person1.name, person1.age)  # --> Alice 30
print(person2.name, person2.age)  # --> Bob 25


#========================
# 3. Instance Methods
#========================
# Instance methods receive the object as their first argument (`self`).
class Person:
    """A person who can introduce themselves."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."


person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

print(person1.greet())  # --> Hello, my name is Alice and I am 30 years old.
print(person2.greet())  # --> Hello, my name is Bob and I am 25 years old.


#========================
# 4. Class Attributes
#========================
# A class attribute is shared by every instance (and by the class itself).
class Animal:
    """An animal with a shared `species` value."""

    species = "Mammal"  # class attribute

    def __init__(self, name, age):
        self.name = name  # instance attributes
        self.age = age


dog = Animal("Buddy", 5)
cat = Animal("Whiskers", 3)

print(dog.species)     # --> Mammal
print(cat.species)     # --> Mammal
print(Animal.species)  # --> Mammal


#========================
# 5. Class Methods
#========================
# @classmethod receives the class (`cls`) instead of an instance, so it can
# read/modify class state or act as an alternative constructor.
class MyClass:
    """Counts how many instances have been created."""

    class_variable = 0  # shared counter

    def __init__(self, value):
        self.instance_variable = value
        MyClass.class_variable += 1

    @classmethod
    def get_class_variable(cls):
        return cls.class_variable

    @classmethod
    def class_type(cls, genre):
        """Alternative constructor: builds an instance based on `genre`."""
        if genre == "simple":
            return cls(0)
        return cls(100)


obj1 = MyClass(1)
obj2 = MyClass(2)

print(MyClass.get_class_variable())  # --> 2
print(MyClass.class_type("simple"))  # --> <__main__.MyClass object at 0x...> (creates a 3rd instance)
print(obj1.get_class_variable())     # --> 3 (the counter is shared)
print(obj2.get_class_variable())     # --> 3


#========================
# 6. Static Methods
#========================
# @staticmethod takes neither `self` nor `cls`. Use it for utility functions
# that are related to the class but don't touch class or instance state.
class MathOperations:
    """Group of simple math helpers."""

    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def multiply(x, y):
        return x * y


print(MathOperations.add(5, 3))       # --> 8
print(MathOperations.multiply(5, 3))  # --> 15


#========================
# 7. Magic Methods (Dunder)
#========================
# __init__ : initializes a new instance
# __str__  : human-readable output (used by print() and str())
# __repr__ : detailed, unambiguous output (used by repr())
# __len__  : result of len(obj)
class Skills:
    """A container of skills that supports str(), repr() and len()."""

    def __init__(self):
        self.skills = ["python", "php", "javascript"]

    def __str__(self):
        return f"this is my skills now: {self.skills}"

    def __len__(self):
        return len(self.skills)

    def __repr__(self):
        return f"Skills({self.skills})"


profile = Skills()
print(str(profile))   # --> this is my skills now: ['python', 'php', 'javascript']
print(len(profile))   # --> 3
print(repr(profile))  # --> Skills(['python', 'php', 'javascript'])

# len() always reflects the current state of the list
profile.skills.append("html")
print(len(profile))   # --> 4


#========================
# 8. Inheritance - Single
#========================
# A child class inherits attributes and methods from its parent
# and can override them.
class Animal:
    """Parent class."""

    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."


class Dog(Animal):
    """Child class that overrides speak()."""

    def speak(self):
        return f"{self.name} barks."


animal = Animal("Generic Animal")
dog = Dog("Buddy")

print(animal.speak())  # --> Generic Animal makes a sound.
print(dog.speak())     # --> Buddy barks.


#========================
# 9. Inheritance - Multiple
#========================
# A class can inherit from more than one parent.
class Flyable:
    def fly(self):
        return "Flying"


class Swimmable:
    def swim(self):
        return "Swimming"


class Duck(Flyable, Swimmable):
    """Gets fly() and swim() from both parents."""


duck = Duck()
print(duck.fly())   # --> Flying
print(duck.swim())  # --> Swimming


#========================
# 10. Inheritance - Multilevel
#========================
# A child inherits from another child (Grandparent -> Parent -> Child).
# super() calls the next class up the chain.
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


#========================
# 11. Inheritance - Hierarchical
#========================
# Several children inherit from the same parent.
class Parent:
    def __init__(self, name):
        self.name = name


class Child1(Parent):
    pass


class Child2(Parent):
    pass


child1 = Child1("Child 1")
child2 = Child2("Child 2")
print(child1.name)  # --> Child 1
print(child2.name)  # --> Child 2


#========================
# 12. Method Overriding with super()
#========================
# The child extends __init__ (via super()) and overrides speak() with its own version.
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # reuse the parent's initialization
        self.breed = breed      # extra attribute only Dog has

    def speak(self):  # overrides Animal.speak()
        return f"{self.name} barks. Breed: {self.breed}"


dog = Dog("Buddy", "Golden Retriever")
print(dog.speak())  # --> Buddy barks. Breed: Golden Retriever


#========================
# 13. Polymorphism
#========================
# Different classes expose the same method name, so one loop works for all.
# The parent raises NotImplementedError to force children to implement speak().
class Animal:
    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


for animal in [Dog(), Cat()]:
    print(animal.speak())
# --> Woof!
# --> Meow!


#========================
# 14. Encapsulation - Getters & Setters
#========================
# A double underscore prefix (__marks) makes the attribute "private".
# Python mangles its name to _Student__marks, so it can't be reached as
# student.__marks. Access goes through methods that can validate the data.
class Student:
    """A student whose marks can only be changed through validation."""

    def __init__(self, name, marks):
        self.name = name        # public attribute
        self.__marks = marks    # private attribute

    def show_the_marks(self):  # getter
        return self.__marks

    def change_the_marks(self, new_marks):  # setter with validation
        if 0 <= new_marks <= 100:
            self.__marks = new_marks
            return f"The marks has been changed to: {new_marks}"
        return "The marks should be between 0 and 100"


student = Student("Ahmed", 85)

print(student.name)  # --> Ahmed

# Direct access to the private attribute fails.
# (The original code let this crash the script; try/except lets the rest run.)
try:
    print(student.__marks)
except AttributeError as error:
    print(f"AttributeError: {error}")  # --> AttributeError: ... no attribute '__marks'

print(student.show_the_marks())        # --> 85
print(student.change_the_marks(90))    # --> The marks has been changed to: 90
print(student.show_the_marks())        # --> 90


#========================
# 15. @property Decorator
#========================
# @property lets a method be read like an attribute (no parentheses).
class Member:
    """A member whose age in days is computed on demand."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        return f"Hello {self.name}"

    @property
    def age_in_days(self):
        return self.age * 365


man = Member("ahmed", 40)
print(man.age_in_days)  # --> 14600
# print(man.age_in_days())  # TypeError: 'int' object is not callable


#========================
# 16. @property with Encapsulation
#========================
# @property + @<name>.setter give clean attribute-style access
# (acc.balance) while still validating the value being set.
class BankAccount:
    """Account whose balance can't be set to a negative value."""

    def __init__(self):
        self.__balance = 0

    @property
    def balance(self):  # getter
        return self.__balance

    @balance.setter
    def balance(self, value):  # setter (negative values are silently ignored)
        if value >= 0:
            self.__balance = value


acc = BankAccount()
acc.balance = 1000
print(acc.balance)  # --> 1000


#========================
# 17. Abstraction (ABC)
#========================
# An abstract class can't be instantiated. Subclasses must implement every
# @abstractmethod, otherwise Python raises a TypeError.
class Animal(ABC):
    """Abstract base class."""

    @abstractmethod
    def make_sound(self):
        """Must be implemented by every subclass."""

    def sleep(self):  # regular method shared by all subclasses
        print("This animal is sleeping.")


class Dog(Animal):
    def make_sound(self):
        print("Woof! Woof!")


class Cat(Animal):
    def make_sound(self):
        print("Meow!")


dog = Dog()
dog.make_sound()  # --> Woof! Woof!
dog.sleep()       # --> This animal is sleeping.

cat = Cat()
cat.make_sound()  # --> Meow!
cat.sleep()       # --> This animal is sleeping.