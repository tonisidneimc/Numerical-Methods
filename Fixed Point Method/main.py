from fixed_point import *
import math

if __name__ == "__main__" :
  
  def g_1(x) :
    return 0.5 * math.sqrt(10 - x**3)
    
  print(fixed_point(g_1, 1.5, 1.0e-9, 30))
  
  def g_2(x) :
    return math.sqrt(10/(4+x))
    
  print(fixed_point(g_2, 1.5, 1.0e-9, 11))
  
  def g_3(x) :
    return x - (x**3 + 4*x**2 - 10)/(3*x**2+8*x)
    
  print(fixed_point(g_3, 1.5, 1.0e-9, 4))
