# Check Whether a Number is a Prime or Not
# Given an integer input the objective is to write a program to Check Whether a Number is a Prime or Not.

# Example
# Input : 11
# Output : 11 is a Prime



num = int(input("Give number = "))

sieve_prime = ["T"] * (num+1)
sieve_prime[0] = "F"
sieve_prime[1] = "F"



for i in range(2,num+1):
  if sieve_prime[i]=="T":
    for j in range(i*i,num+1,i):
      sieve_prime[j] = "F"



print("prime" if sieve_prime[-1]=="T" else "non prime")



