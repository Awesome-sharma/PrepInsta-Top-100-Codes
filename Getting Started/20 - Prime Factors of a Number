# Find the Prime Factors of a Number.
# Given an integer input as the number, the objective is to Find all the Prime Factors of a the given integer input number. Therefore, we’ll write a program to Find the Prime Factors of a Number.

# Example
# Input : 10
# Output : 2 5


num = int(input("give input = "))
def PrimeFactors(num):
  if num < 4: # 3 and 2 are the only prime factor of themselves
        return num
  n = num//2
  ans = []
  sp = ["T"]*(n+1)
  sp[0],sp[1]="F","F"
  for i in range(2,n+1):
    if sp[i]=="T":
      if num%i==0:
        ans.append(i)
      for j in range(i*i,n+1,i):
        sp[j]="F"
  return ans
print(PrimeFactors(num))
