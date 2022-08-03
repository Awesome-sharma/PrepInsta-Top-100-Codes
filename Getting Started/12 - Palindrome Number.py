# Check Whether or Not the Number is a Palindrome.
# Given an integer number as an input, the objective is to check Whether or not the number is a palindrome. Therefore, we write a code to Check Whether or Not the Number is a Palindrome.

# Example
# Input : 1221
# Output : Palindrome

num = int(input("give number = "))

def method1(num):
  num = str(num)
  pnum = num[::-1]
  return "Palindrome" if num == pnum else "Not Palindrome"
print("Method 1 = ",method1(num))

def method2(num):
  n = num
  pnum = ""
  while n>0:
    pnum += str(n%10)
    n = n//10
  return "Palindrome" if int(num) == int(pnum) else "Not Palindrome"
print("Method 2 = ",method2(num))

def method3(num):
  n = str(num)
  for i in range(len(n)//2):
    if n[i]==n[(len(n)-(1+i))]:
      continue
    else:
      return "Not Palindrome"
  return "Palindrome"
print("Method 3 = ",method3(num))
    
