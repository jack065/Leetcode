class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # Catch to ensure that string is not empty to prevent error
        if len(s) == 0:
            return 0
        
        # Creating an empty list to store the various strings
        subString = []
        
        # Temporary string to store any non repeating characters
        temp = ''
        
        # For loop to iterate through all the characters in the entered string
        for r in s:
            # Checks that characters are not in temp
            if r not in temp:
                # If values are not in temp, keep adding and append said values
                
                temp += r
                subString.append(temp)
            else:
                repeat = temp.index(r)
                temp = temp[repeat+1:] + r
                
        return max([len(item) for item in subString])