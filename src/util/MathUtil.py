from decimal import Decimal


class MathUtility:

    # function to calculate the factorial of given number.

    '''
    INPUT

    num=Number whose factorial is required

    '''
    def factorial(self,num):
        if num<1:
            return 1;
        else:
            return num * self.factorial(num-1);

    #Function for rounding off number to specific point
    '''
    INPUT
    
    num=Number to be roundoff
    point = Total number needed after decimal point
    
    '''
    def roundno(self,num, point):
        scale = 10 ** point;
        return int(num * scale) / scale;


    # Calculating value of pi using chudnovskyBig algorithm
    '''
    INPUT
    
    no_of_iteration_for_accuracy=No of iteration to be made for chudnovskyBig algorithm
    round_of_true = whether to round of the value of pi or not
    round_off = total digit in decimal
    
    '''
    def chudnovskyBig(self,no_of_iteration_for_accuracy,round_of_true,round_off): #http://en.wikipedia.org/wiki/Chudnovsky_algorithm
        pi = 0;
        k = 0;
        while k < no_of_iteration_for_accuracy:
            pi += (Decimal(-1)**k)*(Decimal(self.factorial(6*k))/((self.factorial(k)**3)*(self.factorial(3*k)))* (13591409+545140134*k)/(640320**(3*k)));
            k += 1;
        pi = pi * Decimal(10005).sqrt()/4270934400;
        pi = pi**(-1);
        if round_of_true==1:
            return self.roundno(pi,round_off);
        else:
            return pi;

    # Calculating sin value using tayler series

    '''
    INPUT
    
    degree=Cosine degree
    no_of_terms = no of terms to be calculated in tayler series
    rounding_upto = total digit in decimal
    
    '''

    def findSin(self,degree,no_of_terms,rounding_upto):
        sine = 0;
        pi = self.chudnovskyBig(5,1,5);
        for i in range(no_of_terms):
            sign = (-1)**i;
            y=degree*(pi/180);
            sine = sine + ((y**(2.0*i+1))/self.factorial(2*i+1))*sign;
        return self.roundno(sine,rounding_upto)

    #Calculating cos value using tayler series
    '''
    INPUT
    
    degree=Cosine degree
    no_of_terms = no of terms to be calculated in tayler series
    rounding_upto = total digit in decimal
    
    '''
    def findCosine(self,degree,no_of_terms,rounding_upto):
        cosx = 1
        sign = -1
        pi=self.chudnovskyBig(5,1,5);
        for i in range(2, no_of_terms, 2):
            y=degree*(pi/180)
            cosx = cosx + (sign*(y**i))/self.factorial(i)
            sign = -sign
        return self.roundno(cosx,rounding_upto)