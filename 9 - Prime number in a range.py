# Find the Prime Numbers in a Given Range
# Given two integer as Limits, low and high, the objective is to write a code to in Python Find Prime Numbers in a Given Range in Python Language. To do so we’ll use nested loops to check for the Prime while Iterating through the range.
# Example
# Input : low = 2 , high = 10
# Output : 2 3 5 7


low , high = map(int,input("give range = ").split())

sp = ["T"] * (high+1)
sp[0],sp[1]="F","F"

for i in range(2,high+1):
  if sp[i]=="T":
    for j in range(i*i,high+1,i):
      sp[j]="F"

for i in range(len(sp)):
  if sp[i]=="T":
    print(i,end=" ")
