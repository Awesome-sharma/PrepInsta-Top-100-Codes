# Given an integer input as the number, the objective is to check whether or the given integer number is an Abundant Number or not. 

# A Number that is smaller than the sum of all it's factors except the number itself is known as an Abundant number.

# Example
# Input : Number = 12
# Output : Yes, It's an Abundant Number
# Explanation : The Factors for the number 12 are, 1, 2, 3, 4 and 6. We don't want to include the number itself.
# Now the sum of the factors except the number itself is :
# 1 + 2 + 3 + 4 + 6 = 16
# as the number 16>12 , the number itself.
# It's an abundant number.


n = int(input("Give input = "))

def isAbundant(n):
    factors = [1]
    for i in range(2, (n // 4) + 2):
        if n % i == 0 and i not in factors:
            factors.append(i)
            if (n // i) not in factors:
                factors.append(n // i)
    if sum(factors)>n:
        return factors,"Yes it is a Abundant"
    else:
        return factors,"No It is not a Abundant number"

print(isAbundant(n))
