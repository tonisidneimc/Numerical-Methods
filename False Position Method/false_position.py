import math
import numpy

def false_position(f : type(lambda x : float), a, b : float, tol : float) -> float :

  assert(callable(f))

  if a >= b or tol <= 0 :
    raise ValueError("This procedure does not apply for a >= b or precision <= 0")
  elif abs(f(a)) <= tol or abs(f(b)) <= tol :
    if abs(f(a)) <= abs(f(b)) :
      return a
    else :
      return b
  elif numpy.sign(f(a)) == numpy.sign(f(b)) :
    raise RuntimeError("The given function has no root in the range")
  else :
    while abs(f(a)) > tol and abs(f(b)) > tol :
      p = (a*f(b) - b*f(a)) / (f(b) - f(a))
      y = f(p)
      
      if abs(y) <= tol :
        return p
      elif numpy.sign(f(a)) == numpy.sign(y) :
        a = p
      else :
        b = p

