
from cgi import MiniFieldStorage
from pyexpat import model
from attr import s

from matplotlib.dates import YearLocator


class encapsulation:
    __name = None

    def __init__(self, name):
        self.__name = name

    def getname(self):
        return self.__name

e = encapsulation('name_place')
print(e.getname())

print('_______________')

class car(object):
    def __init__(self, model='rolls', year=1956): #can't be changed but from here
        self.__model=model
        self.__year=year 
       
    
    def cardetail(self):
        print('the car model is: %s'  %(self.__model))

    def velocity(self, speed):
        print('the speed is: %s' %(speed))

c = car()
print(c.cardetail())
print(c.velocity(45))