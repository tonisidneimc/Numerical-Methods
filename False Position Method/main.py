from false_position import *

if __name__ == "__main__" :
  def f_1(x) :
    return x**3 - 20*x**2
  
  print(false_position(f_1, 10, 40, 1.0e-5))
