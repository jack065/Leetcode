class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lower_boundary = 0;
        upper_boundary = len(nums) - 1
        while(lower_boundary <= upper_boundary):
            pivot = (lower_boundary + upper_boundary) // 2 #//    returns a rounded off value compared to /
            if nums[pivot] == target:
                return pivot
            if nums[pivot] < target: #target is to the right of pivot
                lower_boundary = pivot + 1;
            else:
                upper_boundary = pivot - 1;
        return -1
        
        