from src.util.MathUtil import MathUtility as math

class CheersUtility:

    #To calculate the value of alpha

    '''
    INPUT

    value_of_sin = Value of sin
    value_of_pi  = Value of pi

    '''
    def calAlpha(self,value_of_sin,value_of_pi):
        return value_of_pi/2+value_of_sin

     # To calculate the value of alpha

    '''
    INPUT

    value_of_alpha = value of angle made in between the two circle
    radius  = radius of Coaster

    '''

    def calLength(self, value_of_alpha, radius):
        obj=math();
        return 2*radius(1-obj.findCosine(value_of_alpha/2,11,5))