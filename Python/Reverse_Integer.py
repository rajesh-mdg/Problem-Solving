# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

# Example 1:

# Input: x = 123
# Output: 321
# Example 2:

# Input: x = -123
# Output: -321
# Example 3:

# Input: x = 120
# Output: 21
# Example 4:

# Input: x = 0
# Output: 0


#Code 1: 
class Solution(object):
    def reverse(self,n):
            o = ""
            if n > 0:
                s = "{}".format(n)
                for i in range(1,len(s)+1):
                    o += s[-i]
                    p = int(o)
            else:
                s = "{}".format(-n)
                for i in range(1,len(s)+1):
                    o += s[-i]
                    p = -1*int(o)
            return p if p<=(2**31 - 1) and p>(-(2**31)) else 0

S1 = Solution()
print(S1.reverse(-23433334))
