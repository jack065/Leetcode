class Solution:
    def search(self, nums: List[int], target: int) -> int:
        upper = len(nums) - 1
        lower = 0
        while upper >= lower:
            pivot = round((upper + lower)/2)
            if (target > nums[pivot]):
                lower = pivot + 1
            elif (target < nums[pivot]):
                upper = pivot - 1
            elif (target == nums[pivot]):
                return pivot
        return -1
        
        
        