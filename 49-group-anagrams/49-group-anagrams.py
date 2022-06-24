class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Use defaultdict to ensure that no key value errors will be raised
        # defaultdict(list) just means defining a dictionary with lists as its values
        res = defaultdict(list)
        
        # Iterate through each word in the list of words
        for s in strs:
            # create a hashing function, setting 26 [0]'s
            count = [0] * 26
            
            # for each character in the word
            for c in s:
                # count[ord(c) - ord("a")] returns the index of this hashing function where a = 0, b = 1 etc
                # increment the number at this index in count by one to signify that one of this character                  is present in the substring. This will be the hashing value we use
                count[ord(c) - ord("a")] += 1
                
            # store hashing value as a tuple to prevent it from being changed unexpectedly. Append the string s into the index the hashing value dictates. Two strings with the same hashing value will be stored in the same index.
            res[tuple(count)].append(s)
        
        # return all values in res.
        return res.values()