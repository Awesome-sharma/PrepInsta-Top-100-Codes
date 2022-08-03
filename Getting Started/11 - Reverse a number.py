# Find the Reverse of a Number 
# Given an integer input the objective is to reverse the given integer number using loops and slicing. Therefore, we’ll write a program to Find the Reverse of a Number.

# Example
# Input : 123
# Output : 321

n = int(input("give = "))
# method 1

ans = ""
while n > 0:
  ans += str(n%10)
  n = n//10
print(ans)


# method 2

sn = str(n)
print(sn[::-1])

# method 3
ans = ""
for i in list(str(n)):
  ans = i + ans
print(ans)
