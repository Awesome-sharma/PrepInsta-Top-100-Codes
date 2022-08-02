# Find the Greatest of the Two Numbers
# Given two integer inputs as number1 and number2, the objective is to find the largest among the two. Therefore we’ll write a code to Find the Greatest of the Two Numbers in Python Language.

# Example
# Input : 20 40
# Output : 40


num1 , num2 = map(int,input("give num1 and num2 = ").split())

if num1 == num2 :
  print("both are equal")
elif num1 > num2:
  print(num1," is greater")
else:
  print(num2, " is greater")
