class Solution {
    public int removePalindromeSub(String s) {
        if ((isPalindrome(s)) == true){
            return 1;
        }
        else{
            return 2;
        }
    }
    private boolean isPalindrome(String s){
        int l = 0;
        int h = s.length();
        while (l <= h/2){
            if (s.charAt(l) != s.charAt(h - 1 - l++)){
                return false;
            }
        }
        return true;
    }
}