# Date :  7-june-2021
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# input_arr  = list(input("enter the array: "))
# target = int(input("enter the target: "))

#Code 1:

input_arr = [2,85,7,11,15,85]
target = 170

output = []
length = len(input_arr)
for i in range(0,length):
    diff = target-input_arr[i]
    if input_arr[i] == target:
        print(input_arr.index(target))
        break
    if input_arr.__contains__(diff) and input_arr.index(diff) != i:
        print(i,input_arr.index(diff))
        break
    else:
        pass

#Code 2:

nums = [2,85,7,11,15,0]
target = 85

class Solution():
    def twoSum(self,nums,target):
        List = []
        length = len(List)
        for i in range(0,length):
            diff = target - nums[i]
            if nums[i] == target:
                List.append(i)
                print(List)
                break
            elif nums.__contains(diff) and nums.index(diff) != i:
                List.append(i)
                List.append(nums.index(diff))
                print(List)
                break
if __name__ == "__main__":
    s = Solution()
    s.twoSum(nums,target)
