class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = f"{x}"
        return (x == x[::-1])
        