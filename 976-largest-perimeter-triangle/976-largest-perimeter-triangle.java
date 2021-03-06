class Solution {
    public int largestPerimeter(int[] nums) {
        Arrays.sort(nums);
        int perim = 0;
        int length = nums.length;
        for (int i = length - 1; i >= 2; i--){
            int a = nums[i-2];
            int b = nums[i-1];
            int c = nums[i];
            if (c < a + b){
                return a+b+c;
            }
        }
    return 0;
    }
}