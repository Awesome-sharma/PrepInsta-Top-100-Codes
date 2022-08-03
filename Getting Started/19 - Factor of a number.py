# Find the Factors of a Number.
# Given an integer Number as input, the objective is to search for all the factors of the Given integer input.
# Therefore, we write a program to Find the Factors of a Number,

# Example
# Input : 10
# Output : 2 5


def Divisors(n) :
    i = 1
    while i <= n :
        if (n % i==0) :
            print (i,end=" ")
        i = i + 1

n = int(input("Give input = "))
Divisors(n)
