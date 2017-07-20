from decimal import *

#function to calculate the factorial of given number.
def factorial(n):
    if n<1:
        return 1;
    else:
        return n * factorial(n-1);

#Function for rounding off number to specific point
def roundno(num, point):
    scale = 10 ** point;
    return int(num * scale) / scale;

# Calculating value of pi using chudnovskyBig algorithm
def chudnovskyBig(no_of_iteration_for_accuracy,round_of_true,round_off): #http://en.wikipedia.org/wiki/Chudnovsky_algorithm
    pi = 0;
    k = 0;
    while k < no_of_iteration_for_accuracy:
        pi += (Decimal(-1)**k)*(Decimal(factorial(6*k))/((factorial(k)**3)*(factorial(3*k)))* (13591409+545140134*k)/(640320**(3*k)));
        k += 1;
    pi = pi * Decimal(10005).sqrt()/4270934400;
    pi = pi**(-1);
    if round_of_true==1:
        return roundno(pi,round_off);
    else:
        return pi;

# Calculating sin value using tayler series
def sin2(x,n,rounding_upto):
    sine = 0;
    pi = chudnovskyBig(5);
    for i in range(n):
        sign = (-1)**i;
        y=x*(pi/180);
        sine = sine + ((y**(2.0*i+1))/factorial(2*i+1))*sign;
    return roundno(sine,rounding_upto)


