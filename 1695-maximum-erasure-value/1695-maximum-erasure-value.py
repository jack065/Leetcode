class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        hashSet = set()
        
        left = 0
        max_result = 0
        res= 0
        
        for right in range(len(nums)):
            while nums[right] in hashSet:
                hashSet.remove(nums[left])
                max_result -= nums[left]
                left += 1
            hashSet.add(nums[right]) 
            max_result += nums[right]
            res = max(res, max_result)
        return res