# Find the Sum of the Numbers in a Given Range
# Given two integer inputs as the range [ low , high ], the objective is to find the sum of the numbers that lay in the intervals given by the integer inputs. Therefore we’ll write a code to Find the Sum of the Numbers in a Given Range in Python Language.

# Example
# Input : 2 5
# Output : 14


low , high = map(int,input("give values = ").split())

# method 1
ans = 0
for i in range(low,high+1):
  ans += i
print(ans)


# method 2
print((int(high*(high+1)/2))-(int(low*(low-1)/2)))
