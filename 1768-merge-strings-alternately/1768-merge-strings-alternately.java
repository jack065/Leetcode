class Solution {
    public String mergeAlternately(String word1, String word2) {
        int pointer1 = 0, pointer2 = 0, pointer = 0;
        int length1 = word1.length(), length2 = word2.length();
        char[] results = new char[length1 + length2];
        while ((pointer1 < length1) || (pointer2 < length2)){
            if (pointer1 < length1){
                results[pointer] = word1.charAt(pointer1);
                pointer++;
                pointer1++;
            }
            if (pointer2 < length2){
                results[pointer] = word2.charAt(pointer2);
                pointer++;
                pointer2++;
            }
        }
        return new String(results);
    }
}