class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        newNode = {}
        for i, n in enumerate(numbers):
            hit = target - numbers[i]
            if hit in newNode:
                return ((newNode[hit]+1), (i+1))
            newNode[n] = i
        return 