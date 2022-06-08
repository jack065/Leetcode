class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Empty dictionary to store the index and values, ie key-value pair
        hashMap = {}
        
        # i being the index and n being the value itself
        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashMap:
                return [hashMap[diff], i]
            hashMap[n] = i 
        return