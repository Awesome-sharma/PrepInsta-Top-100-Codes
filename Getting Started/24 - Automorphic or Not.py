# Check Whether or Not the Number is an Automorphic Number.

# Given an integer input for a number, the objective is to check whether or not the number is Automorphic or not.

#A number whose square ends with the same number is known as an Automorphic number. 

# Example
# Input : 5
# Output : It's an Automorphic Number.

n = int(input("Give input = "))
    
# Method 1
def isAutomorphic(n):
  if (n*n)%10 == n%10:
    return "Number is Automorphic"
  return "it is not "

print(isAutomorphic(n))

# Method 2
def checkAutomorphic(n):
  return "Number is Automorphic" if n%10 in [0,1,5,6] else "it is not "   # 0,1,5,6 are the only integers with Automorphic propertry

print(checkAutomorphic(n))
