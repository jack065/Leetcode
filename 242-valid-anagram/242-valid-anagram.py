class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}
        
        # Since we know both string s and t are of the same length, we can iterate through just one for loop
        for i in range(len(s)):
            # .get function takes in 2 parameters. If s[i] is present, it takes the value from s[i], if not,             it sets the default value to zero.
            # Populating both hashmaps
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS:
            # Same logic as above, as we are iterating through countS, we are uncertain if the element is also present in countT as such, if it is not present, we should set its default value to be 0, hence the use of a .get function
            if countS[c] != countT.get(c, 0):
                return False
            
        return True