# Check Whether or Not the Number is a Perfect Number.
# Given an integer input as a number, the objective is to check whether or not a number is a Perfect Number.

# Therefore, we write a program to Check Whether or Not the Number is a Perfect Number in Python Language.

# A Number that can be represented as the sum of all the factors of the number is known as a Perfect Number.

# Example
# Input : 28
# Divisors : [1, 2, 4, 7, 14]
# Sum = 1 + 2 + 4 + 7 + 14 = 28
# Output : It's a Perfect Number


num = int(input("give input = "))

def isPerfect(n):
  t = 0
  for i in range(1,(n//2)+1):
    if n%i==0:
      t+=i
      print(t,i)
  if t == n:
    return "yes"
  else:
    return "no"


isPerfect(num)
