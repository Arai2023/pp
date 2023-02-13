
class Myclass:
    x = 5
print(Myclass)

class Myclass :
    x =5
p1 = Myclass()
print(p1.x)

#the _init_() function
class Person:
    def _init_(self , name , age) :
        self.name = name
        self.age = age
p1 = Person("John", 16)
print(p1.name)
print(p1.age)

#the __str__() function
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"    

p1 = Person("John", 36)

print(p1)

#object methods
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

#the self parameter
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()

#modify object proporities
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)

p1.age = 40

print(p1.age)

#the pass statement
class Person:
    pass

#exercises
class Myclass:
    x=5

class Myclass:
    x=5
p1 = Myclass()

class Myclass:
    x=5
p1 = Myclass()
print(p1.x)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age






