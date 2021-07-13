
#Date : 06th-June-2021
#Problem 1 :

# Given an integer N, return any array that contains N elements who sum to zero. 
# Ex: Given the following N... N = 1, return [0] (1 number that sums to zero is 0 itself). 
# Ex: Given the following N... N = 2, return [-1, 1] (this is one possible solution).

# Example 1:

# Input: n = 5
# Output: [-7,-1,1,3,4]
# Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].

# Example 2:

# Input: n = 3
# Output: [-1,0,1]
# Example 3:

# Input: n = 1
# Output: [0]




#Code 1 :

# import random

# integer = int(input("enter the integer: "))
# arr = []

# while True:
#     v = random.randint(-1000,1000)
#     arr.append(v)
#     if len(arr) == integer and sum(arr) == 0:
#         print(arr)
#         break
#     elif len(arr) < integer:
#         continue
#     else:
#         arr.clear()

#Code 2:

def findNumbers(N):
     
    for i in range(1, N // 2 + 1):
         
        # Print 2 symmetric numbers
        print(i, end = ', ')
        print(-i, end = ', ')
         
    # Print a extra 0 if N is odd
    if N % 2 == 1:
        print(0, end = '')
     
# Driver code
if __name__=='__main__':
    N = 5
    findNumbers(N)
