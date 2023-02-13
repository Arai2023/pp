#calling a function
def my_function():
    print("Hello from a function")
my_function()

#arguments
def my_function(fname):
    print(fname + "Refsnes")
my_function("Emil")
my_function("Tobias")
my_function("Linus")

#number of arguments
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")

#arbitrary arguments, *args
def my_function(*kids):
    print("My youngest child is " + kids[2])
my_function("Karl", "Tobias", "Linus")

#keyword arguments
def my_function(child3, child2, child1):
    print("The youngest child is " + child3)
my_function(child3 = "Tobias", child2 = "Emily", child3 = "Linus")

#arbitrary keyword arguments, **kwargs
def my_function(**kid):
    print("His last name is " + kid["lname"])
my_function(fname = "Tobias", lname = "Refsnes")

#default parameter value
def my_function(country = "Norway"):
    print("I am from " + country)
my_function("Kazakhstan")
my_function("USA")
my_function()
my_function("Vietnam")

#passing a list as an argument
def my_function(food):
    for x in food:
        print(x)
fruits = ["apple", "banana", "cherry"]
my_function(fruits)

#return values
def my_function(x):
    return 5*x
print(my_function(3))
print(my_function(5))
print(my_function(9))

#the pass statement
def myfunction():
  pass

#recursion
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)

#exercises
def my_function():
    print("Hello from a function")


def my_function():
  print("Hello from a function")
my_function()

def my_function(fname, lname):
    print(fname)

def my_function(x):
    return x+5

def my_function(*kids):
    print("The youngest child is " + kids[2])

def my_function(**kid):
    print("His last name is " + kid["lname"])

