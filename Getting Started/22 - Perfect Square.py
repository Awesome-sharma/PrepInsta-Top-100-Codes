# Check for Perfect Square.
# Here on this page, we will learn how to Check for Perfect Square.
# We are given an integer number and need to print “True” if it is, otherwise “False”.

import math
n = int(input("give input = "))


def isPerfect(n):
  if n>0:
    s = int(math.sqrt(n))
    return "True" if n == s*s else "False"

print(isPerfect(n))
