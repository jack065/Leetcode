class Solution {
    public int strStr(String haystack, String needle) {
        // Create variables to store the length of both strings
        int s = haystack.length();
        int l = needle.length();
        
        // 2 pointer method
        int i = 0, j = 0;
        
        // if the haystack is shorter than the needle, return -1 as no possible substring
        if (haystack.length() < needle.length()){
            return -1;
        }
        
        // if the haystack is the same as the needle, return 0 as they are the same thing
        if (haystack.equals(needle)){
            return 0;
        }
        
        // 2 pointer method to iterate through both haystack and needle strings
        // While loop activates for as long as i is smaller than length of haystack
        while (i < haystack.length()){
            // If the character at the i index in haystack is the same as the character at the j index in needle, store i index as a temp variable.
            if (haystack.charAt(i) == needle.charAt(j)){
                int temp = i;
                // As long as i is smaller than the length of haystack, and the character at i is the same as the character at j, increase i and j till length of j is the same as length of needle. If not possible, reset i to temp and j back to zero
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
            // Increment i by one with each loop.
            i++;
        }
        return -1;
    }
}