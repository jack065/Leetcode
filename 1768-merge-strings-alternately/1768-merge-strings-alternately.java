class Solution {
    public String mergeAlternately(String word1, String word2) {
        int pointer1 = 0, pointer2 = 0, pointer = 0;
        char[] results = new char[(word1.length() + word2.length())];
        while ((pointer1 < word1.length()) || (pointer2 < word2.length())){
            if (pointer1 < word1.length()){
                results[pointer] = word1.charAt(pointer1);
                pointer++;
                pointer1++;
            }
            if (pointer2 < word2.length()){
                results[pointer] = word2.charAt(pointer2);
                pointer++;
                pointer2++;
            }
        }
        return new String(results);
    }
}