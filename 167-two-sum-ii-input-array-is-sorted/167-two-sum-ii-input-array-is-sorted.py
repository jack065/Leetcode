class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # How does the program work?
        # Create 2 pointers at the start and end of the entire list
        # Add up the values at the pointers
        # If the sum of the values is smaller than the target, increment the lower pointer by one
        # If the sum of the values is larger than the target, decrement the higher pointer by one
        
        # Another method is similar to the original two sum where you create a hashmap, compare the values
        # then submit the indexes of the matching pairs.
    
        start = 0
        end = len(numbers) - 1
        while start != end:
            summer = numbers[start] + numbers[end]
            if summer > target:
                end -= 1
            elif summer < target:
                start += 1
            else:
                # Return the pointers + 1
                return [start + 1, end + 1]
            