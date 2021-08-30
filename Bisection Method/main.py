from bisection import *
import numpy

if __name__ == "__main__" :
   
   def f_1(x) :
     return x**3 - 20*x**2
     
   print(bisection(f_1, 10, 40, 1.0e-15))
   
   def f_2(x) :
     return x**3 + 4*x**2 - 10
     
   print(bisection(f_2, 1.0, 2.0, 1.0e-4))
   
   def f_3(x) :
     return -x**2 + 1
     
   print(bisection(f_3, -1.0, 1.0, 1.0e-4))
   
   def f_4(x) :
     return -x**2
   
   try :
     # no roots in the interval
     y = bisection(f_4, 1.0, 2.0, 1.0e-4)
   except Exception as err:
     print(err)
   else :
     print(y)
     
   def f_5(x) :
     return x - 2**(-x)
     
   print(bisection(f_5, 0.0, 1.0, 1.0e-5))
   
   def f_6(x) :
     return x**3 - 25
     
   # approximated value for cubic root of 25
   print(bisection(f_6, 2.0, 3.0, 1.0e-5))
   
   def f_7(x) :
     return numpy.sin(x)
     
   print(bisection(f_7, -0.5, 1.5, 1.0e-5))
   print(bisection(f_7, -0.5, 1.5, 2))
   
   def f_8(x) :
     return x**2 - x
   
   try :
     # a >= b
     y = bisection(f_8, 1.0, 0.0, 1.0e-5) # interval error
   except Exception as err:
     print(err)
   else :
     print(y)
     
