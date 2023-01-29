#lists
thislist = ["apple" , "banana", "cherry"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
print(len(thislist))

list1 = ["apple", "banana", "cherry"]
list2 = [1,5,7,3, 9]
list3 = [True, False, False]
print(list1)
print(list2)
print(list3)


list4 = [3, "male", True , "hi"]
print(list4)


mylist = ["apple", "banana", "cherry"]
print(type(mylist))

thisislist = list(("banana", "apple", "cherry"))
print(thisislist)

#access items
thisislist = ["banana", "apple", "cherry"]
print(thisislist[1])

thisislist = ["banana", "apple", "cherry"]
print(thisislist[-1])

thisislist = ["banana", "apple", "cherry" , "kiwi", "mango", "orange"]
print(thisislist[2:5])

thisislist = ["banana", "apple", "cherry" , "kiwi", "mango", "orange"]
print(thisislist[:4])

thisislist = ["banana", "apple", "cherry" , "kiwi", "mango", "orange"]
print(thisislist[2:])

thisislist = ["banana", "apple", "cherry" , "kiwi", "mango", "orange"]
print(thisislist[-4 : -1])

thisislist = ["banana", "cherry", "apple"]
if "apple" in thisislist:  
 print("Yes,'apple' is in the fruits list")

#change list items
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = "blackcurrant", "watermelon"
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = "blackcurrant", "watermelon"
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = "watermelon"
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

#add list items
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "watermelon")
print(thislist)

thislist = ["apple", "banana", "cherry"]
tropical = ["papaya", "mango", "pineapple"]
thislist.extend(tropical)
print(thislist)


thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist) 

#remove list items
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#loop list
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)


thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])


thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1


thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

#comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"]
print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits]
print(newlist)


newlist = [x for x in range(10) if x < 5]
print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)

#sort list 
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)


thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

#copy list
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

#join lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print(list1)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)

#exercises
fruits = ["apple", "banana", "cherry"]
print(fruits[1])

fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"
print(fruits)

fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)

fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon")
print(fruits)

fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
print(fruits)

fruits = ["apple", "banana", "cherry"]
print(fruits[-1])

fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits [2:5])

fruits = ["apple", "banana", "cherry"]
print(len(fruits))


