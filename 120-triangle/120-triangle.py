class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # List to store every bottom value in triangle, + 1 to store the possible overshoot value as a result of bottom first search
        dp = [0] * (len(triangle) + 1)
        
        # triangle[::-1] reverses the triangle array allowing row to loop through starting from the bottom
        for row in triangle[::-1]:
            for i, n in enumerate(row):
                # The minimum value at index i is equals to the existing value at i plus the minimum of both of its childs
                dp[i] = n + min(dp[i], dp[i+1])
                
        # Since we did a bottom first search, the value at indedx 0 of dp will return the minimum value after navigating the entire list
        return dp[0]