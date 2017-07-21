from src.util.MathUtil import MathUtility

class Coaster:
    def __init__(self,radius):
        self.__radius=radius;

    def getRadius(self):
        return self.__radius;

    def getArea(self):
        obj=MathUtility();
        return obj.chudnovskyBig(15)*self.__radius*self.__radius

    def getPerimeter(self):
        obj=MathUtility();
        return 2*obj.chudnovskyBig(15)*self.__radius