class Solution:
    def climbStairs(self, n: int) -> int:
        first, second = 1, 1
        for i in range(n):
            temp = first
            first = first + second
            second = temp
        return second
    
        