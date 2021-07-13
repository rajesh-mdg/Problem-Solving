class Solution {
    public int findPeakElement(int[] nums) {
        int low = 1; 
        int high = nums.length-2;
        
        if(nums.length==1)                         // if the array contains only 1 element
            return 0;
        
        while(low<=high)
        {
            if((nums[low]>nums[low-1]) && (nums[low]>nums[low+1]))   // left end checking
                return low;
            if((nums[high]>nums[high-1]) && (nums[high]>nums[high+1]))    //right end checking
                return high;
            low++;
            high--;
        }
        if(nums[0]>nums[1])             // if the array is in decending order
            return 0;
        return nums.length-1;          // if the array is in asscending order
        
    }
}
