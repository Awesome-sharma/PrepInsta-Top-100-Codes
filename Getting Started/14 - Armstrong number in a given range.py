# Find the Armstrong Number in a given Range.
# Given two integers high and low for limits as inputs, the objective is to write a code to Find the Armstrong Numbers in a given Interval.

# For Instance,
# Input : 150 160
# Output : 153

a = input("Give lower bound = ")
b = input("Give high bound = ")

def checkArmstrong(num):
  arm = 0
  for i in range(len(str(num))):
    arm += (int(num[i]) ** len(num))

  if num == str(arm):
    return True


for i in range(int(a),int(b)+1):
  if checkArmstrong(str(i)):
    print(i)
    break
  elif i == int(b):
    print("This range don't have any armstrong number")
  
