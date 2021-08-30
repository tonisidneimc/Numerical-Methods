import math
import numpy

def bisection(f : type(lambda x : float), a, b : float, tol : float) -> float :

  assert(callable(f))

  if a >= b or tol <= 0 :
    raise ValueError("This procedure does not apply for a >= b or precision <= 0")
  elif f(a) == 0.0 :
    return a
  elif f(b) == 0.0 :
    return b
  elif numpy.sign(f(a)) == numpy.sign(f(b)) :
    raise RuntimeError("The given function has no root in the range")
  else :
    # theoretical estimate of the number of iterations
    n = int(math.ceil(math.log((b-a)/tol)/math.log(2))) + 1
    
    i = 1
    while i <= n :
      p = (a + b)/2
      y = f(p)
      
      if y == 0.0 or ((b-a)/2) < tol :
        return p
      elif numpy.sign(f(a)) == numpy.sign(y) :
        a = p
      else :
        b = p
      i += 1
    
    return p
