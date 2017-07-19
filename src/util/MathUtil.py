from decimal import *
from math import *

def factorial(n):
    if n<1:
        return 1
    else:
        return n * factorial(n-1);

def chudnovskyBig(no_of_iteration_for_accuracy): #http://en.wikipedia.org/wiki/Chudnovsky_algorithm
    pi = Decimal(0)
    k = 0
    while k < no_of_iteration_for_accuracy:
        pi += (Decimal(-1)**k)*(Decimal(factorial(6*k))/((factorial(k)**3)*(factorial(3*k)))* (13591409+545140134*k)/(640320**(3*k)))
        k += 1
    pi = pi * Decimal(10005).sqrt()/4270934400
    pi = pi**(-1)
    return pi;

# http://www.sanfoundry.com/python-program-find-sum-sine-series/
def sin2(x,n,rounding_upto):
    sine = 0
    pi = chudnovskyBig(5)
    for i in range(n):
        sign = (-1)**i
        y=x*(pi/180)
        sine = sine + ((y**(2*i+1))/factorial(2*i+1))*sign
    return round(sine,rounding_upto)

print sin2(30,11,2)


