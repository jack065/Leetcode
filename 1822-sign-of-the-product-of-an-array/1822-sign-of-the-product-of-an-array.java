class Solution {
    public int arraySign(int[] nums) {
        int product = 1;
        int negative = 0;
        int result = -1;
        for (int i = 0; i < nums.length; i++){
            if (nums[i] < 0){
                negative++;
            }
            if (nums[i] == 0){
                return 0;
            }
        }
        if (negative%2 != 0){
            product = -1;
        }
        return product;
    }
}