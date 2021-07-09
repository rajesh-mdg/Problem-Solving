
#Date : 06th-June-2021
#Problem 1 :

# Given an integer N, return any array that contains N elements who sum to zero. 
# Ex: Given the following N... N = 1, return [0] (1 number that sums to zero is 0 itself). 
# Ex: Given the following N... N = 2, return [-1, 1] (this is one possible solution).

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
