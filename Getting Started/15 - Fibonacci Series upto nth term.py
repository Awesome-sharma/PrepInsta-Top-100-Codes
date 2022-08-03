# Find the Fibonacci Series up to Nth Term.
# Given an integer as an input, the objective is to find the Fibonacci series until the number input as the Nth term.
# Therefore, we write a program to Find the Fibonacci Series up to Nth Term.

# Example
# Input : 4
# Output : 0 1 1 2



num = int(input("Give input = "))

a = 0
b = 1
print(a,end=" ")
print(b,end=" ")
while num > 2:
  c = a + b
  print(c,end=" ")
  a = b
  b = c
  num -= 1
