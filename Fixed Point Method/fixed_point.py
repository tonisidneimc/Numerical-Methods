import math
import numpy

def fixed_point(g : type(lambda x : float), p0 : float, tol : float, n : int) -> float:
  assert(callable(g))

  i = 0
  while i <= n :
    p = g(p0)
    
    if abs(p - p0) < tol:
      return p
    i += 1
    p0 = p
    
  raise RuntimeError(f"The method has failed after {n} iterations")
  
