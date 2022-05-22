class Solution {
    public int arraySign(int[] nums) {
        int product = 1;
        int result = -1;
        for (int i = 0; i < nums.length; i++){
            if (nums[i] < 0){
                nums[i] = -1;
            }
            if (nums[i] > 0){
                nums[i] = 1;
            }
            if (nums[i] == 0){
                product = 0;
            }
            product *= nums[i];
        }
        return product;
    }
}