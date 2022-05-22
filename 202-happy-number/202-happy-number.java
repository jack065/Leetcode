class Solution {
    public boolean isHappy(int n) {
        int sum = 0;
        int counter = 0;
        while (counter < 10){ //Sets a time out condition. Less optimal for larger numbers
            while (n > 0){
                int placeholder = n % 10;
                sum += Math.pow(placeholder, 2);
                n /= 10;
            }
            if (sum == 1){
                return true;
            }
            n = sum;
            sum = 0;
            counter++;
        }
        return false;
    }
}