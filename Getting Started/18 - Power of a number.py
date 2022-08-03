# Find the Power of a Number.
# Given two integer input numbers, the objective is to find the power of the number raise to the power variable.
# Therefore, we’ll write a code to Find the Power of a Number.

# Example
# Input : 2 3
# Output : 8

num , pw = map(int,input("Give number and power = ").split())
print() #for an empty line


def using_for_loop(num,pw):
  ans = 1
  for i in range(1,pw+1):
    ans *= num
  return ans
print("using_for_loop =",using_for_loop(num,pw))
print()


def using_while_loop(num,pw):
  ans = 1
  while pw>0:
    ans *= num
    pw -= 1
  return ans

print("using_while_loop =",using_while_loop(num,pw))
print()


def using_Recursion(num,pw,ans):
  if pw==1:
    return ans*num
  return using_Recursion(num,pw-1,ans*num)

print("using_Recursion =",using_Recursion(num,pw,1))
print()


print("using operator",num,"**",pw,"=",num**pw)
