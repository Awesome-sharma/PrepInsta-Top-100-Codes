# Strong number.
# In this program we will find whether a number is strong number.
# A Strong Number is a number whose sum of factorial digits is equal to the number itself.

# Ex:- number is 145

# 1! + 4! + 5! = 145 

# So it is a strong number.

def fact(n):
  ans = 1
  for i in range(2,n+1):
    ans *= i
  return ans

def isStrong(num):
  n = num
  s = 0
  while n!=0:
    a = n%10
    n = n//10
    s += fact(a)
  if s == num:
    return "\nIt is a Strong Number \n"
  else:
    return "It is not a Strong Number"


num = int(input("Give value = "))
print(isStrong(num))
    
