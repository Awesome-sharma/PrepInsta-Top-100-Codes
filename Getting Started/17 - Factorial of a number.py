# Factorial of a Number.
# Here we will discuss how to find the Factorial of a Number.

# Factorial of any number is the product of it and all the positive numbers below it for example factorial of 5 is 120

# Factorial of n (n!) = 1 * 2 * 3 * 4....n
# 5! = 1 x 2 x 3 x 4 x 5 = 120 7! = 1 x 2 x 3 x 4 x 5 x 6 x 7 = 5040



num = int(input("Give input = "))
ans = 1
for i in range (2,num+1):
  ans *= i
print(ans)
