# Find the Greatest of the Three Numbers
# Given three integer inputs the objective is to find the largest among them. Therefore we write a code to Find the Greatest of the Three Numbers in Python.

# Example
# Input : 20 30 10
# Output : 30


a,b,c = map(int,input("give a, b, c = ").split())

# method 1
if a == b == c:
  print("all numbers are equal")
elif a>b>c:
  print(a," is greater")
elif a<b>c:
  print(b," is greater")
else:
  print(c," is greater")


# method 2

print(max(a,b,c))
