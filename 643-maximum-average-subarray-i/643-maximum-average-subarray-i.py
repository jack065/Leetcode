class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # How does the program work?
        length = len(nums)
        # Firstly, calculate the sum of subarrays of length k starting from index 0
        currSum = maxSum = sum(nums[:k])
        
        # Start i at k then end it at length
        for i in range(k, length):
            # Subtract the last element in the subarray
            currSum -= nums[i-k]
            # Add the first element in the subarray
            currSum += nums[i]
            # Update the new max value
            maxSum = max(currSum, maxSum)
            
        return maxSum/k