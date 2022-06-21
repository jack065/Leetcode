class Solution {
    public int strStr(String haystack, String needle) {
        int s = haystack.length();
        int l = needle.length();
        
        int i = 0, j = 0;
        
        if (haystack.length() < needle.length()){
            return -1;
        }
        if (haystack.equals(needle)){
            return 0;
        }
        
        while (i < haystack.length()){
            if (haystack.charAt(i) == needle.charAt(j)){
                int temp = i;
                while (i < haystack.length() && haystack.charAt(i) == needle.charAt(j)){
                    i++;
                    j++;
                    if (j == needle.length()){
                        return temp;
                    }
                }
                i = temp;
                j = 0;
            }
            i++;
        }
        return -1;
    }
}