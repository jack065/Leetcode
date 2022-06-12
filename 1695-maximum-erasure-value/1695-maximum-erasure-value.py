class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        # Initial idea was correct, problem was with adding up the values in the hashSet. Not sure why sum(hashSet) doesn't work so I'll
        # have to look into it more.
        
        # Sliding window technique. ( Time Complexity : O(n) ), ( Space Complexity : O(n) )
        hashSet = set()
        
        # Initialise pointer, this will be the end of the "window"
        left = 0
        # Random for storage
        max_result = 0
        # Return variable
        res = 0
        
        # Iterate through entire list
        for right in range(len(nums)):
            # while nums[right] is in the hashSet, loop through till no instances of this repeat is in the hashset
            while nums[right] in hashSet:
                hashSet.remove(nums[left])
                # Deduct the value of the removed number from the temporary variable
                max_result -= nums[left]
                # Increment the window to allow it to 'move'
                left += 1
            # If the number is not in the hashset, add it to the hashset
            hashSet.add(nums[right]) 
            # Add the number to the temporary variable
            max_result += nums[right]
            # Max used to compare the previous obtained to the current and set the return value to the maximum.
            res = max(res, max_result)
        return res