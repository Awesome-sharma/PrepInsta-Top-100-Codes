# Check Whether or Not a Number is a Harshad.
  
# Given an integer input the objective is to check whether or not the given number is a Harshad Number or not. To do so we’ll check if the sum of the digits can perfectly divide the number or not.

# A Number that is divisible by the sum of it's digits is known as a Harshad number.

# Example
# Input : 21
# Output : Yes It's a Harshad Number

n = int(input("Give Input = "))

def isHarshad(n):
  num = n
  total = 0
  while num != 0:
    total  += num % 10
    num //=10
  if n % total ==0:
    return "Yes It's a Harshad Number"
  return "It is not a Harshad Number"

print(isHarshad(n))
