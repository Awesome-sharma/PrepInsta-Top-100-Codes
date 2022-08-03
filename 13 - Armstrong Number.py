# Check Whether a Given Number is an Armstrong Number or Not.

# For a given integer the objective is to check whether or not the given integer is an Armstrong number or not. 
# The Armstrong number is briefly defined in the section below.

# Example
# Input : 371
# Output : It's an Armstrong Number

# Armstrong Number -- 371 = 3^3 + 7^3 + 1^3 = 371



num = input("Give input = ")

def checkArmstrong(num):
  arm = 0
  for i in range(len(str(num))):
    arm += (int(num[i]) ** len(num))
  if num == str(arm):
    return "it is Armstrong"
  else:
    return " it is not"

print(checkArmstrong(num))
