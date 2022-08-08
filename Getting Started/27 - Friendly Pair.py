# Given two integer numbers as the input, the objective is to check whether or not the two numbers are Friendly pairs of each other. 

# Example
# Input : 6 28
# Output : Yes, they are a friendly pair

# The numbers whose ( sum of divisors ) / number ratio is same are known as Friendly Pair Numbers.

# Example
# Input : 6 28
# Output : Yes, they are a friendly pair
# Explanation : The factors of 6 and 28 except the numbers themselves are 1, 2, 3 and 1, 2, 4, 7, 14 respectively.
# Now the sum of factors of both the numbers are 6 and 28 respectively. 
# When we divide the sums with the numbers we get 1 and 1 respectively. 
# As the ratio of both the number match, they are considered as a friendly pair.

n , m = map(int,input("Give input = ").split())

def allfactors(n):
    factors = [1]
    for i in range(2, (n // 4) + 2):
        if n % i == 0 and i not in factors:
            factors.append(i)
            if (n // i) not in factors:
                 factors.append(n // i)
    return factors
def isFriendlyPair(num1,num2):
    sum1 = sum(allfactors(num1))
    sum2 = sum(allfactors(num2))
    if sum1/num1 == sum2/num2:
        return "Yes this number is a Friendly Pair"
    else:
        return "No it is not a Friendly Pair"

print(isFriendlyPair(n,m))
