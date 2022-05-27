class Solution {
    public String mergeAlternately(String word1, String word2) {
        int pointer1 = 0;
        int pointer2 = 0;
        String result = "";
        int length = Math.max(word1.length(), word2.length());
        for (int i = 0; i < length; i++){
            if (pointer1 < word1.length()){
                result += word1.charAt(i);
                pointer1++;
            }
            if (pointer2 < word2.length()){
                result += word2.charAt(i);
                pointer2++;
            }
        }
        return result;
    }
}