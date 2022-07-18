class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        length = len(nums)
        
        currSum = maxSum = sum(nums[:k])
        
        for i in range(k, length):
            currSum -= nums[i-k]
            currSum += nums[i]
            maxSum = max(currSum, maxSum)
            
        return maxSum/k