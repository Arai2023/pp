import os
dir = "Nikhil"
location = "D:/Pycharm projects/GeeksforGeeks/Authors/"
path = os.path.join(location, dir)
os.remove(path)
print("% s has been removed successfully" % dir)
 