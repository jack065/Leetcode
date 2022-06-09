class Solution {
    public int searchInsert(int[] nums, int target) {
        // One pass binary search
        int high = nums.length - 1;
        int low = 0;
        int middle = 0;
        
        while (low <= high){
            middle = (low + (high - low) / 2);
            if (target < nums[middle]){
                high = middle - 1;
            }
            else if (target > nums[middle]){
                low = middle + 1;
            }
            else if (target == nums[middle]){
                return middle;
            }
        }
        return low;
    }
}