# A peak element is an element that is strictly greater than its neighbors.

# Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

# You may imagine that nums[-1] = nums[n] = -∞.

# You must write an algorithm that runs in O(log n) time.

 # Example 1:

# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index number 2.



#Code 1:

# class Solution:
#     def findPeakElement(self, nums):
#         return nums.index(max(nums))


#Code 2 Binary search:

class Solution:
    def findPeakElement(self, nums) -> int:
        low, high = 0, len(nums)-1
        while low < high:
            mid = low + int((high-low)/2)
            if nums[mid] < nums[mid+1]:
                low = mid+1
            else:
                high = mid
        return low

s  = Solution()
nums = [2,9,7,6,4]
print(s.findPeakElement(nums))
