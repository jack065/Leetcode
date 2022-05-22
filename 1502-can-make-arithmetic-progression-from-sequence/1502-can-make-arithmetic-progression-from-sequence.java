class Solution {
    public boolean canMakeArithmeticProgression(int[] arr) {
        Arrays.sort(arr);
        int difference = arr[0] - arr[1];
        int tester = 0;
        for (int i = 0; i < arr.length-1; i++){
            tester = arr[i] - arr[i+1];
            if (difference != tester){
                return false;
            }
        }
        return true;
    }
}