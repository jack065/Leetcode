class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subString = []
        temp = ''
        
        if len(s) == 0:
            return 0
        
        for r in s:
            if r not in temp:
                temp += r
                subString.append(temp)
            else:
                repeat = temp.index(r)
                temp = temp[repeat+1:] + r
                
        return max([len(item) for item in subString])