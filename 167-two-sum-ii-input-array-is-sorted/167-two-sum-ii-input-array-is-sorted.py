class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1
        
        while start != end:
            summer = numbers[start] + numbers[end]
            if summer > target:
                end -= 1
            elif summer < target:
                start += 1
            else:
                return [start + 1, end + 1]
            