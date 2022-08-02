# Find the Sum of The First N Natural Numbers in Python
# Given an integer input the objective is to write a code to Find the Sum of First N Natural Numbers in C++. To do so we simply keep adding the value of the iter variable using a for loop.

# Example
# Input : num = 8
# Output : 36

num = int(input("give value = "))

# method 1
print(int(num*(num+1)/2))

# method 2
ans = 0
for i in range(1,num+1):
  ans += i
print(ans)
