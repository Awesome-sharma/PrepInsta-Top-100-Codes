# Find the sum of the Digits of a Number in Python
# Given an input the objective to find the Sum of Digits of a Number in Python. To do so we’ll first extract the last element of the number and then keep shortening the number itself.

# Example
# Input : number = 123
# Output : 6

num = list(input("give input = "))
ans = 0
for i in num:
  ans += int(i)
print(ans)
