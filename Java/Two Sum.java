class Solution {
    public int[] twoSum(int[] nums, int target) {
        if(nums == null || nums.length == 0) {
        	return new int[0];
        }
        
        Map<Integer, Integer> map = new HashMap<>();
        
        for(int i =0; i < nums.length; i++) {
        	int n2 = target - nums[i];
        	if(map.containsKey(n2)) {
        		return new int[] {map.get(n2), i};
        	}
            
        	map.put(nums[i], i);
        }
        
        return new int[0];
    }
}
