from abc import ABC, abstractmethod
import math
class shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass
    @abstractmethod
    def calculate_perimeter(self):
        pass
class circle(shape):
    def __init__(self,radius):
        self.__radius=radius
    def calculate_area(self):
        return math.pi *self.__radius**2
    def calculate_perimeter(self):
        return  2 * math.pi *self.__radius
class ractangle(shape):
    def __init__(self,heigth,width):
        self.__heigth=heigth
        self.__width=width
    def calculate_area(self):
        return self.__heigth *self.__width
    def calculate_perimeter(self):
        return 2* (self.__heigth +self.__width)
Circle =circle(5)
print(Circle.calculate_area())
print(Circle.calculate_perimeter())
Ractangle=ractangle(10,20)
print(Ractangle.calculate_area())
print(Ractangle.calculate_perimeter())