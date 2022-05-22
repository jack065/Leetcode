class Solution {
    public boolean canMakeArithmeticProgression(int[] arr) {
        Arrays.sort(arr);
        int difference = arr[1] - arr[0];
        int tester = 0;
        for (int i = 0; i < arr.length-1; i++){
            tester = arr[i+1] - arr[i];
            if (difference != tester){
                return false;
            }
        }
        return true;
    }
}