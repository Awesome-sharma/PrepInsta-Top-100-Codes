# HCF of Two Numbers also known as GCD (Greatest Common Divisor).

# x is called HCF of a & b two conditions :

# x can completely divide both a & b leaving remainder 0
# No, other number greater than x can completely divide both a & b

def findHCF(num1, num2):
    
    # Everything divides 0
    if num1 == 0 or num2 == 0:
        return num1 + num2
    
    # base case
    if num1 == num2:
        return num1
    
    # num1>num2
    if num1 > num2:
        return findHCF(num1 - num2, num2)
    else:
        return findHCF(num1, num2 - num1)


num1 = 36
num2 = 60

print("Hcf of", num1, "and", num2, "is", findHCF(num1, num2))
